#!/bin/bash

dmesg -n 1
echo -ne "\033[9;0]"




Device_detect() {
    clear
        
    #txt_color # Call txt color
    echo -e "${number}i. Device list...${normal}"
    printf "\n"
    
    # 1. Get all SSD devices.
    ssd_devices=($(lsblk -d -o NAME,MODEL | grep -i "SSD\|M.2\|InnoDisk\|mSATA\|MRVL" | awk '{print "/dev/"$1}'))
    #ssd_devices=($(lsblk -d -o NAME,MODEL | grep -i "SSD\|M.2\|InnoDisk\|mSATA\|Generic_FCR_SATA_Loader" | awk '{print "/dev/"$1}'))
    num_ssd_devices=${#ssd_devices[@]}
    updated_devices=()
    not_updated_devices=()

    if [ $num_ssd_devices -gt 0 ]; then
        for ssd_device in "${ssd_devices[@]}"; do
            # 2. Get SSD model name and firmware version
            model=$(smartctl -i "${ssd_device}" | sed '2d; /Device Model:/!d; s/.*: *//')
            ssd_version=$(smartctl -i "${ssd_device}" | awk '/Firmware Version:/ {print $NF}')

            # 3. Print all SSD information
            echo "${ssd_device}, ${model}, firmware: ${ssd_version}"
        done
    else
        echo -e "${fgred}Cannot found any SSD.${normal}"
    fi
    printf "\n\n"
}

show_main_menu(){

    #txt_color # Call txt color
	
    printf " ---> How do you wanna the device to do? " #modify: 2024/06/04
    printf " \n"
    printf "   ${menu}*** Main menu **********************************************************              ${normal}\n"
    printf "   ${menu}**           *. Upgrade FW                                                            ${normal}\n"
    printf "   ${menu}**                 ${number} 1) Current FW: L22A26i                                   ${normal}\n"
    printf "   ${menu}**                                - modify phy tune.                                  ${normal}\n"
    printf "   ${menu}**                 ${number} 2) debug FW: L24202i                                     ${normal}\n"
    printf "   ${menu}**                                - add more debug message.                           ${normal}\n"
    printf "   ${menu}**           *. Dump elog                                                             ${normal}\n"
    printf "   ${menu}**                 ${number} 5) elog Utility                                          ${normal}\n"  
    printf "   ${menu}**           *. Read device Info                                                      ${normal}\n"
    printf "   ${menu}**                 ${number} 6) iSMART Utility		                            ${normal}\n"
    printf "   ${menu}**           *. Other                                                                 ${normal}\n"
    printf "   ${menu}**                 ${number} 7) Quick Erase (Erase user data/MBR/FAT table)           ${normal}\n"
    printf "   ${menu}**                 ${number} 8) Reboot                                                ${normal}\n"
    printf "   ${menu}**                 ${number} 9) Power off                                             ${normal}\n"
    printf "   ${menu}************************************************************************              ${normal}\n"
    printf "   Please enter a menu option and enter or ${fgred}x to exit. ${normal}"
    read opt
	
    while [ $opt != '' ]
    do
		if [ $opt = '' ]; then
			exit;
		else
			case $opt in
			1) clear;
				#option_picked "Option 1 Picked"; 	#CurrentFW: L22A26i,
                                #cd /mnt/DLM #USB dongle
                                cd /home/aaa/Desktop/USB_dongle_console #X86 platform
				./Update_L22A26i.sh                         
				echo -e $number 
				read -p "Click Enter to proceed... " userInput              
				./FW_update_hdparm_dlmc.sh
				break;	
			;;
			2) clear;
				#option_picked "Option 3: Picked"; 	#Upgrade debugFW: L24202i,
                                #cd /mnt/DLM #USB dongle
                                cd /home/aaa/Desktop/USB_dongle_console #X86 platform
				./Update_L24202i.sh                         
				echo -e $number 
				read -p "Click Enter to proceed... " userInput              
				./FW_update_hdparm_dlmc.sh	
				break;	
			;;
			5) clear;
				#option_picked "Option 5: Picked"; 	#Dump elog,
                                #cd /mnt/DLM #USB dongle
                                cd /home/aaa/Desktop/USB_dongle_console #X86 platform
				./Dump_elog.sh                         
				echo -e $number 
				read -p "Click Enter to proceed... " userInput              
				./FW_update_hdparm_dlmc.sh	
				break;		
			;;
			6) clear;
				#option_picked "Option 6 Picked"; 	#iSMART, Read device info
                                #cd /mnt/DLM #USB dongle
                                cd /home/aaa/Desktop/USB_dongle_console #X86 platform
				./iSMART_Info.sh    
				echo -e $number 
				read -p "Click Enter to proceed... " userInput              
				./FW_update_hdparm_dlmc.sh
				break;				
			;;
			7) clear;
				#option_picked "Option 7 Picked"; 	#iSMART, Quick Erase
                		#cd /mnt/DLM #USB dongle
                		cd /home/aaa/Desktop/USB_dongle_console #X86 platform
				./iSMART_QE.sh                          
				echo -e $number 
				read -p "Click Enter to proceed... " userInput              
				./FW_update_hdparm_dlmc.sh
				break;	
			;;
			8) clear;
				#option_picked "Option 8 Picked"; 	#Reboot
				reboot
			;;
			9) clear;
				#option_picked "Option 9 Picked"; 	#Power off
				poweroff
			;;
			x) exit;
			;;
			\n) exit;
			;;
			*) clear;
				#option_picked "Pick an option from the menu";
				show_main_menu;
				break;
			;;
		esac
		fi
	done	
}

txt_color(){
	normal=`echo "\033[m"` #White
	menu=`echo "\033[36m"` #Blue
	number=`echo "\033[33m"` #Yellow
	fgred=`echo "\033[31m"` #Red
	pass=`echo "\033[32m"` #Green
}
clear

txt_color
Device_detect
show_main_menu
