#!/bin/sh

for DAYS in `seq 730`; do
  DATE=`date -d "2019-09-29 +$DAYS days" +%Y%m%d`

  FILES=`ls | grep ^$DATE`
  if [ -z "$FILES" ]; then
    continue
  fi

  TEMPDIR=`mktemp -d`

  for CSVGZ in $DATE-*.csv.gz; do
    CSV=`mktemp`
    NEWCSV=$TEMPDIR/`echo $CSVGZ | sed 's/\.gz//'`
    cat $CSVGZ | gunzip > $CSV
  
    DEVICE_ID=`head -n 2 $CSV | tail -n 1 | awk -F, '{print $2}'`
    NEW_DEVICE_ID=`echo $DEVICE_ID | sed -e 's/-/_/g'`

    NEWCSV=$TEMPDIR/`echo $CSVGZ | sed -e 's/\.gz//' -e "s/$DEVICE_ID/$NEW_DEVICE_ID/g"`

    head -n 1 $CSV | python3 convert-header.py > $NEWCSV
    tail -n +2 $CSV >> $NEWCSV
    sed -i -e "s/$DEVICE_ID/$NEW_DEVICE_ID/" $NEWCSV
  
    rm $CSV
  done

  python3 /home/qi/restore_csv_data_with_qfeeder.py $TEMPDIR/
  if ! [ $? -eq 0 ]; then
    exit 1
  fi
  rm -r $TEMPDIR

  mv $DATE-*.csv.gz finish/
done
