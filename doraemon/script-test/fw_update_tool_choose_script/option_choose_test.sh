#!/bin/bash  

func() {
    echo "Usage:"
    echo "option_choose_test.sh [-h123] [<device>] [<filename>]"
    echo "Description:"
    echo "-1                   Use hdparm tool."
    echo "-2                   Use nvme-cli tool."
    echo "-3                   Use DLMC tool."
    echo "-4                   Use iSMART tool."
    echo "device               Which device need to DLMC."
    echo "FW name              Choose the FW bin file."
    echo "Hdparm Example:      ./option_choose_test.sh -1 /dev/sdx abc.bin"
    echo "NVME Example:        ./option_choose_test.sh -2 /dev/sdx abc.bin"
    echo "DLMC Example:        ./option_choose_test.sh -3 /dev/sdx abc.bin"
    echo "iSMART Example:      ./option_choose_test.sh -4 /dev/sdx"
    exit -1
}

if [ -z $1 ] ; then 
    func
    exit 0
elif [ $1 != "-1" ] && [ $1 != "-2" ] && [ $1 != "-3" ] && [ $1 != "-4" ]; then 
    func
elif [ -z $2 ] && [ $1 != "-h" ] ; then 
    echo "Miss device"; 
    exit 0
elif [ $1 == "-1" ] && [ -z $3 ]; then 
    echo "Miss bin file";
    exit 0 
elif [ $1 == "-2" ] && [ -z $3 ]; then 
    echo "Miss bin file";
    exit 0 
elif [ $1 == "-3" ] && [ -z $3 ]; then 
    echo "Miss bin file";
    exit 0 
fi

while getopts h1:2:3:4: option  
do  
    case $option in  
        1)
        hdparm --yes-i-know-what-i-am-doing --please-destroy-my-drive --fwdownload-mode7 $3 $2
        ;;  
        2)
        nvme fw-download $2 -f $3
        nvme fw-commit $2 -s 1 -a 1
        ;;  
        3)
        ./DLMicro_64  -d $2 -f $3
        ;; 
        4)
        ./iSMART_64  -d $2
        ;; 
        h)
        func
        ;;
        *)
        echo "Invalid arg!"
        ;;  
        ?)
        func
        exit -1
        ;;  
    esac  
done  
