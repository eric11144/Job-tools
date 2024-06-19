#!/bin/sh

# *****************************************************
#   MANDATORY SETTINGS
# ********************************************************

SSD_PATH=""


# ********************************************************
#    OPTIONAL SETTINGS
# ********************************************************

# Duration of the test (recording) in seconds
RUN_DURATION=288000

# Delay (tempo) between 2 files creation (recording) in seconds
# to fake the CDMA buffer filling
# SDFO recom : flow of 20GB per hour => 4GB every 12 minutes (720 seconds)
# EEV return : flow of 1GB per hour => 4GB every 4 hours (14 400 seconds)
# Default value : 300 seconds => 4GB every 5 minutes
DELAY_BTW_2FILES=300

# Size of files created into the SSD in GB
# Default value : 4 GB
CREATE_FILE_SIZE_IN_GB=4

# Minimal free space on the disque in GB requested to create a new file
# Default value : 5 GB
MIN_FREE_SSD_SPACE_IN_GB=5


# ********************************************************
#    INTERNAL SCRIPT SETTING (do not modify)
# ********************************************************

# 1 GB = 1048576 KB
size_1GB_in_KB=1048576


# ********************************************************
#    FUNCTIONS
# ********************************************************

help_msg () {
   echo
   echo "Usage: $0 [-h|--help] -p <SSD mounted path> [-t <run duration in s>] [-d <delay between 2 files creation in s>] [-fs <size of file to create in GB>] [-ms <min free space on SSD in GB>]"
   echo
   echo "   Parameter between [] are optional and have default value :"
   echo "      - (-t) <run duration in s> = $RUN_DURATION (`expr $RUN_DURATION / 3600` hours)"
   echo "      - (-d) <delay between 2 files creation in s> = $DELAY_BTW_2FILES (`expr $DELAY_BTW_2FILES / 60` minutes)"
   echo "      - (-fs) <size of file to create in GB> = $CREATE_FILE_SIZE_IN_GB GB"
   echo "      - (-ms) <min free space on SSD in GB> = $MIN_FREE_SSD_SPACE_IN_GB GB"
}


# ********************************************************
#    MAIN SCRIPT BEGIN
# ********************************************************

# Test the number of parameter passed
if [ $# -lt 1 -o $# -gt 10 ]; then
    help_msg
    exit 1
fi

P_PARAM_PASSED=0

# Read parameter passed to the script
while [ $# -gt 0 ] ; do
    key="$1"
    case $key in
        -h|--help)
            help_msg
            exit 0
            ;;
        -p)
            P_PARAM_PASSED=1
	    if [ "$2" = "" -o ! -d "$2" ]; then
	       echo "Error : command line option '-p' requires the path where is mounted the SSD to test (path <"$2"> not found)" 
	       echo
	       help_msg
	       exit 1
	    fi
            SSD_PATH="$2"
            shift
            shift
            ;;
        -t)
	    if [ "$2" = "" -o -z "${2##*[!0-9]*}" ]; then
	       echo "Error : command line option '-t' requires a number of second (<"$2"> is not an integer)" 
	       echo
	       help_msg
	       exit 1
	    fi
            RUN_DURATION="$2"
            shift
            shift
            ;;
        -d)
	    if [ "$2" = "" -o -z "${2##*[!0-9]*}" ]; then
		    echo "Error : command line option '-d' requires a number of second (<"$2"> is not an integer)"
	       echo
	       help_msg
	       exit 1
	    fi
            DELAY_BTW_2FILES="$2"
            shift
            shift
            ;;
	-fs)
            if [ "$2" = "" -o -z "${2##*[!0-9]*}" ]; then
               echo "Error : command line option '-fs' requires a number of GB (<"$2"> is not an integer)"
               echo
               help_msg
               exit 1
            fi
            CREATE_FILE_SIZE_IN_GB="$2"
            shift
            shift
            ;;
        -ms)
            if [ "$2" = "" -o -z "${2##*[!0-9]*}" ]; then
                    echo "Error : command line option '-ms' requires a number of GB (<"$2"> is not an integer)"
               echo
               help_msg
               exit 1
            fi
            MIN_FREE_SSD_SPACE_IN_GB="$2"
            shift
            shift
            ;;
        *)
	    echo "Error : command line option <$key> not recognized"
	    echo
            help_msg
            exit 1
          
    esac
done

# Check if mandatory param -p (SSD_PATH) had been called
if [ $P_PARAM_PASSED -ne 1 ]; then
   echo "Error : command line option '-p <SSD mounted path>' is mandatory"
   echo
   help_msg
   exit 1
fi

echo
echo "Parameter settings :"
echo "   - SSD_PATH : $SSD_PATH"
echo "   - Tests duration : $RUN_DURATION seconds (`expr $RUN_DURATION / 3600` hours)"
echo "   - Delay between 2 files creation on SSD : $DELAY_BTW_2FILES seconds (`expr $DELAY_BTW_2FILES / 60` minutes)"
echo "   - Created file size : $CREATE_FILE_SIZE_IN_GB GB"
echo "   - Free left space limit on SSD : $MIN_FREE_SSD_SPACE_IN_GB GB" 
echo

current_pwd0="`pwd`"
cd "$SSD_PATH"

# Display the remaining space on the SSD disk
free_space=$(df --output=avail . | sed -n 2p)
free_space_in_GB=`expr $free_space / $size_1GB_in_KB`
echo "Free space under <$SSD_PATH> before starting: $free_space_in_GB GB"

# Get the last folder index if folder_XX already exist on the SSD
last_folder=`ls -ltd folder_[0-9]*/ 2> /dev/null | head -n 1 | awk '{ print $NF }' | cut -f1 -d/`
if [ ! -z "$last_folder" ]; then
   last_folder_index=`echo $last_folder | tr -d "folder_"`
  
   # Increment or reset to 1 the last folder index
   if [ $last_folder_index -lt 99 ]; then
      folder_counter=`expr $last_folder_index + 1`
   else
      folder_counter=1
   fi
else
   folder_counter=1
fi

echo
echo "Starting time : " `date +"%d/%m/%Y - %H:%M:%S"`

# Repeat during X times (X times defined by the global variable RUN_DURATION in seconds)
starttime=`date +%s`
while [ $(( $(date +%s) - $RUN_DURATION )) -lt $starttime ]; do

   # Create the new folder and remove it before if it already exists
   echo
   
   # Remove the new folder if it already exist
   if [ -d folder_$folder_counter ]; then 
       echo "Delete an old existing folder folder_$folder_counter (`du -h folder_$folder_counter | cut -f1`B)" 
       /bin/rm -rf folder_$folder_counter
   fi
   echo "Create folder folder_${folder_counter}"
   /bin/mkdir -p folder_${folder_counter}
   cd folder_${folder_counter}

   # Create 4 files of CREATE_FILE_SIZE_IN_GB GB
   for i in 1 2 3 4; do

      # Check and free space if necessary/possible
      free_space=$(df --output=avail . | sed -n 2p)
      free_space_in_GB=`expr $free_space / $size_1GB_in_KB`
      # echo "Free space $free_space_in_GB GB versus $MIN_FREE_SSD_SPACE_IN_GB GB"
      while [ $free_space_in_GB -lt $MIN_FREE_SSD_SPACE_IN_GB ]; do

         # Remove the oldest folder folder_* different than the current folder folder_*
	 cd "$SSD_PATH"
	 oldest_folder=`ls -ltrd folder_[0-9]*/ 2> /dev/null | head -n 1 | awk '{ print $NF }' | cut -f1 -d/`
	 exist_a_folder_to_delete=0
	 if [ ! "$oldest_folder" = "" ]; then
	    
            # oldest_folder is not the current folder
	    if [ ! "$oldest_folder" = "folder_$folder_counter" ]; then
	        exist_a_folder_to_delete=1
	        echo "Delete the oldest folder $oldest_folder (`du -h $oldest_folder | cut -f1`B)"
                /bin/rm -rf $oldest_folder
                free_space=$(df --output=avail . | sed -n 2p)
                free_space_in_GB=`expr $free_space / $size_1GB_in_KB`
                echo "Free space under $SSD_PATH : $free_space_in_GB GB"
	    fi
	 fi

	 if [ $exist_a_folder_to_delete -eq 0 ]; then
	     echo "No folder to remove, abort the script $0"
             echo
             echo "Finished time : " `date +"%d/%m/%Y - %H:%M:%S"`

             # Display the remaining space on the SSD disk
             free_space=$(df --output=avail . | sed -n 2p)
             free_space_in_GB=`expr $free_space / $size_1GB_in_KB`
             echo "Free space under $SSD_PATH : $free_space_in_GB GB"
             cd "$current_pwd0"
	     exit 1
	 fi

         cd folder_${folder_counter}
      done
      # End while Check and free space if necessary/possbile

      echo " - Write file : file_$i.raw"
      dd if=/dev/zero of=file_$i.raw bs=1 count=0 seek=${CREATE_FILE_SIZE_IN_GB}G status=none

      sleep $DELAY_BTW_2FILES
   done
   # End of for loop to create 4 files in the folder
  
   cd "$SSD_PATH"

   # Increment or reset to 1 the folder counter
   if [ $folder_counter -lt 99 ]; then
      folder_counter=`expr $folder_counter + 1`
   else
      folder_counter=1
   fi

done
# end while loop Repeat X times

# Display end time
echo
echo "Finished time : " `date +"%d/%m/%Y - %H:%M:%S"`

# Display the remaining space on the SSD disk
free_space=$(df --output=avail . | sed -n 2p)
free_space_in_GB=`expr $free_space / $size_1GB_in_KB`
echo "Free space under <$SSD_PATH> : $free_space_in_GB GB"

cd "$current_pwd0"

exit 0
