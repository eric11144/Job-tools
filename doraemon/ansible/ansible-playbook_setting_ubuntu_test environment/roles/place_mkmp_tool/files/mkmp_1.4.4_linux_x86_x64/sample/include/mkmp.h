#ifndef __MKMP_H__
#define __MKMP_H__

#define DIM(var, type)  (sizeof(var)) / sizeof(type)

/* for MKMP */
#define MEM_MAX_PROG_SIZE_KB    (240)
#define MEM_MAX_PROG_SIZE_BYTE  (MEM_MAX_PROG_SIZE_KB << 10)
#define SECTOR_SIZE             512

/* for DLMicro */
#define MAX_BIN_SIZE    512 * 256 
#define SECTOR_SIZE     512 
#define SECTOR_CNT      8   

#define GDP_BIN     "GDP.bin"
#define FW_BIN      "Q2TNCGHC.bin"

#if defined(OS_FREEBSD)
    #define DEV_HANDLE  struct cam_device*
#else
    #define DEV_HANDLE  int
#endif


/*-----------------------------------------------------------------------------------------------------------*/
typedef struct
{
    unsigned char cdb[16];
    unsigned char *buf;
    unsigned long buf_size;

    int protocol;   /* 3: non-data, 4: data in, 5: data out              */
    int extend;     /* 0: 24 bit cdb[0] = 0xA1, 1: 48 bit cdb[0] = 0x85  */
    int ck_cond;    /* set to 1 to read register(s) back                 */
    int t_dir;      /* 0: to device, 1: from device                      */
    int byte_block; /* 0: 0 bytes, 1: 512 byte blocks                    */
    int t_length;   /* 0: no data transferred                            */
    int timeout;    /* msec                                              */

} CDB_INFO;

typedef struct
{
    char SN[21];
    char bin[64];
    int  mode;
} FILTER_INFO;

typedef struct
{
    int  size;
    char ID[8];
    char bin[64];
} SIZE_INFO;

/*------------------------------------------------------------------------------------------------------------*/
#define LEN_MODEL_NAME  40
#define LEN_SERIAL_NUM  20
#define LEN_FW_VERSION  8

typedef struct
{
    char  model_name[LEN_MODEL_NAME+1];
    char  serial_num[LEN_SERIAL_NUM+1];
    char  fw_version[LEN_FW_VERSION+1];
    char  TAG[4];
    char  FLASH_ID[10];
    float capacity;

} ID_INFO;

typedef struct
{
    char          file[128];
    unsigned int  len;
    unsigned char *data;
} BIN_INFO;

/*------------------------------------------------------------------------------------------------------------*/
extern int   get_id_info(DEV_HANDLE fd, ID_INFO *id);
extern int   jump_to_rom(DEV_HANDLE fd);
extern int   jump_to_fw(DEV_HANDLE fd);
extern int   write_sram_bin(DEV_HANDLE fd, unsigned char *sram, int size);
extern int   jump_to_ram(DEV_HANDLE fd);
extern int   setup_gdp(DEV_HANDLE fd);
extern int   write_code(DEV_HANDLE fd, unsigned char *fw, int size);
extern bool  dl_micro_sata(DEV_HANDLE fd, int mode, BIN_INFO BinInfo);
extern int   fw_restart(DEV_HANDLE fd);
extern int   modify_sram(DEV_HANDLE fd, int n);
extern char* get_build_date(void);
extern char* get_lib_ver(void);
extern void  reset(void);

#endif