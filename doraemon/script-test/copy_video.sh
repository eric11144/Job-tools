#!/bin/sh

count=1
file_path="/media/ubuntu/38B96F392ECD8490"

echo "start copy file"

while true;
do
    if [ -d "$file_path/test" ]; then
        echo $count
        cp test.avi $file_path/test/
        mv $file_path/test/test.avi $file_path/test/test_$count.avi
        count=$(( count + 1 ))
        du -h $file_path/test/
        sleep 5
    else 
        mkdir $file_path/test
    fi
done
