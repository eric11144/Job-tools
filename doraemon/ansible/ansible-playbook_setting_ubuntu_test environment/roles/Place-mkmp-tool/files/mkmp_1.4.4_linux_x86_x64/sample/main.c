#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdbool.h>
#include <pthread.h>
#include <getopt.h>

#if defined(OS_FREEBSD)
    #include <camlib.h>
    #define OPTION_DEVICE   "device (/dev/ada0)"
#else
    #define OPTION_DEVICE   "device (/dev/ada)"
#endif

#include "mkmp.h" 
#include "msg.h"

#define MN_ROM      "Generi Loader SATA Device"
#define MN_GDP      "Maxiotek GDP"
#define MN_RTY      10
#define BIN_TAG     "MAS09_FWTAG"
#define EXCEPTION   "exception.txt"

enum
{
    MODE_DLMICRO       = 0,
    MODE_WRITC_CODE,
    MODE_DLMICRO_SRAM,
};

enum
{
    IS_BIN    = 0,
    HIT_SN,
    UNKNOW_SN,
};

/*-----------------------------------------------------------------------------------------------------------*/
static pthread_t msg_th;
static bool isShowDot = false;

static char *BinFile[] = 
{ "Q2TNCGBC.bin", "Q2TNCGDC.bin", "Q2TNCGHC.bin", "Q2TNCGPC.bin", 

  /* Allen 2022.09.30 */
  "Q2TNCAAC.bin", "Q2TNCGAC.bin", "Q2TNCGFC.bin", "Q2TNCGDC_1125.bin", 
  "Q2TNCGHC_1125.bin",
};

/*-----------------------------------------------------------------------------------------------------------*/
static const struct option long_opt[] =
{
    { "Device",        1, NULL, 'd' },   
    { "FW bin file",   1, NULL, 'f' },   
    { "Download mode", 1, NULL, 'm' },   
    { "Reset",         0, NULL, 'r' },   
    { NULL,            0, NULL, '0' },
};

/*-----------------------------------------------------------------------------------------------------------*/
static void show_title(void)
{
    printf("************************************************************************\n");
    printf("* Innodisk FW Update (%s)                               %s *\n", get_lib_ver(), get_build_date());
    printf("************************************************************************\n");
}

/*-----------------------------------------------------------------------------------------------------------*/
static void show_usage(char *name)
{
    show_title();
    printf("Syntax: %s [-option ...]\n", name);
    printf("Sample: %s -d /dev/ada1 -f Q2TNCGDC.bin -m 0\n", name);    
    printf("Option:\n");
    printf("  -d : %s \n", OPTION_DEVICE);
    printf("  -f : FW bin file \n");
    printf("  -m : update (0:Microcode 1:Write code 2:Microcode & modify SRAM) \n");
    printf("  -r : reset system \n");
}

/*-----------------------------------------------------------------------------------------------------------*/
static void show_msg(char *str, bool ShowDot)
{
    printf("%s", str);
    fflush(stdout);
    isShowDot = ShowDot;
}

/*-----------------------------------------------------------------------------------------------------------*/
static unsigned char get_key(char *str)
{
    static int c;

    printf("%s", str);
    fflush(stdout);
    scanf("%d", &c);
    
    clearerr(stdin);

    return c;   
}

/*-----------------------------------------------------------------------------------------------------------*/
static int show_id_info(char *dev, ID_INFO *id, bool isShow)
{
    int ret;

    #if defined(OS_FREEBSD)
        struct cam_device *fd = cam_open_device(dev, O_RDWR);
    #else
        int fd = open(dev, O_RDWR);
    #endif

    if(fd)
    {
        memset(id, 0, sizeof(ID_INFO));

        ret = get_id_info(fd, id);    

        if(!ret && isShow)
        {
            show_title();
            printf("Model name  : %s \n", id->model_name);
            printf("FW version  : %s \n", id->fw_version);
            printf("Serian num  : %s \n", id->serial_num);
            printf("TAG         : %s \n", id->TAG);
        }    
    }
    else
        DBGMSG("Open %s fail !!", dev);
    
    #if defined(OS_FREEBSD)
        if(fd)
            cam_close_device(fd);
    #else
        if(fd)
            close(fd);
    #endif

    return ret;
}

/*-----------------------------------------------------------------------------------------------------------*/
static int get_file_len(const char *file)
{
    FILE *fp;
    int  len = 0;
    
    fp = fopen(file, "rb");

    if(fp)
    {
        fseek(fp, 0, 2);
        len = ftell(fp);
        fseek(fp, 0, 0); 
        
        if(len % 1024)
            len = (len / 1024 + 1) * 1024;
    }

    if(fp)
        fclose(fp);

    return len;
}

/*-----------------------------------------------------------------------------------------------------------*/
static void load_file(const char *file, unsigned char *buf, int size)
{
    FILE *fp;
    int  i;
    
    fp = fopen(file, "rb");

    memset(buf, 0, size);

    if(fp)
    {
        for(i=0; i<size; i++)
            buf[i] = getc(fp);
    }

    if(fp)
        fclose(fp);
}

/*-----------------------------------------------------------------------------------------------------------*/
static void* show_dot(void *ptr)
{
    while(1)
    {
        usleep(1000000);

        if(isShowDot)
        {
            printf(".");
            fflush(stdout);
        }
    }

    return NULL;
}

/*-----------------------------------------------------------------------------------------------------------*/
static int filter_sn(char *bin, char *sn, FILTER_INFO *f)
{
    FILTER_INFO ff;
    FILE        *fp = NULL;    
    char        buf[64];
    int         ret = UNKNOW_SN;
    bool        isException = false;

    /*------------------------------------------------------------*/
    /* filter SN */
    fp = fopen(bin, "r");

    if(fp)
    {
        fread(buf, sizeof(buf), 1, fp);

        if(strstr(buf, BIN_TAG))
        {
            ret = IS_BIN;
            goto EXIT;
        }
        else
        {
            fseek(fp, 0, 0);

            while(feof(fp) == 0)
            {
                memset(f, 0, sizeof(FILTER_INFO));

                fscanf(fp, "%s\t%d\t%s\n", f->SN, &f->mode, f->bin);

                if(strstr(sn, f->SN))
                {
                    ret = HIT_SN;
                    break;
                }
            }
        }
    }
    else
        DBGMSG("Open %s fail !!", bin);

    if(fp)
        fclose(fp);  

    fp = NULL;

    /*------------------------------------------------------------*/
    /* exception */
    if(ret == HIT_SN)
    {
        fp = fopen(EXCEPTION, "r");

        if(fp)
        {
            while(feof(fp)== 0)
            {
                memset(&ff, 0, sizeof(FILTER_INFO));

                fscanf(fp, "%s\t%d\t%s\n", ff.SN, &ff.mode, ff.bin);

                if(strstr(ff.SN, sn))
                {
                    isException = true;
                    f->mode     = ff.mode;
                    memcpy(f->bin, ff.bin, strlen(ff.bin));
                    break;
                }
            }
        }
        else
            DBGMSG("Open %s fail !!", EXCEPTION);   
    }

    /*------------------------------------------------------------*/
    if(ret == HIT_SN)
    {
        printf("BIN       : %s \n", f->bin);
        printf("Mode      : %d \n", f->mode);
        printf("Exception : %s \n", (isException) ? "Yes" : "No");
        printf("==================================================\n");
    }

EXIT:

    if(fp)
        fclose(fp);

    return ret;
}

/*-----------------------------------------------------------------------------------------------------------*/
static void WriteCode(char *dev, char *bin)
{
    ID_INFO       id;
    unsigned char *gdp = NULL;
    unsigned char *fw = NULL;
    int           i, ret, gdp_len, fw_len, isSuccess = false;

    #if defined(OS_FREEBSD)
        struct cam_device *fd = cam_open_device(dev, O_RDWR);
    #else
        int fd = open(dev, O_RDWR);
    #endif

    if(fd)
    {
        ret = show_id_info(dev, &id, true);

        if(!strstr(id.TAG, "DK1"))
        {
            printf("Unknow device !! \n");
            goto EXIT;
        }
    }
    else
    {
        DBGMSG("Open %s fail !!", dev);
        goto EXIT;
    }       

    /*------------------------------------------------------------*/
    /* load GDP & FW */
    gdp_len = get_file_len(GDP_BIN);

    if(!gdp_len)
    {
        DBGMSG("Open %s fail !!", GDP_BIN);
        goto EXIT;
    }
    else
    {
        gdp_len = 240 * 1024;

        gdp = malloc(sizeof(unsigned char) * gdp_len); 

        load_file(GDP_BIN, gdp, gdp_len);
    }

    fw_len = get_file_len(bin);

    if(!fw_len)
    {
        DBGMSG("Open %s fail !!", bin);
        goto EXIT;
    }
    else
    {
        fw = malloc(sizeof(unsigned char) * fw_len); 
        load_file(bin, fw, fw_len);
    }

    /*------------------------------------------------------------*/
    pthread_create(&msg_th, NULL, show_dot, NULL);

    /*------------------------------------------------------------*/
    /* jump_to_rom */
    show_msg("Jump to ROM : ", true);    

    ret = jump_to_rom(fd);

    if(!ret)
    {
        for(i=0; i<MN_RTY; i++)
        {
            usleep(1000000);

            memset(&id, 0, sizeof(ID_INFO));

            ret = show_id_info(dev, &id, false);
        
            if(!ret && strstr(id.model_name, MN_ROM))
                break;    
        }

        if(!strstr(id.model_name, MN_ROM))
        {
            printf("Unknow device !! \n");
            goto EXIT;
        }    
    }
    else
    {
        DBGMSG("jump_to_rom fail !! \n");
        goto EXIT;
    }

    show_msg("Success \n", false);     

    /*------------------------------------------------------------*/
    /* write_sram_bin */  
    show_msg("Write GDP   : ", true);

    ret = write_sram_bin(fd, gdp, gdp_len);

    if(ret)
    {
        DBGMSG("write_sram_bin fail !! \n");
        goto EXIT;
    }

    show_msg("Success \n", false);

    /*------------------------------------------------------------*/
    /* jump_to_ram */  
    show_msg("Jump to RAM : ", true);

    ret = jump_to_ram(fd);

    if(!ret)
    {
        for(i=0; i<MN_RTY; i++)
        {
            usleep(1000000);

            memset(&id, 0, sizeof(ID_INFO));

            ret = get_id_info(fd, &id); 
        
            if(!ret && strstr(id.model_name, MN_GDP))
                break;    
        }

        if(!strstr(id.model_name, MN_GDP))
        {
            printf("Unknow device !! \n");
            goto EXIT;
        }    
    }
    else
    {
        DBGMSG("jump_to_ram fail !!");
        goto EXIT;
    }     

    show_msg("Success \n", false);

    #if defined(OS_FREEBSD)
        if(fd)
            cam_close_device(fd);
    #else
        if(fd)
            close(fd);
    #endif

    usleep(4000000);
    
    /*------------------------------------------------------------*/
    /*------------------------------------------------------------*/
    #if defined(OS_FREEBSD)
        fd = cam_open_device(dev, O_RDWR);
    #else
        fd = open(dev, O_RDWR);
    #endif

    if(!fd)
    {
        DBGMSG("Open %s fail !!", dev);
        goto EXIT;
    }         

    /*------------------------------------------------------------*/
    /* setup_gdp */
    show_msg("Setup GDP   : ", true);

    ret = setup_gdp(fd);

    if(ret)
    {
        DBGMSG("setup_gdp fail !!");
        goto EXIT;
    }

    show_msg("Success \n", false);

    /*------------------------------------------------------------*/
    /* write_code */
    show_msg("Write code  : ", true);

    ret = write_code(fd, fw, fw_len);

    if(ret)
    {
        DBGMSG("write_code fail !!");
        goto EXIT;
    }
    else
    {   
        isSuccess = true;
        show_msg("Success \n", false);
    }        

    (isSuccess) ? printf("Update success !! \n")
                : printf("Update fail !! \n");

    /*------------------------------------------------------------*/
    /* jump_to_fw */
    printf("==================================================\n");
    show_msg("Jump to FW : ", true);

    ret = jump_to_fw(fd);

    if(!ret)
    {
        show_msg("Success \n", false);

        usleep(1000000);

        memset(&id, 0, sizeof(ID_INFO));

        ret = get_id_info(fd, &id);    

        if(!ret)
        {
            printf("Model name  : %s \n", id.model_name);
            printf("FW version  : %s \n", id.fw_version);
            printf("Serian num  : %s \n", id.serial_num);
        }
    }
    else
    {
        DBGMSG("jump_to_fw fail !!");
        goto EXIT;
    }     
    
EXIT:

    #if defined(OS_FREEBSD)
        if(fd)
            cam_close_device(fd);
    #else
        if(fd)
            close(fd);
    #endif

    if(gdp)
        free(gdp);

    if(fw)
        free(fw);
}

/*-----------------------------------------------------------------------------------------------------------*/
static void DLMicro(char *dev, char *bin, bool isModifySRAM)
{
    BIN_INFO    BinInfo;
    ID_INFO     id;
    FILTER_INFO f; 
    SIZE_INFO   s;
    FILE        *fp;
    int         i, t, ret;

    memset(&BinInfo, 0, sizeof(BIN_INFO));

    #if defined(OS_FREEBSD)
        struct cam_device *fd = cam_open_device(dev, O_RDWR);
    #else
        int fd = open(dev, O_RDWR);
    #endif

    /*------------------------------------------------------------*/
    if(fd)
    {
        memset(&id, 0, sizeof(ID_INFO));
        ret = get_id_info(fd, &id);    

        if(!ret)
        {
            printf("==================================================\n");
            printf("Model name  : %s \n",      id.model_name);
            printf("FW version  : %s \n",      id.fw_version);
            printf("Serian num  : %s \n",      id.serial_num);
            printf("TAG         : %s \n",      id.TAG);
            printf("Capacity    : %.2f GB \n", id.capacity);
            printf("Flash ID    : %s \n",      id.FLASH_ID);            
        }    

        if(!strstr(id.TAG, "DK1"))
        {
            printf("Unknow device !! \n");
            goto EXIT;
        }
    }
    else
    {
        DBGMSG("Open %s fail !!", dev);
        goto EXIT;
    }       

    /*------------------------------------------------------------*/
    /* filter SN */
    ret = filter_sn(bin, id.serial_num, &f);

    if(ret == IS_BIN)
    {
        sprintf(BinInfo.file, "%s", bin);

        /* Allen 2023.01.06 */
        if(isModifySRAM)
        {
            for(i=0; i<DIM(BinFile, char*); i++)
            {
                if(strstr(BinInfo.file, BinFile[i]))
                    modify_sram(fd, i);
            }            
        }        

    }
    else if(ret == HIT_SN)
    {
        for(i=0; i<DIM(BinFile, char*); i++)
        {
            if(strstr(f.bin, BinFile[i]))
            {
                sprintf(BinInfo.file, "%s", f.bin);

                if(f.mode == 1 && strstr(id.fw_version, "S20615"))
                    modify_sram(fd, i);                    

                break;                    
            }
            else if(f.mode == 0)
            {
                /* Allen 2023.02.03 for SN mode 0 */
                sprintf(BinInfo.file, "%s", f.bin);
                break;
            }
        }            
    }
    else if(id.capacity > 200 && id.capacity <= 256)
    {
        printf("------------------------------\n");

        while(1)
        {
            t = get_key("1. 4CH 1C\n2. 2CH 2C\nSelect:");
            if(t >= 1 && t <= 2)
            {
                if(t == 1)      sprintf(BinInfo.file, "%s", "Q2TNCGDC.bin");
                else if(t == 2) sprintf(BinInfo.file, "%s", "Q2TNCGFC.bin");
                break;
            }
        }
    }
    else
    {
        fp = fopen("size.txt", "r");

        i = 0;

        if(fp)
        {
            fseek(fp, 0, 0);

            while(feof(fp) == 0)
            {
                memset(&s, 0, sizeof(SIZE_INFO));

                fscanf(fp, "%d\t%s\t%s\n", &s.size, s.ID, s.bin);

                if(id.capacity < s.size)
                {
                    if(strstr(s.ID, "-----") || strstr(id.FLASH_ID, s.ID))
                        sprintf(BinInfo.file, "%s", s.bin);
                    else
                        continue;

                    break;
                }
            }
        }

        if(fp)
            fclose(fp);

        fp = NULL;
    }    

    printf("FW bin      : %s \n", BinInfo.file);
    printf("==================================================\n");

    /*------------------------------------------------------------*/
    /* DLMicro */
    fp = fopen(BinInfo.file, "rb");

    if(fp > 0)
    {
        fseek(fp, 0, 2);
        BinInfo.len  = ftell(fp);
        BinInfo.data = malloc(sizeof(char) * BinInfo.len);

        fseek(fp, 0, 0); 
        fread(BinInfo.data, 1, BinInfo.len, fp);
        fclose(fp);

        ret = dl_micro_sata(fd, 3, BinInfo);

        if(!ret)
        {
            #if defined(OS_FREEBSD)
                if(fd)
                    cam_close_device(fd);

                fd = cam_open_device(dev, O_RDWR);
            #else
                if(fd)
                    close(fd);

                fd = open(dev, O_RDWR);
            #endif

            if(fd)
            {
                usleep(500000);

                memset(&id, 0, sizeof(ID_INFO));           
                ret = get_id_info(fd, &id);    

                if(!ret)
                {
                    printf("Model name  : %s \n", id.model_name);
                    printf("FW version  : %s \n", id.fw_version);
                    printf("Serian num  : %s \n", id.serial_num);
                }
            }
        }
        else
        {
            DBGMSG("DLMicro fail !!");
            goto EXIT;
        }     
    }     
    else
        DBGMSG("Open %s fail !!", BinInfo.file);

EXIT:

    #if defined(OS_FREEBSD)
        if(fd)
            cam_close_device(fd);
    #else
        if(fd)
            close(fd);
    #endif
}

/*-----------------------------------------------------------------------------------------------------------*/
int main(int argc, char **argv)
{
    ID_INFO id;
    char    dev[64] = { 0 }, bin[128] = { 0 };
    int     opt, mode = -1;
    bool    isReset      = false;

    memset(&id, 0, sizeof(ID_INFO));

    if(getuid())
    {
        show_usage(argv[0]);
        printf("\nPermission denied !!\nYou are not logged as root.\n\n");
        return 0;
    }

    while((opt = getopt_long(argc, argv, "?hd:f:m:r", long_opt, NULL)) != -1)
    {
        switch(opt)
        {
            case 'd': strcpy(dev, optarg); break;
            case 'f': strcpy(bin, optarg); break;
            case 'm': mode = atoi(optarg); break;
            case 'r': isReset = true;      break;
            case 'h':
            case '?':
            default:  show_usage(argv[0]);
                      return 0;      
        }
    }

    if(argc < 6)
    {
        (strlen(dev) > 0) ? show_id_info(dev, &id, true) : show_usage(argv[0]);
        return 0;
    }    

    show_title();

    (mode == MODE_DLMICRO)      ? DLMicro(dev, bin, false) : 
    (mode == MODE_DLMICRO_SRAM) ? DLMicro(dev, bin, true)  : WriteCode(dev, bin);

    if(isReset)
    {
        printf("Reset system ... \n");        
        reset();
    }

    return 0;
}

