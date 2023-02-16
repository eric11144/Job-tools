# iSMART Linux #
## iSMART Disk Info ##

![command](/home/ubuntu/command.png)
`sudo ./iSMART_64 -d /dev/sda -a 1`  
* `-d` : 指定查詢 `Disk`
* `-a 1 `: 將 `iAnalyzer` 開啟.

![disk_info](/home/ubuntu/disk_info.png)  
* `Model name`: `產品號`
* `Serial Num`: `序號`
* `FW Version`: `外顯 FW`
* `WWN / EUI64`: `全球名稱`

* `BusType`: `硬碟匯流排類型( Serial Attached SCSI(SAS) )`
* `Capacity`: `硬碟容量`
* `LABs`: `區塊位址數`
* `Health`: `健康度`
* `P/E Cycle`: `寫入/抹除次數`
* `AVG. Erase`: `平均抹除次數`
* `Temperature`: `硬碟溫度`
* `Power on Hours`: `上電時間(小時)`
* `Power ON Cycle`: `上電次數`
* `LBA48`: `磁碟讀取方式`
* `HPA`: `主機保護區`
* `NCQ`: `命令緩衝區`
* `TRIM`: `ATA資料集管理指令`
* `Security`: `加密`
* `TSensor`: `溫度感測器`
* `Crypto Erase`: `加密刪除`
* `Transfer`: `傳輸模式`
* `Interface`: `傳輸界面`
* `Standard`: `規範`
* `Analyzer`: `分析儀`
* `Write Protect`: `寫入保護`
* `InnoRobust`: `資料安全技術`
* `QErase`: `快速清除`

![smart_info](/home/ubuntu/smart_info.png)  

* `Later Bad`: `使用後造成故障區塊數`
* `Power On Hours`: `上電時間(小時)`
* `Power Cycle Count`: `上電次數`
* `Total Bad Block Count`: `總共故障區塊數`
* `Max Erase Count`: `最大抹除數`
* `Avg Erase Count`: `平均抹除數`
* `Device Life`: `硬碟壽命`
* `Spare Block Count`: `備用區塊數`
* `Program Fail Count`: `程序失敗次數`
* `Erase Fail Count`: `抹除失敗次數`
* `Abnormal power cycle count`: `不正常斷電次數`
* `Temperature`: `溫度`
* `Flash ID`: `Flash ID`
* `Later Bad Block Read`: `使用後造成故障區塊數(讀取)`
* `Later Bad Block Write`: `使用後造成故障區塊數(寫入)`
* `Later Bad Block Erase`: `使用後造成故障區塊數(抹除)`
* `Total LBAs Written`: `總區塊位址數(寫入)`
* `Total LBAs Read`: `總區塊位址數(讀取)`

![seq_read](/home/ubuntu/seq_read.png)  

![seq_write](/home/ubuntu/seq_write.png)  

![rand_read](/home/ubuntu/rand_read.png)

![rand_write](/home/ubuntu/rand_write.png)  