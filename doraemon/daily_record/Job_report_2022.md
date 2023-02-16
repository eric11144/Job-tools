# 工作日誌 #

# 2022-01-01
* 交付 `溫度量測` 最新程式於家名.
* TODO
    * [x] 協助家名測試 `溫度量測` 程式.

# 2022-01-03
* 協助家名測試 `溫度量測` 程式.
  * 修正 `溫度狀態值` 初始化問題.
  * 修正 `溫度正常值`, `溫度異常值` 加減造成數值小數點失真問題.
* TODO
  * [x] 協助家名測試 `RPI4` 多組 `I2C` 功能.
  * [x] 協助家名查詢 `類比訊號` 輸入腳位.

# 2022-01-04
* 協助家名查詢 `RPI4` 多組 `I2C` 功能.
* 協助家名查詢 `類比訊號` 輸入腳位, 查詢文獻後, 發現無此功能.
* TODO
  * [x] 協助家名測試 `RPI4` 多組 `I2C` 功能.
  * [x] 測試 `Modbus RTU` 通訊功能.

# 2022-01-05
* 協助家名測試 `RPI4` 多組 `I2C` 功能, 經測試後, 無法使用 `I2C 0`, 需透過電路板串接於同一個腳位測試.
* 測試 `Modbus RTU` 通訊功能, 目前尚未測通, 已和家名討論.
* TODO
  * [x] 測試 `Modbus RTU` 通訊功能.
  * [x] 安裝變色龍於 `MXE-201` 測試 `Modbus RTU`.
  * [x] 測試透過 `Modbus RTU client` 通訊 `Box2` `Modbus RTU`.

# 2022-01-06
* 測試 `Modbus RTU` 通訊功能, 後續發現端子台位置 `6` 與 `9` 相反( `RS485 +` -> `1`, `RS485 -` -> `9` ).
* 安裝變色龍於 `MXE-201` 測試 `Modbus RTU`, 已成功通訊.
* 測試透過 `Modbus RTU client` 通訊 `Box2` `Modbus RTU`, 已測試成功, 執行程式時, 需加上 sudo.
* TODO
  * [x] Nothing.

# 2022-01-07
* Nothing.
* TODO
  * [x] 與家名取得並測試 `TOF-10120` 距離感測器.

# 2022-01-10
* 與家名取得並測試 `TOF-10120` 距離感測器.
* TODO
  * [x] 於 `RPI4` 接上訊號線並測試 `TOF-10120` 距離感測器.
  * [x] 查詢 `TOF-10120` 距離感測器使用方法.

# 2022-01-11
* 於 `RPI4` 接上訊號線並測試 `TOF-10120` 距離感測器, 已成功將數據讀取出來, 並與溫度感測器合併做測試, 已將狀況回報.
* TODO
  * [x] 協助家名測試 `距離感測器` 距離遠近反應.
  * [x] 提供 `距離感測器` source code.

# 2022-01-12
* 協助家名測試 `距離感測器` 距離遠近反應.
* 提供 `距離感測器` source code.
* TODO
  * [x] 觀看英文影片.

# 2022-01-13
* 觀看英文影片.
* TODO
  * [x] 觀看英文影片.
  * [x] `1/18` 前往蘆竹區藥廠測試.

# 2022-01-14
* 觀看英文影片.
* TODO
  * [x] 協助家名現場測試 `距離感測器`.

# 2022-01-17
* 協助家名現場測試 `距離感測器`.
* TODO
  * [x] 尋找郵局本子, 並拍照提供給家名.
  * [x] 觀看 `C++` 環境架設.

# 2022-01-18
* 尋找郵局本子, 並拍照提供給家名.
* 觀看 `C++` 環境架設.
* TODO
  * [x] 前往蘆竹 `瑞健集團` 藥廠出差.

# 2022-01-19
* 前往蘆竹 `瑞健集團` 藥廠出差.
  * 透過 `Box2` 將 `FX1N` PLC 資料透過 `RS-422` 讀取出來, 並傳送至 `OPCUA`.
  * 過程發生 `Box2` 無法將專案寫入錯誤, 後續將專案匯入至 `USB` 重制 `Box2`, 再重新下載專案即可.
* TODO
  * [x] 協助家名詢問 `欣興電子-蘆竹二廠` 快速入場問題.

# 2022-01-20
* 協助家名詢問 `欣興電子-蘆竹二廠` 快速入場問題.
* TODO
  * [x] 協助家名觀看電子投幣器相關 `API` 操作文件.

# 2022-01-21
* 協助家名觀看電子投幣器相關 `API` 操作文件.
  * `API` 主要透過 `RS-422` 傳送相關 `Json` 格式.
  * 傳送時間間隔最少為 `1` 秒.
  * 相關應用寫於 `P25` 後.
* TODO
  * [x] 協助家名研究 `Viber message` & `MSSQL` 串接.
  * [x] 協助家名研究 `Apache Kafka` 使用.

# 2022-01-22
* 協助家名研究 `Viber message` API 使用方法, 目前尚未完成.
* TODO
  * [x] 協助家名處理 `溫度量測` 無感測器 以及 程式重起相關功能.

# 2022-01-24
* 協助家名處理 `溫度量測` 無感測器 以及 程式重起相關功能.
  * 透過 `systemd` 啟動 & 重啟.
    * [Unit]
      Description=Start Temp Scan

      [Service]
      Environment=DISPLAY=:0.0
      Environment=XAUTHORITY=/home/pi/.Xauthority
      ExecStart=/usr/bin/python3 /home/pi/pyqtgraph_temp.py
      Restart=always
      RestartSec=10s
      KillMode=process

      [Install]
      WantedBy=graphical.target
* TODO
  * [x] 測試 `viber` 傳送訊息環境.

# 2022-01-25
* 測試 `viber` 傳送訊息環境, 以及研究如何架設 `webhook`, 後續發現需要透過架設 `webhook` 才可傳送訊息, 以及 `https` 相關認證問題, 暫時無法完成, 已將狀況回報.
* TODO
  * [x] 與 `欣興電子-蘆二廠` 窗口了解相關智慧化工廠後續規劃.

# 2022-01-26
* 與 `欣興電子-蘆二廠` 窗口了解相關智慧化工廠後續規劃.
* TODO
  * [x] 陪同前往設計公司收帳.

# 2022-01-27
* 陪同前往設計公司收帳.
* TODO
  * [x] 協助家名新增 `溫度量測` 相關功能(距離數值累積五次後, 開始量測溫度).

# 2022-06-06
* 準備 `宜鼎` 報到相關資料.
* TODO
  * [x] 前往 `宜鼎` 報到.

# 2022-06-07
* 前往 `宜鼎` 報到.
  * 自我快篩.
  * 填寫個人資料, 以及自傳.
  * `HR` 導覽公司環境.
  * 觀看組內實驗室, 以及相關環境.
  * 制定 `試用期` 3 個月目標.
  * 觀看 `新人線上訓練( EIP, eHRD, Outlook )`, `同仁資訊安全通識`, `綠色產品概述` 課程影片.
  * 觀看 `Linux` 之 `FIO`, `Hdparm` 相關指令操作.
* TODO
  * [x] 觀看 `危害性化學品標示及通識規則` 課程影片.
  * [x] 觀看 `新人基礎訓練` 課程影片.
  * [x] 觀看 `新人進階訓練` 課程影片.
  * [x] 參與組內週會.
  * [x] Miller 講解公司組織圖.

# 2022-06-08
* 觀看 `危害性化學品標示及通識規則` 課程影片.
* 觀看 `新人基礎訓練` 課程影片.
  * `勞工安全衛生及工作環境維護`.
  * `健康促進`.
  * `保密與合約流程`.
  * `假勤與使用說明`.
  * `員工福利委員會說明`.
  * `生產流程與 5S 現場規範`.
* 觀看 `新人進階訓練` 課程影片.
  * `基礎產品介紹-DRAM`.
  * `基礎產品介紹-FLASH`.
  * `基礎產品介紹-EP`.
  * `教育訓練簡介`.
  * `公司電腦使用注意事項`.
  * `智慧財產權-商標, 專利, 著作權`.
  * `品質系統介紹`.
* 參與組內週會.
* Miller 講解公司組織圖.
* TODO
  * [x] 觀看 `SATA` 基本架構.
  * [x] 觀看 `OOB` 相關資料.
  * [x] 與 `Nick` 預約講解時間.
  * [x] 觀看組內訓練影片.
    * [x] `簡易 DRAM 工作原理介紹`.
    * [x] `DRAM Part Number Decoder`.
    * [x] `DRAM IC suppliers`.
    * [x] `DRAM competitors`.
    * [x] `iRAID Product brief`.
    * [x] `SOP and BOM Table Inquiry`. 

# 2022-06-09
* 觀看 `SATA` 基本架構.
* 觀看 `OOB` 相關資料.
* 與 `Nick` 預約講解時間, 目前訂為 `6/10` 下午.
* 觀看組內訓練影片.
  * `簡易 DRAM 工作原理介紹`.
  * `DRAM Part Number Decoder`.
  * `DRAM IC suppliers`.
  * `DRAM competitors`.
  * `iRAID Product brief`.
  * `SOP and BOM Table Inquiry`. 
* TODO
  * [x] 觀看 `OOB` 相關資料.
  * [x] 整理幾周觀看影片之英文單字.
  * [x] 觀看組內訓練影片.
    * [x] `EP Introduction`.
    * [x] `EP CANbus overview`.
    * [x] `SSD 產品常見故障檢測排查`.
    * [x] `案例分享`.
    * [x] `SSD Structure Basic 1`.

# 2022-06-10
* 觀看 `OOB` 相關資料.
* 整理幾天觀看影片之英文單字.
* 觀看組內訓練影片.
  * `EP Introduction`.
  * `EP CANbus overview`.
  * `SSD 產品常見故障檢測排查`.
  * `案例分享`.
  * `SSD Structure Basic 1`.
* TODO
  * [x] 參與公司內部 `PSM` 技術分享會議.
  * [x] 觀看組內訓練影片.
    * [x] `SSD Structure Basic 2`.
    * [ ] `FW-File System & Hard Disk contorl`.
    * [ ] `FW-Flash Operation-Block Mode Introduction`.
  * [x] 聽 `Nick` 講解 `OOB` & `示波器使用`.

# 2022-06-13
* 參與公司內部 `PSM` 技術分享會議.
* 觀看組內訓練影片.
  * `SPD code programing process`.
  * `DRAM 燒機測試軟體使用( DRAM burn-in tool )`.
  * `SSD Structure Basic 2`.
* 聽 `Nick` 講解 `OOB` 流程, 組內測試 `SSD` 相關工具, 問題解決相關流程.
* TODO
  * [x] 觀看組內訓練影片.
    * [x] `FW-File System & Hard Disk contorl`.
    * [x] `FW-Flash Operation-Block Mode Introduction`.
    * [x] `顆粒組態計算(DRAM capacity caculation method)`.
    * [x] `內存與系統架構(Memory and system structure)`.
    * [x] `DRAM 故障分析(DRAM defect analysis - I)`.
  * [x] `Nick` 協助我了解樓層單位( `QA`, `PE`, `佩佩`, `PM`, `業務` ).
  * [x] 架設 `Ubuntu OS` 環境電腦.

# 2022-06-14
* 觀看組內訓練影片.
  * `FW-File System & Hard Disk contorl`.
  * `FW-Flash Operation-Block Mode Introduction`.
  * `顆粒組態計算(DRAM capacity caculation method)`.
  * `內存與系統架構(Memory and system structure)`.
  * `DRAM 故障分析(DRAM defect analysis - I)`.
* `Nick` 協助我了解樓層單位( `QA`, `PE`, `佩佩`, `PM`, `業務`, `硬體單位實驗室` ).
* 架設 `Ubuntu OS` 環境電腦.
* TODO
  * [ ] 參加組內週會.
  * [ ] 下午與 kenzi 討論後續進度會議.
  * [x] 觀看組內訓練影片.
    * [x] `DRAM 故障分析(DRAM defect analysis - II)`.
    * [x] `Data Retention`.
    * [ ] `Product_An Introduction to SSDs`.

# 2022-06-15
* 觀看組內訓練影片.
  * `DRAM 故障分析(DRAM defect analysis - II)`.
  * `Data Retention`.
* 與 Miller 討論學習目標.
  * 熟悉組內相關產品開卡流程, 以及注意事項( 修改 `序號`, `外顯 FW`, `WWN`, `EUI64` ).
  * 進階學習 `3TE7` 如何修改 `Phy` 設定.
  * `FIO` tool 相關操作學習. 
* 觀看 `FIO` 相關操作, 以及操作文件.
* TODO
  * [x] 觀看組內訓練影片.
    * [x] `DRAM Sales Kit`.
    * [x] `Product An Introduction to SSDs`.
    * [x] `Product Other Solutions`.
  * [x] 向 `Nick` 詢問組內相關產品開卡流程.

# 2022-06-16
* 觀看組內訓練影片.
  * `DRAM Sales Kit`.
  * `Product An Introduction to SSDs`.
  * `Product Other Solutions`.
* 向 `Nick` 詢問組內相關產品開卡流程.
  * 學習如何操作 `iSMART`, 以及需先將 `起始 Disk 資訊`, `Device Information`, `S.M.A.R.T` 畫面擷取並存取歸檔.
  * 觀看硬碟上的 `IC` 編號, 至 `EIP` 內的 `ePLM` -> `Inno PLM` 輸入產品 `P/N`, 查詢 `IC` 編號 Double check.
  * 透過 `iPacker` 輸入 `P\N` 取得該產品開卡包.
  * 至 `C://pack/xxxxx/` 點選 `MXMPTool_MAP100x.exe`, 執行開卡程式.
  * 確認開卡程式是否抓到硬體.
  * 點選 `Auto Detect` 點選硬體對應之 `IC` 編號 `FW`.
  * 至 `Device Setting` 頁面修改相關參數.
    * `Firmware Version( 外顯 FW )`.
    * `Serial Number( 序號 )`.
* 練習將硬碟 `Firmware Version( 外顯 FW )`, `Serial Number( 序號 )` 修改正確.
* 安裝 `Windows 10` 環境.
* TODO
  * [x] 協助 `Nick` 處理產品 `RMA`.
  * [x] 聽取 `Nick` 講解 `USB` 相關認證資訊.
  * [x] 統計週邊缺少之設備, 以便日後採購.
  * [x] 繼續處理 `Windows 10` 環境.
  * [x] 觀看 `WWN`, `EUI64` 命名相關規則.
  * [x] 練習將硬碟 `EUI64` 修正正確.
  * [x] 測試桌上相關 `SSD` 是否可以透過 `轉板` 讀取到.
  * [x] 觀看 `眼圖` 相關應用原理.

# 2022-06-17 
* 協助 `Nick` 處理產品 `RMA`.
* 聽取 `Nick` 講解 `USB` 相關認證資訊, 以及如何使用組內顯微鏡.
* 統計週邊缺少之設備, 以便日後採購.
* 繼續處理 `Windows 10` 環境, 後續發現需透過 `Windows` 環境格式化硬碟, 不可透過 `Ubuntu` 格式化, 否則會無法讀取到.
* 觀看 `WWN`, `EUI64` 命名相關規則.
* 練習將硬碟 `EUI64` 修正正確, 並透過開卡程式修改.
* 測試桌上相關 `SSD` 是否可以透過 `轉板` 讀取到.
* 觀看 `眼圖` 相關應用原理.
* TODO
  * [ ] `Kenzi` 教導觀看 `電路圖`.
  * [x] 索取新版開卡程式, 以及 `3TE7` 轉卡板.
  * [x] 練習如何修改 `WWN`, 並驗證.
  * [x] 協助 `Nick` 紀錄 `4` 張 `3TE7` `SMART` 截圖.
    * [X] `YCA12105050041254`.
    * [X] `YCA12105050020576`.
    * [X] `YCA12105050040158`.
    * [X] `YCA12105050032926`.
  * [x] 協助 `Nick` 開卡 `3TE7`, 並將 `Serial Numer`, `WWN/EUI64` 修正正確.
    * [x] `BCA12112240320009`.
  * [x] 領取 `防靜電衣`, 以及 `拖鞋`.
  * [x] 觀看 `眼圖` 相關資料.
  * [x] `Nick` 教導如何操作 `示波器` 以及 `眼圖` 的操作形成.
  * [x] 參加 `Intel AI Tech` 分享會.
  * [x] 測試讀取 `3TG6-P` 以及 `開卡` 流程.

# 2022-06-20
* 索取新版開卡程式, 以及 `3TE7` 轉卡板.
* 練習如何修改 `WWN`, 並透過 `iSMART` 驗證.
* 協助 `Nick` 紀錄 `4` 張 `3TE7` `SMART` 截圖.
  * `YCA12105050041254`.
  * `YCA12105050020576`.
  * `YCA12105050040158`.
  * `YCA12105050032926`.
* 協助 Nick 開卡 `3TE7`, 並將 `Serial Numer`, `WWN/EUI64` 修正正確.
  * `BCA12112240320009`.
* 領取 `防靜電衣`, 以及 `拖鞋`.
* 觀看 `眼圖` 相關資料.
* `Nick` 教導如何操作 `示波器` 以及 `眼圖` 的操作形成.
* 參加 `Intel AI Tech` 分享會.
* 測試讀取 `3TG6-P` 以及 `開卡` 流程.
* TODO
  * [x] 協助 `Nick` 寄送產品回 `Kinoshita`.
  * [x] 觀看 `FIO` 相關操作指令, 以及 `log` 欄位資訊.
  * [x] 參與 `Nick` & `Kenzi` 電路圖 Review.
  * [x] 協助 `Nick` 擷取 `北捷` 送修之 `mSATA-3ME4` 硬碟( `YCA12004090320028`, `YCA12004090320024` ).
  * [x] 觀看及查詢 `iSMART` 相關欄位意義( `Later bad`, `訊號問題欄位`, `ECC` ).

# 2022-06-21
* 協助 `Nick` 寄送產品回 `Kinoshita`.
* 觀看 `FIO` 相關操作指令, 以及 `log` 欄位資訊.
* 參與 `Nick` & `Kenzi` 電路圖 Review.
* 協助 `Nick` 擷取 `北捷` 送修之 `mSATA-3ME4` 硬碟( `YCA12004090320028`, `YCA12004090320024` ).
* 觀看及查詢 `iSMART` 相關欄位意義( `Later bad`, `訊號問題欄位`, `ECC` ).
* TODO
  * [x] 觀看及查詢 `iSMART` 相關欄位意義( `Later bad`, `訊號問題欄位`, `ECC` ).
  * [x] 與 `Nick` 了解烘烤機如何使用.
  * [x] 整理進幾周訓練表單與完成時間.
  * [x] 與 `Kenzi` 討論訓練表單時間與人員.
  * [x] 練習 `3TE7` 開卡流程, 以及修改相關欄位.
  * [x] 協助 `Nick` 錄製 `Nexcom` 報修產品( `M.2(S42) 3TE7` ).
    * [x] `YCA12105050032926`.
    * [x] `YCA12105050040158`.
    * [x] `YCA12105050041254`.
    * [x] `YCA12105050020576`.

# 2022-06-22
* 觀看及查詢 `iSMART` 相關欄位意義( `Later bad`, `訊號問題欄位`, `ECC` ).
* 與 `Nick` 了解烘烤機如何使用.
* 整理進幾周訓練表單與完成時間.
* 與 `Kenzi` 討論訓練表單時間與人員.
* 練習 `3TE7` 開卡流程, 以及修改相關欄位.
* 協助 `Nick` 錄製 `Nexcom` 報修產品( `M.2(S42) 3TE7` ).
  * `YCA12105050032926`.
  * `YCA12105050040158`.
  * `YCA12105050041254`.
  * `YCA12105050020576`.
* TODO
  * [ ] 協助 `Nick` 烘烤產品(環測).
  * [x] 討論新人訓練相關表單.
  * [x] `Nick` 教導如何使用 `熱風槍`, `焊槍`, `吸錫器`, `清潔劑`, `錫油.`
  * [x] 借取相關開卡練習設備.
    * [x] `3ME3`(開卡須特殊轉板, 與讀取轉板不同).
    * [x] `3ME4/3IE4`.
    * [ ] `3MG2-P`.
    * [x] `3TE7`.
    * [ ] `3TG6-P`.
    * [ ] `3ME2/3TE2`(`cold`).
    * [x] `3TE6`.
  * [x] 安裝 `Linux` 版本 `iSMART`, 並了解操作.
  * [x] 報修電腦, 以及網路設定.
  * [x] 參加組內 `Global TSE Meeting`.

# 2022-06-23
* 討論新人訓練相關表單.
* `Nick` 教導如何使用 `熱風槍`, `焊槍`, `吸錫器`, `清潔劑`, `錫油.`
* 借取相關開卡練習設備.
    * `3ME3`(開卡須特殊轉板, 與讀取轉板不同).
    * `3TE7`.
    * `3IE4`.
  * 安裝 `Linux` 版本 `iSMART`, 並了解操作.
  * 報修電腦, 以及網路設定.
  * 參加組內 `Global TSE Meeting`.
* TODO
  * [x] `Nick` 講解相關 `硬碟` 測試工具.
  * [x] `Nick` 講解 `Download Micro code` 相關流程.
  * [x] 練習 `3TG6-P` 開卡.
  * [x] 撰寫 `iSMART` 相關解釋文件.

# 2022-06-24
* `Nick` 講解相關 `硬碟` 測試工具.
* `Nick` 講解 `Download Micro code` 相關流程.
* 練習 `3TG6-P` 開卡.
  * 遇到開卡任不到設備, 最後是直接接上主機板進行開卡.
  * 開卡須點選 `FW` `bin` 檔案, 否則會造成開卡失敗, 進入 `Load Mode`.
  * `WWN` 欄位於開卡包未看到, 需向研發單位索取. 
* 撰寫 `iSMART` 相關解釋文件.
* TODO
  * [x] 前往 `5` 樓參加新進員工健康諮詢.
  * [x] 與 `Miller` 簡述報告 `Topic` 執行進度.
  * [x] 練習 `3IE4` 開卡動作.
  * [x] 協助 `Nick` 側錄 `3TE7` `UART` log.
  * [x] 觀看組內訓練影片.
    * [x] `SLC Cache Technology`.
    * [x] `iCAP Product brief`.
    * [x] `iCAP features`.
    * [x] `QVS 系統教學`.
    * [x] `Product SATA Modules`.

# 2022-06-27
* 前往 `5` 樓參加新進員工健康諮詢.
* 與 `Miller` 簡述報告 `Topic` 執行進度.
* 練習 `3IE4` 開卡動作.
* 協助 `Nick` 側錄 `3TE7` `UART` log.
* 觀看組內訓練影片.
  * `SLC Cache Technology`.
  * `iCAP Product brief`.
  * `iCAP features`.
  * `QVS 系統教學`.
  * `Product SATA Modules`.
* TODO
  * [x] 撰寫 `3MG2-P` `SMART` 欄位意義.
  * [x] 與 `Miller`, `Nick`, `Kenzi` 報告進度以及 `iSMART`.

# 2022-06-28
* 撰寫 `3MG2-P` `SMART` 欄位意義.
* 與 `Miller`, `Nick`, `Kenzi` 報告進度以及 `iSMART`.
* TODO
  * [x] 觀看 `iSLC`, `GC`, `TRIM`, `AES`.
  * [ ] 觀看 `Page Mode`, `Block Mode`.
  * [ ] 觀看 `Read Desterver`.
  * [ ] 查詢 `SSD Thermal Throttling`.
  * [ ] 觀看 `SSD 產品常見故障檢測` PPT, 並學習如何講解.
  * [ ] 測試產品開卡包
    * [ ] `SATA`: `3MG2-P`
    * [ ] `PCIe`: `3TG3-P`, `3TE6-P`, `3TG6-P`.

# 2022-06-29
* 觀看組內訓練影片
  * `Product SSD`.
  * `Techincal AES`.
  * `Technical iCell and iData Gurad`.
  * `Technical iSLC GC TRIM`.
  * `Technical iSMART`.
* 參與 `RD` 月報會.
* TODO
  * [x] 觀看 `Page Mode`, `Block Mode`.
  * [ ] 觀看 `Read Disturb`.
  * [ ] 查詢 `SSD Thermal Throttling`.
  * [ ] 觀看 `SSD 產品常見故障檢測` PPT, 並學習如何講解.
  * [ ] 測試產品開卡包
    * [ ] `SATA`: `3MG2-P`
    * [ ] `PCIe`: `3TG3-P`, `3TE6-P`, `3TG6-P`.

# 2022-06-30
* 觀看組內訓練影片
  * `Technical Other Characteristics of SSD`.
  * `Technical Page mode & Block mode`.
  * `Technical Pin7 & Pin8`.
  * `Vertical market Gaming Market Sales kit`.
  * `Flash 101-CHT`.
* TODO
  * [x] 觀看 `Read Disturb`.
  * [x] 查詢 `SSD Thermal Throttling`.
  * [ ] 觀看 `SSD 產品常見故障檢測` PPT, 並學習如何講解.
  * [ ] 測試產品開卡包
    * [ ] `SATA`: `3MG2-P`
    * [ ] `PCIe`: `3TG3-P`, `3TE6-P`, `3TG6-P`.

# 2022-07-01
* 觀看 `Read Disturb`.
* 查詢 `SSD Thermal Throttling`.
* 觀看組內訓練影片
  * `Flash Reliability`.
  * `NAND Flash Characterization, Mitigation and Recovery`.
* TODO
  * [x] 觀看 `SSD 產品常見故障檢測` PPT, 並學習如何講解.
  * [ ] 測試產品開卡包
    * [ ] `SATA`: `3MG2-P`
    * [ ] `PCIe`: `3TG3-P`, `3TE6-P`, `3TG6-P`.

# 2022-07-04
* 參加 `PSM` 會議.
* 觀看 `SSD 產品常見故障檢測` PPT, 並學習如何講解.
* TODO
  * [x] 觀看組內訓練影片
    * [x] `NAND Flash 文件摘要介紹`.
    * [x] `Storage System & SATA Interface`.
    * [x] `Vertical market Military Market Sales kit`.
    * [x] `Vertical market In Vehicle computing system`.
    * [x] `Server Boot-up market sales kit`.
    * [x] `Military Market Sales kit`.
  * [x] 與 `Kenzi` 討論進度以及了解 `FTA` 文件擺放位置.
  * [ ] 測試產品開卡包
    * [ ] `SATA`: `3MG2-P`
    * [ ] `PCIe`: `3TG3-P`, `3TE6-P`, `3TG6-P`.

# 2022-07-05
* 觀看組內訓練影片
  * `NAND Flash 文件摘要介紹`.
  * `Storage System & SATA Interface`.
  * `Vertical market Military Market Sales kit`.
  * `Vertical market In Vehicle computing system`.
  * `Server Boot-up market sales kit`.
  * `Military Market Sales kit`.
* 與 `Kenzi` 討論進度以及了解 `FTA` 文件擺放位置.
* TODO
  * [ ] 觀看 `FTA` 文件.
  * [x] 修改 `SSD 產品常見故障檢測` 文件.
  * [x] 參加組內 `FAE` 週會.
  * [ ] 測試產品開卡包
    * [ ] `SATA`: `3MG2-P`
    * [ ] `PCIe`: `3TG3-P`, `3TE6-P`, `3TG6-P`.

# 2022-07-06
* 修改 `SSD 產品常見故障檢測` 文件, 以及練習講解.
* 參加組內 `FAE` 週會.
* TODO
  * 撰寫 `Disk 專有名詞介紹` PPT.
  * [x] 報告第一個月 `Topic`.
    * [x] `Disk 專有名詞介紹`.
    * [ ] `SSD 產品常見故障檢測`.
  * [ ] 測試產品開卡包
    * [ ] `SATA`: `3MG2-P`
    * [ ] `PCIe`: `3TG3-P`, `3TE6-P`, `3TG6-P`.

# 2022-07-07
* 撰寫 `Disk 專有名詞介紹` PPT.
* 報告第一個月 `Topic`.
  * `Disk 專有名詞介紹`. 
* 查找 `GC`, `TRIM` 詳細介紹.
* TODO
  * [x] `Nick` 教育訓練
    * [x] `FW release information query`.
    * [x] `Myinnodisk operation`.
  * [x] `Kenzi` 教育訓練
    * [x] `Chamber` 操作.
    * [x] `BurnInTest` 操作.
    * [x] `Flash product training`.
    * [x] `Known Issue on existing product`.
    * [x] `產品編碼原則( Product Coding Rule )`.
  * [x] 處理 `新漢` 客訴案, 並將 `UART` log 傳給 `FW`. 

# 2022-07-08
* `Nick` 教育訓練
  * `FW release information query`.
  * `Myinnodisk operation`.
* `Kenzi` 教育訓練
  * `Chamber` 操作.
  * `BurnInTest` 操作.
    * 每次只能寫入容量的 `15%`.
  * `Flash product training`.
  * `Known Issue on existing product`.
  * `產品編碼原則( Product Coding Rule )`.
* 處理 `新漢` 客訴案, 已將 `UART` log 傳給 `FW`, 等 `FW` 觀看結果分析.
* TODO
  * [x] 報修筆電.
  * [x] 撰寫 `hdparm` shell script( 執行次數, 以及速度平均 ).
  * [x] `Nick` 講解 `PE` `PM` `IC` 相關資訊.

# 2022-07-11
* 報修筆電.
* 撰寫 `hdparm` shell script( 執行次數, 以及速度平均 ).
* `Nick` 講解 `PE` `PM` `IC` 相關資訊.
* TODO
  * [x] 觀看 `InnoAGE` 相關資訊.
  * [x] 觀看 `InnoOSR` 相關資訊.
  * [x] 持續追蹤 `新漢` 客訴案, 已將 `UART` log 傳給 `FW`, 等 `FW` 觀看結果分析.
  * [x] 新進同仁關懷.
  * [x] 協助 `PM Jack` 擷取 `iSMART` 相關資訊.

# 2022-07-12
* 觀看 `InnoAGE` 相關資訊.
* 觀看 `InnoOSR` 相關資訊.
* 持續追蹤 `新漢` 客訴案, 已將 `UART` log 傳給 `FW`, 等 `FW` 觀看結果分析.
* 新進同仁關懷.
* 協助 `PM Jack` 擷取 `DES25-01TDK1GC1QL-A15C` `10` 片 `iSMART` 相關資訊.
* TODO
  * [x] 協助 `Kenzi` 觀看客訴問題
    * [x] `3TG6-P` 無法正常 Format.
    * [x] `3MG2-P` 無法安裝 `OS`.
  * [x] 協助 `Miller` 觀看 `CASwell` 客訴案件, 並了解問題狀況.
  * [x] 查找 `Secure Erase` 解決 `Read retry` 問題相關文章.

# 2022-07-13
* 協助 `Kenzi` 觀看客訴問題, 目前都可正常認到碟, `SMART` 並無特別異常數值.
  * `3TG6-P` 無法正常 Format.
  * `3MG2-P` 無法安裝 `OS`.
* 協助 `Miller` 觀看 `CASwell` 客訴案件, 並了解問題狀況.
  * 因 `Disk` 客戶分成 `OS`, `Backup`, `Data`, 但 `OS` 並無時常 `Update`, 造成此區域並無搬移的動作, 故發生 `漏電` 問題 以及 `ECC` 過高, 造成 `Disk` 不斷執行 `Read retry`, 造成 `Command timeout`.
  * `FW` 修改為開機強至執行一次 `Read retry`, 後續 `6s` 執行一次.
  * 目前解法是將 `Flash` 執行 `Secure Erase`, 更新 `FW`, 再安裝 `OS` 可暫時解決問題.
* 查找 `Secure Erase` 解決 `Read retry` 問題相關文章.
* 參與 `CASwell` `EU` 討論會議.
* TODO
  * [x] 前往 `樺漢 Ennoconn` 了解客訴問題, 並擷取相關 `Log`.
  * [x] 協助 `PM Jack` 擷取 `DEMSR-A28DK1GCADF * 10`, `DGS25-01TM71GCAQF * 2` 片 `iSMART` 相關資訊.
  * [x] 與 `Miller` 討論 `樺漢 Ennoconn` 擷取之 `Log`.
  * [x] 發出 `樺漢 Ennoconn` 相關問題以及 `Uart Log` 給 FW.
  * [x] 協助 `Kenzi` 觀看客訴問題, 撈取 `3TG6-P` `Uart Log`.

# 2022-07-14
* 前往 `樺漢 Ennoconn` 了解客訴問題, 並擷取相關 `Log`.
  * 設備上電開機, 進入 `OS`.
  * 進入 `OS`, 點選 `Suspend`.
  * 喚醒後, 設備畫面無法進入 `OS`, 只顯示 `Terminal`.
* 協助 `PM Jack` 擷取 `DEMSR-A28DK1GCADF * 10`, `DGS25-01TM71GCAQF * 2` 片 `iSMART` 相關資訊.
* 與 `Miller` 討論 `樺漢 Ennoconn` 擷取之 `Log`.
* 發出 `樺漢 Ennoconn` 相關問題以及 `Uart Log` 給 `FW`.
* 協助 `Kenzi` 觀看客訴問題, 撈取 `3TG6-P` `Uart Log`, 後續發現撈取都是亂碼, 需要重錄.
* TODO
  * [x] 協助 `FW` 測試 `3TE6` 其他大容量是否有相同問題( `512GB`, `1T` ), 以及其他版本 `Ubuntu OS`.
  * [x] 詢問業務 `Jamie` 客戶相關應用, 以及錯誤率.
  * [x] 參加 `Josh` 開卡相關課程.
  * [x] 請教 `Kerry` 如何使用 `SATA analyzer`
  * [x] 協助 `FW-Allen` 錄製 `SATA` `analyzer`( `41254` ), 以及 `Uart Log`.

# 2022-07-15
* 協助 `FW` 測試 `3TE6` 其他大容量是否有 `Suspend` 問題( `512GB`, `1T` ), 以及其他版本 `Ubuntu OS`.
  * `Ubuntu 20.04`, `Ubuntu 17.04` 於 `512GB`, `1T` `Suspend` 問題均會發生.
* 詢問業務 `Jamie` 客戶相關應用, 以及錯誤率.
* 參加 `Josh` 開卡相關課程.
* 請教 `Kerry` 如何使用 `SATA analyzer`.
* 協助 `FW-Allen` 錄製 `SATA analyzer`( `41254` ), 以及 `Uart Log`, 並上傳於 `Temp`.
* TODO
  * [x] 參與 `FW-Isaac` 講解 `FW 架構演算法` 課程.
  * [x] 協助 `FW-Adson` 測試 `3TE3-P` 於 `Ubuntu 17.04` 是否會發生 Suspend 問題.
  * [x] 請教 `Kenzi` 如何使用 `PCIe analyzer`.
  * [x] 協助 `FW-Adson` 錄製 `PCIe analyzer`.
  * [x] 協助 `Kenzi` 重新撈取 `3TG6-P` `Uart Log`.
  * [x] 協助 `Weihsiang`, `Alex` 如何修改 `3TE7` 眼圖參數.

# 2022-07-18
* 參與 `FW-Isaac` 講解 `FW 架構演算法` 課程.
* 協助 `FW-Adson` 測試 `3TE3-P` 於 `Ubuntu 17.04` 是否會發生 Suspend 問題.
* 請教 `Kenzi` 如何使用 `PCIe analyzer`.
* 協助 `FW-Adson` 錄製 `PCIe analyzer`.
* 協助 `Kenzi` 重新撈取 `3TG6-P` `Uart Log`.
  * 需使用藍色 `Uart` 線.
  * 使用開卡包錄取 log, 需 load `auth_key`.
  * log 讀取完畢後, 需下 `sl`, `el`, 以上兩個指令跑完後, 再將 log 取出.
* 協助 `Weihsiang`, `Alex` 如何修改 `3TE7` 眼圖參數, 後續發現開卡有問題, 更新開卡板 `FW` 後依然無法開卡.
* TODO
  * [x] 處理 `3TE7` 眼圖參數無法開卡問題.
  * [x] 與 `Nick` 尋找 `FW-Allen` 討論 `新漢` 掉速問題.
  * [x] 協助 `Kenzi` 測試於 `3TE2` 安裝 `Ubuntu` 是否會發生 `Suspend` 問題.
    * [x] `Ubuntu 14.04`.
    * [ ] `Linux`.
  * [x] 協助 `Miller` 量測 `Y534200826` `3TE7` `10` 片, `YCA1210120` `3TE7` `5` 片 `SMART` -> `Power on Hours`.
  * [x] 整理 `PM Jack` 擷取 `DEMSR-A28DK1GCADF * 10`, `DGS25-01TM71GCAQF * 2` 片 `iSMART` 相關資訊.
  * [x] 協助 `Kenzi` 測試 `DGS25-B56F81BC3QC-26` `3MG2-P` 安裝 `OS`.

# 2022-07-19
* 處理 `3TE7` 眼圖參數無法開卡問題, 依然無法成功開卡, 已請 `Weihsiang` 聯絡 `Howard` .
* 與 `Nick` 尋找 `FW-Allen` 討論 `新漢` 掉速問題, 發現客戶使用情境為防火牆, 已發信詢問 `FW-Allen` 是否與 `Stormshield` 遇到 `cold-data` 問題相同.
* 協助 `Kenzi` 測試於 `3TE2` 安裝 `Ubuntu` 是否會發生 `Suspend` 問題.
  * `Ubuntu 14.04` 發生相同問題.
* 協助 `Miller` 量測 `Y534200826` `3TE7` `10` 片, `YCA1210120` `3TE7` `5` 片 `SMART` -> `Power on Hours`.
  * `YCA1210120` `3TE7` `5` 發現一片異常.
* 整理 `PM Jack` 擷取 `DEMSR-A28DK1GCADF * 10`, `DGS25-01TM71GCAQF * 2` 片 `iSMART` 相關資訊.
* 協助 `Kenzi` 測試 `DGS25-B56F81BC3QC-26` `3MG2-P` 安裝 `OS`.
  * 已擷取 `SMART`.
  * 可儲存檔案.
  * 可格式化.
* TODO
  * [x] 參加組內週會, 分享案例.
  * [x] 處理 `3MG2-P` 安裝 `OS`, 觀察是否與客訴問題一樣, 無法安裝作業系統.
  * [x] 協助新竹 `FW RD` 幫忙測試 `3TG6-P` `PCIe` 安裝 `Ubuntu 20.04` 是否會發生 `Suspend` 問題.
  * [x] 協助新竹 `FW RD` 寄送 `3TG3-P` 樣品.
  * [x] 參加 `Nick` 電路圖觀看教學.
  * [x] 參加`佩佩` 教導庫存查詢與設備借用操作.
  * [x] 參加 `新漢` 案件處理會議.
  * [x] 協助 `樺漢` 案件測試 `3TE6` 退回舊版 `FW` 是否會發生 `Suspend` 問題.
  * [x] 與 `歐洲-荷蘭` `FAE` 討論電容損壞量測實驗. 
  * [x] 協助 `FW RD` 錄製 `3TG6-P` 無法 `Format` 客訴案相關 `Uart Log`.

# 2022-07-20
* 參加組內週會, 分享案例.
* 處理 `3MG2-P` 安裝 `OS`, 經過測試後, 觀察是否與客訴問題一樣, 無法安裝作業系統, 經過驗證後, 發現無此問題.
  * `Windows 10` 安裝成功.
  * `Ubuntu 20.04` 安裝成功.
  * 於 `Windows` 環境測試 `BurninTest` `1` hr, 通過無問題.
  * 撰寫結案報告.  
* 協助新竹 `FW RD` 幫忙測試 `3TG6-P` `PCIe` 安裝 `Ubuntu 20.04` 是否會發生 `Suspend` 問題, 經過驗證後, 會發生問題.
* 協助新竹 `FW RD` 寄送 `3TG3-P` 樣品, 於下午一點請 `佩佩` 協助寄送.
* 參加 `Nick` 電路圖觀看教學.
* 參加`佩佩` 教導庫存查詢與設備借用操作.
* 參加 `新漢` 案件處理會議.
  * 原先處理方向為 `cold data`, 與 `stormshield` 相同, 但 `Miller` 看完 `SMART` 數值發現與 `stormshield` 不同, 需與客戶確認狀況.
  * 上電時間過短.
  * 讀寫次數不多.
  * 需與客人確認是否出貨前會先安裝 `OS`, 隔一段時間後, 才會出貨給客戶使用, 懷疑是擺放過久, 導致電子遺失, 使 `device` 觸發 `read-retry`.
* 協助 `樺漢` 案件測試 `3TE6` 退回舊版 `FW` 是否會發生 `Suspend` 問題, 經過測試後, 依然會發生同樣問題.
* 與 `歐洲-荷蘭` `FAE` 討論電容損壞量測實驗. 
  * 需挑出兩種有問題的產品( `Load mode` & `磁碟無法辨認` ).
  * 如 `磁碟無法辨認` 需放入 `chamber` 做持續加溫, 確認是否會隨著溫度變化影響 `device` retry 動作.
  * 需加熱至 `85` 度, 並維持 `3` 分鐘, 看看 `device` 是否會復甦.
* 協助 `FW RD` 錄製 `3TG6-P` 無法 `Format` 客訴案相關 `Uart Log`, 已將 log 寄出.
* TODO
  * [ ] 處理 `3MG2-P` 結案報告.
  * [x] 確認 `樺漢` 案件測試 `3TE6` 是否成功退回舊版 `FW`.
  * [x] 紀錄 `歐洲-荷蘭` 客訴案剩餘 `10` `SMART` 數據紀錄, 以及做加溫測試.
  * [x] 協助 `樺漢` 案件測試 `4TG2-P` (512 GB), `Kingstone FURY PCIe 4.0 NVMe M.2 2280` (1 TB), 是否發生 Suspend 無法喚醒問題.
    * [x] `4TG2-P` (512 GB)
    * [x] `Kingstone FURY PCIe 4.0 NVMe M.2 2280` (1 TB)

# 2022-07-21
* 確認 `樺漢` 案件測試 `3TE6` 是否成功退回舊版 `FW`.
* 紀錄 `歐洲-荷蘭` 客訴案剩餘 `10 pcs` `SMART` 數據紀錄, 以及做加溫測試.
  * `10 pcs` 出現 `9 pcs` 異常 `device`, 異常 `90%`.
* 協助 `樺漢` 案件測試 `4TG2-P` (512 GB), `Kingstone FURY PCIe 4.0 NVMe M.2 2280` (1 TB), 是否發生 Suspend 無法喚醒問題.
  * `4TG2-P` (512 GB) -> pass
  * `Kingstone FURY PCIe 4.0 NVMe M.2 2280` (1 TB) -> pass
* TODO
  * [x] 教導 `Weihsiang` 如何測試 `Kontron` 客訴案 device, 以及如何紀錄資訊.
  * [x] 統整 `Kontron` 電容問題量測數據.
  * [x] 取出`Kontron` 電容問題 `2` 片異常 `3TE7`, 進行 `解焊`, `解焊再回焊` 電容, 看是否異常解除.
  * [x] 發送 `Kontron` 電容問題討論會議邀請.

# 2022-07-22
* 早上出車禍, 於 `10:35` 進公司處理事項.
* 教導 `Weihsiang` 如何測試 `Kontron` 客訴案 device, 以及如何紀錄資訊.
* 統整 `Kontron` 電容問題量測數據.
* 取出`Kontron` 電容問題 `2` 片異常 `3TE7`, 進行 `解焊`, `解焊再回焊` 電容, 看是否異常解除.
  * `Y5342008260030385` -> `解焊再回焊` -> pass.
  * `Y5342008260031056` -> `解焊` -> pass.
* 發送 `Kontron` 電容問題討論會議邀請.
* TODO
  * [x] 與 `HW-Chiyang` 討論 `Kontron` 電容問題 device 電路, 量測方式與數據是否有誤.
  * [x] 協助 `HW-Chiyang` 了解 `Kontron` 電容問題狀況, 以及測試流程.
  * [x] 協助 `Yichuan` 查找 `Kontron` 電容問題 device 歷史最高溫度.
  * [x] 參與 `Kontron` 電容問題會前討論會議.
  * [x] 參與 `國巨` 電容問題討論會議.
  * [x] 修改並發送 `國巨` 電容問題討論會議結果.
  * [x] 針對 `Kontron` `2 psc` 電容問題 device, 進行 `150` 度加溫 `1` hr, 再放入 `chamber` 中, `85` 度 `15` mins, 觀察是否可認到碟.
  * [x] 詢問 `歐洲-荷蘭` 分公司同仁, `Kontron` 客訴品, 使用之設備, 環境溫度, 客退數量, 以及測試方式.
  * [x] 協助 `Nick` 撰寫 `FW` 更新 `Script`.

# 2022-07-25
* 與 `HW-Chiyang` 討論 `Kontron` 電容問題 device 電路, 量測方式與數據是否有誤.
* 協助 `HW-Chiyang` 了解 `Kontron` 電容問題狀況, 以及測試流程, 借出 2 片異常 device.
  * `Y5342008260030330`.
  * `Y5342008260031485`.
* 協助 `Yichuan` 查找 `Kontron` 電容問題 device 歷史最高溫度.
* 參與 `Kontron` 電容問題會前討論會議.
* 參與 `國巨` 電容問題討論會議.
* 修改並發送 `國巨` 電容問題討論會議結果.
* 針對 `Kontron` `2 psc` 電容問題 device, 進行 `150` 度加溫 `1` hr, 再放入 `chamber` 中, `85` 度 `15` mins, 觀察是否可認到碟.
* 詢問 `歐洲-荷蘭` 分公司同仁, `Kontron` 客訴品, 使用之設備, 環境溫度, 客退數量, 以及測試方式.
  * 客戶使用之設備 -> 香煙販賣機( `panel pc` ).
  * 環境溫度 -> 室溫, 並具有 空調.
  * 客退數量 -> `4` 機台.
  * 測試方式 -> 將設備透過氣泡墊包覆 `panel pc`, 進行 `BurninTest`, 測試最高溫為 `65` 度.
* TODO
  * [x] 統整 `Kontron` 電容問題 device 歷史高溫紀錄.
  * [x] 前往尋找 `Angus`, `Tobby` 了解如何切割電容.
  * [x] 切割 `5 psc` 電容寄回 `國巨` 分析.
  * [x] 協助 `Nick` 撰寫 `FW` 更新 `Script`.

# 2022-07-26
* 統整 `Kontron` 電容問題 device 歷史高溫紀錄.
* 前往尋找 `Angus`, `Tobby` 了解如何切割電容.
* 切割 `5 psc` 電容寄回 `國巨` 分析, .
* 協助 `Nick` 撰寫 `FW` 更新 `Script`.
  * 透過 `hdparm` tool 更新 FW.
  * `3TE6` PCIe `2240`( `64 GB`, `128 GB`, `256 GB` ), `2280`( `64 GB`, `128 GB`, `512 GB`, `1T`, `2T` ).
  * 測試過程中發生主機板相容性問題( `NVMe` 辨識問題 ).
  * 透過 `hdparm` tool 無法正常更新.
  * 透過 `DLMicro` tool 無法正常更新.
* TODO
  * [x] 測試透過 `nvme-cli` tool 是否可正常更新 `FW`.
  * [x] 修改 `FW` 更新 `Script`.
  * [x] 透過美工刀切割 `3TE7` 內 `5` 顆 `C192` 電容.
  * [x] 整理 `Kontron` 測試結果, 並回覆 `EU` team.
  * [x] 回覆 `國巨` 樣品使用狀況詢問信件.
  * [x] 參與組內週會.

# 2022-07-27
* 測試透過 `nvme-cli` tool 是否可正常更新 `FW`, 需先執行 `fw-download`, 以及 `fw-commit` 才算完成更新.
  * 需先執行 `nvme fw-download -f $fw_path  $device_path`.
  * 最後執行 `nvme fw-commit /dev/nvme0 -s 1`
* 修改 `FW` 更新 `Script`, 並將相關使用程式打包於 `Image`.
* 透過美工刀切割 `3TE7` 內 `5` 顆 `C192` 電容.
  * 切割過程, 發生 `2` 顆電容遺失, 以及與 `Angus` 至工廠量測電容值(常溫), 發現 `2` 電容問題, 故再量測 `7` psc, 再裁切 `5` psc 電容.
  * 已於下午寄送樣品電容 `C192` 於 `國巨`.
* 整理 `Kontron` 測試結果, 並回覆 `EU` team.
* 回覆 `國巨` 樣品使用狀況詢問信件.
* 參與組內週會.
* TODO
  * [x] 撰寫 `樺漢` 客訴報告.
  * [x] 撰寫 `研揚` `3TG6-P`, `3MG2-P` 客訴報告.
  * [x] 整理 `Kontron` 測試結果於 `Excel`, 並回覆 `EU` team.
  * [x] 參與 `Rex` 教導之 `InnoAGE` 相關操作課程.
  * [x] 參與 `EU` team 客訴處理進度會議.
  * [x] 參與 `FAE` 月會分享.

# 2022-07-28
* 撰寫 `樺漢` 客訴報告.
* 撰寫 `研揚` `3TG6-P`, `3MG2-P` 客訴報告.
* 整理 `Kontron` 測試結果於 `Excel`, 並回覆 `EU` team.
* 參與 `Rex` 教導之 `InnoAGE` 相關操作課程.
* 參與 `EU` team 客訴處理進度會議.
* 參與 `FAE` 月會分享.
* TODO
  * [x] 測試 `EU` team 寄送回來之 `3` 片 device.
  * [x] 查找 `Kontron` `2` 片 `Fail` device, 並交給 `Chiyang` 做量測.
  * [x] 統整 `EU` team 客訴處理進度會議內容.
  * [x] 協助 `登科` 測試 `新漢` 客訴案件產品, 更新 `FW`, 觀察是否回溫.
  * [x] 轉交 `139` 片 `Kontron` 客訴 device, 並至廠區協助測試.
  * [x] 參與 `EU` 週會.

# 2022-07-29
* 測試 `EU` team 寄送回來之 `3` 片 device.
  * `YCA12101200130748` -> Pass.
  * `Y5342008260030261` -> Fail.
  * `YCA12101200130952` -> Pass.
* 查找 `Kontron` `2` 片 `Fail` device, 並交給 `Chiyang` 做量測.
* 統整 `EU` team 客訴處理進度會議內容.
* 協助 `登科` 測試 `新漢` 客訴案件產品, 更新 `FW`, 觀察是否回溫, 目前觀察時好時壞.
* 轉交 `139` 片 `Kontron` 客訴 device, 並至廠區協助測試.
* 參與 `EU` 週會.
* TODO
  * [x] 統計 `139` 片 `Kontron` 客訴 device 量測結果.
  * [x] 與 `Angus` & `Chiyang` 前往四樓量測 `常溫` -> `高溫` 電容值變化.
  * [x] 協助 `登科` 測試 `新漢` 客訴案件產品, 需要 `Nick` 提供當初測試環境.
  * [x] 更新 `Kontron` 處理進度.
  * [x] 測試 `EU` team 寄送回來之 `3` 片 device.
  * [x] 修改 `宸曜` `FW` 更新 `tool`.
  * [x] 參與 `宸曜` 檢討會議.

# 2022-08-01
* 統計 `139` 片 `Kontron` 客訴 device 量測結果.
  * 已將 `180` 片量測結果統整於 `Excel`.
  * `Fail Rate` -> `47.2%`( `85/180` ).
  * `Loader Mode` -> `0%`.
* 與 `Angus` & `Chiyang` 前往四樓量測 `常溫` -> `高溫` 電容值變化.
  * 利用 `熱風槍` `120` 度, 針對電容加溫, 不到兩分鐘就可以看到電容值下降到 `spec` 之外.
* 協助 `登科` 測試 `新漢` 客訴案件產品.
  * 透過 `UART rs232` 錄製 `disk` 所有過程.
  * 利用 `AIDA 64` 測試 `disk` 讀取速度.
  * 將 `disk` 靜放至 `idle`, 觀察其行為.
* 更新 `Kontron` 處理進度.
  * 送驗樣品已到 `高雄` 分析單位, 預計下週五會有分析報告.
* 測試 `EU` team 寄送回來之 `3` 片 device.
  * 透過 `SATA` 轉板直接接入 `主機板`.
  * 利用 `熱風槍` 加熱至 `85` 度.
  * 目前並無發現 `Loader Mode` 現象, 已將 `3` 片 device 放至於 `Chamber` 加熱至 `85` 度.
* 修改 `宸曜` `FW` 更新 `tool`, 已將 `Float` & `Integer` 比較 bug 修正.
* 參與 `宸曜` 檢討會議.
* 修改 `新漢` 分析報告之 `客戶名稱`, 並重新發信.
* TODO
  * [x] 協助 `登科` 測試 `新漢` 客訴案件產品, 觀看 `disk` `Idle` 裝況.
  * [x] 測試 `EU` team 寄送回來之 `3` 片 device, 透過 `Chamber` 加熱至 `5` 度, 再透過 `SATA` 連接至主機板, 觀看是否有 `Loader Mode` 現象.
  * [x] 與 `Kenzi` 前往尋找業務 `Alan`, 討論 `研楊` 客訴案, 並檢查分析報告之客戶名稱.
  * [ ] 與 `Angus` & `Chiyang` 前往四樓量測 `常溫` -> `高溫` 電容值變化, 量測實際溫度, 並加入正常 `device` 電容.
  * [x] 參與 `新漢` 客訴案件會議討論, 以及修正分析報告.
  * [x] 修改 `FW` 更新 `Script`, 新增執行 log, 容量條件限制, 以及全部不符合就不動作.

# 2022-08-02
* 協助 `登科` 測試 `新漢` 客訴案件產品, 觀看 `disk` `Idle` 裝況.
* 測試 `EU` team 寄送回來之 `3` 片 device, 透過 `Chamber` 加熱至 `5` 度, 再透過 `SATA` 連接至主機板, 觀看是否有 `Loader Mode` 現象.
* 與 `Kenzi` 前往尋找業務 `Alan`, 討論 `研楊` 客訴案, 並檢查分析報告之客戶名稱.
* 參與 `新漢` 客訴案件會議討論, 以及修正分析報告.
* 修改 `FW` 更新 `Script`, 新增執行 log, 容量條件限制, 以及全部不符合就不動作.
* 與吉洋討論電容溫度變化
* `Miller` 教導如何撰寫 `8d` report.
* TODO
  * [ ] 與 `Angus` & `Chiyang` 前往四樓量測 `常溫` -> `高溫` 電容值變化, 量測實際溫度, 並加入正常 `device` 電容.
  * [x] 參加組內週會.
  * [x] 與 `Kenzi` 前往尋找業務討論 `3TG6-P` `bad queue` 議題.
  * [x] 修改 `Kontron` `8d` report.
  * [x] 與業務 `James` & `Miller` & `Nick` 討論 `Nexcom` 問題回覆.
  * [x] 與 `EU FAE` 了解 `DGM28-02TDA1ECBEH-S9RA` 客訴案相關背景, 以及回報 `Kontron` 進度.

# 2022-08-03
* 參加組內週會.
* 與 `Kenzi` 前往尋找業務討論 `3TG6-P` `bad queue` 議題, 與業務討論完結果是不要出分析報告, 可以直接結案, 業務後續會直接出新品給客戶.
* 修改 `Kontron` `8d` report.
* 與業務 `James` & `Miller` & `Nick` 討論 `Nexcom` 問題回覆.
* 與 `EU FAE` 了解 `DGM28-02TDA1ECBEH-S9RA` 客訴案相關背景, 以及回報 `Kontron` 進度.
* TODO
  * [x] 與業務 `James` & `Sam` &`Miller` & `Nick` & `Karen` 討論 `Nexcom` 問題回覆.
  * [x] 與 `Angus` & `Chiyang` 前往四樓量測 `常溫` -> `高溫` 電容值變化, 量測實際溫度, 並加入正常 `device` 電容.
  * [x] 與 `Micky` 了解 `DGM28-02TDA1ECBEH-S9RA` 客訴案相關背景, 以及狀況.
  * [x] 協助 `Kiwi` 量測 `FTB220728001` 客訴案.
  * [x] 協助 `Nick` 修改 `fw update` script, 以及壓制 image.
  * [x] 與 `Kiwi` 對於 `Kontron` `2` 片異常 device, 透過焊接還原電容狀態.
  * [x] 與 `Alife` 討論 `Kontron` & `DGM28-02TDA1ECBEH-S9RA` 客訴案狀況.

# 2022-08-04
* 與業務 `James` & `Sam` &`Miller` & `Nick` & `Karen` 討論 `Nexcom` 問題回覆.
* 與 `Angus` & `Chiyang` 前往四樓量測 `常溫` -> `高溫` 電容值變化, 量測實際溫度, 並加入正常 `device` 電容.
  * `全新品電容` -> `293.8`.
  * `正常品電容` -> `289.6`.
  * `異常品電容` -> `275.8`.
* 與 `Micky` 了解 `DGM28-02TDA1ECBEH-S9RA` 客訴案相關背景, 以及狀況.
  * `DGM28-02TDA1ECAEH-S9RA` 給客戶做測試沒問題, 但內部發現 `PCB` 上的 `DRAM` 第二顆位置良率不好, 故建議客戶更換為 `DGM28-02TDA1ECBEH-S9RA` 做測試, 但卻發生掉碟的問題.
  * 目前樣品在 `Tommy` 那邊, 明日會取得樣品.
* 協助 `Kiwi` 量測 `FTB220728001` 客訴案, 已將結果圖寄出.
* 協助 `Nick` 修改 `fw update` script, 以及壓制 image.
* 與 `Kiwi` 對於 `Kontron` `2` 片異常 device, 透過焊接還原電容狀態, 結果為正常.
* 與 `Alife` 討論 `Kontron` & `DGM28-02TDA1ECBEH-S9RA` 客訴案狀況.
* TODO
  * [x] 前往 `Tommy` 那邊, 取得樣品( `DGM28-02TDA1ECBEH-S9RA` ).
  * [ ] 修改 `Kontron` `8d` report.
  * [x] 參加 `EU` 週會.
  * [ ] 協助 `Josh` 觀看 `EU` 客訴案.
  * [x] 參與 `Kontron` 客訴討論案.
  * [x] 執行 `Kontron` `10pcs` 加熱至 `150` 度, 放置 `1` hr, 再透過 `Chamber` 加熱至 `85` 度, 觀看現象.
  * [x] 執行 `Kontron` `2pcs` 透過顯微鏡觀看外觀是否有異常.
  * [x] 執行 `Kontron` `2pcs` 外借給 `Chiyang`.
  * [x] 執行 `Kontron` `1pcs` 透過 `焊槍` `200` 度, 點處電容焊接兩處, 觀察是否現象消失.
  * [x] 請採購協助詢問 `Samsung`, `華新科` 電容老化是否會影響 `IR` 值.
  * [x] 協助 `FW RD` 複製 `DGM28-02TDC1GWBEQH-S9RA` 客訴問題.

# 2022-08-05
* 參加 `EU` 週會.
* 前往 `Tommy` 那邊, 取得樣品( `DGM28-02TDC1GWBEQH-S9RA` ).
* 參與 `Kontron` 客訴討論案.
* 執行 `Kontron` `10pcs` 加熱至 `150` 度, 放置 `1` hr, 再透過 `Chamber` 加熱至 `85` 度, 觀看現象.
  * `10pcs` 量測正常.
* 執行 `Kontron` `2pcs` 透過顯微鏡觀看外觀是否有異常.
  * `2pcs` 量測無異常.
* 執行 `Kontron` `2pcs` 外借給 `Chiyang`.
* 執行 `Kontron` `1pcs` 透過 `焊槍` `200` 度, 點處電容焊接兩處, 觀察是否現象消失.
  * 現象無消失.
* 請採購協助詢問 `Samsung`, `華新科` 電容老化是否會影響 `IR` 值.
  * `Samsung` 回覆是電容老化不會造成 `IR` 值變化, 通常變化主因是內部已經裂掉或不良.
  * `華興科` 回覆是通常保存條件濕氣重, 或是電容內部已經裂掉或不良, 才會影響.
* 協助 `FW RD` 複製 `DGM28-02TDC1GWBEQH-S9RA` 客訴問題.
* TODO
  * [ ] 協助 `Josh` 觀看 `EU` 客訴案.
  * [x] 修改 `Kontron` `8d` report.
  * [x] 參與 `Kontron` 討論會議.
  * [x] 執行 `Kontron` 濕度實驗.
  * [x] 執行 `Kontron` 取已加溫到 `150`度 `1pcs`, 實驗加溫 `110` 度, 是否可以認到碟.

# 2022-08-08
* 參與 `Kontron` 討論會議.
* 執行 `Kontron` 濕度實驗.
  * `濕度`: `60%`, `時間`: `14` hrs, `result`: `pass`.
  * `濕度`: `95%`, `時間`: `3` hrs, `result`: `pass`.
* 執行 `Kontron` 取已加溫到 `150`度 `1pcs`, 實驗加溫 `110` 度, 是否可以認到碟.
  * `result`: `pass`. 
  * 加溫至 `120` 度: `fail`.
* 修改 `Kontron` `8d` report.
* TODO
  * [x] 修改 `Kontron` `8d` report.
  * [x] 觀看 `Kontron` 濕度實驗.
  * [x] 與 `國巨` 開會討論分析結果.
  * [x] 與 `EU Team` 開會討論 `Kontron` 分析結果.
  * [x] 量測電容 `IR` 值.

# 2022-08-09
* 修改 `Kontron` `8d` report.
* 觀看 `Kontron` 濕度實驗.
  * `6pcs` 加溼 `95%`, 放置 `3` 天, 透過熱風槍加熱至 `85` 度, 結果是可辯認到 `Disk`.
* 與 `國巨` 開會討論分析結果.
* 會議記錄如下:
  * 1.儲存環境對電性(`IR` 值)不會有影響，只對焊錫性有關.
  * 2.`國巨` 標準電容測試流程，額定電壓 (`10v`)，加壓 `1` min 後量測, 超過 `10v` 就是超過耐壓, 不建議提高電壓.
  * 3.影響 `IR` 值的原因有哪些?  高溫/濕度/環境應力.
  * 4.`MLCC` `X5R` 有容值變化量的規範，但針對 `IR` 值是沒有規範，目前只有下限值 > `1.52 E+02`.
  * 5.濕度造成的 `IR` 下限值為 `0.76E+02`.

  `TODO`:  
    `國巨`:
    * 1.提供電測流程圖
    * 2.提供 `ATE` 測試 `IR` 值紀錄，常態分佈是多少? 會不會有變化量
    * 3.測試生產留樣兩個批次(各 `200` pcs，總共 `400` pcs) => 標準量測 (`25` 度C & `85` 度C), `8/10` 提供 `2` 個批次結果 (`Status`: 先取 `2` 個批次各 `50` pcs，共 `100` pcs => 觀看 `IR` 值的常態分佈), 剩餘 `300` pcs( `2` 個批次各 `150` pcs)，於 `8/12` 提供結果.

    `Innodisk`:
    * 1.提供測試樣品(送驗前先量測 `IR` 值, 確定後續與 `國巨` 量測數值之差異).
    * 2.測試樣品需將附近電路以及 `IC` 切除乾淨.
* 與 `EU Team` 開會討論 `Kontron` 分析結果.
* 量測電容 `IR` 值.
  * 發現 `保險絲` 燒毀, 有前往五金行購買新品更換, 但又再度燒毀, 懷疑內部電路燒毀.
  * 儀器損壞, 已送回原廠維修.
* TODO
  * [x] 修改 `Kontron` `8d` report.
  * [x] 量測電容 `IR` 值.
  * [x] 量測 `10` pcs( `異常品 150 度烘烤` ), 放置 `Chamber` `85` 度, 靜至 `30` mins, 看是否可以認到 `Disk`.
  * [x] 與 `EU Team` 開會討論 `Kontron` 分析結果.

# 2022-08-10
* 修改 `Kontron` `8d` report.
* 量測電容 `IR` 值.
  * `全新品` : `2132`
  * `正常品` : `2051`
  * `客退異常品加溫150度` : `2021`
  * `加溼 95%` : `1763`
  * `泡水` : `1563`
* 量測 `10` pcs( `異常品 150 度烘烤` ), 放置 `Chamber` `85` 度, 靜至 `30` mins, 看是否可以認到 `Disk`.
  * 皆可認到 `Disk`.
* 與 `EU Team` 開會討論 `Kontron` 分析結果.
    * `HW`
      1. 添購量測儀器  (PIC: `Pater`)
      2. 客退不良品 `5` pcs 割除銅線&周圍電子零件, `10V` 量測 `IR` 值(通電 `2s` & `1` mins)
         * `常溫(25)`
         * `高溫(70/85)`
      3. 根據第 `2` 點結果, 決定是否要做烘烤 `150度C` `1hr`，`10V` 量測 `IR` 值.
         * `常溫(25)`
         * `高溫(70/85)`
      4. 詢問 `Reset IC` 廠商, 是否因電阻會導致 `IC` 不良.
    
    * `FAE`
      1. 客退不良品 `5` pcs, 量測常溫(`25`) `power on/off` `3` 次 (PIC: `Peter`)
      2. 客退正常品 `6` pcs 割線量測(常溫(`25`), 高溫(`70 & 85`)) `IR` 值, 再將 `4` pcs 加濕 `95%`, `2` pcs 泡水, 維持 `1` 周, 觀看 `IR` 值是否會降低.
      3. 全新品 `6` pcs 加濕 `95%`, `3` pcs 泡水, 維持 `1` 周, 觀看 `IR` 值是否會降低.
    
    * `採購`
      1. Search `100M` 電阻, 並提供樣品給 `Pater`. (PIC: `Carney`)
* TODO
  * [x] 整理 `Kontron` 討論結果.
  * [x] 協助 `Pater` 處理客退不良品 `5` pcs, 切割電容周圍電路, 並量測結果.
  * [x] 協助 `Pater` 處理客退正常品 `6` pcs, 切割電容周圍電路, 並量測結果.
  * [x] 全新品 `6` pcs 放入 `Chamber` 內 加濕 `95%`, `3` pcs 泡水, 維持 `1` 周, 觀看 `IR` 值是否會降低.
  * [x] 與 `Kenzi` 討論 `Nexcom` 客戶提問回答.
  * [x] 測試 `Nexcom` 客訴品, 新舊版 `FW` 速度差異.
  * [x] 與 `Nexcom` `FAE-Duncan` 討論相關問題與狀況.
  * [x] 與 `EU Team` 開會討論 `Kontron` 分析結果.
  * [x] 量測 `晶達` 客訴品(`3TE6`).
  * [x] 協助 `Pater` 詢問 `電阻量測儀` 報價.

# 2022-08-11
* 整理 `Kontron` 討論結果.
* 協助 `Pater` 處理客退不良品 `5` pcs, 切割電容周圍電路, 並量測結果 -> `Pass`.
* 協助 `Pater` 處理客退正常品 `6` pcs, 切割電容周圍電路, 並量測結果 -> `Pass`.
* 全新品 `6` pcs 放入 `Chamber` 內 加濕 `95%`, `3` pcs 泡水, 維持 `1` 周, 觀看 `IR` 值是否會降低.
* 與 `Kenzi` 討論 `Nexcom` 客戶提問回答.
* 測試 `Nexcom` 客訴品, 新舊版 `FW` 速度差異.
  * 將 `Disk` `NAND FLASH` 位置全部清為 `0`.
  * 透過 `AIDA 64` 量測 `Linear Read`.
  * 因將 `NAND FLASH` 位置全部清為 `0`, 故速度上並無差異.
* 與 `Nexcom` `FAE-Duncan` 討論相關問題與狀況.
  * 需要了解 `data retention` 發生機率.
  * `FW` 新舊版更新效率.
  * `read retry` `3` 階段機制是否可以降低現象(`RAID retry`).
* 與 `EU Team` 開會討論 `Kontron` 分析結果.
* 量測 `晶達` 客訴品(`3TE6`).
* TODO
  * [x] 透過業務 `Alan` 詢問 `晶達` 人員使用 `Disk` 過程, 釐清問題.
  * [x] 透過 `電阻量測儀` 量測客退不良品 `5` pcs(切割電容周圍電路) `IR` 值.
  * [x] 透過 `電阻量測儀` 量測客退正常品 `6` pcs(切割電容周圍電路) `IR` 值.
  * [x] 修改 `Kontron` `8d` report.
  * [x] 討論 `Nexcom` 客戶提問回覆內容.
  * [x] 與 `EU Team` 開會討論 `Kontron` 分析結果.

# 2022-08-12
* 透過業務 `Alan` 詢問 `晶達` 人員使用 `Disk-3TE6` 過程, 釐清問題.
* 透過 `電阻量測儀` 量測客退不良品 `5` pcs(切割電容周圍電路) & 客退正常品 `6` pcs(切割電容周圍電路)`IR` 值.
  * `全新品` -> 常溫 `400MΩ`
  * `客退正常品`:
    * `30320`-> 常溫 `305MΩ`, 高溫 `417MΩ`.
    * `30120`-> 常溫 `284MΩ`
    * `30377`-> 常溫 `346MΩ`
    * `30096`-> 常溫 `231MΩ`
    * `31018`-> 常溫 `335MΩ`
    * `30971`-> 常溫 `336MΩ`
  * `客退異常品`:
    * `30354`-> 常溫 `91.5MΩ`, 高溫 `11MΩ`.
    * `30418`-> 常溫 `68.8MΩ`, 高溫 `4.2MΩ`.
    * `30121`-> 常溫 `127.5MΩ`, 高溫 `4.44MΩ`.
    * `31197`-> 常溫 `139.3MΩ`, 高溫 `10.77MΩ`.
    * `30857`-> 常溫 `77.6MΩ`, 高溫 `3.73MΩ`.
* 修改 `Kontron` `8d` report, 已經寫到 `4d`.
* 討論 `Nexcom` 客戶提問回覆內容, 並將回覆內容寄給客戶.
* 與 `EU Team` 開會討論 `Kontron` 分析結果.
* TODO
  * [x] 補測剩餘數據, 透過 `電阻量測儀` 量測客退不良品 `5` pcs(切割電容周圍電路) & 客退正常品 `6` pcs(切割電容周圍電路)`IR` 值.
  * [x] 協助 `Benson` 準備並量測 `4` pcs `客退異常品` `IR` 值.
  * [x] 修改 `Kontron` `8d` report.
  * [x] 與 `EU Team` 開會討論 `Kontron` 分析結果.

# 2022-08-15
* 補測剩餘數據, 透過 `電阻量測儀` 量測客退不良品 `5` pcs(切割電容周圍電路) & 客退正常品 `6` pcs(切割電容周圍電路)`IR` 值.
  * `全新品` -> 常溫 `400MΩ`, 高溫75 `225MΩ`, 高溫85 `210MΩ`
  * `客退正常品`:
    * `30320`-> 常溫 `305MΩ`, 高溫75˚C `417MΩ`.
    * `30120`-> 常溫 `284MΩ`, 高溫75˚C `13.04MΩ`.
    * `30377`-> 常溫 `346MΩ`, 高溫75˚C `234MΩ`.
    * `30096`-> 常溫 `231MΩ`, 高溫75˚C `21.4MΩ`.
    * `31018`-> 常溫 `335MΩ`, 高溫75˚C `245MΩ`.
    * `30971`-> 常溫 `336MΩ`, 高溫75˚C `12.2MΩ`.
  * `客退異常品`:
    * `30354`-> 常溫 `91.5MΩ`, 高溫75˚C `11MΩ`, 高溫85˚C `2.68MΩ`.
    * `30418`-> 常溫 `68.8MΩ`, 高溫75˚C `4.2MΩ`, 高溫85˚C `1.231MΩ`.
    * `30121`-> 常溫 `127.5MΩ`, 高溫75˚C `4.44MΩ`, 高溫85˚C `1.46MΩ`.
    * `31197`-> 常溫 `139.3MΩ`, 高溫75˚C `10.77MΩ`, 高溫85˚C `1.753MΩ`.
    * `30857`-> 常溫 `77.6MΩ`, 高溫75˚C `3.73MΩ`, 高溫85˚C `1.572MΩ`.
* 協助 `Benson` 準備並量測 `4` pcs `客退異常品` `IR` 值.
  * `30708`-> 常溫 `82.8MΩ`, 高溫85˚C `1.231MΩ`.
  * `30544`-> 常溫 `84.8MΩ`, 高溫85˚C `2.68MΩ`.
  * `30578`-> 常溫 `92.5MΩ`, 高溫85˚C `1.46MΩ`.
  * `30935`-> 常溫 `121.2MΩ`, 高溫85˚C `1.753MΩ`.
* 抽取 `1` pcs 客退異常品, 透過 `錫爐` 加溫 `6` 分鐘後, 量測 `IR` 值.
  * `30857`-> 常溫 `170.2MΩ`, 高溫85 `203MΩ`.
* 抽取 `4` pcs 客退異常品 & `1` pcs 加溼 95% 電容, 透過 `烤箱` 加溫至 `150˚C` `1` 小時後, 量測 `IR` 值.
  * `30354`-> 常溫 `196MΩ`, 高溫85˚C `180.7MΩ`.
  * `30418`-> 常溫 `311MΩ`, 高溫85˚C `250MΩ`.
  * `30121`-> 常溫 `211MΩ`, 高溫85˚C `192.4MΩ`.
  * `31197`-> 常溫 `323.4MΩ`, 高溫85˚C `219MΩ`.
  * `1`> 常溫 `366MΩ`, 高溫85˚C `255MΩ`.
* 抽取 `6` pcs 透過 `Chamber` 加溼 `95%`, 放置 `7` 天, 量測 `IR` 值.
  * `1`-> 常溫 `100.3MΩ`.
  * `2`-> 常溫 `174.2MΩ`.
  * `3`-> 常溫 `138.3MΩ`.
  * `4`-> 常溫 `296MΩ`.
  * `5`-> 常溫 `383MΩ`.
  * `6`-> 常溫 `481MΩ`.
* 抽取 `3` pcs, 泡水放置 `7` 天, 量測 `IR` 值. 
  * `1`-> 常溫 `407MΩ`.
  * `2`-> 常溫 `346MΩ`.
  * `3`-> 常溫 `337MΩ`.
* 修改 `Kontron` `8d` report, 並與 `Miller` 討論內容.
* 與 `EU Team` 開會討論 `Kontron` 分析結果.
* TODO
  * [x] 修改 `Kontron` `8d` report.
  * [x] 修改 `Nexcom` `FAE` 分析報告.
  * [x] 分析 `晶達` `3TE6` 客訴問題.
  * [x] 分析 `Hiper` `3ME3` 客訴問題.

# 2022-08-16
* 修改 `Kontron` `8d` report.
* 修改 `Nexcom` `FAE` 分析報告, 已與 `Miller` 討論.
* 分析 `晶達` `3TE6` 客訴問題, 從 `Uart log` 看到 `ASSERT` 訊息.
* 分析 `Hiper` `3ME3` 客訴問題, 並無看到客戶反應之問題.
  * `熱插拔` `5` 次, 都可辨認.
  * 重複開關機 `5` 次, `Bios` & `Dsik manager` 都可辨認.
  * 因熱插拔導致 `Ubuntu 22.04` 發生問題, 無法操作, 已重灌, 修改 `Bios` `SATA` -> `熱插拔`.
* TODO
  * [x] 維修筆電螢幕.
  * [x] 參與組內週會. 
  * [x] 修改 `Nexcom` `FAE` 分析報告.
  * [x] 整理 `Hiper` 客訴案處理進度, 並回報給業務.
  * [x] 與 `Pater` 前往與 `HIOKI` 儀器商測試 `IR` 值.
  * [x] 架設 `Kontron` 廣告機, 並觀察 `SSD` 溫度變化.
  * [x] 測試 `Nexcom` 客訴品中 `40158`, `41254` 重新開卡, 觀看現象是否消失.
  * [x] 上單借取相關設備.

# 2022-08-17
* 維修筆電螢幕.
* 參與組內週會. 
* 修改 `Nexcom` `FAE` 分析報告.
* 整理 `Hiper` 客訴案處理進度, 並回報給業務.
* 與 `Pater` 前往與 `HIOKI` 儀器商測試 `IR` 值.
* 架設 `Kontron` 廣告機, 並觀察 `SSD` 溫度變化, 目前溫度為 `64.6`.
* 測試 `Nexcom` 客訴品中 `40158`, `41254` 重新開卡, 觀看現象是否消失.
* 上單借取相關設備.
* TODO
  * [x] 測試 `Nexcom` 客訴品中 `40158`, `41254` 重新開卡, 透過 `hdparm` 量測速度.
  * [x] 修改 `Nexcom` `FA` 分析報告.
  * [x] 修改 `Kontron` 8d report, 並回報內部.
  * [x] 協助 `Benson` 準備 `2` pcs 客退異常品, 以及量測加溼 `95%` 電容.
  * [x] 焊接細針於碳針上.

# 2022-08-18
* 測試 `Nexcom` 客訴品中 `40158`, `41254` 重新開卡, 透過 `hdparm` 量測速度, 並回報給內部人員.
  * `40158` -> `532.63 MB/s`.
  * `41254` -> `533.07 MB/s`.
* 修改 `Nexcom` `FA` 分析報告, 並將相關結果寄給客戶.
* 修改 `Kontron` 8d report, 並回報內部人員.
* 協助 `Benson` 準備 `2` pcs 客退異常品, 以及量測加溼 `95%` 電容.
  * `30931` -> `127.7MΩ`.
  * `30309` -> `155.3MΩ`.
  * 加溼 `95%` 電容(5) -> `180MΩ`.
* 焊接細針於碳針上.
* 回報 `Hiper` 客訴案處理進度給業務, 客訴品已交還回去(`NPF`).
* TODO
  * [x] 測試 `晶達` 客訴案 `3TE6` 問題復現.
  * [x] 與 `EU Team` 開會討論 `Kontron` 分析結果.
  * [x] 參與 `EU FAE Team` 週會.
  * [x] 參與公司 `消防演習`.

# 2022-08-19
* 測試 `晶達` 客訴案 `3TE6` 問題復現, 測試 `8` hr, 並無發現問題, 有與業務討論客戶操作手法.
* 與 `EU Team` 開會討論 `Kontron` 分析結果.
* 參與 `EU FAE Team` 週會.
* 參與公司 `消防演習`.
* 協助 `Kiwi` 處理 `YCA12206170090001` 電阻錯料問題.
* TODO
  * [x] 休假.

# 2022-08-22
* 休假.
* TODO
  * [x] 協助 `Pater` 測試 `Kontron` 客退正/異常品濕度 `95%` 量測(`7` pcs).
  * [x] 撰寫新進人員工作紀錄表.
  * [x] 測試 `晶達` 客訴案 `3TE6` 問題復現, `BurninTest` 時間增加到 `48` hr.
  * [x] 協助 `Nick` 壓製 `DLMC` image.
  * [x] 撰寫 `Data Retention Official FAQ` 問題整理 PPT.
  * [x] 與 `EU Team` 開會討論 `Kontron` 分析結果.
  * [x] 協助 `EU Team` 分析 `3MV2-P` 客訴案.

# 2022-08-23
* 協助 `Pater` 測試 `Kontron` 客退正/異常品濕度 `95%` 量測(`7` pcs).
* 撰寫新進人員工作紀錄表.
* 測試 `晶達` 客訴案 `3TE6` 問題復現, `BurninTest` 時間增加到 `48` hr.
* 協助 `Nick` 壓製 `DLMC` image.
* 撰寫 `Data Retention Official FAQ` 問題整理 PPT.
* 與 `EU Team` 開會討論 `Kontron` 分析結果.
* 協助 `EU Team` 分析 `3MV2-P` 客訴案.
* TODO
  * [x] 參加組內週會.
  * [x] 協助 `EU Team` 分析 `3MV2-P` 客訴案.
  * [x] 撰寫 `Data Retention Official FAQ` 問題整理 PPT.
  * [x] 測試 `晶達` 客訴案 `3TE6` 問題復現.

# 2022-08-24
* 參加組內週會.
* 協助 `EU Team` 分析 `3MV2-P` 客訴案.
  * `BCA12103030390146` -> `Crystal` 零件異常, 更換後可正常辨認.
  * `BCA12110120030002` -> 可進 `Loader mode`, 從 `MP tool` 發現 `NAND Flash` mapping 有異常數值, 疑似 `Controller` 有異常.
  * 以上異常已上申請單領新料, 做日後更換.
* 撰寫 `Data Retention Official FAQ` 問題整理 PPT.
* 測試 `晶達` 客訴案 `3TE6` 問題復現, 發現執行 `2 days` 為正常.
* TODO
  * [x] 更新 `eFAE` 客訴相關紀錄( `FTD220714001`, `FEB220812005` ).
  * [x] 測試 `晶達` 客訴案 `3TE6` 問題復現, 執行 `BurninTest` 時, 強致將電源關閉, 再觀察現象.
  * [x] 撰寫 `Data Retention Official FAQ` 問題整理 PPT.
  * [x] 觀看 `Kontron` 加溼實驗狀況.
  * [x] 協助 `Nick` 撰寫 `DLMC` 相關 script.
  * [x] 詢問 `國巨` 關於電容老化相關問題, 以及回覆量測參數 & 測試手法.

# 2022-08-25
* 更新 `eFAE` 客訴相關紀錄( `FTD220714001`, `FEB220812005` ).
* 測試 `晶達` 客訴案 `3TE6` 問題復現, 執行 `BurninTest` 時, 強致將電源關閉, 再重開機後, 發現與客戶相同的問題, 將 `FW` 更新至 `211180A`, 再重複相關動作. 並無發現相同問題, 並將結果回覆給業務 `Alan`.
* 撰寫 `Data Retention Official FAQ` 問題整理 PPT.
* 觀看 `Kontron` 加溼實驗狀況.
* 協助 `Nick` 撰寫 `DLMC` 相關 script, 測試完後，已寄出.
* 詢問 `國巨` 關於電容老化相關問題, 以及回覆量測參數 & 測試手法.
* TODO
  * [x] 協助 `Kiwi` 查找 `libATA` 錯誤代碼訊息.
  * [x] 協助 `Kiwi` 觀看 `Korea` 平台相關問題.
  * [x] 撰寫 `Data Retention Official FAQ` 問題整理 PPT.
  * [x] 與 `EU Team` 開會討論 `Kontron` 分析結果.
  * [x] 參與 `eHRD` 課程.
  * [x] 前往 `RMA 智原` 協助幫忙更換 Controller.

# 2022-08-26
* 協助 `Kiwi` 查找 `libATA` 錯誤代碼訊息.
* 協助 `Kiwi` 觀看 `Korea` 平台相關問題.
* 撰寫 `Data Retention Official FAQ` 問題整理 PPT.
* 與 `EU Team` 開會討論 `Kontron` 分析結果.
* 參與 `eHRD` 課程.
* 前往 `RMA 智原` 協助幫忙更換 Controller.
* TODO
  * [x] 撰寫 `Data Retention Official FAQ` 問題整理 PPT, 並找 `Kenzi`, `Miller` 討論內容.
  * [x] 協助 `EU-FAE YingXiang` 詢問 `iCF card 4000` 是否有 tool 可以讀取 `CIS` 資訊.
  * [x] 協助 `Nick` 處理 `Japan 3TE7` 電容量測問題.
  * [x] 協助 `Kiwi` 觀看 `Korea` 平台相關問題.
  * [x] 參與 `Japan` 詢問 `SSD` 存放 `20` years 的相關問題, 以及 `SSD` 寫入資料行為.

# 2022-08-29
* 撰寫 `Data Retention Official FAQ` 問題整理 PPT, 並找 `Kenzi`, `Miller` 討論內容.
* 協助 `EU-FAE YingXiang` 詢問 `iCF card 4000` 是否有 tool 可以讀取 `CIS` 資訊.
  * 已請 `吉洋` 提供相關 `hySMART` 工具, 但無法正常辨識.
  * 後續詢問 `Hank`, 發現廠內並無法提供工具, 因廠區驗證工具為 `DOS` 平台, 以及需透過 `PATA` 界面才能讀取 `CIS` 資訊, 並將狀況回報給 `YingXiang`.
  * 已發信詢問 `Hyperstone` 相關 `FAE` 人員詢問是否有其他工具可以讀取.
* 協助 `Nick` 處理 `Japan 3TE7` 電容量測問題.
* 詢問 `Pater` 關於 `Kontron` 會議上分享三位置電壓圖.
* 協助 `Kiwi` 觀看 `Korea` 平台相關問題, 目前尚未完成平台架設.
* 參與 `Japan` 詢問 `SSD` 存放 `20` years 的相關問題, 以及 `SSD` 寫入資料行為.
* TODO
  * [x] 詢問 `Hyperstone` 相關 `FAE` 人員詢問是否有其他工具可以讀取.
  * [x] 追蹤 `國巨` 相關電容問題詢問.
  * [x] 修改 `Data Retention Official FAQ` 問題整理 PPT.
  * [x] 協助 `Kiwi` 觀看 `Korea` 平台相關問題.
  * [x] 測試 `RMA` 維修後的 `3MV2-P`.
  * [x] 透過 `示波器` 量測 `3MV2-P` `Crystal` 訊號.
  * [x] 詢問 `Alan` 晶達 `3TE6` 客訴案狀況.
  * [x] 上傳新人訓練表單, 以及新人自評評分表.

# 2022-08-30
* 詢問 `Hyperstone` 相關 `FAE` 人員詢問是否有其他工具可以讀取, 已將 `hySMART` 寄給 `EU-FAE YingXiang`.
* 追蹤 `國巨` 相關電容問題詢問, 尚未回覆, 已經再次寄信詢問.
* 修改 `Data Retention Official FAQ` 問題整理 PPT.
* 協助 `Kiwi` 觀看 `Korea` 平台相關問題, 與 `Korea` 相關技術人員遠端了解系統如何操作.
* 測試 `RMA` 維修 `Controller` 後的 `3MV2-P`, 重開卡後, `NAND FLASH Mapping` & `BurninTest` 皆已正常.
* 詢問 `Alan` 晶達 `3TE6` 客訴案狀況, 需要再討論內容, 但不需出分析報告.
* 透過 `示波器` 量測 `3MV2-P` `Crystal` 訊號.
* 上傳新人訓練表單, 以及新人自評評分表.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 修改 `Nexcom` FA 分析報告.
  * [x] 測試 `RMA` 維修 `Crystal` 後的 `3MV2-P`.
  * [x] 參與 `RD` 月會.
  * [x] 協助 `Nick` 觀看 `Nexcom` `3TE7` 無法認碟問題.
  * [x] 協助 `EU-FAE YingXiang` 處理 `hySMART` tool 啟動相關問題.

# 2022-08-31
* 參與 `FAE` 週會.
* 修改 `Nexcom` FA 分析報告.
* 測試 `RMA` 維修 `Crystal` 後的 `3MV2-P`, 已可正常運作, `Crystal` 訊號也正常.
* 參與 `RD` 月會.
* 協助 `Nick` 看 `Nexcom` `3TE7` 無法認碟問題, 經過量測發現是 `U38` IC `1.1v` 電源供應問題.
* 協助 `EU-FAE YingXiang` 處理 `hySMART` tool 啟動相關問題, 已可成功啟動.
  * `執行環境` -> `Ubuntu 16.04`.
  * 缺少相關套件 `libftk-images1.3`.
  * 設備串接中間不能透過開卡板, 需直接串接 `SATA`.
* TODO
  * [x] 參與 `FAE` 月會.
  * [x] 修改 `Nexcom` FA 分析報告.
  * [x] 協助 `Pater` 量測加溼 `IR` 值.
  * [x] 與 `Miller` 討論 `Kontron` `180pcs` & `300pcs` 相關實驗.
  * [x] 盤點 `Kontron` `180pcs` 數量.
  * [ ] 撰寫 `B&R` FA 分析報告.

# 2022-09-01
* 參與 `FAE` 月會, 分享 `Read retry issue` 案例.
* 修改 `Nexcom` FA 分析報告.
* 協助 `Pater` 量測加溼 `IR` 值, 量測 `4` pcs(客退異常品->經過高溫處理), `2`(客退正常品), `1`(客退異常品).
* 與 `Miller` 討論 `Kontron` `180pcs` & `300pcs` 相關實驗, 並將 excel 欄位制定完成, 發送信件給相關人員.
* 盤點 `Kontron` `180pcs` 數量.
  * 目前: `169` pcs.
  * Benson: `3` pcs.
  * 損壞: `3` pcs.
  * 庫房: `4`pcs.
* TODO
  * [x] 修改 `Nexcom` FA 分析報告.
  * [x] 整理 `Kontron` 量測加溼 `IR` 值, 量測 `4` pcs(客退異常品->經過高溫處理), `2`(客退正常品), `1`(客退異常品).
  * [x] 重新量測 `Kontron` 加溼 `IR` 值, 量測 `4` pcs(客退異常品->經過高溫處理), `2`(客退正常品), `1`(客退異常品).
  * [x] 參加 `EU-FAE` 週會.
  * [x] 與 `EU Team` 開會 Update `Kontron` 分析結果.
  * [x] 協助 `Kiwi` 架設台達 `InnoOSR` 測速環境.
  * [x] 與 `Anita` 討論 `Kontron` 後續的量測.

# 2022-09-02
* 修改 `Nexcom` FA 分析報告, 已寄出給客戶.
* 整理 `Kontron` 量測加溼 `IR` 值, 量測 `4` pcs(客退異常品->經過高溫處理), `2`(客退正常品), `1`(客退異常品).
* 重新量測 `Kontron` 加溼 `IR` 值, 量測 `4` pcs(客退異常品->經過高溫處理), `2`(客退正常品), `1`(客退異常品).
* 參加 `EU-FAE` 週會.
* 與 `EU Team` 開會 Update `Kontron` 分析結果.
* 協助 `Kiwi` 架設台達 `InnoOSR` 測速環境, 已將測速結果提供.
* 與 `Anita` 討論 `Kontron` 後續的量測.
* TODO
  * [x] 紀錄 `169` pcs & `300` pcs `SMART` 數值.
  * [x] 參與 `Kontron` 討論會議.
  * [x] 協助 `Nick` 量測 `3TE7` power sequence.
  * [x] 與廠區人員討論 `169` pcs & `300` pcs 加熱量測實驗.

# 2022-09-05
* 紀錄 `169` pcs & `300` pcs `SMART` 數值.
* 參與 `Kontron` 討論會議.
* 協助 `Nick` 量測 `3TE7` power sequence.
* 與廠區人員討論 `169` pcs & `300` pcs 加熱量測實驗.
* TODO
  * [x] 撰寫 SMART Log 撈取, 以及轉換為 excel 程式.
  * [x] 與 `Nick` 學習 `SSD` `power` 訊號量測.
  * [x] 整理 `Kontron` 相關測試數據結果.

# 2022-09-06
* 撰寫 SMART Log 撈取, 以及轉換為 excel 程式.
* 與 `Nick` 學習 `SSD` `power` 訊號量測.
* 整理 `Kontron` 相關測試數據結果.
* TODO
  * [x] 整理 `Kontron` 相關測試數據結果.
  * [x] 協助 `Kiwi` 處理台達客訴案, 依照客人環境參數去作驗證.
  * [x] 撰寫 `B&R` 分析報告.

# 2022-09-07
* 整理 `Kontron` 相關測試數據結果.
* 協助 `Kiwi` 處理台達客訴案, 依照客人環境參數去作驗證.
* 撰寫 `B&R` 分析報告.
* 參加 `Kontron` 討論會議.
* TODO
  * [x] 查找 `Kontron` 客退品 `300pcs` 中, `shift read retry` 較多的 device, 並轉交給 `FW RD`.
  * [x] 紀錄 `Kontron` 客退品 `169pcs` `shift read retry` 資訊.
  * [x] 向 `Peter Hong` 借取 `5pcs` 轉板
  * [x] 排序 `Kontron` 客退品 `169pcs`, 並尋找遺漏之 `device`.
  * [x] 參加 `Kontron` 討論會議.

# 2022-09-08
* 查找 `Kontron` 客退品 `300pcs` 中, `shift read retry` 較多的 device, 並轉交給 `FW RD`.
* 紀錄 `Kontron` 客退品 `169pcs` `shift read retry` 資訊.
* 向 `Peter Hong` 借取 `5pcs` 轉板
* 排序 `Kontron` 客退品 `169pcs`, 並尋找遺漏之 `device`.
* 參加 `Kontron` 討論會議.
* TODO
  * [x] 紀錄 `Kontron` 客退品 `300pcs` 中, `58pcs` 之 `shift read retry` 資訊.
  * [x] 量測 `廠區` 協助找出之 `Kontron` 客退品 `300pcs` 中, `65C˚C`中 `11pcs` 異常品運作狀況(於客戶平台內.) 
  * [x] 參加 `Kontron` 討論會議.
  * [x] 挑取 `3pcs` 65C 異常品, 分別透過 `x86` 以及客退平台架設測試運行狀況.

# 2022-09-12
* 紀錄 `Kontron` 客退品 `300pcs` 中, `58pcs` 之 `shift read retry` 資訊.
* 量測 `廠區` 協助找出之 `Kontron` 客退品 `300pcs` 中, `65C˚C`中 `11pcs` 異常品運作狀況(於客戶平台內.) 
* 參加 `Kontron` 討論會議.
* 挑取 `3pcs` 65˚C 異常品, 分別透過 `x86` 以及客退平台架設測試運行狀況.
* TODO
  * [x] 復測 `Kontron` 客退品 `300pcs` 中, `65˚C`中 `11pcs` 異常品, 以及 `23pcs` 正常品(分別測試 `65˚C`, `85˚C`).
  * [x] 參加 `Kontron` 討論會議.
  * [x] 觀看 `3pcs` 65˚C 異常品, 分別透過 `x86` 以及客退平台架設測試運行狀況.
  * [x] 整理 `Kontron` 實驗相關數據.
  * [x] 查找 `GigaByte` 主板無法啟動之問題.

# 2022-09-13
* 復測 `Kontron` 客退品 `300pcs` 中, `65˚C`中 `11pcs` 異常品, 以及 `23pcs` 正常品(分別測試 `65˚C`, `85˚C`).
  * 廠區驗證異常品(`6pcs`):
    * `65˚C`: `1pcs`
    * `85˚C`: `5pcs`
  * 廠區驗證正常品(`23pcs`):
    * `65˚C`: All Pass
    * `85˚C`: 
      * `Fail`: `6pcs`
      * `Pass`: `17pcs` 
* 參加 `Kontron` 討論會議.
* 觀看 `3pcs` 65C 異常品, 分別透過 `x86` 以及客退平台架設測試運行狀況.* 整理 `Kontron` 實驗相關數據.
  * `Power on/off cycle`: `10s` 後上電, 等待 `90s`, 廣告機可正常播廣告後, 再斷電重啟.
  * 後續先改為上電後持續播放廣告, 看是否會發生問題.
  * 停止 `Power on/off cycle`: 當 `Uart log` 無抓取到 `6.0G`.
  * 架設 `示波器` 量測 `Host` -> `device` & `bead`  `3.3V` 電壓, 當電壓低於 `2.6V`, 就會 trigger 停止量測.
* 查找 `GigaByte` 主板無法啟動之問題, 後續發現為 `3TG6-P` pcie 硬碟問題.
* TODO
  * [x] 調整撈取 `SMART Log` 資訊程式.
  * [x] 整理 `Kontron` `300pcs` `SMART Log` 資訊.
  * [x] 參加組內 `FAE` 週會.
  * [x] 觀察客退平台架設測試運行狀況.
  * [x] 參加 `Kontron` 討論會議.

# 2022-09-14
* 調整撈取 `SMART Log` 資訊程式.
* 整理 `Kontron` `300pcs` `SMART Log` 資訊.
* 協助 `Kiwi` 架設 `台達` 客訴案環境, 並執行測速.
* 重灌 `Windows 10` 平台.
* 參加組內 `FAE` 週會.
* 觀察客退平台架設測試運行狀況, 後續有複製出現象.
  * 固定於 `12:22~12:23` 左右, 設備會重啟.
  * 重啟過程中, 設備殘電可能會造成 Device 有機率認不到.
  * 從 `SMART` Log, 可以觀看出 `Power on cycle` `Total LBAs Read` 有異常高數值.
  * 目前將 `Power on/off cycle` 改為 `1s` 後上電, 等待 `90s`, 廣告機可正常播廣告後, 再斷電重啟.
  * 如靠近上午 `11:00`, 現象尚未複製出來的話, 則改為持續播放廣告, 直至 `12:22~12:23` 左右看設備是否會重啟.
* 參加 `Kontron` 討論會議.
* TODO
  * [x] 整理 `Kontron` `300pcs` `SMART Log` 資訊.
  * [x] 觀察客退平台架設測試運行狀況.
  * [x] 觀看 `台達` 客訴案測速狀況.

# 2022-09-15
* 整理 `Kontron` `300pcs` `SMART Log` 資訊.
* 觀察客退平台架設測試運行狀況, 因原先第一台客退平台損壞, 故無法繼續量測問題.
* 觀看 `台達` 客訴案測速狀況, 後續發現寫入檔案路徑尚未修改正確, 故需重新測試.
* 整理測試平台位置.
* TODO
  * [x] 協助 `FW-RD` 架設 `Kontron` `5` 台客退平台.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 修改 `B&R` 分析報告.
  * [x] 撰寫祕密盤點表.
  * [x] 協助 `Kiwi` 重新處理 `台達` 客訴案測速.

# 2022-09-16
* 協助 `FW-RD` 架設 `Kontron` `5` 台客退平台.
  * `1` 台接上 `Uart log`, `示波器`, `Thermometer`.
  * `4` 台接上 `Uart log`.
* 參與 `EU-FAE` 週會.
* 修改 `B&R` 分析報告, 並寄給 `Jason` review.
* 撰寫祕密盤點表, 已寄給 `Kenzi`.
* 協助 `Kiwi` 重新處理 `台達` 客訴案測速.
* TODO
  * [x] 觀察 `Kontron` `5` 台客退平台運作狀況.
  * [x] 整理 `Kontron` 測試過程報告.
  * [x] 參與 `Kontron` 討論會議.
  * [x] 整理 `台達` 客訴案測速狀況, 並轉接給 `Kiwi`.

# 2022-09-19
* 觀察 `Kontron` `5` 台客退平台運作狀況
  * `1` 台接上 `Uart log`, `示波器`, `Thermometer`.
    * `示波器`: 觀察到 `Host` 端已經供電給 `Device`, 但 `Device` 中的 `Reset IC` 並無作動( `0V` ).
    * `Thermometer`: 運行 `1` hr, 溫度高達 `71˚C`.
* 整理 `Kontron` 測試過程報告.
* 參與 `Kontron` 討論會議.
  * 需挑取 `5` pcs `shift read retry` 過高的 `Device`, 每隔 `30` mins `power on/off`.
* 整理 `台達` 客訴案測速狀況, 並轉接給 `Kiwi`.
* TODO
  * [x] 觀察 `Kontron` `5` 台客退平台運作狀況.
  * [x] 整理 `Kontron` 測試過程報告.
  * [x] 參與 `Kontron` 討論會議.
  * [x] 修改 `B&R` FA 分析報告.

# 2022-09-20
* 觀察 `Kontron` `5` 台客退平台運作狀況.
* 參與 `Kontron` 討論會議.
* 整理 `Kontron` 測試過程報告.
* 修改 `B&R` FA 分析報告, 並寄出給 `Jessica`.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 修改 `Kontron` 系統 `Script`, 開始播放廣告 `2` mins 後, 重啟系統.
  * [x] 尋找 `大A` 討論 `iSMART` Log 存取問題.
  * [x] 整理 `Kontron` 測試過程報告.

# 2022-09-21
* 參與 `FAE` 週會.
* 修改 `Kontron` 系統 `Script`, 開始播放廣告 `2` mins 後, 重啟系統.
* 尋找 `大A` 討論 `iSMART` Log 存取問題.
* 整理 `Kontron` 測試過程報告.
* TODO
  * [x] 觀察 `Kontron` `5` 台客退平台運作狀況.
  * [x] 從 `180pcs` & `300pcs` 中, 挑出各 `20pcs` 做 `DLMC`(顯示溫度).
  * [x] 協助 `Benson` 討論 `MSI` & `Kontron` 電容問題.
  * [x] 測試 `Kontron` `3TE7` `DLMC` 功能(`顯示溫度`). 
  * [x] 測試 `SATA` 拷貝機.

# 2022-09-22
* 觀察 `Kontron` `5` 台客退平台運作狀況.
  * `30652` 發生 `PLL TO K-cnt=292`.
  * 其餘 `4pcs` 都正常運行.
* 從 `180pcs` & `300pcs` 中, 挑出各 `20pcs` 做 `DLMC`(顯示溫度).
  * 經過討論後, `180pcs` 不需做執行測試, 改為 `300pcs` 中選出 `50pcs`做 `DLMC`(顯示溫度).
  * 並將 `50pcs` 更換入客戶機台內, 觀察何時機台溫度會到達 `70˚C`.
  * 協助 `Benson` 討論 `MSI` & `Kontron` 電容問題.
  * 測試 `Kontron` `3TE7` `DLMC` 功能(`顯示溫度`). 
  * 測試 `SATA` 拷貝機.
* TODO
  * [x] 觀察 `Kontron` `5` 台客退平台運作狀況.
  * [x] 統整 `Kontron` 目前 `300pcs` 測試遇到之問題.
  * [x] 參與 `Kontron` 討論會議.

# 2022-09-23
* 觀察 `Kontron` `5` 台客退平台運作狀況.
* 統整 `Kontron` 目前 `300pcs` 測試遇到之問題.
* 參與 `Kontron` 討論會議.
* TODO
  * [x] 分配 `5` 台 `Kontron` 客退平台, 請同仁協助測試, 並講解流程, 以及如何紀錄.
  * [x] 與 `業務-James` 討論 `Nexcom` 信中提問.
  * [x] 測試 `Nexcom` 客製 `FW` `DLMC` 功能.
  * [x] 修改 `Kontron` 測試實驗參數( `on/off`: `5` min -> `2` min )

# 2022-09-26
* 分配 `5` 台 `Kontron` 客退平台, 請同仁協助測試, 並講解流程, 以及如何紀錄.
* 與 `業務-James` 討論 `Nexcom` 信中提問, 需要協助測試 `Windows` & `Linux` 平台.
* 測試 `Nexcom` 客製 `FW` `DLMC` 功能, 後續發現借測 `3TE7` device 與 客戶的 device 不同, 故無法 `DLMC`.
* 修改 `Kontron` 測試實驗參數( `on/off`: `5` min -> `2` min ).
* TODO
  * [x] 透過 `拷貝機` 測試 `Kontron` 測試實驗參數( `on/off`: `5` min -> `2` min ).
  * [x] 洽詢廠區協助借用 `拷貝機`.
  * [x] 協助 `FW-RD` 準備 `Delta` 測速平台, 討論如何在寫資料時, `device` 不做 `GC`.
  * [x] 整理 `Kontron` device 測試遇到之狀況.
  * [x] 與 `業務-James` 討論 `Nexcom` 客訴案.
  * [x] 測試 `Intel 12 代 CPU`, 看是否可以架設 `Windows`.
  * [x] 協助 `Nick` 測試 `SSH` 功能.
  * [x] 協助 `Kiwi` 紀錄 `CFast card` `Erase count` 較高的 `device`0

# 2022-09-27
* 透過 `拷貝機` 測試 `Kontron` 測試實驗參數( `on/off`: `5` min -> `2` min ).
* 洽詢廠區協助借用 `拷貝機`.
* 協助 `FW-RD` 準備 `Delta` 測速平台, 討論如何在寫資料時, `device` 不做 `GC`.
* 整理 `Kontron` device 測試遇到之狀況.
* 與 `業務-James` 討論 `Nexcom` 客訴案.
* 測試 `Intel 12 代 CPU`, 看是否可以架設 `Windows`.
* 協助 `Nick` 測試 `SSH` 功能.
* 協助 `Kiwi` 紀錄 `CFast card` `Erase count` 較高的 `device`.
  * `4080F` -> `7159`.
  * `06807` -> `455`.
  * `06808` -> `3498`.
  * `06807` -> `2348`.
* TODO
  * [x] 量測並觀察 `Kontron` device 測試狀況.
  * [x] 參與 `FAE-週會`, 並分享 `Kontron` 目前測試狀況.
  * [x] 將廠區協助拷貝 `Kontron` `60pcs`  device, 一片一片做 `DLMC`(更新為 `Uart log` 顯示 `temp`).
  * [x] 與廠區協調 `Kontron` device 拷貝, 將剩餘 `170pcs` 轉交於廠區人員處理.
  * [x] 測試 `Nexcom` device `DLMC` 功能.
  * [x] 與登科討論 `Loader mode` device.

# 2022-09-28
* 量測並觀察 `Kontron` device 測試狀況.
* 參與 `FAE-週會`, 並分享 `Kontron` 目前測試狀況.
* 將廠區協助拷貝 `Kontron` `60pcs`  device, 一片一片做 `DLMC`(更新為 `Uart log` 顯示 `temp`).
* 與廠區協調 `Kontron` device 拷貝, 將剩餘 `170pcs` 轉交於廠區人員處理.
* 測試 `Nexcom` device `DLMC` 功能, 後續發現還是無法更新, 已將 `log` 轉交給 `FW-RD`.
* 與登科討論 `Loader mode` device, 目前先確認是否有 `crack`, 已請 `Chris Kao` 協助照 `X-ray`.
* TODO
  * [x] 量測並觀察 `Kontron` device 測試狀況.
  * [x] 與 `大A` 討論 `3TE7` `DLMC` 軟體開發(`Linux`), 因 `3TE7` 有小板號更新問題, 所以需將特定存放位置讀取出來判斷 `FW` 位置.
  * [x] 將廠區協助拷貝 `Kontron` `170pcs`  device, 一片一片做 `DLMC`(更新為 `Uart log` 顯示 `temp`).
  * [x] 盤點 `Kontron` 目前測試片數.
  * [x] 參與 `FAE-月會`.

# 2022-09-29
* 量測並觀察 `Kontron` device 測試狀況.
* 與 `大A` 討論 `3TE7` `DLMC` 軟體開發(`Linux`), 因 `3TE7` 有小板號更新問題, 所以需將特定存放位置讀取出來判斷 `FW` 位置.
* 將廠區協助拷貝 `Kontron` `170pcs`  device, 一片一片做 `DLMC`(更新為 `Uart log` 顯示 `temp`).
  * 發現 `4pcs` 出現 `Loader mode` 狀況, `Write code` 發生問題, 已將 `log` 轉給 `FW-RD` 協助觀看.
* 盤點 `Kontron` 目前測試片數.
* 參與 `FAE-月會`.
* TODO
  * [x] 驗證 `iSMART` 儲存 `shift read retry` log 功能.
  * [ ] 透過系統上單申請 `Software` 處理 `Nexcom` `3TE7` `DLMC` tool.
  * [x] 參與 `Kontron` 討論會議.
  * [x] 量測並觀察 `Kontron` device 測試狀況.

# 2022-09-30
* 驗證 `iSMART` 儲存 `shift read retry` log 功能.
* 參與 `Kontron` 討論會議.
* TODO
  * [x] 參與 `iOAPL` 教育訓練.
  * [x] 協助 `Kiwi` 架測 `智邦` 客訴案(`3ME4`). 
  * [x] 撰寫 `8D` report.
  * [x] 量測並觀察 `Kontron` device 測試狀況.

# 2022-10-03
* 參與 `iOAPL` 教育訓練.
* 協助 `Kiwi` 架測 `智邦` 客訴案(`3ME4`). 
* 撰寫 `8D` report.
* 量測並觀察 `Kontron` device 測試狀況.
* TODO
  * [x] 量測並觀察 `Kontron` device 測試狀況.
  * [x] 發起 `iSMART` tool 軟體需求單.
  * [x] 協助 `Kiwi` 紀錄 `智邦` 客訴案(`3ME4`)平台執行 log.
  * [x] 協助 `EU-FAE` 回覆 `3ME2` 相關問題.

# 2022-10-04
* 量測並觀察 `Kontron` device 測試狀況.
* 發起 `iSMART` tool 軟體需求單.
* 協助 `Kiwi` 紀錄 `智邦` 客訴案(`3ME4`)平台執行 log.
* 協助 `Kenzi` 測試 `3TE7` DLMC tool.
  * `64GB` -> `ok`.
  * `128GB` -> `wait for device`.
  * `256GB` -> `wait for device`.
  * `512GB` -> `ok`.
  * `1T` -> `ok`.
* 協助 `EU-FAE` 回覆 `3ME2` 相關問題.
  * 測試過程中, 電流數值多少.
  * 多久 `上斷電` 一次.
  * `1R` 電阻能承受電流為多少.
  * 相關的電流 `spec` table 表.
* TODO
  * [x] 協助 `Kenzi` 測試 `3TE7` DLMC tool.
    * [x] `128GB`.
    * [x] `256GB`.
  * [x] 量測並觀察 `Kontron` device 測試狀況.
  * [x] 參與 `FAE-週會`, 並分享 `Kontron` 目前測試狀況.
  * [x] 觀看 `iSMART` tool source code.
  * [x] 製作 `Uart` 量測針腳(`18`個).

# 2022-10-05
* 協助 `Kenzi` 測試 `3TE7` DLMC tool.
  * `128GB` -> `ok`.
  * `256GB` -> `ok`.
* 量測並觀察 `Kontron` device 測試狀況, 並統整數量.
* 參與 `FAE-週會`, 並分享 `Kontron` 目前測試狀況.
* 觀看 `iSMART` tool source code.
* 製作 `Uart` 量測針腳(`18`個).
* TODO
  * [x] 協助 `Kenzi` 測試 `3TE7` DLMC tool(`Nexcom`).
  * [x] 量測並觀察 `Kontron` device 測試狀況.
  * [x] 協助 `Alex` 觀看效能測試 script. 
  * [x] 觀看 `iSMART` 更新 source code.

# 2022-10-06
* 協助 `Kenzi` 測試 `3TE7` `DLMC tool` (`Nexcom`), 發現 DLMC Fail.
  * 與 `FW-RD Allen` 一同測試, 發現 `DLMC tool`  顯示及功能不符合預期.
  * 明日會一同前往找尋 `大 A` 討論.
* 量測並觀察 `Kontron` device 測試狀況.
* 協助 `Alex` 觀看效能測試 script. 
* 觀看 `iSMART` 更新 source code.
* TODO
  * [x] 協助 `Kiwi` 觀看 `FA221005002`, `FA221005003` 客訴案.
  * [x] 協助 `業務-Jolie` 觀看 `裕達` 客訴品.
  * [x] 測試 `3TE7 DLMC` mkmp tool 功能.
  * [x] 參與 `EU-FAE` 週會.

# 2022-10-07
* 協助 `Kiwi` 觀看 `FA221005002`, `FA221005003` 客訴案.
  * `FA221005002` -> `3ME2` 發生 `device` 啟動一段時間後, 發生 `shutdown`, 再啟動的循環動作.
* 協助 `業務-Jolie` 觀看 `裕達` 客訴品.
* 測試 `3TE7 DLMC` mkmp tool 功能, 後續前往與 `大 A` 討論.
  * 需透過 `vender command` 更新 `SSD`, `-f` 不能輸入指定 `bin` 檔, 需帶入 `SN.txt`.
* 參與 `EU-FAE` 週會.
  * 討論 `3TE7 DLMC` mkmp tool 功能測試結果.
  * mkmp tool `mode 0` & `mode 1` 功能.
* TODO
  * [x] 測試 `3TE7 DLMC` mkmp tool 功能, 後續前往與 `大 A` 討論.
  * [x] 與 `FW-RD` 討論 mkmp tool 執行步驟, 以及 `FW` 版本更新.
  * [x] 修改 `Kontron` `8D` report.
  * [x] 協助 `Kiwi` 修改 `3TE6` FW update 步驟報告.
  * [x] 測試 `FTB221006001` -> `3ME3` 開機 `UART` log 錄製, 以及挑取全新 `device` copy 母碟程式觀看現象是否一樣.

# 2022-10-11
* 測試 `3TE7 DLMC` mkmp tool 功能, 後續前往與 `大 A` 討論.
* 與 `FW-RD` 討論 `mkmp tool` 執行步驟, 以及 `FW` 版本更新, 發現缺少檔案, 以及程式 `log` 顯示有誤.
  * `exception.txt`.
  * `SN.txt`.
  * `Version` -> `1.4.1`.
* 修改 `Kontron` `8D` report( `3D` ).
* 協助 `Kiwi` 修改 `3TE6` FW update 步驟報告, 已將報告寄出.
* 測試 `FTB221006001` -> `3ME3` 開機 `UART` log 錄製, 以及挑取全新 `device` copy 母碟程式觀看現象是否一樣, 經過測試, 發現為一樣.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 參與 `Kontron` `8D` report 討論會議.
  * [x] 修改 `Kontron` `8D` report( `5D`, `6D`, `7D` ).
  * [x] 測試 `FTB221006001` -> 挑取全新 `3ME3`, 安裝 `Windows` OS, 觀看於客戶平台是否可正常被辨識.
  * [x] 與 `EU-FAE` 討論 `8D` report.

# 2022-10-12
* 參與 `FAE` 週會.
* 參與 `Kontron` `8D` report 討論會議.
* 修改 `Kontron` `8D` report( `5D`, `6D`, `7D` ).
* 測試 `FTB221006001` -> 挑取全新 `3ME3`, 安裝 `Windows` OS, 觀看於客戶平台是否可正常被辨識, 經過測試可正常進入系統.
* 與 `EU-FAE` 討論 `8D` report, 經過討論後, 需取得 `Anita` 同意.
* 整理信件, 以及電腦檔案.
* TODO
  * [x] 修改 `Kontron` `8D` report( `5D`, `6D`, `7D` ).
  * [x] 測試 `mkmp tool`.
  * [ ] 撰寫 `3TE7` 對應 `FW` bin 檔程式.
  * [ ] 觀看 `Alex` 測試 `script`.
  * [x] 觀看 `FA221005003` 客訴案.

# 2022-10-13
* 修改 `Kontron` `8D` report( `5D`, `6D`, `7D` ).
* 測試 `mkmp tool`.
* 觀看 `FA221005003` 客訴案.
  * `BCA12205230120259`, `BCA12205230120260` 與客戶看到一樣現象, 應為資料遺失, 需要詢問客戶操作或是測試手法.
  * `BCA12208290110003` 為 `UNC`, 但已超出設備儲存量, 需要詢問客戶操作或是測試手法.
* TODO
  * [x] 測試 `mkmp tool`.
  * [x] 參與 `EU-FAE` 週會.

# 2022-10-14
* 測試 `mkmp tool`, 外顯需為 `S20615` 才可更新, `Nexcom` 外顯為 `S20813S`, 故會有問題, 另外 `SN.txt` 需輸入產品 `SN` 碼, 最後 `4` 碼流水號不需輸入.
  * `64G RAID` & `64G nonRAID` -> `Pass`.
  * `256G` & `256G-1125` -> `Pass`.
  * `512G` & `512G-1125` -> `Pass`.
  * `128G` -> No device.
  * `256GB 2CH 2CE` -> No device.
  * `1T` -> No device.
* TODO
  * [x] 借出以下 `3TE7` 設備, 各一片.
    * [x] `128G`.
    * [x] `256GB 2CH 2CE`.
    * [x] `1T`.
  * [x] 請業務詢問 `FA221005003` 客戶使用方式.
  * [x] 與 `FW-RD Allen` 討論 `Kontron` device `FW` Version.
  * [x] 修改 `8D` report.
  * [x] 與 `MIS-Micky` & `Hank` 討論 `iPacker` 打包問題.

# 2022-10-17
* 借出以下 `3TE7` 設備, 各一片.
  * `128G`.
  * `256GB 2CH 2CE`.
  * `1T`.
* 請業務詢問 `FA221005003` 客戶使用方式.
* 與 `FW-RD Allen` 討論 `Kontron` device `FW` Version, 因 `Device` 為 `Bics 3`, `FW` 需使用 `S22921`.
* 修改 `8D` report.
* 與 `MIS-Micky` & `Hank` 討論 `iPacker` 打包問題, 發現 `V2.2.5` 無法使用, `V2.1.5` 可執行, 但需在 `Server` 上執行, 無法於桌面執行, 後續請 `MIS` 協助觀看.
* TODO
  * [ ] 撰寫 `3TE7` 對應 `FW` bin 檔程式.
  * [ ] 觀看 `Alex` 測試 `script`.
  * [x] 測試 `FA221005003` 其中 `1` pcs, 重灌 `Win10`.
  * [x] 與 `Yichuan Chen`, `Chris Kao`, `Benson` 討論 `Kontron` `5D` ~ `7D` 內容.
  * [x] 參與 `Kontron` 討論會議.
  * [x] 與 `FW-RD Allen` 討論 `FA221005003` `UNC` 問題.
  * [x] 結案 `Nexcom` 客訴案.

# 2022-10-18
* 測試 `FA221005003` 其中 `1` pcs, 重灌 `Win10`, 安裝過程發現客戶 `Disk` 切割為 `MBR`, 故需研究如何將 `Disk` 安裝 `Win10` 時, `Disk` 切割不為 `GPT`.
* 與 `Yichuan Chen`, `Chris Kao`, `Benson` 討論 `Kontron` `5D` ~ `7D` 內容.
* 參與 `Kontron` 討論會議.
* 與 `FW-RD Allen` 討論 `FA221005003` `UNC` 問題, 需透過開卡包中的 `Utility` 觀察是否有 `Error` message.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 測試 `FA221005003` 其中 `1` pcs, 重灌 `Win10`, 切割表需為 `MBR`.
  * [x] 測試 `mkmp tool` 功能.
    * [x] `128G`.
    * [x] `256GB 2CH 2CE`.
    * [x] `1T`.
  * [x] 轉交 `B&R` 客訴品.
  * [x] 透過開卡包中的 `Utility` 觀察是否有 `Error` message(`FA221005003`).
  * [x] 協助 `Kiwi` 觀看 `Disk` `mount/umount` 測試 `read/write` 速度.
  * [x] 處理 `iPacker` tool 問題.
  * [x] 處理並了解 `FPS` tool 問題.
  * [x] 測試 `裕達` 正常品拷貝至 `客訴品` 是否可正常運行.

# 2022-10-19
* 參與 `FAE` 週會.
* 測試 `FA221005003` 其中 `1` pcs, 重灌 `Win10`, 切割表需為 `MBR`, 已成功完成測試.
  * 需將 `USB` 內的 `efi` file & `boot-efi` 兩個檔案刪除.
  * 將 `disk` 切割表預先改為 `MBR`.
* 測試 `mkmp tool` 功能, 已全數驗證完成, 並回報狀況給 `EU` 同仁.
  * `128G`.
  * `256GB 2CH 2CE`.
  * `1T`.
* 轉交 `B&R` 客訴品, 已交付給 `Jessica`.
* 透過開卡包中的 `Utility` 觀察是否有 `Error` message(`FA221005003`).
  * 觀看其中 `2` pcs 無法 `boot` device, 皆無 `Error` message.
* 協助 `Kiwi` 觀看 `Disk` `mount/umount` 測試 `read/write` 速度.
* 處理 `iPacker` tool 問題, 需透過 `S槽掛掉可打包` 之 `iPacker` 才可正常操作.
* 處理並了解 `FPS` tool 問題, `company id` 需為 `innodisk`, 程式關閉時, 開卡包會隨之刪除, 故需先將開卡包(`InnoDiskFiles`) `copy` 於 `pack`.
* 測試 `裕達` 正常品拷貝至 `客訴品` 是否可正常運行, 目前測試可正常登錄, 但無法成功運行客戶程式, 經由業務詢問, 發現客戶寄送來的 `Device` 為新機種的 `Device`, 無法在舊機台運行.
* TODO
  * [x] 回報 `裕達` 測試狀況給客戶, 並將其餘 `3` pcs 全新品 `copy` 新機種程式.
  * [x] 透過開卡包中的 `Utility` 觀察 `UNC` device 是否有 `Error` message(`FA221005003`).
  * [x] 撰寫 `mkmp` tool 操作手冊.
  * [x] 修改 `Kontron` `8D` report.
  * [ ] 撰寫 `3TE7` 對應 `FW` bin 檔程式.
  * [ ] 觀看 `Alex` 測試 `script`.

# 2022-10-20
* 回報 `裕達` 測試狀況給客戶, 並將其餘 `3` pcs 全新品 `copy` 新機種程式.
* 透過開卡包中的 `Utility` 觀察 `UNC` device 是否有 `Error` message(`FA221005003`), 經過測試發現有相關訊息, 並將結果轉接給 `FW-RD`.
* 撰寫 `mkmp` tool 操作手冊, 已完成並寄送給 `EU-FAE`.
* 修改 `Kontron` `8D` report, 已將 `2` 份 report 寄出.
* 與 `EU-FAE` 討論 `8D` report & `Siemens` USB 客訴案.
* TODO
  * [x] 撰寫 `FA221005002` FA report.
  * [x] 撰寫 `FA221005003` FA report.
  * [x] 參與 `EU-FAE` 週會.
  * [ ] 撰寫 `3TE7` 對應 `FW` bin 檔程式.
  * [x] 觀看 `Alex` 測試 `iotest` `script`.

# 2022-10-21
* 撰寫 `FA221005002` FA report, 因 `Device` 問題尚未找到, 故無法撰寫.
* 撰寫 `FA221005003` FA report, 已有初版.
* 參與 `EU-FAE` 週會.
* 觀看 `Alex` 測試 `iotest` `script`, 遇到 `dmesg` 執行有權限問題.
* TODO
  * [x] 觀看 `Alex` 測試 `iotest` `script`.
  * [x] 協助 `Kiwi` 測試 `iotest` `script`(`3ME4` 掉速問題).
  * [x] 協助 `Kiwi` 測試 `3TE7` `iCell` `40GB` 容量問題.
  * [x] 撰寫 `FA221005002` FA report.
  * [x] 測試 `智邦` `3TE7` 掉速問題.

# 2022-10-24
* 觀看 `Alex` 測試 `iotest` `script`.
* 協助 `Kiwi` 測試 `iotest` `script`(`3ME4` 掉速問題).
* 協助 `Kiwi` 測試 `3TE7` `iCell` `40GB` 容量問題, 已將結果回報.
* 撰寫 `FA221005002` FA report, 經由重開卡後, 研究如何安裝 `CentOS 8`.
* 測試 `智邦` `3TE7` 掉速問題.
* TODO
  * [x] 觀看 `Kiwi` 測試 `iotest` `script`(`3ME4` 掉速問題).
  * [x] 測試 `智邦` `3TE7` 掉速問題.
  * [x] 撰寫 `FA221005002` FA report, 並將報告上傳.
  * [x] 修改 `iotest` `script`.

# 2022-10-25
* 觀看 `Kiwi` 測試 `iotest` `script`(`3ME4` 掉速問題).
* 測試 `智邦` `3TE7` 掉速問題.
* 撰寫 `FA221005002` FA report, 並將報告上傳.
* 修改 `iotest` `script`.
* TODO
  * [x] 參加 `FAE` 週會.
  * [x] 處理 `裕達` 客訴案.
  * [x] 處理 `台達` 測速案.
  * [x] 協助 `EU-FAE` 借取 `R2DGM28-02TDC1GWDEQ-MN` 樣品.
  * [x] 透過顯微鏡照 `FEC221003004` 客訴案 `Siemens` USB. 
  * [x] 處理 `FA221005002`, `FA221005003` FA report, 並提供給業務.
  * [x] 參加 `RD` 月會.
  * [x] 向 `Josh` 借取 `USB` analyzer.

# 2022-10-26
* 參加 `FAE` 週會.
* 處理 `裕達` 客訴案, 已查找出問題, 主要是客戶機台內, 存取 `log` 之 `WD` disk 無法透過機台主板辨識, 透過 `USB 轉板` 即可正常開啟.
* 協助 `EU-FAE` 借取 `R2DGM28-02TDC1GWDEQ-MN` 樣品.
* 透過顯微鏡照 `FEC221003004` 客訴案 `Siemens` USB. 
* 處理 `FA221005002`, `FA221005003` FA report, 並提供給業務.
* 向 `Josh` 借取 `USB` analyzer.
* TODO
  * [x] 參加 `FAE` 月會.
  * [x] 處理 `裕達` 客訴案, 並將狀況 demo 給客戶看.
  * [x] 協助 `Kiwi` 將 `CFast card` 對應編碼整理, 並轉交給業務 `Vincent`.
  * [x] 處理 `FEC221003004` 客訴案 `Siemens` USB 客訴案, 並將照片轉交給 `QA-Chris`, 協助分析.
  * [x] 與 `EU-FAE` 討論客訴案相關處理跟細節.
  * [x] 處理 `台達` 測速案, 並紀錄其結果.
  * [x] 協助 `EU` `FED221026007` 測試 `3TG6-P R2DGM28-02TDC1GWDEQ-MN`, 安裝 `Ubuntu`, 測試 `shutdown`, `halt`, `reboot` 功能.

# 2022-10-27
* 參加 `FAE` 月會.
* 處理 `裕達` 客訴案, 並將狀況 demo 給客戶看, 後續將設備歸還給客戶.
* 協助 `Kiwi` 將 `CFast card` 對應編碼整理, 並轉交給業務 `Vincent`.
* 處理 `FEC221003004` 客訴案 `Siemens` USB 客訴案, 並將照片轉交給 `QA-Chris`, 協助分析, 經過分析後, 發現無空焊問題.
* 與 `EU-FAE` 討論客訴案相關處理跟細節.
* 處理 `台達` 測速案, 並紀錄其結果, 已將結果回報給 `PM-Jack`, 並協助測試 `Phison` SSD `CDM` & `AIDA64`.
* 協助 `EU` `FED221026007` 測試 `3TG6-P R2DGM28-02TDC1GWDEQ-MN`, 安裝 `Ubuntu`, 測試 `shutdown`, `halt`, `reboot` 功能.
  * `shutdown` -> `Pass`
  * `reboot` -> `Pass`
  * `halt` -> `Fail`, 螢幕熄滅, 但電源並無切斷.
* TODO
  * [x] 處理 `台達` 測速案, 更換 `device` 為 `M.2 S80 3TE7`(將 `Phison` 程式 copy 出來 ).
  * [x] 測試 `EU` `FEC221019005` USB 插拔, 觀看是否出現 `Loader mode`.
  * [x] 協助 `EU` `FED221026007` 測試 `Samsung 860` & `3TE6` 於 `Ubuntu` 執行 `halt` 功能, 觀看是否與 `3TG6-P R2DGM28-02TDC1GWDEQ-MN` 狀況相同.
  * [x] 整理 `台達` 測速案結果, 並轉交給業務 `MJ Lee`.

# 2022-10-28
* 處理 `台達` 測速案, 更換 `device` 為 `M.2 S80 3TE7`(將 `Phison` 程式 copy 出來 ).
* 測試 `EU` `FEC221019005` USB 插拔, 觀看是否出現 `Loader mode`.
* 協助 `EU` `FED221026007` 測試 `Samsung 860` & `3TE6` 於 `Ubuntu` 執行 `halt` 功能, 觀看是否與 `3TG6-P R2DGM28-02TDC1GWDEQ-MN` 狀況相同.
* 整理 `台達` 測速案結果, 並轉交給業務 `MJ Lee`.
* TODO
  * [x] 協助 `Kiwi` 量測 `3ME4`, `3ME3` `power construction`.
  * [x] 處理 `台達` 測速案, 紀錄結果, 並轉交 `UART` log 給 `FW-RD`.
  * [x] 協助 `EU` `FED221026007` 測試 `3TG6-P R2DGM28-02TDC1GWDEQ-MN`, 將其 `FW` 刷成 `C22307`.
  * [x] 測試 `EU` `FEC221019005` USB 插拔, 插拔 `10` 次, reboot `50` 次.
  * [x] 參加 `innoGrid` 封包教育訓練.
  * [x] 協助 `Kiwi` 紀錄 `Quixant` `CFast card` `SMART` value.

# 2022-10-31
* 協助 `Kiwi` 量測 `3ME4`, `3ME3` `power construction`.
* 處理 `台達` 測速案, 紀錄結果, 並轉交 `UART` log 給 `FW-RD`, 並協助 `FW-RD` 更新 `FW`, 再重新測試一遍.
* 協助 `EU` `FED221026007` 測試 `3TG6-P R2DGM28-02TDC1GWDEQ-MN`, 將其 `FW` 刷成 `C22307`, 狀況與新 `FW` 相同, 並將結果回報給 `EU-FAE`.
* 測試 `EU` `FEC221019005` USB 插拔, 插拔 `10` 次, reboot `50` 次, 狀況都無問題, 並將結果回報給 `EU-FAE`.
* 參加 `innoGrid` 封包教育訓練.
* 協助 `Kiwi` 紀錄 `Quixant` `CFast card` `SMART` value.
* TODO
  * [x] 協助 `Kiwi` 紀錄 `Quixant` `CFast card` `SMART` value.
  * [x] 協助 `FW-RD` 架設 `Delta` 測試環境.
  * [x] 查詢 `Compliance test` 如何透過 `SATA analyzer` 運作.
  * [x] 協助 `Alex` 觀看 `Ubuntu` 無法進入, 直接進入 `grub` 問題.
  * [x] 協助回覆 `EU-FAE` 相關問題.

# 2022-11-01
* 協助 `Kiwi` 紀錄 `Quixant` `CFast card` `SMART` value.
* 協助 `FW-RD` 架設 `Delta` 測試環境.
* 查詢 `Compliance test` 如何透過 `SATA analyzer` 運作, 後續發現需要裝額外擴充卡( `External Power Expansion card` )才可執行, 已將狀況回報給 `EU-FAE`.
* 協助 `Alex` 觀看 `Ubuntu` 無法進入, 直接進入 `grub` 問題.
* 協助回覆 `EU-FAE` 相關問題( `3TG6-P` 測試結果 & `4TG2-P` DLMC tool ).
* TODO
  * [x] 參加 `FAE` 週會.
  * [x] 協助 `Alex` 觀看 `Ubuntu` 無法進入, 直接進入 `grub` 問題.
  * [x] 協助 `Kiwi` 處理 `B&R` `CFexpress` `Re-MP` 以及放入 `Chamber` 高溫測試 `BurninTest`, 紀錄 `SMART` value.
  * [x] 撰寫 `Ericsson` 測試 `USB` reboot `shell script`.
  * [x] 協助 `EU-FAE` 詢問 `eye tool` 相關資訊.
  * [x] 清潔測試 `Gigabyte` 平台.

# 2022-11-02
* 參加 `FAE` 週會.
* 協助 `Alex` 觀看 `Ubuntu` 無法進入, 直接進入 `grub` 問題, 後續發現為 `bitmap` 有錯誤, 無法修正, 需將 device 重新安裝.
* 協助 `Kiwi` 處理 `B&R` `CFexpress` `Re-MP` 以及放入 `Chamber` 高溫測試 `BurninTest`, 紀錄 `SMART` value.
* 撰寫 `Ericsson` 測試 `USB` reboot `shell script`, 已開始測試.
* 協助 `EU-FAE` 詢問 `eye tool` 相關資訊, 並將相關資訊給出.
* 清潔測試 `Gigabyte` 平台.
* TODO
  * [x] 修改 `innoWorks` FA report & 結案.
  * [x] 協助 `Kiwi` 製作 `USB` 開機 `OS`. 
  * [x] 參與 `Delta` 客訴案討論.
  * [x] 寄出 `3TE7` `DLMC-tool`.
  * [x] 處理 `FEC220830004-Siemens` USB 客訴案.
  * [x] 領取採購 `2m-網路線 * 10` 條.

# 2022-11-03
* 修改 `innoWorks` FA report & 結案, 並將新版 FA report 上傳.
* 協助 `Kiwi` 製作 `USB` 開機 `OS`. 
* 參與 `Delta` 客訴案討論.
* 寄出 `3TE7` `DLMC-tool`.
* 處理 `FEC220830004-Siemens` USB 客訴案, 發現無法進入 `Loader mode`, 已經申請領料.
* 領取採購 `2m-網路線 * 10` 條.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 測試 `3TE7` ( `DEM24-32GDK1EW1SF-G14` ) 是否可透過 `Debian` 執行 `DLMC` 更新 `FW`.
  * [x] 撰寫 `台達` `DLMC` 流程操作, 以及 `UART` log 錄製步驟.
  * [x] 測試 `智邦` `3TE7` ( `DEM24-32GDK1KCASL-E56` ) 於客戶平台之 `SATA Link` 狀況.
  * [x] 整理 `3TE7` `DLMC` 出貨表格, 以及撰寫容量對應 `FW bin` 檔程式. 

# 2022-11-04
* 參與 `EU-FAE` 週會.
* 測試 `3TE7` ( `DEM24-32GDK1EW1SF-G14` ) 是否可透過 `Debian` 執行 `DLMC` 更新 `FW`.
* 撰寫 `台達` `DLMC` 流程操作, 以及 `UART` log 錄製步驟.
* 測試 `智邦` `3TE7` ( `DEM24-32GDK1KCASL-E56` ) 於客戶平台之 `SATA Link` 狀況.
* 整理 `3TE7` `DLMC` 出貨表格, 以及撰寫容量對應 `FW bin` 檔程式. 
* TODO
  * [x] 協助 `Miller` 整理 `Kontron` 不良品數據, 以及 `FW-S19C04B` -> `FW-S20615` 更新內容.
  * [x] 撰寫人才推薦表.
  * [x] 協助 `EU-Nancy` 回覆 `Kontron` 相關賠償問題.
  * [x] 觀察 `台達` 測速結果.
  * [x] 撰寫 `3TE7` 容量對應 `FW bin` 檔程式 (`0721`). 
  * [x] 協助 `Jesse` 將 `4` 支 `3ME4` 開卡.
  * [x] 協助 `EU-FAE` 準備 `RS232 TO USB` 轉接線.

# 2022-11-07
* 協助 `Miller` 整理 `Kontron` 不良品數據, 以及 `FW-S19C04B` -> `FW-S20615` 更新內容.
  * 修正 `GC`, `EOL` 問題
  * `Enterprise command timeout` ( `Table Swap` 利用 HW `RLS buffer`)
  * `Trim` 掉盤問題 ( `CMT` 爆掉)
  * 修正 `power cycle` 後, `Idle` 狀態產生 `Later Bad`, FW fix power on active block 將 `raid` 資料補滿( `dummy data` ).
  * 修正建表過久的問題(劃線 `/cmt acc` 啟動).
  * Modify TSB `shift read` table(`bics3_64GB/bics4`).
  * Fix dynamic SLC cache `tst` 後, 造成 `GC` 卡住掉碟.
* 撰寫人才推薦表.
* 協助 `EU-Nancy` 回覆 `Kontron` 相關賠償問題.
  * `電容` 有問題批次的 `不良佔比`? -> `110 / 500` = `22%`.
  * `FW` 跟之前版本的差異:
    * 1. 解決 `PLL` issue.     
    * 2. 解決 `Assert` issue.  
* 觀察 `台達` 測速結果.
* 撰寫 `3TE7` 容量對應 `FW bin` 檔程式. 
* 協助 `Jesse` 將 `4` 支 `3ME4` 開卡.
* 協助 `EU-FAE` 準備 `RS232 TO USB` 轉接線.
* TODO
  * [x] 轉換 `Delta` 測速結果, 並寄出.
  * [x] 透過 `SATA analyzer` 錄製 `Delta` 平台 `SATA Link` 調速問題.
  * [x] 追蹤 `ICC` `mSATA 3SE` `NCQ` 測項狀況.
  * [ ] 撰寫 `3TE7` 容量對應 `FW bin` 檔程式 (`1125`). 
  * [x] 協助 `Kiwi` 觀看 `FA` report(`FA220908002`).

# 2022-11-08
* 轉換 `Delta` 測速結果, 並寄出.
* 透過 `SATA analyzer` 錄製 `Delta` 平台 `SATA Link` 調速問題.
* 追蹤 `ICC` `mSATA 3SE` `NCQ` 測項狀況.
* 協助 `Kiwi` 觀看 `FA` report(`FA220908002`).
* TODO
  * [x] 參加 `FAE` 週會.
  * [x] 處理 `EU-Jason` `FEC221019005` `NCQ2`, `NCQ3` 測試 `mSATA 3SE`.
  * [x] 處理 `EU-YingXiang` `FEC221003004` 更換 `Controller` 相關進度.
  * [x] 處理 `EU-YingXiang` `Reflex M.2 P80 3TG6-P` 更新 `DLMC` tool 使用文件及流程.
  * [x] 協助 `Kiwi` 處理 `3TG6-P` 開卡問題.
  * [x] 協助 `Jesse` 處理 `智邦` 大陸廠檔案寫入問題.

# 2022-11-09
* 參加 `FAE` 週會.
* 處理 `EU-Jason` `FEC221019005` `NCQ2`, `NCQ3` 測試 `mSATA 3SE`.
* 處理 `EU-YingXiang` `FEC221003004` 更換 `Controller` 相關進度.
* 處理 `EU-YingXiang` `Reflex M.2 P80 3TG6-P` 更新 `DLMC` tool 使用文件及流程.
* 協助 `Kiwi` 處理 `3TG6-P` 開卡問題.
* 協助 `Jesse` 處理 `智邦` 大陸廠檔案寫入問題.
* TODO
  * [x] 撰寫 `3TE7` 容量對應 `FW bin` 檔程式 (`1125`).
  * [x] 修改 `mkmp` tool 使用手冊( For `客戶` ).
  * [x] 測試 `PM-Jack` `mkmp` tool( `20210114_WWN` ).
  * [x] 測試 `ICC` `mSATA 3SE` `NCQ` 測項狀況( `Write code` 更新 `FW` -> `SYS_S_S130710K` ).
  * [x] 整理 `mkmp` 走正常 `DLMC` 流程, 並寄出與 `大A` 討論.
  * [x] 撰寫 `size.txt` 檔案.
  * [x] 參與 `B&R` 討論.

# 2022-11-10
* 撰寫 `3TE7` 容量對應 `FW bin` 檔程式 (`1125`), 已完成, 並將結果寄給 `PM-Jack` double check.
* 修改 `mkmp` tool 使用手冊( For `客戶` ).
* 測試 `PM-Jack` `mkmp` tool( `20210114_WWN` ), 已測試完畢, 並將 tool 寄出.
* 測試 `ICC` `mSATA 3SE` `NCQ` 測項狀況( `Write code` 更新 `FW` -> `SYS_S_S130710K` ).
  * 需挑選較舊的 `開卡板`, 並非所有 `開卡板` 都可使用.
  * `ctrl + F12` 可修改開卡包相關參數.
* 整理 `mkmp` 走正常 `DLMC` 流程, 並寄出與 `大A` 討論.
  * 需準備 `Device`.
  * 需準備 `size.txt`.
* 撰寫 `size.txt` 檔案.
* 參與 `B&R` 討論.
* TODO
  * [x] 追蹤 `ICC` `mSATA 3SE` `NCQ` 測項狀況.
  * [x] 提供相關資料給 `大A` 開發 `mkmp` tool, 並討論細節.
  * [x] 測試 `3TE7` `DEM24-A28DK1CADL` 用 `S22A03` 觀看測速狀況, 並將平台寄回.
  * [x] 整理 `3TE7` 對應 `SN`, 因發現有重複 `SN`, 已發現並重新寄出.
  * [x] 測試 `3TE6` 安裝 `RHEL8`, 觀看是否與客戶發生相同問題.
  * [x] 協助 `Kiwi` 處理 `Citrix` `DLMC` 問題.
  * [x] 參與 `EU-FAE` 週會.

# 2022-11-11
* 追蹤 `ICC` `mSATA 3SE` `NCQ` 測項狀況, 更換為 `S141119_141006 Initial PLL issue`, 測項一樣有問題.
* 提供相關資料給 `大A` 開發 `mkmp` tool, 並討論細節.
* 測試 `3TE7` `DEM24-A28DK1CADL` 用 `S22A03` 觀看測速狀況, 並將平台寄回.
* 整理 `3TE7` 對應 `SN`, 因發現有重複 `SN`, 已發現並重新寄出.
* 測試 `3TE6` 安裝 `RHEL8`, 觀看是否與客戶發生相同問題, 經測試可正常運行.
* 協助 `Kiwi` 處理 `Citrix` `DLMC` 問題.
* 參與 `EU-FAE` 週會.
* TODO
  * [x] 測試 `3TE6` 安裝 `RHEL 7.6`, 觀看是否與客戶發生相同問題.
  * [x] 測試 `ICC` `mSATA 3SE` `NCQ` 測項, 透過開卡包將 `NCQ` 功能關閉.
  * [x] 參加部門聚餐.
  * [x] 了解 `Leo` `power on/off` cycling 工具操作.
  * [x] 觀看 `Jack` 協助檢查之 `3TE7` 對應 `SN` 表單.
  * [x] 協助回覆 `台達-Lan` 相關操作問題.

# 2022-11-14
* 測試 `3TE6` 安裝 `RHEL 7.6`, 觀看是否與客戶發生相同問題.
  * 測試 `FW` -> `V21118`, `V211180A_20220715`, `V211180A_20220914`, 皆發生安裝卡住問題.
  * 嘗試透過修改安裝包設定, 依然有相同問題.
  * 測試 `3MG3-P` 無此問題.
  * 測試 `Samsung 860`, 無此問題.
* 測試 `ICC` `mSATA 3SE` `NCQ` 測項, 透過開卡包將 `NCQ` 功能關閉, 等待 `Chihwei Kuo` 測試結果.
* 參加部門聚餐.
* 了解 `Leo` `power on/off` cycling 工具操作.
* 觀看 `Jack` 協助檢查之 `3TE7` 對應 `SN` 表單.
* 協助回覆 `台達-Lan` 相關操作問題. 
* TODO
  * [x] 追蹤 `ICC` `mSATA 3SE` `NCQ` 測項狀況.
  * [x] 驗證 `Siemens` USB 更換 `controller` 後, 是否可正常運作.
  * [x] 驗證 `3TE7` `MKMP` tool( `DLMC` ).
  * [x] 提供 `SATADOM` 更新 `FW` bin 檔於 `Cas-well` 窗口.

# 2022-11-15
* 追蹤 `ICC` `mSATA 3SE` `NCQ` 測項狀況.
* 驗證 `Siemens` USB 更換 `controller` 後, 是否可正常運作.
* 驗證 `3TE7` `MKMP` tool( `DLMC` ).
  * `64GB`, `128GB`, `512GB`, `1024GB` 皆已驗證完成.
  *  發現 `256GB` `4CH 1CE`, `2CH 2CE` `Flash id` 皆相同無法做分辨.
* 提供 `SATADOM` 更新 `FW` bin 檔於 `Cas-well` 窗口.
* TODO
  * [x] 與 `大A` 討論 `3TE7` `MKMP` tool 關於 `256GB` `4CH 1CE`, `2CH 2CE` 更新判斷.
  * [x] 參與 `FAE` 週會.
  * [x] 轉交台達外殼於業務助理 `Fannie`.
  * [x] 協助 `Kiwi` 將 `mSATA 3TG6-P` 重新開卡並紀錄 `SMART`.
  * [x] 撰寫 `3TG6-P` 開卡流程.

# 2022-11-16
* 與 `大A` 討論 `3TE7` `MKMP` tool 關於 `256GB` `4CH 1CE`, `2CH 2CE` 更新判斷, 改用選項的方式讓客戶選擇.
* 參與 `FAE` 週會.
* 轉交台達外殼於業務助理 `Fannie`.
* 協助 `Kiwi` 將 `mSATA 3TG6-P` 重新開卡並紀錄 `SMART`.
* 撰寫 `3TG6-P` 開卡流程.
* TODO
  * [ ] 驗證 `3TE7` `MKMP` tool( `DLMC` ).
  * [x] 協助 `Kiwi` 觀看 `智邦` `3ME4` `BurninTest`, 並修改測試次數為 `255`.
  * [x] 協助 `台達` 錄製 `UART` log, 並回報異常 log 於 `FW-RD`.
  * [x] 協助 `Kiwi` 處理 `Caswell` `SATADOM` `FW` 更新問題.
  * [x] 協助 `Kiwi` 處理 `3ME4` 重新開卡.
  * [x] 處理 `Siemens` USB 更換 `controller`, 需保留異常品, 送回 `SMI` 原廠分析, 並領出相同 `controller`.
  * [x] 訊問 `3TG6-P` 遇到 `iOPAL` Locked 相關問題釐清.
  * [x] 詢問 `Josh` 如何架設 `iOPAL`.
 
# 2022-11-17
* 協助 `Kiwi` 觀看 `智邦` `3ME4` `BurninTest`, 並修改測試次數為 `255`.
* 協助 `台達` 錄製 `UART` log, 並回報異常 log 於 `FW-RD`, 目前只看出 `device` 在做 `idle GC`, 需要錄製完整 log 才可分析.
* 協助 `Kiwi` 處理 `Caswell` `SATADOM` `FW` 更新問題, 已將外顯重包, 以及驗證後, 已將 `FW` bin 檔轉交給客戶.
* 協助 `Kiwi` 處理 `3ME4` 重新開卡.
* 處理 `Siemens` USB 更換 `controller`, 需保留異常品, 送回 `SMI` 原廠分析, 並領出相同 `controller`.
* 訊問 `3TG6-P` 遇到 `iOPAL` Locked 相關問題釐清.
* 詢問 `Josh` 如何架設 `iOPAL`, 需先透過開卡包點選 `2.FORCE_ERASE_SEARCH_MODE`, 開卡完成後, 再透過開卡包點選 `8.SETUP_TCG_OPAL_PSID_MODE`, 執行開啟 `TCG` 功能, 重啟後, 可從開卡包觀看到 `Support TCG Opal:1`, 表示 `TCG` 功能已開啟.
* TODO
  * [x] 驗證 `3TE7` `MKMP` tool( `DLMC` ).
  * [x] 協助 `台達` 人員觀看 `reboot` issue 問題.
  * [x] 協助 `Kiwi` 處理 `SATADOM 3TG6-P`, `3TE7` 轉交給業務.
  * [x] 協助詢問 `ICC` `mSATA 3SE` `NCQ` 客戶提出相關問題.
  * [x] 與 `PM-Becky` 了解 `PCIe 3TG6-P` 相關 `TCG` 開案問題.
  * [x] 協助 `Kiwi` 觀看 `智邦` `3ME4` `BurninTest` 是否有持續執行.
  * [ ] 了解如何操作 `iOPAL`.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 架設 `台達` `powercycle` 測試環境.

# 2022-11-18
* 驗證 `3TE7` `MKMP` tool( `DLMC` ), 已將 `256GB` 驗證完成, 並開需求單.
* 協助 `台達` 人員觀看 `reboot` issue 問題, 後續發現接地腳位焊接有誤, 重新焊接後, 可正常錄製 `UART` log.
* 協助 `Kiwi` 處理 `SATADOM 3TG6-P`, `3TE7` 轉交給業務.
* 協助詢問 `ICC` `mSATA 3SE` `NCQ` 客戶提出相關問題.
* 與 `PM-Becky` 了解 `PCIe 3TG6-P` 相關 `TCG` 開案問題, 並借取相關 sample.
* 協助 `Kiwi` 觀看 `智邦` `3ME4` `BurninTest` 是否有持續執行, 目前正常運作中.
* 參與 `EU-FAE` 週會.
* 架設 `台達` `powercycle` 測試環境, 後續發現 `UART` 線鬆脫, 導致 `11/18 03:15` 時, 程式停擺.
* TODO
  * [x] 處理 `3TG6-P` 遇到 `iOPAL` Locked 相關問題釐清.
  * [x] 了解如何操作 `iOPAL`.
  * [x] 撰寫 `3TE7` `MKMP` tool ( `1.4.2` ) 操作手冊.
  * [x] 協助 `Kiwi` 調整 `智邦` `3TE7` 眼圖設定.

# 2022-11-21
* 處理 `3TG6-P` 遇到 `iOPAL` Locked 相關問題釐清.
  * 客戶是用平台資訊
    * `UEFI` mode.
    * `Linux system (built with buildroot). OS is Debian Bullseye`.
* 了解如何操作 `iOPAL`, 操作加密功能.
* 撰寫 `3TE7` `MKMP` tool ( `1.4.2` ) 操作手冊, 目前已寫出一版.
* 協助 `Kiwi` 調整 `智邦` `3TE7` 眼圖設定.
* 測試台達 `powercycle`, 異常斷電測試, 進入 `OS` 等待 `20s` 後, 斷電 `15s`, 再上電.
* TODO
  * [x] 與 `Miller` 討論 `3TE7` `MKMP` tool ( `1.4.2` ) 操作手冊內容.
  * [x] 協助 `Kiwi` 調整 `智邦` `3TE7` 眼圖設定.
  * [x] 協助新人了解工作環境.
  * [x] 統整 `台達` `powercycle`, 異常斷電測試, 進入 `OS` 等待 `20s` 後, 斷電 `15s`, 再上電測試結果.

# 2022-11-22
* 與 `Miller` 討論 `3TE7` `MKMP` tool ( `1.4.2` ) 操作手冊內容.
* 協助 `Kiwi` 調整 `智邦` `3TE7` 眼圖設定.
* 協助新人了解工作環境.
* 統整 `台達` `powercycle`, 異常斷電測試, 進入 `OS` 等待 `20s` 後, 斷電 `15s`, 再上電測試結果, 與客戶回報後, 客戶建議將上電進入 `OS` 時間拉長到 `120s`, 再進行量測.
* TODO
  * [x] 統整 `台達` `powercycle`, 異常斷電測試, 進入 `OS` 等待 `130s` 後, 斷電 `15s`, 再上電測試結果.
  * [x] 協助 `Kiwi` 調整 `智邦` `3TE7` 眼圖設定.
  * [x] 參與 `FAE` 週會.
  * [x] 調整 `3TE7` `MKMP` tool ( `1.4.2` ) 操作手冊內容, 並發信給大家.

# 2022-11-23
* 統整 `台達` `powercycle`, 異常斷電測試, 進入 `OS` 等待 `130s` 後, 斷電 `15s`, 再上電測試結果.
* 協助 `Kiwi` 調整 `智邦` `3TE7` 眼圖設定.
* 參與 `FAE` 週會.
* 調整 `3TE7` `MKMP` tool ( `1.4.2` ) 操作手冊內容, 並發信給大家.
* TODO
  * [x] 測試 `iOPAL` 功能於 `AIOT` 主機板.
  * [x] 統整 `智邦` `3TE7` 眼圖測試結果.
  * [x] 了解 `iOPAL` `PBA` 功能如何架設.
  * [x] 協助新人觀看 `3ME3` 客訴案.
  * [x] 協助新人架設平台以及安裝作業系統.
  * [x] 回報 `台達` 客訴案進度於相關人員.
  * [x] 回報 `iOPAL` 測試結果於 `EU` 相關人員.

# 2022-11-24
* 測試 `iOPAL` 功能於 `AIOT` 主機板, 遇到與客戶相同狀況, 輸入完密碼解鎖後, 無法進入系統, 無限重複解鎖畫面.
  * 測試 `Debian` -> Fail.
  * 測試 `Windows 10` -> Fail.
* 統整 `智邦` `3TE7` 眼圖測試結果.
* 了解 `iOPAL` `PBA` 功能如何架設, 需透過 `SED utility` 下載 `UEFI64--1.15-5ad84d8`.
* 協助新人觀看 `3ME3` 客訴案.
* 協助新人架設平台以及安裝作業系統.
* 回報 `台達` 客訴案進度於相關人員.
* 回報 `iOPAL` 測試結果於 `EU` 相關人員.
* TODO
  * [x] 觀看 `innoWorks` 3pcs `3ME3` 客訴問題.
  * [x] 撰寫 `績效考核` 評量表.
  * [x] 架設測試平台.
  * [x] 協助 `Kiwi` 調整 `智邦` `3TE7` 眼圖設定.
  * [x] 歸還 `Ericsson` pcs USB 於 `Jessica`.

# 2022-11-25
* 觀看 `innoWorks` 3pcs `3ME3` 客訴問題, 發現為 `Avg erase count` 超過 `3000`, 詢問業務後, 可直接出分析報告.
* 撰寫 `績效考核` 評量表.
* 架設測試平台.
* 協助 `Kiwi` 調整 `智邦` `3TE7` 眼圖設定.
* 歸還 `Ericsson` pcs USB 於 `Jessica`.
* TODO
  * [x] 協助 `PM-Becky` 量測 `CFexpress` 於高溫效能執行狀況, `40GB`, `120GB`, `240GB`, `512 GB`, `1T`.
    * [x] `BurninTest` 1 hr.
    * [x] `AIDA 64` `Linear Read`.
    * [x] `AIDA 64` `Linear Write`.
  * [x] 接收 `FR005` `50` pcs 產品.
  * [x] 教學新人 `BPM` `SOP` `庫存查詢` 系統, 以及如何借出產品.
  * [x] 教學新人 `CFexpress` 相關量測過程.
  * [x] 協助 `PM-Davis` 測試 `3TE6` `Benchmark`.
    * [x] `V21118`.
    * [x] `V22B17` (iSLC).

# 2022-11-28
* 協助 `PM-Becky` 量測 `CFexpress` 於高溫效能執行狀況, `40GB`, `120GB`, `240GB`, `512 GB`, `1T`.
  * `BurninTest` 1 hr.
  * `AIDA 64` `Linear Read`.
  * `AIDA 64` `Linear Write`.
  * 
    |             `Device`              | `iSMART` | `Thermometer` | `Chamber` |  `Flash 1`  |  `Flash 2`  |
    |  -------------------------------  | -------  |  -----------  | --------  | ----------  | ----------  |
    | `swissbit - 40GB` (`idle 10min`)  |  `81℃`  |    `88.6℃`   |   `85℃`   |
    | `swissbit - 40GB` (`test 60min`)  |  `114℃` |    `92.8℃`   |   `85℃`   |
    | `swissbit - 120GB` (`idle 10min`) |  `82℃`  |    `87.4℃`   |   `85℃`   |
    | `swissbit - 120GB` (`test 60min`) |  `117℃` |    `94℃`     |   `85℃`   |
    | `swissbit - 240GB` (`idle 10min`) |  `82℃`  |    `87.7℃`   |   `85℃`   |
    | `swissbit - 240GB` (`test 60min`) | `119.9℃`|    `96.4℃`   |   `85℃`   |
    | `AV PRO - 512GB`   (`idle 10min`) |  `74℃`  |    `89.6℃`   |   `85℃`   |
    | `AV PRO - 512GB`  (`test 60min`)  |  `78℃`  |    `90.6℃`   |   `85℃`   |
    | `Innodisk - 1T`    (`idle 10min`) |  `95℃`  |    `97.6℃`   |   `85℃`   |   `92.1℃`  |   `90.9℃`  |
    | `Innodisk - 1T`   (`test 60min`)  |  `108℃` |    `109.7℃`  |   `85℃`   |   `100.3℃` |    `98℃`   |
* 接收 `FR005` `50` pcs 產品.
* 教學新人 `BPM` `SOP` `庫存查詢` 系統, 以及如何借出產品.
* 教學新人 `CFexpress` 相關量測過程.
* 協助 `PM-Davis` 測試 `3TE6` `Benchmark`, 並將結果寄出.
  * `V21118`.
  * `V22B17` (iSLC).
* TODO
  * [x] 協助 `PM-Becky` 量測 `CFexpress` 於高溫效能執行狀況, `40GB`, `120GB`, `240GB`, `512 GB`, `1T`.
    * [x] `AIDA 64` `Linear Read`.
    * [x] `AIDA 64` `Linear Write`.
  * [x] 協助 `PM-Becky` 量測 `CFexpress` 各系列產品透過 `Asmedia`, `Sandisk` 讀卡機辨識狀況, 以及讀寫功能.
  * [x] 測試  `50` pcs `mSATA 3TE7` 的 ATA command.
  * [x] 協助 `EU-FAE` 查詢 `device` 容量對應 `bin` file. 

# 2022-11-29
* 協助 `PM-Becky` 量測 `CFexpress` 於高溫效能執行狀況, `40GB`, `120GB`, `240GB`, `512 GB`, `1T`.
  * `AIDA 64` `Linear Read`.
  * `AIDA 64` `Linear Write`.
  * 
    |      `Device`      |   `Read`  |  `Write`  | `Chamber` |     `Flash 1`    |      `Flash 2`      |
    |  ----------------  | --------  |  -------  | --------  | ---------------  | ------------------  |
    | `swissbit - 40GB`  | `114.7℃` | `109.6℃` |   `85℃`   |
    | `swissbit - 120GB` | `99.2℃`  | `99.7℃`  |   `85℃`   |
    | `swissbit - 240GB` | `100.5℃` | `101.8℃` |   `85℃`   |
    | `AV PRO - 512GB`   | `89.4℃`  | `90.6℃`  |   `85℃`   |
    | `Innodisk - 1T`    | `104℃`   | `107.2℃` |   `85℃`   | `95.9℃ / 98.2℃` | `94.1℃ / 96.1℃`  |
* 協助 `PM-Becky` 量測 `CFexpress` 各系列產品透過 `Asmedia`, `Sandisk` 讀卡機辨識狀況, 以及讀寫功能.
  * `Innodisk-1602` `ubuntu 22.04` -> 可讀可寫, 寫入需要透過 command.
  * `Innodisk-1602` `windows 10` -> 不可讀, 不可寫, 可辨識.
  * `Innodisk-1602` 透過轉板 -> 可讀可寫.
  * `swissbit`, `AV PRO` -> 皆可讀可寫
* 測試  `50` pcs `mSATA 3TE7` 的 ATA command, 透過客戶平台無法辨識到 `device`, 透過 log 發現疑似 bios 無下達解鎖 command, 已將狀況回報給 `PM-Jack`.
* 協助 `EU-FAE` 查詢 `device` 容量對應 `bin` file. 
* TODO
  * [x] 撰寫 `innoWorks` 3pcs `3ME3` 客訴報告.
  * [x] 追蹤 `50` pcs `mSATA 3TE7` 的 ATA command 狀況.
  * [x] 參與 `FAE` 週會.
  * [x] 修改 `3TE7` mkmp tool 於 image 可自動執行程式.

# 2022-11-30
* 撰寫 `innoWorks` 3pcs `3ME3` 客訴報告.
* 追蹤 `50` pcs `mSATA 3TE7` 的 ATA command 狀況.
* 參與 `FAE` 週會.
* 修改 `3TE7` mkmp tool 於 image 可自動執行程式.
* TODO
  * [x] 協助 `PM-Becky` 量測 `CFexpress` `innodisk` `128GB`, `256GB`, `512GB` & `AV PRO` `512GB` 破殼 溫度.
    * [x] `AIDA 64` `Linear Read`.
    * [x] `AIDA 64` `Linear Write`.
    * [x] `BurninTest`.
  * [x] 參與 `FAE` 月會.
  * [x] 與 `PM-Jack` 參與 `50` pcs `mSATA 3TE7` 的 ATA command 會議討論. 
  * [x] 協助 `EU-FAE` 將 `Siemens` USB controller 送原廠分析.
  * [x] 協助 `EU PM-Alfie` 回覆 `iOPAL` 狀況.

# 2022-12-01
* 協助 `PM-Becky` 量測 `CFexpress` `innodisk` `128GB`, `256GB`, `512GB` & `AV PRO` `512GB` 破殼 溫度.
  * `AIDA 64` `Linear Read`.
  * `AIDA 64` `Linear Write`.
  * `BurninTest`.
* 參與 `FAE` 月會.
* 與 `PM-Jack` 參與 `50` pcs `mSATA 3TE7` 的 ATA command 會議討論, 後續發現需將 `mSATA 3TE7` 安裝於背面, 原先安裝位置為網卡位置. 
* 協助 `EU-FAE` 將 `Siemens` USB controller 送原廠分析.
* 協助 `EU PM-Alfie` 回覆 `iOPAL` 狀況.
* TODO
  * [x] 修改 `3TE7` mkmp tool 於 image 可自動執行程式.
  * [x] 協助 `業務-Jolie` 回答 `CF card` 相關問題.
  * [x] 修改 `innoWorks` 3pcs `3ME3` 客訴報告.

# 2022-12-02
* 修改 `3TE7` mkmp tool 於 image 可自動執行程式, 已做相關的修改, 並將 `image` 提供給 `EU`.
* 協助 `業務-Jolie` 回答 `CF card` 相關問題.
* 修改 `innoWorks` 3pcs `3ME3` 客訴報告, 已寄出報告於 `Sales-Millessa`.
* 協助新人了解 `OOB`, `PHY 設定`, `BurninTest`, `open block issue` 相關操作以及原理.
* 與 `EU-PM Alife` 討論 `iOPAL` 後續相關測試.
* TODO
  * [x] 設定 `50` pcs `mSATA 3TE7` 的 ATA command.
  * [x] 協助 `EU-PM Alife` 透過 `SMI` controller 設定 `TCG OPAL` 功能.
  * [x] 整理 `mkmp tool` autorun 相關步驟.
  * [x] 參與 `PSM` 會議.
  * [x] 協助新人觀看兩週驗收報告.
  * [x] 追蹤 `SMI` controller 回原廠分析進度.

# 2022-12-05
* 設定 `50` pcs `mSATA 3TE7` 的 ATA command.
* 協助 `EU-PM Alife` 透過 `SMI` controller 設定 `TCG OPAL` 功能.
* 整理 `mkmp tool` autorun 相關步驟.
* 參與 `PSM` 會議.
* 協助新人觀看兩週驗收報告.
* 追蹤 `SMI` controller 回原廠分析進度.
* TODO
  * [x] 轉交 `台達` 4pcs 於 `業務-MJ`.
  * [x] 追蹤 `SMI` controller 回原廠分析進度.
  * [x] 協助新人觀看兩週驗收報告.
  * [x] 重新包裝 `mkmp tool` autorun image.
  * [x] 協助 `EU-FAE` 測試 `windows embedded` `DLMC` bus-type error 狀況.

# 2022-12-06
* 轉交 `台達` 4pcs 於 `業務-MJ`.
* 追蹤 `SMI` controller 回原廠分析進度.
* 協助新人觀看兩週驗收報告.
* 重新包裝 `mkmp tool` autorun image, 將版本降至 `ubuntu 20.04`, 測試兩隻 device 都沒有問題, 並將檔案上傳.
* 協助 `EU-FAE` 測試 `windows embedded` `DLMC` bus-type error 狀況.
* 協助新人回答 `Direct to TLC` 相關問題.
* TODO
  * [x] 協助 `EU-FAE` 測試 `windows embedded` `DLMC` bus-type error 狀況.
  * [x] 協助新人架設 `ubuntu` 作業系統.
  * [x] 觀看 `FTB221102001 - CFast 3ME4`, `FTB221116001 - CFast 3TE7`, `FTB220913001 - 3MG2-P (2 NPF , bit flip)`.
  * [x] 回覆 `EU-Sales` `iOPAL` 進度回報.

# 2022-12-07
* 協助 `EU-FAE` 測試 `windows embedded` `DLMC` bus-type error 狀況, 無看到異常.
* 協助新人架設 `ubuntu 22.04` 作業系統.
* 觀看 `FTB221102001 - CFast 3ME4`, `FTB221116001 - CFast 3TE7`, `FTB220913001 - 3MG2-P (2 NPF , bit flip)`.
  * `FTB221102001 - CFast 3ME4` -> 接觸不良.
  * `FTB221116001 - CFast 3TE7` -> Flash 異常.
  * `FTB220913001 - 3MG2-P (2 NPF , bit flip)` -> 針對 `bit flip` 問題回應.
* 回覆 `EU-Sales` `iOPAL` 進度回報.
* 協助 `EU-Sales` 將 `mkmp tool` autorun image 上傳至 `Google drive`.
* 處理 `Gigabyte` 主機板無法開機問題, 後續發現為 `CPU` 腳位有問題.
* TODO
  * [x] 撰寫 `台達` `FTB221116001 - CFast 3TE7` 客訴報告.
  * [x] 協助 `Kiwi` 量測 `3ME4` Flash 問題.
  * [x] 參與 `iOPAL` 客訴討論會議.
  * [x] 盤點財產以及歸還財產.
  * [x] 協助 `Sales-Jolie` 回覆 `read retry` 相關問題.

# 2022-12-08
* 撰寫 `台達` `FTB221116001 - CFast 3TE7` 客訴報告.
* 協助 `Kiwi` 量測 `3ME4` Flash 問題, 後續將 Flash 取下後, 發現為焊接點脫落.
* 參與 `iOPAL` 客訴討論會議.
* 盤點財產以及歸還財產.
* 協助 `Sales-Jolie` 回覆 `read retry` 相關問題.
* TODO
  * [x] 架設 `iOPAL` 環境.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `Sales-MJ` 寄出 `FA report` & 相關客戶問題回答.
  * [x] 協助 `iOPAL` team 錄製 PCIe analyzer.
  * [x] 協助 `Sales-Jolie` 回覆 `bit flip` 問題.
  * [x] 協助回覆 `mkmp` tool 使用相關注意事項.

# 2022-12-09
* 架設 `iOPAL` 環境.
* 參與 `EU-FAE` 週會.
* 協助 `Sales-MJ` 寄出 `FA report` & 相關客戶問題回答.
* 協助 `iOPAL` team 錄製 PCIe analyzer.
* 協助 `Sales-Jolie` 回覆 `bit flip` 問題.
* 協助回覆 `mkmp` tool 使用相關注意事項.
* TODO
  * [x] 回覆 `EU-FAE` `Siemens` 客訴品 `controller` 送回原廠分析, 預計兩週後提供分析結果.
  * [x] 協助 `Kiwi` 觀看 `3pcs` `SD Card` 客訴狀況.
  * [x] 協助新人操作 `焊接`, `熱風槍` 相關使用.
  * [x] 盤點外借設備.
  * [x] 處理 `台達` 客訴品送驗 `Flash` 相關文件.
  * [x] 協助組內處理冷氣更換, 設備外觀包裝事宜.
  * [x] 整理相關客訴案報告, 並分類.
  * [x] 準備其他 `OS` 平台 USB 安裝碟. 

# 2022-12-12
* 回覆 `EU-FAE` `Siemens` 客訴品 `controller` 送回原廠分析, 預計兩週後提供分析結果.
* 協助 `Kiwi` 觀看 `3pcs` `SD Card` 客訴狀況, NPF.
* 協助新人操作 `焊接`, `熱風槍` 相關使用.
* 盤點外借設備.
* 處理 `台達` 客訴品送驗 `Flash` 相關文件.
* 協助組內處理冷氣更換, 設備外觀包裝事宜.
* 整理相關客訴案報告, 並分類.
* 準備其他 `OS` 平台 USB 安裝碟. 
* TODO
  * [x] 處理 `台達` 客訴品送驗 `Flash` 相關文件.
  * [x] 協助 `PM-Davis` 將 `3TE6` `256GB` -> `64GB`(`iSLC`).
  * [x] 協助 `Kiwi` 測試 `3pcs` `SD Card` 放入 `3G` 檔案, 並刪除, 測試功能是否正常, 以及透過 `iTracker` 將 `SMART` 資訊截圖下來.
  * [x] 撰寫年度績效考核-自評部份.
  * [x] 協助 `EU-FAE` 提供 `mkmp-tool` 使用手冊原檔.
  * [x] 協助 `Kiwi` 測試 `3TG6-P` `512GB` FIO Seq R/W 速度.
  * [x] 參與 `SD card type setting` 傳輸 `5MB` 以上資料掉碟.

# 2022-12-13
* 處理 `台達` 客訴品送驗 `Flash` 相關文件.
* 協助 `PM-Davis` 將 `3TE6` `256GB` -> `64GB`(`iSLC`).
* 協助 `Kiwi` 測試 `3pcs` `SD Card` 放入 `3G` 檔案, 並
* 撰寫年度績效考核-自評部份.
* 協助 `EU-FAE` 提供 `mkmp-tool` 使用手冊原檔.
* 協助 `Kiwi` 測試 `3TG6-P` `512GB` FIO Seq R/W 速度.
* 參與 `SD card type setting` 傳輸 `5MB` 以上資料掉碟.
* TODO
  * [x] 修改 `FA221122003` FA report.
  * [x] 協助 `Alex` 提供 `MKMP tool`.
  * [x] 參與 `FAE 週會`.
  * [x] 協助 `Sales-Amy` & `Sales MJ` close 客訴案.
  * [x] 協助測試 `iOPAL` 功能驗證.

# 2022-12-14
* 修改 `FA221122003` FA repo
* 協助 `Alex` 提供 `MKMP too
* 參與 `FAE 週會`.
* 協助 `Sales-Amy` & `Sales 
* 協助測試 `iOPAL` 功能驗證, 後續發現為 `PBA` image Version `1.15.2` 有異常, 透過 `SED Utility` 內部 `OS` 發現 image 需使用 `1.20.0`, 就可正常使用
  * 已將資訊提供給 `EU-FAE`.
  * 協助 `EU-FAE` 錄製影片以及提供相關 `image`.
* TODO
  * [x] 協助新人回答驗收報告答案.
  * [x] 協助 `Sales-MJ` 將 `台達` 異常品 `Flash` 送回原廠分析, 並提供相關資訊.
  * [x] 協助 `Sales-Millessa` 將 `InnoWorks` `mSATA 3TE7` 3pcs 轉送 `RMA`, 並將其餘客訴品歸還.
  * [x] 協助新人準備 `示波器` demo 產品與環境( `Crystal` & `power sequence` ).
  * [x] 協助 `Kiwi` 量測 `3TE6` `KIOXIA` Flash `FIO` 測速問題.

# 2022-12-15
* 協助新人回答驗收報告答案.
* 協助 `Sales-MJ` 將 `台達` 異常品 `Flash` 送回原廠分析.
* 協助 `Sales-Millessa` 將 `InnoWorks` `mSATA 3TE7` 3pcs 轉送 `RMA`, 並將其餘客訴品歸還.
* 協助新人準備 `示波器` demo 產品與環境( `Crystal` & `power sequence` )
* 協助 `Kiwi` 量測 `3TE6` `KIOXIA` Flash `FIO` 測速問題.
* TODO
  * [x] 回報 `EU-FAE` `Siemens` 客訴品 `controller` 送回原廠分析結果.
  * [x] 教導新人使用 `示波器`, 量測 `Crystal` & `power sequence`.
  * [x] 教導新人觀看 `電路圖`, 以及 `PTR` 測報.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `EU-FAE` 發問 `controller` 原廠分析相關問題.
  * [x] 送修 `3TE7` `32GB` 更換 `controller`.

# 2022-12-16
* 回報 `EU-FAE` `Siemens` 客訴品 `contr
* 教導新人使用 `示波器`, 量測 `Crystal`
* 教導新人觀看 `電路圖`, 以及 `PTR` 測
* 參與 `EU-FAE` 週會.
* 協助 `EU-FAE` 發問 `controller` 原廠
* 送修 `3TE7` `32GB` 更換 `controller`.
* TODO
  * [x] 協助 `EU-FAE` 錄製 `iOPAL` 設定相關流程影片.
  * [x] 協助新人處理 `power sequence` 量測.
  * [x] 協助 `Sales-Jesse` 修改 `智邦` `3TE7` 測速報告, 加入 `SMI` 原廠分析結果. 
  * [x] 協助 `Kiwi` 執行 `3TE6` DLMC.

# 2022-12-19
* 協助 `EU-FAE` 錄製 `iOPAL` 設定相關流程影片.
* 協助新人處理 `power sequence` 量測.
* 協助 `Sales-Jesse` 修改 `智邦` `3TE7` 測速報告, 加入 `SMI` 原廠分析結果. 
* 協助 `Kiwi` 執行 `3TE6` DLMC.
* TODO
  * [x] 協助 `Kiwi` 觀看 `超恩` 客訴案.
  * [x] 協助 `Kiwi` 執行 `3TE6` DLMC.
  * [x] 從 `RMA` 取回 `智邦` 客訴品 `3TE7`, 並於客戶平台測試 `SATA Link`.
  * [x] 撰寫 `DLMC` script 選項功能.

# 2022-12-20
* 協助 `Kiwi` 觀看 `超恩` 客訴案.
* 協助 `Kiwi` 執行 `3TE6` DLMC.
* 從 `RMA` 取回 `智邦` 客訴品 `3TE7`, 並於客戶平台測試 `SATA Link`.
* 撰寫 `DLMC` script 選項功能.
* 撰寫 `超恩` 客訴案 `FA` report. 
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 修改 `超恩` 客訴案 `FA` report.
  * [x] 協助新人撰寫相關技術問題回覆.
  * [x] 協助 `Kiwi` 測試 `4GT2-P` 於 `Supermicro` 卡住問題.
  * [x] 協助 `KIOXIA` Flash FAE 回答相關分析問題.

# 2022-12-21
* 參與 `FAE` 週會.
* 修改 `超恩` 客訴案 `FA` report.
* 協助新人撰寫相關技術問題回覆.
* 協助 `Kiwi` 測試 `4GT2-P` 於 `Supermicro` 卡住問題.
* 協助 `KIOXIA` Flash FAE 回答相關分析問題.
* TODO
  * [x] 參與 `FAE` 月會.
  * [x] 協助新人查詢產品相關對照問題, 以及修改後續報告內容.
  * [x] 參與新人驗收報告討論會議.
  * [x] 協助 `Kiwi` 觀看 `智邦` `3ME4` 客訴案. 
  * [x] 撰寫 `DLMC` tool 選擇 `script`.
  * [x] 持續追蹤 `Siemens` USB `controller` 分析狀況.

# 2022-12-22
* 參與 `FAE` 月會.
* 協助新人查詢產品相關對照問題, 以及修改後續報告內容.
* 參與新人驗收報告討論會議.
* 協助 `Kiwi` 觀看 `智邦` `3ME4` 客訴案. 
* 撰寫 `DLMC` tool 選擇 `script`.
* 持續追蹤 `Siemens` USB `controller` 分析狀況.
* TODO
  * [x] 增加 `DLMC` tool 選擇 `script` 功能.
  * [x] 協助新人觀看驗收報告.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `Kiwi` 測試 `智邦` `3ME4` `warm / cold boot`.
  * [x] 協助新人找尋 `modern approach` 文件.

# 2022-12-23
* 增加 `DLMC` tool 選擇 `script` 功能.
* 協助新人觀看驗收報告.
* 參與 `EU-FAE` 週會.
* 協助 `Kiwi` 測試 `智邦` `3ME4` `warm / cold boot`.
* 協助新人找尋 `modern approach` 文件.
* TODO
  * [x] 從維修部取回 `智邦` 客訴品, 並測試 `SATA Link`.
  * [x] 協助 `Sales-MJ` 回覆 `2.5吋` `PCIe` 相關問題.
  * [x] 協助 `Nick` 備份 `Update-tool` image.

# 2022-12-26
* 從維修部取回 `智邦` 客訴品, 並測試 `SATA Link`, 發現是原 `controller` 有問題.
* 協助 `Sales-MJ` 回覆 `2.5吋` `PCIe` 相關問題, 有 `U.2` 規格.
* 協助 `Nick` 備份 `Update-tool` image.
* TODO
  * [x] 查找 `ubuntu` image 備份壓縮方法.
  * [x] 協助 `PM-Davis` 測試 `3TE6` `ADIA 64`, `CDM`, `iSMART LBA` 相關資訊.
  * [x] 協助 `Kiwi` 查找 `FIO` 測試 `dummy` 方法, 並測試 `3TE6`.

# 2022-12-27
* 查找 `ubuntu` image 備份壓縮方法.
* 協助 `PM-Davis` 測試 `3TE6` `ADIA 64`, `CDM`, `iSMART LBA` 相關資訊.
* 協助 `Kiwi` 查找 `FIO` 測試 `dummy` 方法, 並測試 `3TE6`.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 參與 `RD` 月會.
  * [x] 協助 `Kiwi` 參與 `廣達` `FIO` script 討論會議.
  * [x] 協助 `PM-Davis` 提供 `3TE6` `ADIA 64`, `CDM`, `iSMART LBA` 相關資訊.
  * [x] 協助新人回答相關問題.
  * [x] 協助 `Kiwi` 測試 `3TE7` BiCS5 容量問題, 觀看是否可以開到 `55.9GB`.

# 2022-12-28
* 參與 `FAE` 週會.
* 參與 `RD` 月會.
* 協助 `Kiwi` 參與 `廣達` `FIO` script 討論會議.
* 協助 `PM-Davis` 提供 `3TE6` `ADIA 64`, `CDM`, `iSMART LBA` 相關資訊.
* 協助新人回答相關問題.
* 協助 `Kiwi` 測試 `3TE7` BiCS5 容量問題, 觀看是否可以開到 `55.9GB`, 需將 `Full Capacity` 勾選起來, 才可開到客戶指定容量.
* TODO
  * [x] 協助新人回答相關問題.
  * [x] 修改 `dlmc` tool.
  * [x] 測試 `ubuntu` image 備份及壓縮.

# 2022-12-29
* 協助新人回答相關問題.
* 修改 `dlmc` tool.
* 測試 `ubuntu` image 備份及壓縮.
* TODO
  * [x] 協助 `PM-Davis` 開卡( `20`pcs 3IE6 `128GB` -> `40GB` ).
  * [x] 協助 `PM-Davis` 開卡測速 `3IE6` `512GB` -> `160GB`.
  * [x] 參加 `FAE` 月會(`PCIE Gen4產品` `FA` 分享 ).

# 2022-12-30
* 協助 `PM-Davis` 開卡( `20`pcs 3IE6 ).
* 協助 `PM-Davis` 開卡測速 `3IE6` `512GB` -> `160GB`.
* 參加 `FAE` 月會(`PCIE Gen4產品` `FA` 分享 ).
* TODO
  * [x] 協助 `Sales-Jesse` 修改 `智邦` `FA` report.
  * [x] 協助 `Sales-Millessa` 開卡設定.
  * [x] 協助新人開卡.
  * [x] 教導新人操作 `DLMC` tool 使用.
