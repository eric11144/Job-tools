# 工作日誌 #

# 2023-01-03
* 協助 `Sales-Jesse` 修改 `智邦` `FA` report.
* 協助 `Sales-Millessa` 開卡設定.
* 協助新人開卡.
* 教導新人操作 `DLMC` tool 使用.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `EU` 觀看客訴案.
    * [x] `HighTech Nordic AB` `4`pcs `3TE7` `512GB`.
    * [x] 觀看 `iSMART`.
  * [x] 協助新人安裝 `Ubuntu` & 相關指令操作.

# 2023-01-04
* 參與 `FAE` 週會.
* 協助 `EU` 觀看客訴案.
  * `HighTech Nordic AB` `4`pcs `3TE7` `512GB`.
  * 觀看 `iSMART`.
* 協助新人安裝 `Ubuntu` & 相關指令操作.
* TODO
  * [x] 觀看 `HighTech Nordic AB` `4`pcs `3TE7` UART log.
    * [x] `2` pcs -> `SRR`.
    * [x] `1` pcs -> `Laa over1`.
    * [x] `1` pcs -> `Loader mode`.
  * [x] 協助 `PM-Davis` 將 `3TE6` 開卡, FW `V2281020`.
  * [x] 架設 `iCAP` 軟體.
  * [x] 觀看 `Siemens` USB `controller` 分析報告.

# 2023-01-05
* 觀看 `HighTech Nordic AB` `4`pcs `3TE7` UART log.
  * `2` pcs -> `SRR`.
  * `1` pcs -> `Laa over1`.
  * `1` pcs -> `Loader mode`.
* 協助 `PM-Davis` 將 `3TE6` 開卡, FW `V2281020`.
* 架設 `iCAP` 軟體.
* 觀看 `Siemens` USB `controller` 分析報告.
* TODO
  * [x] 協助 `RD-Allen` `HighTech Nordic AB` `4`pcs `3TE7` 做 `Write code`.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 教導新人架設 `iCAP` 軟體, 講解 `Docker` 相關指令操作, 以及 `中文輸入法`.
  * [x] 觀看 `SIMOS Elektronik / ATRON ELECTRONIC` 從維修部送回 `8`pcs.

# 2023-01-06
* 協助 `RD-Allen` `HighTech Nordic AB` `4`pcs `3TE7` 做 `Write code`.
* 參與 `EU-FAE` 週會.
* 教導新人架設 `iCAP` 軟體, 講解 `Docker` 相關指令操作, 以及 `中文輸入法`.
* 觀看 `SIMOS Elektronik / ATRON ELECTRONIC` 從維修部送回 `8`pcs.
  * `5` pcs -> NPF.
  * `1` pcs -> PPQ.
  * `1` pcs -> PHY lost.
  * `1` pcs -> controller issue.
  * `1` pcs -> power short.
* TODO
  * [x] 協助 `Jessica` 回覆 `Avantix` `3TG6-P` 相關問題.
  * [x] 借出產品.
  * [x] 整理客訴案 `月報`.
  * [x] 協助新人觀看 `week 7` 報告.
  * [x] 撰寫 `innoWorks` NPF FA report.

# 2023-01-07
* 協助 `Jessica` 回覆 `Avantix` `3TG6-P` 相關問題.
* 借出產品.
* 整理客訴案 `月報`.
* 協助新人觀看 `week 7` 報告.
* 撰寫 `innoWorks` NPF FA report.
* TODO
  * [x] 參與新人 `week 7` 驗收會議.
  * [x] 協助 `Sales-Jesse` 撰寫 `智邦` `3ME4` 驗收報告.
  * [x] 協助新人串接 `iCAP` `Server` & `Client`.
  * [x] 協助 `Nick` 包裝 `DLMC` image.

# 2023-01-09
* 參與新人 `week 7` 驗收會議.
* 協助 `Sales-Jesse` 撰寫 `智邦` `3ME4` 驗收報告.
* 協助新人串接 `iCAP` `Server` & `Client`.
* 協助 `Nick` 包裝 `DLMC` image.
* TODO
  * [x] 協助新人架設 `iCAP`.
  * [x] 協助新人架設以及操作 `innoOSR`.
  * [x] 教導新人操作以及架設 `Github`.
  * [x] 學習如何架設 `innoAgent`.
  * [x] 協助 `Sales-MJ` 回覆 `台達` 客訴案.
  * [x] 處理 `BIOS` 於關機時無法停止風扇問題.

# 2023-01-10
* 協助新人架設 `iCAP`.
* 協助新人架設以及操作 `innoOSR`.
* 教導新人操作以及架設 `Github`.
* 學習如何架設 `innoAgent`.
  * 需接上 `UART` 線.
  * 需要 `USB` 不斷供電才可操作.
  * 電源操作, 需要注意 `GPIO PIN`, `1` 為開關機, `2` 為重開機.
    * 開關機需接 `Power` 左邊 `GPIO`.
      * `GPIO 1` -> `High` (關機).
      * `GPIO 1` -> `Low` (開機).
    * 重新開關機需接 `Reset` 右邊 `GPIO`.
      * `GPIO 2` -> `High` (關機).
      * `GPIO 2` -> `Low` (開機).
* 協助 `Sales-MJ` 回覆 `台達` 客訴案.
* 處理 `BIOS` 於關機時無法停止風扇問題, 需將 `總電源` & `電池` 移除再重新上電即可.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `Miller` 查詢 `Kontron` 電容異常率.
  * [x] 協助新人串接 `iCAP` `innoAgent`  `innoOSR`.
  * [x] 與 `EU-FAE` 討論 `Siemens` controller 分析報告.

# 2023-01-11
* 參與 `FAE` 週會.
* 協助 `Miller` 查詢 `Kontron` 電容異常率.
* 協助新人串接 `iCAP` `innoAgent`  `innoOSR`.
* 與 `EU-FAE` 討論 `Siemens` controller 分析報告.
* TODO
  * [x] 協助教導新人執行 `DLMC` `hdparm` `nvme-cli`.
  * [x] 與 `EU-FAE Jason` 討論 `3SE3` `10` pcs 分析狀況.
  * [x] 協助 `EU-FAE YingXiang` 測試 `3TE7` `64GB` DLMC( `S20615` -> `S22921` ), 以及查詢內顯版號.
  * [x] 協助 `Kiwi` 回覆 `月蘭` 相關技術問題.
  * [x] 協助新人更換測試平台.

# 2023-01-12
* 協助教導新人執行 `DLMC` `hdparm` `nvme-cli`.
* 與 `EU-FAE Jason` 討論 `3SE3` `10` pcs 分析狀況.
* 協助 `EU-FAE YingXiang` 測試 `3TE7` `64GB` DLMC( `S20615` -> `S22921` ), 以及查詢內顯版號.
* TODO
  * [x] 協助 `Kiwi` 錄製 `CFast card` 讀卡機辨識.
  * [x] 協助新人操作 `DD`, `DLMC` auto run script.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 測試 `image` 壓縮工具.

# 2023-01-13
* 協助 `Kiwi` 錄製 `CFast card` 讀卡機辨識.
* 協助新人操作 `DD`, `DLMC` auto run script.
* 參與 `EU-FAE` 週會.
* 測試 `image` 壓縮工具.
* TODO
  * [x] 測試 `3SE3` `2` pcs 維修後狀況.
  * [x] 協助 `EU-FAE Jason` 回覆 `OPAL` 相關操作問題.
  * [x] 撰寫 `2023 年度績效`.
  * [x] 協助新人教學 `3TE6` NVMe update tool.
  * [x] 協助新人回答 `innoOSR` 相關操作問題.
  * [x] 協助 `Kiwi` 修改 `加士達` FA report( `中翻英` ).

# 2023-01-16
* 測試 `3SE3` `2` pcs 維修後狀況.
* 協助 `EU-FAE Jason` 回覆 `OPAL` 相關操作問題.
* 撰寫 `2023 年度績效`.
* 協助新人教學 `3TE6` NVMe update tool.
* 協助新人回答 `innoOSR` 相關操作問題.
* 協助 `Kiwi` 修改 `加士達` FA report( `中翻英` ).
* TODO
  * [x] 協助 `EU-FAE` 處理 `Kontron` 結案.
  * [x] 協助 `EU-FAE` 提供 `Kontron` 更新 bin file.
  * [x] 轉送  `Kontron` `500` pcs 至 `RMA`.
  * [x] 協助新人回答 `innoOSR` 相關操作問題.
  * [x] 協助新人觀看 `innoOSR` 報告.
  * [x] 協助新人操作 `dd`.
  * [x] 協助 `Sales-MJ` follow KIOXIA 原廠分析 `Flash` 相關問題.
  * [x] 追蹤 `SMI` controller 分析相關問題進度.
  * [x] 測試 `image` 壓縮工具.

# 2023-01-17
* 協助 `EU-FAE` 處理 `Kontron` 結案.
* 協助 `EU-FAE` 提供 `Kontron` 更新 bin file.
* 轉送  `Kontron` `500` pcs 至 `RMA`.
* 協助新人回答 `innoOSR` 相關操作問題.
* 協助新人觀看 `innoOSR` 報告.
* 協助新人操作 `dd`.
* 協助 `Sales-MJ` follow KIOXIA 原廠分析 `Flash` 相關問題.
* 追蹤 `SMI` controller 分析相關問題進度.
* 測試 `image` 壓縮工具.
* TODO
  * [x] 參加 `FAE` 週會.
  * [x] 協助 `Kiwi` 參加 `Pansonic` 討論會議.
  * [x] 測試 `image` 壓縮工具.
  * [x] 協助新人操作 & 架設 `innoOSR`.

# 2023-01-18
* 參加 `FAE` 週會.
* 協助 `Kiwi` 參加 `Pansonic` 討論會議.
* 測試 `image` 壓縮工具.
* 協助新人操作 & 架設 `innoOSR`.
* TODO
  * [x] 修改 `DLMC` 更新選項 `Script`( `option_choose_test.sh` ).
  * [x] 整理 `Email`.
  * [x] 觀看英文文法.
  * [x] 協助新人完成驗收 `demo`.
  * [x] 協助 `Nick` 製作 `DLMC` image.

# 2023-01-19
* 修改 `DLMC` 更新選項 `Script`( `option_choose_test.sh` ).
* 整理 `Email`.
* 觀看英文文法.
* 協助新人完成驗收 `demo`.
* 協助 `Nick` 製作 `DLMC` image.
* TODO
  * [x] 早上休假.
  * [x] 回覆 `智邦-YL` 相關技術問題.
  * [x] 協助新人觀看平台問題.
  * [x] 處理 `Kontron` `500` pcs 後續維修.

# 2023-01-30
* 早上休假.
* 回覆 `智邦-YL` 相關技術問題.
* 協助新人觀看平台問題.
* 處理 `Kontron` `500` pcs 後續維修, 需要 `EU-FAE` 協助詢問 `3` pcs 破壞分析, 以及 `1` pcs 不見的處理.
* TODO
  * [x] 協助 `EU-FAE` 查找 `DEMSM-04GD09SCADB-D62` 電路圖.
  * [x] 協助新人觀看 `PCIE` 於 `SMART` `Transfer mode` 顯示問題. 
  * [x] 整理 `10` pcs `3SE3` 維修狀況, 並回覆於 `EU-FAE`.
  * [x] 參與 `FAE-team2` 案件討論.
  * [x] 協助 kiwi 撰寫 `智邦` `mSATA 3ME4` 分析報告.
  * [x] 與 `EU-FAE` 討論 `Kontron` `500` pcs 後續處理, 以及 `Siemens` USB 客訴案.

# 2023-01-31
* 協助 `EU-FAE` 查找 `DEMSM-04GD09SCADB-D62` 電路圖.
* 協助新人觀看 `PCIE` 於 `SMART` `Transfer mode` 顯示問題. 
* 整理 `10` pcs `3SE3` 維修狀況, 並回覆於 `EU-FAE`.
* 參與 `FAE-team2` 案件討論.
* 協助 kiwi 撰寫 `智邦` `mSATA 3ME4` 分析報告.
* 與 `EU-FAE` 討論 `Kontron` `500` pcs 後續處理, 以及 `Siemens` USB 客訴案.
* TODO
  * [x] 測試 `FIO` 功能.
  * [x] 協助 `PM-Jack` 測試 `mSATA 3TE7` FW write code 更新( `S21606` <-> `S23130P` ).
  * [x] 協助 `EU-FAE` 找尋 `mSATA mini 3SE` 電路圖.
  * [x] 取回 `Kontron` `3` pcs 損壞 `device`, 並領取 `4` pcs.
  * [x] 撰寫 `innoWorks` `mSATA 3TE7` `blk 4` issue `FA` report.

# 2023-02-01
* 測試 `FIO` 功能, 並撰寫相關文件.
* 協助 `PM-Jack` 測試 `mSATA 3TE7` FW write code 更新( `S21606` <-> `S23130P` ).
* 協助 `EU-FAE` 找尋 `mSATA mini 3SE` 電路圖.
* 取回 `Kontron` `3` pcs 損壞 `device`, 並領取 `4` pcs.
* 撰寫 `innoWorks` `mSATA 3TE7` `blk 4` issue `FA` report.
* TODO
  * [x] 協助新人操作 `FIO`, 以及如何產生結果圖.
  * [x] 協助 `Kiwi` 回覆英文信件.
  * [x] 撰寫 `智邦` `mSATA 3TE7` UART log 接線圖.
  * [x] 與 `Miller` 討論 `innoWorks` `mSATA 3TE7` `blk 4` issue `FA` report.
  * [x] 協助新人操作&安裝 `FreeBSD`.

# 2023-02-02
* 協助新人操作 `FIO`, 以及如何產生結果圖.
* 協助 `Kiwi` 回覆英文信件.
* 撰寫 `智邦` `mSATA 3TE7` UART log 接線圖.
* 與 `Miller` 討論 `innoWorks` `mSATA 3TE7` `blk 4` issue `FA` report.
* 協助新人操作&安裝 `FreeBSD`.
* TODO
  * [x] 協助新人操作 `Maxcpu` 執行, 並錄製 log.
  * [x] 查詢如何透過程式繪製 log 曲線圖.
  * [x] 參與 `智邦` 討論會議.
  * [x] 協助 `Kiwi` 測試透過 `ELog` 撈取 `3ME4` 相關 event log.
  * [x] 協助 `Sales-Jolie` 修改 `3TE6` model name -> `WARIS PCIe 64GB WT`.
  * [x] 處理 `Kontron` `4` pcs `3TE7` to RMA.

# 2023-02-03
* 協助新人操作 `Maxcpu` 執行, 並錄製 log.
* 查詢如何透過程式繪製 log 曲線圖.
* 參與 `智邦` 討論會議.
* 協助 `Kiwi` 測試透過 `ELog` 撈取 `3ME4` 相關 event log, 發現 `ubuntu 22.04` 無法正常撈取 log, 但 windows `MV Tool` 可正常撈出.
* 協助 `Sales-Jolie` 修改 `3TE6` model name -> `WARIS PCIe 64GB WT`.
* 處理 `Kontron` `4` pcs `3TE7` to RMA.
* TODO
  * [x] 架設 `ubuntu 18.04` 測試透過 `ELog` 撈取 `3ME4` 相關 event log.
  * [x] 協助 `RMA` 找取相關遺失 `device` 之 `SN`.
  * [x] 協助新人觀看 `FreeBSD` 撈取相關 log 操作.
  * [x] 協助 `Nick` 提供 `table swap` 相關 FA report.
  * [x] 協助 `Sales-MJ` 回覆 `台達` 相關問題, 以及查找 `DQE` 測試報告.
  * [x] 協助 `PM-Jack` 測試 `mSATA 3TE7` `WWN` 相關 `FW`.
  * [x] 協助 `Kiwi` 回覆 `智邦` 相關 `iCell` 問題.

# 2023-02-04
* 架設 `ubuntu 18.04` 測試透過 `ELog` 撈取 `3ME4` 相關 event log, 後續發現還是無法正常撈取, 詢問 `Alex` 後, 需於 `CentOS` 執行 `ELog`, 才可正常撈取.
* 協助 `RMA` 找取相關遺失 `device` 之 `SN`, 並回報給 `RMA`.
* 協助新人觀看 `FreeBSD` 撈取相關 log 操作.
* 協助 `Nick` 提供 `table swap` 相關 FA report, 發現原問題為 `BiCS 3`, 並非 `BiCS 5`, 後續再發生, 需詢問 `FW-RD`.
* 協助 `Sales-MJ` 回覆 `台達` 相關問題, 以及查找 `DQE` 測試報告.
* 協助 `PM-Jack` 測試 `mSATA 3TE7` `WWN` 相關 `FW`, 後續發現 `mkmp tool` `SN.txt` 並無支援 `mode 0` 更新, 已請 `SW-Allen` 協助修改.
* 協助 `Kiwi` 回覆 `智邦` 相關 `iCell` 問題.
* TODO
  * [x] 觀看 `stress_test` 相關 `script`.
  * [x] 撰寫 `SN` 遺失尋找程式.
  * [x] 協助新人架設 `FreeBSD` 跑測速.
  * [x] 詢問 `FW-RD` 關於 `3TG6-P` `Juniper` FW 開卡問題.
  * [x] 處理平台無法安裝 `Windows 10` 問題.
  * [x] 與 `Kiwi` 前往 `DQE` 詢問 `Juniper` 量測 `Latency` 相關 `script` 問題.

# 2023-02-06
* 觀看 `stress_test` 相關 `script`.
* 撰寫 `SN` 遺失尋找程式.
* 協助新人架設 `FreeBSD` 跑測速.
* 詢問 `FW-RD` 關於 `3TG6-P` `Juniper` FW 開卡問題, 需要將容量改為 `400GB`, 才可順利開卡.
* 處理平台無法安裝 `Windows 10` 問題, 後續發現需將 `Bios` boot 設定改為 `UEFI`.
* 與 `Kiwi` 前往 `DQE` 詢問 `Juniper` 量測 `Latency` 相關 `script` 問題.
* TODO
  * [x] 測試 `Juniper` `Latency` 相關 `script`.
  * [x] 修正 `read_log_and_draw_plot` 程式( `曲線圖` 呈現問題).
  * [x] 教導新人觀看 `read_log_and_draw_plot` 程式.
  * [x] 與 `EU-FAE` 討論 `Siemens` `USB` 客訴案, 以及 `Ecrin` 搭配 `3TG6-P` & `RAID` 卡發生 `Performance` 下降問題.
  * [x] 協助 `EU-FAE` 將 `10` pcs `3SE3` CFast card 轉送 `RMA`.
  * [x] 協助 `Sales-MJ` 歸還 `DEM24-32GDK1EW1SF-G14`.
  * [x] 協助 `FW-RD` 補發 `mkmp tool` 相關 `FW bin`.

# 2023-02-07
* 測試 `Juniper` `Latency` 相關 `script`.
* 修正 `read_log_and_draw_plot` 程式( `曲線圖` 呈現問題), 後續發現為曲線圖資料輸入時為 `string`, 已將資料改為 `Float`.
* 教導新人觀看 `read_log_and_draw_plot` 程式.
* 與 `EU-FAE` 討論 `Siemens` `USB` 客訴案, 以及 `Ecrin` 搭配 `3TG6-P` & `RAID` 卡發生 `Performance` 下降問題.
* 協助 `EU-FAE` 將 `10` pcs `3SE3` CFast card 轉送 `RMA`.
* 協助 `Sales-MJ` 歸還 `DEM24-32GDK1EW1SF-G14`.
* 協助 `FW-RD` 補發 `mkmp tool` 相關 `FW bin`.
* TODO
  * [x] 協助新人操作 `SATA analyzer` 程式.
  * [x] 詢問 `DQE-Jim` 關於 `Latency` 測試相關操作.
  * [x] 講解 `iOPAL` 操作給新人.
  * [x] 協助 `EU-PM` 處理 `Siemens` `Later bad` case.
  * [x] 參與 `FAE` 週會.

# 2023-02-08
* 協助新人操作 `SATA analyzer` 程式.
* 詢問 `DQE-Jim` 關於 `Latency` 測試相關操作.
* 講解 `iOPAL` 操作給新人.
* 協助 `EU-PM` 處理 `Siemens` `Later bad` case, 詢問客戶是否可以遠端更新 `FW`, 並將外顯改為 `V22620A`.
* 參與 `FAE` 週會.
* TODO
  * [x] 協助 `Sales-Jesse` 修改 `智邦` FA report.
  * [x] 協助 `EU-FAE` 處理 `STELIAU TECHNOLOGY` `3TG6-P`.
  * [x] 詢問 `SMI` 是否可在不拆 `controller` 狀況下分析異常 `Device`.
  * [x] 詢問 `CH-FAE Lyle` 關於 `浪潮` `3TE6` `media error` 相關狀況.
  * [x] 協助新人處理 `Juniper` `Latency` 相關 `script` 問題.

# 2023-02-09
* 協助 `Sales-Jesse` 修改 `智邦` FA report, 新增 `E Log` 相關分析資訊.
* 協助 `EU-FAE` 處理 `STELIAU TECHNOLOGY` `3TG6-P`, 目前先.
* 詢問 `SMI` 是否可在不拆 `controller` 狀況下分析異常 `Device`.
* 詢問 `CH-FAE Lyle` 關於 `浪潮` `3TE6` `media error` 相關狀況.
* 協助新人處理 `Juniper` `Latency` 相關 `script` 問題.
* TODO
  * [x] 協助新人觀看 `Final` report.
  * [x] 協助 `FAE-Rex` 觀看 `AES` 功能如何開啟.
  * [x] 協助 `FAE-Leo` 提供 `Linux` 開機自動執行程式相關資訊.
  * [x] 協助 `EU-FAE` 測試 `DLMC` `3TE7`(`S20615_20220114` -> `S22801_20230208`).
  * [x] 參與 `EU-FAE` 週會.

# 2023-02-10
* 協助新人觀看 `Final` report.
* 協助 `FAE-Rex` 觀看 `AES` 功能如何開啟, 需要修改文字檔, 找到 `enAESKey`, 將 `0` 改為 `1`.
* 協助 `FAE-Leo` 提供 `Linux` 開機自動執行程式相關資訊.
* 協助 `EU-FAE` 測試 `DLMC` `3TE7`(`S20615_20220114` -> `S22801_20230208`).
* 參與 `EU-FAE` 週會.
* TODO
  * [x] 協助 `智邦` 撰寫 `Windows` `DLMC` tool 操作 SOP.
  * [x] 參與新人 `Final report` 會議. 
  * [x] 協助 `Sales-Jolie` 提供 `SMART` 相關資訊.
  * [x] 協助 `Sales-MJ` 將 `Delta` 異常品 `Flash` 送往維修部做交叉測試.
  * [x] 協助 `EU-FAE` 將 `3pcs` `mSATA mini 3SE` 送往維修部更換 `U14`.

# 2023-02-13
* 協助 `智邦` 撰寫 `Windows` `DLMC` tool 操作 SOP.
* 參與新人 `Final report` 會議. 
* 協助 `Sales-Jolie` 提供 `SMART` 相關資訊.
* 協助 `Sales-MJ` 將 `Delta` 異常品 `Flash` 送往維修部做交叉測試, 後續 `UART Log` 發現 `Assert blk7 & 8` 相關問題, 請 `FW-RD` 提供新版 `FW` 做測試, 看是否能解決此問題.
* 協助 `EU-FAE` 將 `3pcs` `mSATA mini 3SE` 送往維修部更換 `U14`.
* TODO
  * [x] 進一步分析 `3pcs` `mSATA mini 3SE` 異常狀況.
  * [x] 與 `kiwi` 一起觀看 `3TE7` `BiSC 5` 老化現象是否造成 `RRD` 問題.
  * [x] 詢問 `FW-RD Eddie` 關於 `Juniper` 修改 `GC` 相關資訊.
  * [x] 參與 `FAE-team2` 週會.
  * [x] 驗證 `DLMC` `3TE7`(`S20615_20220114` -> `S22801_20230208`).
  * [x] 將  `1pcs` `mSATA mini 3SE` 送往維修部更換 `R52` 零件.
  * [x] 設定 `Ventoy` 相關 `Image` 安裝工具.

# 2023-02-14
* 進一步分析 `3pcs` `mSATA mini 3SE` 異常狀況.
  * `2pcs` -> 可正常辨識.
  * `1pcs` -> 無法正常辨識, 後續發現 `R52` 零件破裂.
* 與 `kiwi` 一起觀看 `3TE7` `BiSC 5` 老化現象是否造成 `RRD` 問題, 並無複製問題現象.
* 詢問 `FW-RD Eddie` 關於 `Juniper` 修改 `GC` 相關資訊.
  * `A19926J` 有修改 `GC`, `A22C27J` 並無修改 `GC`.
  * `A22C27J` 主要修改:
    * 1. implement soft reset.
    * 2. move back-up FW to backend operation or idle
    * 3. add SMARTID
    * 4. Sync TCG FTK FW ddr4 parameter
    * 5. Improve error handle for Security erase flow
    * 6. Fix deallocate stream number repeatedly issue
    * 7. sync A21B12_221115 merge feature, fix bug, add workaround.
  * `A19926J` 主要修改 `GC` 機制:
    * `read/write` 權重改由 `GC` 控制.
    * `Free block` -> `30` -> `GC` 輕.
    * `Free block` -> `24` -> `GC` 中.
    * `Free block` -> `14` -> `GC` 重.
    * `Free block` ->  `5` -> `GC` 超重(直接切換為 `read only`, 直到 `GC` 動作完成, 再切回 `write`).
  * 當 `Free block` 拿去置換 `Later bad`, 數量剩餘百分比到達限制時, 會由限制百分比決定 `read/write` 權重.
    * `7%` 以上 -> `GC` 輕.
    * `6.9%` ~ `6%` -> `GC` 中.
    * `5%` 以下 -> `GC` 超重.
* 參與 `FAE-team2` 週會.
* 驗證 `DLMC` `3TE7`(`S20615_20220114` -> `S22801_20230208`).
* 將  `1pcs` `mSATA mini 3SE` 送往維修部更換 `R52` 零件.
* 設定 `Ventoy` 相關 `Image` 安裝工具.
* TODO
  * [x] 將 `6pcs` `mSATA mini 3SE` 送往維修部更換 `U14` 零件.
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `kiwi` 測試 `3TE7` `DLMC` `S21606` -> `S22801`.
  * [x] 協助新人觀看 `SMI` `RS232` tool 使用問題.
  * [x] 測試 `Delta` 新版 `FW`, 觀看 `Assert` 現象是否消失, `device` 是否可以正常 `work`.
  * [x] 與 `大 A` 討論 `EU` `windows auto DLMC tool`, 並準備相關 `FW` bin file & `device`.
  * [x] 參與 `ULink` 訓練課程.
  * [x] 與 `EU-FAE YingXiang` 討論相關客訴案進度.

# 2023-02-15
* 將 `6pcs` `mSATA mini 3SE` 送往維修部更換 `U14` 零件.
* 參與 `FAE` 週會.
* 協助 `kiwi` 測試 `3TE7` `DLMC` `S21606` -> `S22801`.
* 協助新人觀看 `SMI` `RS232` tool 使用問題.
* 測試 `Delta` 新版 `FW`, 觀看 `Assert` 現象是否消失, `device` 是否可以正常 `work`.
* 與 `大 A` 討論 `EU` `windows auto DLMC tool`, 並準備相關 `FW` bin file & `device`.
* 參與 `ULink` 訓練課程.
* 與 `EU-FAE YingXiang` 討論相關客訴案進度.
* TODO
  * [x] 撰寫 `瑞傳` USB BOOT 相關操作手冊.
  * [x] 協助 `瑞傳` 測試相關 `FW` update & check version image, 並提供相關操作說明以及下載連結給客戶.
  * [x] 協助新人觀看 `innoWorks` `3MR2-P` 客訴案問題.
  * [x] 協助 `FW-RD` 錄製 `Delta` `CFast 3TE7` 無法 `Format` 問題.
  * [x] 整理相關 `USB` 安裝 `image`.
  * [x] 協助 `EU-FAE Jason` 測試其餘 `6 pcs` `mSATA mini 3SE` 維修後狀況.
  * [x] 與廠區人員 `Peter Hong` 討論 `1.8 SATA` 轉板借出問題.
  * [x] 協助新人觀看 `FA report` & `eFAE` 系統操作.
  * [x] 協助 `Nick` 觀看 `Nvidia` 系統架設問題. 
  * [x] 參與 `瑞傳` 客訴案討論, 了解客戶端更新 `FW` 後相關問題.

# 2023-02-16
* 撰寫 `瑞傳` USB BOOT 相關操作手冊.
* 協助 `瑞傳` 測試相關 `FW` update & check version image, 並提供相關操作說明以及下載連結給客戶.
* 協助新人觀看 `innoWorks` `3MR2-P` 客訴案問題.
* 協助 `FW-RD` 錄製 `Delta` `CFast 3TE7` 無法 `Format` 問題.
* 整理相關 `USB` 安裝 `image`.
* 協助 `EU-FAE Jason` 測試其餘 `6 pcs` `mSATA mini 3SE` 維修後狀況.
* 與廠區人員 `Peter Hong` 討論 `1.8 SATA` 轉板借出問題.
* 協助新人觀看 `FA report` & `eFAE` 系統操作.
* 協助 `Nick` 觀看 `Nvidia` 系統架設問題. 
* 參與 `瑞傳` 客訴案討論, 了解客戶端更新 `FW` 後相關問題.
* TODO
  * [x] 與 `Sam` & `Kiwi` 討論 `EU` `Siemens` 問題回覆 & `windows update tool` 狀況.
  * [x] 協助 `Sales-MJ` 回覆 `Delta` & `漢翔` 客訴相關進度以及問題.
  * [x] 協助 `FW-RD` 錄製 `Delta` 異常 SSD 相關 `log` & `Assert` 訊息.
  * [x] 前往維修部將 `Delta` 異常 `Flash` 更換至其他 `Device`, 觀看是否有相同異常現象.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 參與 `瑞傳` 問題回覆討論會議.
  * [x] 回覆 `瑞傳` 相關人員關於異常問題處理狀況.

# 2023-02-17
* 與 `Sam` & `Kiwi` 討論 `EU` `Siemens` 問題回覆 & `windows update tool` 狀況.
* 協助 `Sales-MJ` 回覆 `Delta` & `漢翔` 客訴相關進度以及問題.
* 協助 `FW-RD` 錄製 `Delta` 異常 SSD 相關 `log` & `Assert` 訊息.
* 前往維修部取回並測試 `Delta` 異常 `Flash`.
* 參與 `EU-FAE` 週會.
* 參與 `瑞傳` 問題回覆討論會議.
* 回覆 `瑞傳` 相關人員關於異常問題處理狀況.
* TODO
  * [x] 將 `Delta` 異常 `Flash` 更換至 `2.5 SATA SSD` 觀看是否有相同異常.
  * [x] 與 `FW-RD Sid` 了解如何透過 `DLMC` 更新 `4TS2`.
  * [x] 透過顯微鏡觀察 `mSATA mini 3SE` 異常之 `U14` IC 外觀狀況.
  * [x] 協助 `SW-RD Allen` 驗證 `DLMC` tool.
  * [x] 協助 `FAE-Rex` 設定 ＆ `ReMP` `S42 3TG6-P`.
  * [x] 協助新人觀看客訴問題.
  * [x] 協助新人準備教學筆電.
  * [x] 協助 `EU-FAE YingXiang` 查詢 `3TE6` 更新相關 `bin file`.
  * [x] 協助 `EU-FAE Jason` 同步 `mSATA mini 3SE` 客訴分析狀況.
  * [x] 協助 `Kiwi` 處理 `3TE6` 相關測速 `ATT0`, `HDTune`, `CrystalDiskMark`.

# 2023-02-18
* 將 `Delta` 異常 `Flash` 更換至 `2.5 SATA SSD` 觀看是否有相同異常.
* 與 `FW-RD Sid` 了解如何透過 `DLMC` 更新 `4TS2`.
* 透過顯微鏡觀察 `mSATA mini 3SE` 異常之 `U14` IC 外觀狀況.
* 協助 `SW-RD Allen` 驗證 `DLMC` tool.
* 協助 `FAE-Rex` 設定 ＆ `ReMP` `S42 3TG6-P`.
* 協助新人觀看客訴問題.
* 協助新人準備教學筆電.
* 協助 `EU-FAE YingXiang` 查詢 `3TE6` 更新相關 `bin file`.
* 協助 `EU-FAE Jason` 同步 `mSATA mini 3SE` 客訴分析狀況.
* 協助 `Kiwi` 處理 `3TE6` 相關測速 `ATT0`, `HDTune`, `CrystalDiskMark`.
* TODO
  * [x] 測試 `Delta` 異常 `Flash` 更換至 `2.5 SATA SSD` 是否有相同異常.
  * [x] 前往廠區將 `Delta` 異常 `Flash` 照 `X-ray`.
  * [x] 協助 `Kiwi` 撰寫 `3TE6` 測速結果.
  * [x] 撰寫 `4TS2` 更新工具操作流程.
  * [x] 與 `Sam` & `Miller` & `Kiwi` 討論 `Delta` 異常 `Flash` 問題.
  * [x] 協助 `瑞傳`  提供新版 `128GB`, `256GB` `FW bin file` & `Update FW image`, 以及協助回答相關問題.
  * [x] 協助 `Kiwi` 測試透過 `nvme-cli` 更新 `4TS2` FW.
  * [x] 協助新人觀看相關操作問題.
  * [x] 協助 `Sales-MJ` 回報 `Delta` 客訴測試進度.
  * [x] 回報 `DLMC` tool `V3.6.0` 測試狀況, 並提供 `tool` 於 `EU-FAE YingXiang`.
  * [x] 協助 `Sales-Amy` 回覆 `超恩` 相關技術問題, 並提供 `FW` update tool.

# 2023-02-20
* 測試 `Delta` 異常 `Flash` 更換至 `2.5 SATA SSD` 是否有相同異常.
* 前往廠區將 `Delta` 異常 `Flash` 照 `X-ray`.
* 協助 `Kiwi` 撰寫 `3TE6` 測速結果.
* 撰寫 `4TS2` 更新工具操作流程.
* 與 `Sam` & `Miller` & `Kiwi` 討論 `Delta` 異常 `Flash` 問題.
* 協助 `瑞傳`  提供新版 `128GB`, `256GB` `FW bin file` & `Update FW image`, 以及協助回答相關問題.
* 協助 `Kiwi` 測試透過 `nvme-cli` 更新 `4TS2` FW.
* 協助新人觀看相關操作問題.
* 協助 `Sales-MJ` 回報 `Delta` 客訴測試進度.
* 回報 `DLMC` tool `V3.6.0` 測試狀況, 並提供 `tool` 於 `EU-FAE YingXiang`.
* 協助 `Sales-Amy` 回覆 `超恩` 相關技術問題, 並提供 `FW` update tool.
* TODO
  * [x] 協助 `EU-FAE Jason` 提供相關 `DLMC` tool( `v3.6.0` ).
  * [x] 協助新人整理平台與螢幕.
  * [x] 撰寫 `4TS2` `DLMC` tool User Guide.
  * [x] 協助 `Sales-MJ` 討論 `Delta` & `漢翔航空` 客訴案進度.
  * [x] 協助新人操作 `TTS` 系統.
  * [x] 參與 `FAE-team2` 進度會議.
  * [x] 與 `Sam` & `Kiwi` & `Jack` 討論 `瑞傳` 8D report 撰寫方向, 以及 `Delta` 異常 Flash 下一步處理動作.
  * [x] 前往廠區確認 `Delta` 異常 Flash 之 `ID`.



# 2023-02-21
* 協助 `EU-FAE Jason` 提供相關 `DLMC` tool( `v3.6.0` ).
* 協助新人整理平台與螢幕.
* 撰寫 `4TS2` `DLMC` tool User Guide.
* 協助 `Sales-MJ` 討論 `Delta` & `漢翔航空` 客訴案進度.
* 協助新人操作 `TTS` 系統.
* 參與 `FAE-team2` 進度會議.
* 與 `Sam` & `Kiwi` & `Jack` 討論 `瑞傳` 8D report 撰寫方向, 以及 `Delta` 異常 Flash 下一步處理動作.
* 前往廠區確認 `Delta` 異常 Flash 之 `ID`.
* TODO
  * [x] 撰寫 `瑞傳` 8D report.
  * [x] 協助新人觀看客訴問題, 以及 `3TE7` RAID card 客訴整理狀況.
  * [x] 參與 `FAE` 週會.
  * [x] 與 `FW-RD Sid` 討論 `4TS2` DLMC User Guide 內容以及相關操作.
  * [x] 與 `PM-Shao` 討論 `Kontron` 客訴案處理過程, 以及提供相關資料.
  * [x] 與 `PM-Jack` & `FW-RD Ray` 討論 `瑞傳` 8D report 方向, 以及相關 log 問題.
  * [x] 協助 `EU-FAE` 分析 `Siemens` USB 狀況, 以及處理送往原廠分析相關資訊.
  * [x] 回覆 `Sales-Amy` 關於 `dmesg` log 相關問題.
  * [x] 協助 `Sales-MJ` 統整 `Delta` 相關處理狀況.
  * [x] 參與 `AT&T` 產品介紹會議.
  * [x] 協助 `EU-FAE YingXiang` 提供新版 `4TS2` DLMC User Guide 內容以及相關操作.

# 2023-02-22
* 撰寫 `瑞傳` 8D report.
* 協助新人觀看客訴問題, 以及 `3TE7` RAID card 客訴整理狀況.
* 參與 `FAE` 週會.
* 與 `FW-RD Sid` 討論 `4TS2` DLMC User Guide 內容以及相關操作.
* 與 `PM-Shao` 討論 `Kontron` 客訴案處理過程, 以及提供相關資料.
* 與 `PM-Jack` & `FW-RD Ray` 討論 `瑞傳` 8D report 方向, 以及相關 log 問題.
* 協助 `EU-FAE` 分析 `Siemens` USB 狀況, 以及處理送往原廠分析相關資訊, 但目前因帳務問題, 無法將 `device` 送回原廠做分析, 已請 `EU-FAE` 詢問客戶.
* 回覆 `Sales-Amy` 關於 `dmesg` log 相關問題.
* 協助 `Sales-MJ` 統整 `Delta` 相關處理狀況.
* 參與 `AT&T` 產品介紹會議.
* 協助 `EU-FAE YingXiang` 提供新版 `4TS2` DLMC User Guide 內容以及相關操作.
* TODO
  * [x] 與 `Kiwi` 討論 `瑞傳` `8D` report.
  * [x] 協助 `Sales-MJ` 回覆 `Delta` 異常 `Flash` 分析進度.
  * [x] 協助新人觀看 `3TE7` `RAID card` 客訴整理 & `百視美` 客訴狀況.
  * [x] 提供 `瑞傳` `8D` report 於 `Sales-Stanley`.
  * [x] 詢問 `Benson` 關於 `mSATA mini 3SE` `U14` IC 不良狀況, 以及後續保護措施.
  * [x] 協助 `Kiwi` 查找 `Flash` sorting table 相關線路圖.
  * [x] 詢問 `EU-FAE YingXiang` 關於 `3TG8-P` 客訴問題.
  * [x] 與 `EU-PM Alfie` 討論 `FED230214006` `3TE6` `Gen3 * 1` & `mSATA mini 3SE` `U14` IC 不良狀況相關問題. 

# 2023-02-23
* 與 `Kiwi` 討論 `瑞傳` `8D` report.
* 協助 `Sales-MJ` 回覆 `Delta` 異常 `Flash` 分析進度.
* 協助新人觀看 `3TE7` `RAID card` 客訴整理 & `百視美` 客訴狀況.
* 提供 `瑞傳` `8D` report 於 `Sales-Stanley`.
* 詢問 `Benson` 關於 `mSATA mini 3SE` `U14` IC 不良狀況, 以及後續保護措施.
* 協助 `Kiwi` 查找 `Flash` sorting table 相關線路圖.
* 詢問 `EU-FAE YingXiang` 關於 `3TG8-P` 客訴問題.
* 與 `EU-PM Alfie` 討論 `FED230214006` `3TE6` `Gen3 * 1` & `mSATA mini 3SE` `U14` IC 不良狀況相關問題.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 與 `Kiwi` 量測 `Delta` 異常 `Flash` 訊號.
  * [x] 詢問 `TingYi` 關於 `Sorting borad` 測試程式操作.
  * [x] 追蹤 `Siemens` USB 帳務問題狀況.
  * [x] 回覆 `EU-Sales Sylvain` 關於 `mSATA mini 3SE` `U14` IC 不良狀況.
  * [x] 協助 `Sales-MJ` 回報 `Delta` 異常 `Flash` 量測狀況.
  * [x] 協助 `FW-RD` 測試 `3TE6` `V22620R1` FW bin file.
  * [x] 協助新人觀看客訴處理狀況.

# 2023-02-24
* 參與 `EU-FAE` 週會.
* 與 `Kiwi` 量測 `Delta` 異常 `Flash` 訊號.
* 詢問 `TingYi` 關於 `Sorting borad` 測試程式操作.
* 追蹤 `Siemens` USB 帳務問題狀況.
* 回覆 `EU-Sales Sylvain` 關於 `mSATA mini 3SE` `U14` IC 不良狀況.
* 協助 `Sales-MJ` 回報 `Delta` 異常 `Flash` 量測狀況.
* 協助 `FW-RD` 測試 `3TE6` `V22620R1` FW bin file.
* 協助新人觀看客訴處理狀況.
* TODO
  * [x] 協助 `Sales-Phan Huynh Lam` 處理 `iSAMRT` tool 閃退問題.
  * [x] 協助新人觀看 `3ME4` DLMC 問題.
  * [x] 架設 `Windows 11` 測試環境.
  * [x] 協助新人觀看客訴報告.
  * [x] 參加 `Kiwi` 講解 `SMI` 開卡以及更新相關流程.
  * [x] 撰寫 `SMI` 開卡以及 `USB Boot driver` 相關 `SOP`.

# 2023-03-01
* 協助 `Sales-Phan Huynh Lam` 處理 `iSAMRT` tool 閃退問題.
* 協助新人觀看 `3ME4` DLMC 問題.
* 架設 `Windows 11` 測試環境.
* 協助新人觀看客訴報告.
* 參加 `Kiwi` 講解 `SMI` 開卡以及更新相關流程.
* 撰寫 `SMI` 開卡以及 `USB Boot driver` 相關 `SOP`.
* TODO
  * [x] 協助新人觀看 `fsck` 相關指令及原理.
  * [x] 協助新人觀看 `3TG6-P` 客訴案錄製 `UART` log 相關操作.
  * [x] 協助 `EU-FAE YingXiang` 查找 `DLMC` 失敗原因, 以及詢問 `FW-RD` 關於 `FW` bin file 相關問題.
  * [x] 協助 `Sales-Amy` 回覆 `瑞傳` 人員關於 `DLMC` 失敗相關問題.
  * [x] 協助 `EU-PM Alfie` 更新 `Siemens` `3TE6` 客訴案實驗狀況.
  * [x] 協助 `Nick` 測試 `SmartCow` 客訴案, 執行 `3TE6` BurninTest `8hr`.
  * [x] 協助 `Nick` 了解 `mkmp` tool 使用.

# 2023-03-02
* 協助新人觀看 `fsck` 相關指令及原理.
* 協助新人觀看 `3TG6-P` 客訴案錄製 `UART` log 相關操作.
* 協助 `EU-FAE YingXiang` 查找 `DLMC` 失敗原因, 以及詢問 `FW-RD` 關於 `FW` bin file 相關問題.
  * 發現原提供工具 `Flash` `FW` bin file 為 `WD`, 客戶手上的為 `Kioxia`, 故 `FW` bin file 不同.
* 協助 `Sales-Amy` 回覆 `瑞傳` 人員關於 `DLMC` 失敗相關問題, 後續發現為更新順序不對, 抓到 `device` 為 `/dev/sdb`, 重新開機後, 可正常更新.
* 協助 `EU-PM Alfie` 更新 `Siemens` `3TE6` 客訴案實驗狀況.
* 協助 `Nick` 測試 `SmartCow` 客訴案, 執行 `3TE6` BurninTest `8hr`.
* 協助 `Nick` 了解 `mkmp` tool 使用.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `Sales-MJ` 處理 `漢翔` `1.8 SATA 3SE2-P` 認碟問題.
  * [x] 協助 `Leo` 操作 `iSMART` 以及 `3TO7` 開卡相關操作.
  * [x] 協助 `Rex` 處理 `3TG6-P` 開啟 `AES` 功能.
  * [x] 協助新人處理 `3MV2-P` 錄製 `UART` & `BurninTest`.
  * [x] 協助處理 `Siemens` `USB` 送原廠分析.

# 2023-03-03
* 參與 `EU-FAE` 週會.
* 協助 `Sales-MJ` 處理 `漢翔` `1.8 SATA 3SE2-P` 認碟問題.
* 協助 `Leo` 操作 `iSMART` 以及 `3TO7` 開卡相關操作.
* 協助 `Rex` 處理 `3TG6-P` 開啟 `AES` 功能.
* 協助新人處理 `3MV2-P` 錄製 `UART` & `BurninTest`.
* 協助處理 `Siemens` `USB` 送原廠分析.
* TODO
  * [x] 協助 `Kiwi` 處理 `Ericsson` USB 連接問題.
  * [x] 協助新人 & `Sales-Jolie` 觀看 `百視美` 客訴問題回覆.
  * [x] 協助 `Kiwi` 測試 `Gigabyte Z590` 平台.
  * [x] 協助 `Danny` 觀看 `smart cow` `Linux` 測試程式
  * [x] 協助 `Kerry` 提供 `4TG2-P` `DLMC` tool.

# 2023-03-06
* 協助 `Kiwi` 處理 `Ericsson` USB 連接問題, 轉交於 `RMA` 更換 connector.
* 協助新人 & `Sales-Jolie` 觀看 `百視美` 客訴問題回覆.
* 協助 `Kiwi` 測試 `Gigabyte Z590` 平台.
* 協助 `Danny` 觀看 `smart cow` `Linux` 測試程式
* 協助 `Kerry` 提供 `4TG2-P` `DLMC` tool.
* TODO
  * [x] 協助 `Sales-MJ` 回覆 `台達` 相關客訴問題.
  * [x] 選購 `漢翔` 客訴案使用之 `1.8吋` 轉接頭.
  * [x] 協助 `Kiwi` 量測 `3ME4` & `3TE7` SMART 數值 (`C0` & `0C`), 分別針對 `power-off`, `warm-boot`, `abnormal power-off`.
  * [x] 整理 `2` 月相關重大客訴案進度.
  * [x] 參與 `FAE-team2` 週會.
  * [x] 協助新人處理 `百視美` 客訴案處理, 請 `DQE-Summer` 協助加測異常上斷電 `2000` 次.
  * [x] 轉交 `EU` `3TG8-P` & `RAID` card 給 `FW-Mike Yuan`.
  * [x] 於 `RMA` 領回 `Ericsson` USB, 協助 `Kiwi` 測試是否於高速可認碟.

# 2023-03-07
* 協助 `Sales-MJ` 回覆 `台達` 相關客訴問題.
* 選購 `漢翔` 客訴案使用之 `1.8吋` 轉接頭.
* 協助 `Kiwi` 量測 `3ME4` & `3TE7` SMART 數值 (`C0` & `0C`), 分別針對 `power-off`, `warm-boot`, `abnormal power-off`( `Windows 10`, `data device` ).
     ## `3ME4 Table`
    |       Test Item           |    0   |    1    |    2    |    3    |    4    |
    |         :---:             | :----: | :----:  | :----:  | :----:  | :----:  |
    | `Reboot(C0)`              |    3   |   +0    |   +0    |   +0    |   +0    |
    | `Reboot(0C)`              |    1   |   +0    |   +0    |   +0    |   +0    |
    | `Power off(C0)`           |    3   |   +1    |   +1    |   +1    |   +1    |
    | `Power off(0C)`           |    1   |   +0    |   +0    |   +0    |   +0    |
    | `Abnormal power off(C0)`  |    7   |   +1    |   +1    |   +1    |   +1    |
    | `Abnormal power off(0C)`  |    1   |   +1    |   +1    |   +1    |   +1    |
     ## `3TE7 Table`
    |       Test Item           |    0   |    1    |    2    |    3    |    4    |
    |         :---:             | :----: | :----:  | :----:  | :----:  | :----:  |
    | `Reboot(C0)`              |    5   |   +0    |   +0    |   +0    |   +0    |
    | `Reboot(0C)`              |    5   |   +0    |   +0    |   +0    |   +0    |
    | `Power off(C0)`           |    5   |   +1    |   +1    |   +1    |   +1    |
    | `Power off(0C)`           |    5   |   +0    |   +0    |   +0    |   +0    |
    | `Abnormal power off(C0)`  |    9   |   +1    |   +1    |   +1    |   +1    |
    | `Abnormal power off(0C)`  |    5   |   +1    |   +1    |   +1    |   +1    |

* 整理 `2` 月相關重大客訴案進度.
* 參與 `FAE-team2` 週會.
* 協助新人處理 `百視美` 客訴案處理, 請 `DQE-Summer` 協助加測異常上斷電 `2000` 次.
* 轉交 `EU` `3TG8-P` & `RAID` card 給 `FW-Mike Yuan`.
* 於 `RMA` 領回 `Ericsson` USB, 協助 `Kiwi` 測試是否於高速可認碟, 經由測試, 可於 `USB 3.0` 狀態下被辨識.
* TODO
  * [x] 與新人共同量測相關 `Device`( `3TG6-P(SATA)`, `3TG6-P(M.2)`, `3TE4(M.2)`, `3ME2(M.2)`, `3TE6(M.2)`, `3MG2-P(SATA)`, `3TG3-P(M.2)`, `Samsung 970` ), 觀察是否與 `3ME4` & `3TE7` SMART 變化相同.
  * [x] 協助新人回覆 `智邦` 人員相關問題.
  * [x] 協助新人操作 `3TG6-P` 於 `MV Tool` 下 `sl & el` command.
  * [x] 參與 `FAE` 週會.
  * [x] 查找借出之 `Device`( `3TE7`, `3TE6` `BiSC5` ) & `Ericsson` USB 之 connector.
  * [x] 與 `Sales-MJ` 討論 `漢翔` 後續分析狀況.

# 2023-03-08
* 協助新人回覆 `智邦` 人員相關問題.
* 協助新人操作 `3TG6-P` 於 `MV Tool` 下 `sl & el` command.
* 參與 `FAE` 週會.
* 查找借出之 `Device`( `3TE7`, `3TE6` `BiSC5` ) & `Ericsson` USB 之 connector.
* 與 `Sales-MJ` 討論 `漢翔` 後續分析狀況.
* TODO
  * [x] 測試 `1.8吋 SATA` 轉接頭於 `漢翔` 客訴案 device.
  * [x] 撰寫 `copy 影片` script.
  * [x] 協助新人依照客人測試手法, 將 `AVI` 影片檔 copy 於 `3MV2-P`. 
  * [x] 修改 `瑞傳` `read-retry` report.
  * [x] 回覆 `Sales-Jessica` 關於 `Ericsson` USB 狀況, 並將剩餘 `3`pcs 送往 `RMA` 維修.
  * [x] 轉交 `Siemens` `2`pcs USB 於原廠分析.

# 2023-03-09
* 測試 `1.8吋 SATA` 轉接頭於 `漢翔` 客訴案 device.
* 撰寫 `copy 影片` script.
* 協助新人依照客人測試手法, 將 `AVI` 影片檔 copy 於 `3MV2-P`. 
* 修改 `瑞傳` `read-retry` report.
* 回覆 `Sales-Jessica` 關於 `Ericsson` USB 狀況, 並將剩餘 `3`pcs 送往 `RMA` 維修.
* 轉交 `Siemens` `2`pcs USB 於原廠分析.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `EU-FAE` 轉送 `3TG6-P` `3` pcs 至 `RMA`.
  * [x] 詢問 `Sam` & `Pater` 是否能夠提供 `SMI` 原廠相關 `Siemens USB` 線路圖.
  * [x] 協助 `CN-Rowand` 回答關於 `DLMC` 相關操作問題(`V3.6.0`).
  * [x] 詢問 `SW-Allen` 關於 `iSMART` 閃退問題.
  * [x] 測試 `Ericisson` `3` pcs 更換 `connector` 速度狀況.
  * [x] 觀看 `百視美` `3ME4` 加測 `2000` power cycle 測試 log.

# 2023-03-10
* 參與 `EU-FAE` 週會.
* 協助 `EU-FAE` 轉送 `3TG6-P` `3` pcs 至 `RMA`.
* 詢問 `Sam` & `Pater` 是否能夠提供 `SMI` 原廠相關 `Siemens USB` 線路圖.
* 協助 `CN-Rowand` 回答關於 `DLMC` 相關操作問題(`V3.6.0`).
* 詢問 `SW-Allen` 關於 `iSMART` 閃退問題, 後續發現可能與平台有相關, 已將平台借出.
* 測試 `Ericisson` `3` pcs 更換 `connector` 速度狀況, 發現不太穩定.
* 觀看 `百視美` `3ME4` 加測 `2000` power cycle 測試 log.
* TODO
  * [x] 測試 `Ericisson` `3` pcs 更換 `connector` 速度狀況.
  * [x] 測試 `EU` `Gen3x1` `3TE6 128GB BiSC5` 於 `Nexcom` 平台辨識狀況.
  * [x] 操作 `PCIe` analyzer 錄製相關 log 於 `Nexcom` 平台( `3TG6-P`, `3TG3-P`, `4TG2-P`, `Samsung 970` ).
  * [x] 協助新人觀看 `fsck` 相關操作.
  * [x] 協助新人回覆 `智邦` 相關問題.
  * [x] 協助新人觀看 `FA230301003` `FA` report.
  * [x] 協助 `FAE-Danny` 測試 reboot `power cycling` script.

# 2023-03-13
* 測試 `Ericisson` `3` pcs 更換 `connector` 速度狀況.
  * USB `3.1` -> 可辨識.
  * USB `3.0` -> 時好時壞.
  * USB `2.0` -> 可正常辨識.
* 測試 `EU` `Gen3x1` `3TE6 128GB BiSC5` 於 `Nexcom` 平台辨識狀況, 皆無法辨識.
* 操作 `PCIe` analyzer 錄製相關 log 於 `Nexcom` 平台( `3TG6-P`, `3TG3-P`, `4TG2-P`, `Samsung 970` ).
* 協助新人觀看 `fsck` 相關操作.
* 協助新人回覆 `智邦` 相關問題.
* 協助新人觀看 `FA230301003` `FA` report.
* 協助 `FAE-Danny` 測試 reboot `power cycling` script.
* TODO
  * [x] 測試 `EU` `Gen3x1` `3TE6 128GB BiSC5` 於 `Nexcom` 平台辨識狀況.
    * [x] `V20B09` (BiSC3).
    * [x] `V2111803`.
    * [x] `V21118N1`.
    * [x] `V22620X1`.
  * [x] 參與 `FAE-team2` 週會.
  * [x] 詢問 `Sales-MJ` 關於 `Delta` Flash 客訴案後續狀況.
  * [x] 測試 `Ericisson` `4` pcs 連線狀況.
  * [x] 詢問 `Benson` 查找 `Siemens` USB housing 材質.
  * [x] 查找 `Ericisson` 舊款 connector 料號, 並領出.

# 2023-03-14
* 測試 `EU` `Gen3x1` `3TE6 128GB BiSC5` 於 `Nexcom` 平台辨識狀況, 皆無法辨識.
  * `V20B09` (BiSC3).
  * `V2111803`.
  * `V21118N1`.
  * `V22620X1`.
* 參與 `FAE-team2` 週會.
* 詢問 `Sales-MJ` 關於 `Delta` Flash 客訴案後續狀況.
* 測試 `Ericisson` `4` pcs 連線狀況.
  * 透過 `USB` analyzer 可於 `USB 3.2`, `USB 3.0`, `USB 2.0` 辨識.
  * 儲存 `USB` analyzer -> `USB 3.0` 相關資訊.
  * 透過不同平台連線, 部份可辨識, 部份不可辨識.
* 詢問 `Benson` 查找 `Siemens` USB housing 材質, 此材料材質為 `LCP`.
* 查找 `Ericisson` 舊款 connector 料號, 並領出.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 觀看 `C++` 程式.
  * [x] 與 `Sales-Standly` & `FAE-Jay` 討論台達客訴案狀況.
  * [x] 測試 `3TE6 P42 BiSC5 128GB` 使用 `FW-V21118X1`, 測試開關機狀況, 是否認不到碟.

# 2023-03-15
* 參與 `FAE` 週會.
* 觀看 `C++` 程式.
* 與 `Sales-Standly` & `FAE-Jay` 討論台達客訴案狀況.
* 測試 `3TE6 P42 BiSC5 128GB` 使用 `FW-V21118X1`, 測試開關機狀況, 認碟狀況時好時壞, 後續有找到 `100%` 復現 `lane flip 1` 方式.
* TODO
  * [x] 查找 `3TE6 P42 BiSC5 128GB` 短路問題.
  * [x] 借出 `3TE6 P42 BiSC5 128GB`( `DEM24-A28DD1KCCDF` ).
  * [x] 與 `Sales-Standly` & `FAE-Jay` 討論台達客訴案狀況.
  * [x] 協助 `Benson` 提供 `Kontron` 量測 `IR` 值結果.
  * [x] 測試 `3TE6 P42 BiSC5 128GB` 使用 `FW-V21118H2`, 測試開關機狀況, 是否認不到碟.
  * [x] 協助 `FAE-Danny` 觀看 `smart cow` 測試狀況.
  * [x] 協助新人觀看 `FA` report.

# 2023-03-16
* 查找 `3TE6 P42 BiSC5 128GB` 短路問題, 後續發現為 `Flash` 短路, 造成 device 問題.
* 借出 `3TE6 P42 BiSC5 128GB`( `DEM24-A28DD1KCCDF` ).
* 與 `Sales-Standly` & `FAE-Jay` 討論台達客訴案狀況.
* 協助 `Benson` 提供 `Kontron` 量測 `IR` 值結果.
* 測試 `3TE6 P42 BiSC5 128GB` 使用 `FW-V21118H2`, 測試開關機狀況, 經由 `3` 種 `warm boot` 方式, 皆可認到碟.
* 協助 `FAE-Danny` 觀看 `smart cow` 測試狀況.
* 協助新人觀看 `FA` report, 並修改測試 `Shell script`.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 測試 `3TE6 P42 BiSC5 128GB` 使用 `FW-V21118H2` 於 `AIOT-ABBI120` 主機板測試開關機狀況.
  * [x] 協助 `FAE-Danny` 觀看 `smart cow` 測試狀況.
  * [x] 測試 `Siemens` `3SE3` USB `4` pcs 連線速度狀況.
  * [x] 協助新人轉送 device 於 `RMA`.
  * [x] 更新手邊平台 `BIOS` 版本.
  * [x] 測試 `Siemens` `3SE3` USB (已開卡) 執行 `AIDA64`.

# 2023-03-17
* 參與 `EU-FAE` 週會.
* 測試 `3TE6 P42 BiSC5 128GB` 使用 `FW-V21118H2` 於 `AIOT-ABBI120` 主機板測試開關機狀況.
* 協助 `FAE-Danny` 觀看 `smart cow` 測試狀況.
* 測試 `Siemens` `3SE3` USB `4` pcs 連線速度狀況.
* 協助新人轉送 device 於 `RMA`.
* 更新手邊平台 `BIOS` 版本.
* 測試 `Siemens` `3SE3` USB (已開卡) 執行 `AIDA64`.
* TODO
  * [x] 與 `新竹-RD` 討論 `3TE6` 平台測試狀況.
  * [x] 觀看 `FIO` 相關測試 `scipt`.
  * [x] 測試 `CN` 寄回 `5`pcs `3SE3 USB` 客訴品狀況.
  * [x] 協助新人了解 `3TE7` `FW` 進版過程.

# 2023-03-20
* 與 `新竹-RD` 討論 `3TE6` 平台測試狀況, 後續回報為電阻問題.
* 觀看 `FIO` 相關測試 `scipt`.
* 測試 `CN` 寄回 `5`pcs `3SE3 USB` 客訴品狀況, `3`pcs 可被辨識, `2`pcs 無過電.
* 協助新人了解 `3TE7` `FW` 進版過程.
* TODO
  * [x] 協助 `EU-PM` `Alfie` 回報平台相容性問題.
  * [x] 協助新人處理 `VN` 相關客訴問題.
  * [x] 測試 `AIOT` 平台 `ASCI-120` 與 `3TE6` 相容性問題.
  * [x] 參與 `FAE-team2` 週會.
  * [x] 量測 `Ericisson` `2`pcs `3SE3 USB` 無過電狀況.
  * [x] 回報 `Ericisson` `5`pcs `3SE3 USB` 客訴品狀況.

# 2023-03-21
* 協助 `EU-PM` `Alfie` 回報平台相容性問題.
* 協助新人處理 `VN` 相關客訴問題.
* 測試 `AIOT` 平台 `ASCI-120` 與 `3TE6` 相容性問題, 通過 `3` 種手法, 各重開 `5` 次, 並無發生異常.
* 參與 `FAE-team2` 週會.
* 量測 `Ericisson` `2`pcs `3SE3 USB` 無過電狀況, 後續懷疑是 `Crystal` 異常, 已經領料準備更換.
* 回報 `Ericisson` `5`pcs `3SE3 USB` 客訴品狀況.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `PM-Jack` 測試 `3TE7` (`S21606WE_NO_WP`) 於客戶平台黑頻問題.
  * [x] 參與 `內部體檢`.
  * [x] 協助新人觀看 `3TE6` 客訴案回覆 `智邦` 內容.
  * [x] 撰寫 `Ericssion` FA report & 詢問 `Sales-Jessica` 客訴開案問題.

# 2023-03-22
* 參與 `FAE` 週會.
* 協助 `PM-Jack` 測試 `3TE7` (`S21606WE_NO_WP`) 於客戶平台黑頻問題.
* 參與 `內部體檢`.
* 協助新人觀看 `3TE6` 客訴案回覆 `智邦` 內容.
* 撰寫 `Ericssion` FA report & 詢問 `Sales-Jessica` 客訴開案問題.
* TODO
  * [x] 參與 `FAE` 月會.
  * [x] 協助新人觀看 `3TE7 BiCS5` 進版報告.
  * [x] 準備 `FAE` 月會案例分享報告.
  * [x] 錄製 `3TE7` (`S21606WE_NO_WP`) 於客戶平台黑頻問題 `UART` log.
  * [x] 轉送 `Ericssion` `2`pcs 無過電 `USB` 於 `RMA` 更換 `Crystal` & 測試.
  * [x] 協助 `FAE-Danny` 觀看 `smart cow` 相關測試 `Shell Script`.
  * [x] 與 `EU-FAE Jason` 討論 `Ericssion` 客訴開案問題.
  * [x] 撰寫 `Ericssion` FA report.
  * [x] 協助 `FAE-Nick` 測試 `MKMP tool` update image.

# 2023-03-23
* 參與 `FAE` 月會.
* 協助新人觀看 `3TE7 BiCS5` 進版報告.
* 準備 `FAE` 月會案例分享報告.
* 錄製 `3TE7` (`S21606WE_NO_WP`) 於客戶平台黑頻問題 `UART` log.
* 轉送 `Ericssion` `2`pcs 無過電 `USB` 於 `RMA` 更換 `Crystal` & 測試.
* 協助 `FAE-Danny` 觀看 `smart cow` 相關測試 `Shell Script`.
* 與 `EU-FAE Jason` 討論 `Ericssion` 客訴開案問題.
* 撰寫 `Ericssion` FA report.
* 協助 `FAE-Nick` 測試 `MKMP tool` update image.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 錄製 `Winsystem` 客訴品 `3TE7` 黑屏狀況 `UART` log.
  * [x] 與 `EU-PM Alfie` 討論 `Winsystem` 客訴案狀況.
  * [x] 協助新人觀看客訴案相關回答.
  * [x] 協助 `FAE-Nick` 重包 `MKMP tool` update image(更新 `SN.txt`).

# 2023-03-24
* 參與 `EU-FAE` 週會.
* 錄製 `Winsystem` 客訴品 `3TE7` 黑屏狀況 `UART` log.
* 與 `EU-PM Alfie` 討論 `Winsystem` 客訴案狀況.
* 協助新人觀看客訴案相關回答.
* 協助 `FAE-Nick` 重包 `MKMP tool` update image(更新 `SN.txt`).
* TODO
  * [x] 詢問 `Kiwi` 如何調整 `3TG6-P` 早期系列開卡過程, 如何透過 `UART` 進入 `loader mode`.
  * [x] 透過調整電阻使 `3TG6-P` 切換為 `SATA mode`, 可透過 `UART` 進入 `loader mode` 開卡.
  * [x] 處理 `EU` 送回之 `35 pcs` `CFast card`.
  * [x] 協助新人回答 `3TE6` LED 燈號顯示相關問題, 以及 `DLMC` 相關操作.
  * [x] 協助新人測試 `3MV2-P` `CDM` 量測.
  * [x] 協助 `EU-FAE` 準備 `3TE7` `DLMC` 相關 device.
  * [x] 協助 `EU-FAE` 詢問 `DLMC` `-v FW verify` 參數相關問題.
  * [x] 與 `Sales-MJ` 討論 `漢翔` 串接 `1.8` SATA 相關問題.

# 2023-03-25
* 詢問 `Kiwi` 如何調整 `3TG6-P` 早期系列開卡過程, 如何透過 `UART` 進入 `loader mode`.
* 透過調整電阻使 `3TG6-P` 切換為 `SATA mode`, 可透過 `UART` 進入 `loader mode` 開卡.
* 處理 `EU` 送回之 `35 pcs` `CFast card`.
* 協助新人回答 `3TE6` LED 燈號顯示相關問題, 以及 `DLMC` 相關操作.
* 協助新人測試 `3MV2-P` `CDM` 量測.
* 協助 `EU-FAE` 準備 `3TE7` `DLMC` 相關 `device`, 外顯部份未修改正確, 需借出相同 `device`, 並錄製影片證明沒有問題才可提供工具.
* 協助 `EU-FAE` 詢問 `DLMC` `-v FW verify` 參數相關問題, 外顯的檢查符合才更新, 不符合就不執行, 比方說 device 外顯為 `S20615`,  -v 帶 `S22831`, 這樣就不會更新.
* 與 `Sales-MJ` 討論 `漢翔` 串接 `1.8 SATA` 相關問題, 先請客戶透過主機板 `SATA` 直接做串接.
* TODO
  * [x] 分析 `EU` 送回之 `35 pcs` `CFast card`.
  * [x] 分析 `EU` 送回之 `3TG6-P` 相關問題.
  * [x] 提供 `Kiwi` 關於 `block 4` 相關 `FA` report.
  * [x] 與 `Sales-MJ` 討論 `漢翔` `1.8 SATA SSD` 辨識問題.
  * [x] 協助新人測試 `3MV2-P` 透過 `CrystalDiskMark` 測試相關效能.

# 2023-03-27
* 分析 `EU` 送回之 `35 pcs` `CFast card`, 後續發現有 `18pcs` 有異常, 後續會轉送至廠區照 `X-ray`.
* 分析 `EU` 送回之 `3TG6-P` 相關問題, 後續發現為 `U37` power IC 有異常, 已經申請領料以及樣品做交叉驗證.
* 提供 `Kiwi` 關於 `block 4` 相關 `FA` report.
* 與 `Sales-MJ` 討論 `漢翔` `1.8 SATA SSD` 辨識問題, 後續決定借一條 `USB` 轉接線於客戶測試.
* 協助新人測試 `3MV2-P` 透過 `CrystalDiskMark` 測試相關效能.
* TODO
  * [x] 轉送 `18pcs` 異常 `CFast card` 於場區照 `Controller` `X-ray`.
  * [x] 處理 `ASUS B360-F` 主機板無法安裝 `Ubuntu` 相關問題.
  * [x] 參與 `FAE Team 2` 週會.
  * [x] 協助 `EU-FAE` 錄製 `3TE7` DLMC tool 相關影片, 以及提供相關 `FW` bin file.
  * [x] 協助 `PM-Chelsea` 轉借 `3MG3-P` 於 `Thermal` team 人員.
  * [x] 協助 `Leo` 觀看 `Canbus` 相關環境操作.
  * [x] 協助 `Danny` 處理 `Smaer Cow` 相關環境架設, 包含 `partition` 切割 & `dd` 操作.
  * [x] 教導新人如何操作 `mkmp tool`, 以及 `SN.txt` 如何產出.
  * [x] 與 `PM-Jack` 討論 `3TE7 BiCS5` `DLMC tool` 相關內容.
  * [x] 更新 `Ericssion` FA report 案號.

# 2023-03-28
* 轉送 `18pcs` 異常 `CFast card` 於廠區照 `Controller` `X-ray`.
* 處理 `ASUS B360-F` 主機板無法安裝 `Ubuntu` 相關問題, 目前已解決, 需開啟主機板 `Intel VMX` 功能.
* 參與 `FAE Team 2` 週會.
* 協助 `EU-FAE` 錄製 `3TE7` DLMC tool 相關影片, 以及提供相關 `FW` bin file.
* 協助 `PM-Chelsea` 轉借 `3MG3-P` 於 `Thermal` team 人員.
* 協助 `Leo` 觀看 `Canbus` 相關環境操作.
* 協助 `Danny` 處理 `Smaer Cow` 相關環境架設, 包含 `partition` 切割 & `dd` 操作.
* 教導新人如何操作 `mkmp tool`, 以及 `SN.txt` 如何產出.
* 與 `PM-Jack` 討論 `3TE7 BiCS5` `DLMC tool` 相關內容.
* 更新 `Ericssion` FA report 案號.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 參與 `研發部` 月會.
  * [x] 於 `eFAE` 系統補充 `Ericssion` USB 客訴相關處理紀錄.
  * [x] 填寫 `瑞傳` FA case, 並上傳相關分析資料.
  * [x] 詢問 `Benson` 協助觀看 `18pcs` 異常 `CFast card` `X-ray` 照片
  * [x] 協助 `EU-FAE` 回答 `3TE6` `WWN` 產生規則.
  * [x] 詢問 `Jay` 關於 `3TG3-P` `SMI` 開卡方式.
  * [x] 協助新人觀看 `SN` 產出之 `python` code.
  * [x] 協助新人觀看 `智邦` 提問相關問題.
  * [x] 處理 `ASUS B360-F` 主機板無法安裝 `Ubuntu` 相關問題.

# 2023-03-29
* 參與 `FAE` 週會.
* 參與 `研發部` 月會.
* 於 `eFAE` 系統補充 `Ericssion` USB 客訴相關處理紀錄.
* 填寫 `瑞傳` FA case, 並上傳相關分析資料, 並結案.
* 詢問 `Benson` 協助觀看 `18pcs` 異常 `CFast card` `X-ray` 照片
* 協助 `EU-FAE` 回答 `3TE6` `WWN` 產生規則, 後續為如不手動輸入 `WWN`, 則會透過序號自動產生, 如手動輸入, 則會與輸入之 `WWN` 不相同.
* 詢問 `Jay` 關於 `3TG3-P` `SMI` 開卡方式, 後續發現為缺少 `SMI` `Auth key`.
* 協助新人觀看 `SN` 產出之 `python` code.
* 協助新人觀看 `智邦` 提問相關問題.
* 處理 `ASUS B360-F` 主機板無法安裝 `Ubuntu` 相關問題, 已成功安裝完成.
* TODO
  * [x] 透過 `熱風槍` 回烘  `18pcs` 異常 `CFast card`.
  * [x] 觀看 `EU` `mSATA 3TG6-P` 客訴案狀況.
  * [x] 協助新人了解 `elog` 是否會 `partition table` 損壞狀況.
  * [x] 協助新人觀看 `python` 程式撰寫狀況.

# 2023-03-30
* 透過 `熱風槍` 回烘  `18pcs` 異常 `CFast card`.
  * `4` pcs 正常.
  * `14` pcs 還是無法辨識.
* 觀看 `EU` `mSATA 3TG6-P` 客訴案狀況.
* 協助新人了解 `elog` 是否會 `partition table` 損壞狀況.
* 協助新人觀看 `python` 程式撰寫狀況.
* TODO
  * [x] 將 `11` pcs 異常 `CFast card` 送至 `RMA` 更換 `controller`, 其餘 `3` pcs 做進階分析.
  * [x] 協助 `PM-Sharon` 提供 `3TG3-P` `Quick erase` 相關 `command`.
  * [x] 撰寫 `mkmp tool` `SN` 產出程式.
  * [x] 協助新人觀看 `python` 相關撰寫問題.
  * [x] 參加 `EU-FAE` 週會.
  * [x] 協助 `EU` 追蹤 `SMI` 分析狀況.

# 2023-03-31
* 將 `10` pcs 異常 `CFast card` 送至 `RMA` 更換 `controller`, 其餘 `4` pcs 做進階分析.
  * `10` pcs `CFast card` 更換 `controller` 後, 皆可正常辨識.
  * `BCA11706200510866` -> FW issue (`incorrect calculation of 'invalidcnt`).
  * `YCA11806190040175` -> short
  * `BCA11706200510548` -> `loader mode` (Flash ch 0 異常).
  * `YCA11906040110294` -> Cannot format (`Write protect enable`).
* 協助 `PM-Sharon` 提供 `3TG3-P` `Quick erase` 相關 `command`.
* 撰寫 `mkmp tool` `SN` 產出程式.
* 協助新人觀看 `python` 相關撰寫問題.
* 參加 `EU-FAE` 週會.
* 協助 `EU` 追蹤 `SMI` 分析狀況. 
* TODO
  * [x] 整理 `CFast card` `35` pcs 分析狀況, 並回報 `EU`.
  * [x] 撈取 `CFast card` `35` pcs `iSMART` & `UART` 相關資訊.
  * [x] 申請 `CFast card` `Flash` 料件申請.
  * [x] 協助 `EU-FAE` 轉送 `3SE3 USB` 於 `RMA` 開卡設定 `SN`.
  * [x] 將 `EU` `mSATA 3TG6-P` 送至 `RMA` 更換 `U37`.
  * [x] 將 `CFast card` `YCA11806190040175`  送至 `RMA` 更換 `controller`.
  * [x] 將 `CFast card` `BCA11706200510866` 重新開卡, 更新 `FW` (`S21804`). 
  * [x] 漢翔人員回報轉接線可以使用.
  * [x] 協助新人觀看客訴案.

# 2023-04-06
* 整理 `CFast card` `35` pcs 分析狀況, 並回報 `EU`.
* 撈取 `CFast card` `35` pcs `iSMART` & `UART` 相關資訊.
* 申請 `CFast card` `Flash` 料件申請.
* 協助 `EU-FAE` 轉送 `3SE3 USB` 於 `RMA` 開卡設定 `SN`.
* 將 `EU` `mSATA 3TG6-P` 送至 `RMA` 更換 `U37`, 經由測試後, 發現還是無法辨識.
* 將 `CFast card` `YCA11806190040175`  送至 `RMA` 更換 `controller`, 經過測試後, 依然 short.
* 將 `CFast card` `BCA11706200510866` 重新開卡, 更新 `FW` (`S21804`). 
* 漢翔人員回報轉接線可以使用, 後續會進行內部測試討論.
* 協助新人觀看客訴案.
* TODO
  * [x] 分析 `EU` `mSATA 3TG6-P` 無法辨識原因.
  * [x] 將 `EU` `mSATA 3TG6-P` 送至 `RMA` 更換 `U13`.
  * [x] 將 `CFast card` `BCA11706200510548` 送至 `RMA` 更換 `Flash`.
  * [x] 協助 `PM-Eric` 測試 `3TG6-P` `RAID` 效能測試.
  * [x] 參加 `EU` auto FW update 討論會議.
  * [x] 參加 `EU-FAE` 週會.
  * [x] 觀看 `SMI` 分析 `controller` 相關結果.

# 2023-04-07
* 分析 `EU` `mSATA 3TG6-P` 無法辨識原因, 推測是 `U13` 供電異常.
* 將 `EU` `mSATA 3TG6-P` 送至 `RMA` 更換 `U13`.
* 將 `CFast card` `BCA11706200510548` 送至 `RMA` 更換 `Flash`.
* 協助 `PM-Eric` 測試 `3TG6-P` `RAID` 效能測試, 執行一次需花費 `13hr`, 預計下週一測試完成.
* 參加 `EU` auto FW update 討論會議.
* 參加 `EU-FAE` 週會.
* 觀看 `SMI` 分析 `controller` 相關結果.
* TODO
  * [x] 測試 `Kontron` 平台, 並將 `3TE6` 做 `FW` 更新.
  * [x] 測試 `CFast card` `BCA11706200510548`.
  * [x] 測試 `EU` `mSATA 3TG6-P`.
  * [x] 協助 `PM-Eric` 測試 `3TG8-P` `RAID` 效能測試.
  * [x] 協助新人觀看 `3MG2-P` 電路圖.

# 2023-04-10
* 測試 `Kontron` 平台, 並將 `3TE6` 做 `FW` 更新, 後續詢問新竹 `FW-RD`, 發現平台已有異常, 透過 `UART` log 觀看, 平台並未與 `Device` 做 link.
* 測試 `CFast card` `BCA11706200510548`, `Device` 依然無法辨識, 經由查證發現為短路.
* 測試 `EU` `mSATA 3TG6-P`, 更換完 `U13` power IC 後, 可正常辨識.
* 協助 `PM-Eric` 測試 `3TG8-P` `RAID` 效能測試, 後續因客戶未提供 `RAID` 相關設定, 故無法做相關測試.
* 協助新人觀看 `3MG2-P` 電路圖.
* TODO
  * [x] 參與 `FAE Team 2` 週會.
  * [x] 觀看 `clonezilla` 操作以及設定客戶平台.
  * [x] 觀看 `ATA cmd` 如何設定.
  * [x] 協助新人觀看客訴問題.
  * [x] 針對 `Kontron` 平台 `Device` `3TE6` 做 `8hr` `BurninTest`.

# 2023-04-11
* 參與 `FAE Team 2` 週會.
* 觀看 `clonezilla` 操作以及設定客戶平台.
  * 將 `device` `3TE7` 開卡( `S22831WE_NO_WP` / `S21606WE_NO_WP` ).
  * 準備 `1` pcs USB 安裝 `clonezilla` OS.
  * 準備 `1` pcs USB 擺放客戶 `OS` 壓縮檔.
  * 將 `2` pcs USB & `1` pcs 客戶 `device` 接上平台.
  * 透過 `clonezilla` 將客戶 `OS` 倒回.
    * `選擇語言`.
    * `選擇目前語言鍵盤`.
    * `選擇使用再生龍`.
    * `選擇使用印象檔處理整顆硬碟 or 部份分割區`.
    * `選擇掛載USB進行備份`( 此選項進入後無法掛載, 可直接點選 `確定` 選項 ).
    * `進入初學者模式`.
    * `選擇還原印象檔至本機磁碟`.
    * `選擇與備份印象檔相同磁碟切割區`.
    * 後續點選確定執行備份, 執行完之後點選關機即完成備份.
  * 透過 `ATA cmd` 設定加密內容.
    * `Feature` -> `0x16`.
    * `Sec_Cnt` -> `0x41`.
    * `Device/Head` -> `0xE0`.
    * `Command` -> `0x82`.
* 觀看 `ATA cmd` 如何設定, 需設定對應 `FW` 開卡包.
  * `BiCS 5` -> `S22831WE_NO_WP`.
  * `BiCS 3` -> `S21606WE_NO_WP`.
* 協助新人觀看客訴問題.
* 針對 `Kontron` 平台 `Device` `3TE6` 做 `8hr` `BurninTest`, 結果為 `pass`.
* 協助 `PM-Jack` 錄製 `Winsystem` 設定完成之相關影片.
* TODO
  * [x] 參加 `FAE` 週會.
  * [x] 轉交 `Texim` `11` pcs `mSATA mini 3SE` 於 `RMA`.
  * [x] 觀看測試平台問題, 並重灌 `ubuntu` 平台.
  * [x] 協助 `Kiwi`  測試 `3TE7` `DLMC` 功能( `S21606` to `S23204P` ).
  * [x] 處理 `台達` `CFast 3TE7` Flash 客訴案.
  * [x] 協助 `PM-Davis` 將 `3TE6` 調整為 `high pull` device 做開卡, 並於平台做相關 `power on / off` 測試.
  * [x] 將 `EU` `mSATA 3TG6-P` 做 `2hr` `BurninTest` 相關測試.
  * [x] 觀看 `CFast 3SE3` 於客戶平台無法正常辨識狀況.

# 2023-04-12
* 參加 `FAE` 週會.
* 轉交 `Texim` `11` pcs `mSATA mini 3SE` 於 `RMA`.
* 觀看測試平台問題, 並重灌 `ubuntu` 平台.
* 協助 `Kiwi`  測試 `3TE7` `DLMC` 功能( `S21606` to `S23204P` ).
* 處理 `台達` `CFast 3TE7` Flash 客訴案.
* 協助 `PM-Davis` 將 `3TE6` 調整為 `high pull` device 做開卡, 並於平台做相關 `power on / off` 測試.
* 將 `EU` `mSATA 3TG6-P` 做 `2hr` `BurninTest` 相關測試.
* 觀看 `CFast 3SE3` 於客戶平台無法正常辨識狀況.
* TODO
  * [x] 協助 `FW-RD Thomas` 提供 `Kontron` 相關資訊.
  * [x] 詢問 `MIS` 處理 `Microsoft` 認證問題.
  * [x] 架設 `PM-Davis` 將 `3TE6` 調整為 `high pull`, 並於平台做 `reboot` 測試環境.
  * [x] 協助新人處理 `3MR2-P` `ICE` 點位訊號焊接.
  * [x] 協助 `EU-FAE` 提供 `mSATA 3TG6-P` 相關分析結果.
  * [x] 協助 `EU-FAE` 提供 `CFast 3SE3` `35`pcs 相關分析結果.
  * [x] 協助 `EU-FAE` 提供 `Ericission 3SE USB` 相關測試結果圖.

# 2023-04-13
* 協助 `FW-RD Thomas` 提供 `Kontron` 相關資訊.
* 詢問 `MIS` 處理 `Microsoft` 認證問題.
* 架設 `PM-Davis` 將 `3TE6` 調整為 `high pull`, 並於平台做 `reboot` 測試環境.
* 協助新人處理 `3MR2-P` `ICE` 點位訊號焊接.
* 協助 `EU-FAE` 提供 `mSATA 3TG6-P` 相關分析結果.
* 協助 `EU-FAE` 提供 `CFast 3SE3` `35`pcs 相關分析結果.
* 協助 `EU-FAE` 提供 `Ericission 3SE USB` 相關測試結果圖.
* TODO
  * [x] 回報 `3TE6` 調整為 `high pull`, 並於平台做 `reboot` 測試結果.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `PM-Jack` 準備 `Winsystem` 母碟.
  * [x] 協助新人觀看 `3MG2-P S42` crystal 相關問題.
  * [x] 協助 `Sales-Jessica` 修改 `Ericission 3SE USB` 客訴報告.
  * [x] 提供 `EU-FAE` `3TE6` `S22620X1` 相關測試結果( `BurninTest` ).
  * [x] 協助 `EU-FAE` 詢問 `DLMC` tool release note 內容.

# 2023-04-14
* 回報 `3TE6` 調整為 `high pull`, 並於平台做 `reboot` 測試結果.
* 參與 `EU-FAE` 週會.
* 協助 `PM-Jack` 準備 `Winsystem` 母碟.
* 協助新人觀看 `3MG2-P S42` crystal 相關問題.
* 協助 `Sales-Jessica` 修改 `Ericission 3SE USB` 客訴報告.
* 提供 `EU-FAE` `3TE6` `S22620X1` 相關測試結果( `BurninTest` ).
* 協助 `EU-FAE` 詢問 `DLMC` tool release note 內容.
* TODO
  * [x] 將 `Kontron` 平台以及 `3TE6` 轉交給 `Sales-Nancy`.
  * [x] 整理 `CFast 3SE3` `35`pcs 相關分析過程報告.
  * [x] 協助 `Danny` 觀看 `innoAGE` 相關問題.
  * [x] 協助新人前往 `RMA` 維修零件.
  * [x] 詢問 `EU-FAE` 提供 `Vector` RAID 設定流程.

# 2023-04-17
* 將 `Kontron` 平台以及 `3TE6` 轉交給 `Sales-Nancy`.
* 整理 `CFast 3SE3` `35`pcs 相關分析過程報告.
* 協助 `Danny` 觀看 `innoAGE` 相關問題.
* 協助新人前往 `RMA` 維修零件.
* 詢問 `EU-FAE` 提供 `Vector` RAID 設定流程.
* TODO
  * [x] 與 `Kiwi` 討論 `CFast 3SE3` `35`pcs 相關分析過程報告.
  * [x] 測試 `APdate card solution / HAENEL` `CFast card 3SE3` 客訴案平台.
  * [x] 觀看 `CFast card 3SE3` 電路圖並焊接 `Reset` 訊號線.
  * [x] 追蹤 `SMI` 分析 `controller` 進度.
  * [x] 參與 `FAE-Team2` 週會.

# 2023-04-18
* 與 `Kiwi` 討論 `CFast 3SE3` `35`pcs 相關分析過程報告, 並將結果寄出.
* 測試 `APdate card solution / HAENEL` `CFast card 3SE3` 客訴案平台.
* 觀看 `CFast card 3SE3` 電路圖並焊接 `Reset` 訊號線, 經過幾次測試, 發現 `Reset` 電壓較低, 隨機性認碟, 經過討論後, 決定更換 `controller`.
* 追蹤 `SMI` 分析 `controller` 進度, 尚未回覆.
* 參與 `FAE-Team2` 週會.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `EU-FAE` 詢問 `DLMC` tool 相關 release note 細節.
  * [x] 協助新人觀看 `S42 3MG2-P` 無法認碟問題.
  * [x] 處理 `ASUS B360-F` 平台無法安裝 `OS` 於 `PCIE` 問題.
  * [x] 清潔實驗室平台.

# 2023-04-19
* 參與 `FAE` 週會.
* 協助 `EU-FAE` 詢問 `DLMC` tool 相關 release note 細節, 已經回覆給 `EU-FAE`.
* 協助新人觀看 `S42 3MG2-P` 無法認碟問題, 經由電路檢查, 懷疑是 `Crystal` 線路中的電阻有問題, 已申請領料更換.
* 處理 `ASUS B360-F` 平台無法安裝 `OS` 於 `PCIE` 問題, 後續發現為 `CSM` 內之 `PCIE` 欄位需改為 `Legacy`.
* 清潔實驗室平台.
* TODO
  * [x] 整理 `ERICSSON - USB EDC H 3SE3` 客訴處理流程, 並整理成 PPT.
  * [x] 協助新人觀看 `3TE6` `3TE7` 相關客訴案.
  * [x] 與 `Ben` & `Miller` & `Kiwi` 討論 `ERICSSON - USB EDC H 3SE3` 客訴處理.
  * [x] 前往 `RMA` 觀看維修紀錄.
  * [x] 與 `EU-FAE` 討論 `CFast 3SE3` `35` pcs 分析報告內容.
  * [x] 與 `EU-FAE` 討論 `APdata` `3SE3` 測試狀況.
  * [x] 將 `APdata` `3SE3` `00302` 送至 `RMA` 更換 `controller`.
  * [x] 參與 `ERICSSON - USB EDC H 3SE3` 客訴討論會議.

# 2023-04-20
* 整理 `ERICSSON - USB EDC H 3SE3` 客訴處理流程, 並整理成 PPT.
* 協助新人觀看 `3TE6` `3TE7` 相關客訴案.
* 與 `Ben` & `Miller` & `Kiwi` 討論 `ERICSSON - USB EDC H 3SE3` 客訴處理.
* 前往 `RMA` 觀看維修紀錄.
* 與 `EU-FAE` 討論 `CFast 3SE3` `35` pcs 分析報告內容.
* 與 `EU-FAE` 討論 `APdata` `3SE3` 測試狀況.
* 將 `APdata` `3SE3` `00302` 送至 `RMA` 更換 `controller`.
* 參與 `ERICSSON - USB EDC H 3SE3` 客訴討論會議.
* TODO
  * [x] 觀看 `APdata` `3SE3` `00302` 更換 `controller` 狀況.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 分析 `ERICSSON - USB EDC H 3SE3` `5` pcs 中, 發現一片異常品.
  * [x] 協助 `Kerry` 提供 `3TE6` 於 Intel 12代平台修改電阻之資料.
  * [x] 修改 `ERICSSON - USB EDC H 3SE3` `4` pcs FA report.
  * [x] 協助業務處理 `3TE6` `unpublish FW` 紀錄表.

# 2023-04-21
* 觀看 `APdata` `3SE3` `00302` 更換 `controller` 狀況, 換完之後, 異常現象消失.
* 參與 `EU-FAE` 週會.
* 分析 `ERICSSON - USB EDC H 3SE3` `5` pcs 中, 發現一片異常品, 後續發現為 `Crystal` 異常.
* 協助 `Kerry` 提供 `3TE6` 於 Intel 12代平台修改電阻之資料.
* 修改 `ERICSSON - USB EDC H 3SE3` `4` pcs FA report.
* 協助業務處理 `3TE6` `unpublish FW` 紀錄表.
* TODO
  * [x] 測試 `APdata` `3SE3` `20001` 更換 `電容` 狀況.
  * [x] 協助新人觀看客訴問題.
  * [x] 修改 `ERICSSON - USB EDC H 3SE3` `4` pcs FA report.
  * [x] 修改 `CFast 3SE3` `35` pcs FA report.
  * [x] 協助 `EU-FAE` 處理 `3TE7` 缺少之 `FW` bin file.
  * [x] 協助 `Leo` 觀看 `Linux` 執行 `Makefile` 相關問題.

# 2023-04-24
* 測試 `APdata` `3SE3` `20001` 更換 `電容` 狀況, 各測試 `30` 次.
  * `C6` 電容取下 -> Fail rate : `14/30 -> 46%`.
  * 更換 `controller` -> Fail rate : `0/30 -> 0%`.
  * `C6`, `C8` 電容增加 `10nF & 10nf` -> Fail rate : `6/30 -> 20%`.
  * `C6`, `C8` 電容增加 `10nF & 47nf` -> Fail rate : `6/30 -> 20%`.
* 協助新人觀看客訴問題.
* 修改 `ERICSSON - USB EDC H 3SE3` `4` pcs FA report, 並寄出給 `EU`.
* 修改 `CFast 3SE3` `35` pcs FA report.
* 協助 `EU-FAE` 處理 `3TE7` 缺少之 `FW` bin file.
* 協助 `Leo` 觀看 `Linux` 執行 `Makefile` 相關問題.
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 修改 `ERICSSON - USB EDC H 3SE3` `5` pcs FA report.
  * [x] 測試 `APdata` `3SE3` `20001` 加大 `電容` 狀況.
  * [x] 協助整理 `3TE7` 2020 客訴案狀況整理.
  * [x] 協助新人觀看 `Korea` `3MR2-P` wirte protect 問題.

# 2023-04-25
* 參與 `FAE-team2` 週會.
* 修改 `ERICSSON - USB EDC H 3SE3` `5` pcs FA report.
* 測試 `APdata` `3SE3` `20001` 加大 `電容` 狀況, 測試 `30` 次 `power on/off`, 只發生 `1` 次 Fail.
* 協助整理 `3TE7` 2020 客訴案狀況整理.
* 協助新人觀看 `Korea` `3MR2-P` wirte protect 問題.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 測試 `Vector` 設定 `RAID` 功能.
  * [x] 協助 `PM-Davis` & `FW-RD Adson` 測試 `V21118H2` 於 `AIOT` `ASBI-020` 平台.
  * [x] 與廠長 `James` 討論 `35`pcs `CFast card` FA report 內容.
  * [x] 撰寫 `3TE6 AIOT Platform Compatibility` 月會報告.
  * [x] 協助新人觀看 `3MG2-P` 執行 `Write Protect` 相關操作驗證.

# 2023-04-26
* 參與 `FAE` 週會.
* 測試 `Vector` 設定 `RAID` 功能.
* 協助 `PM-Davis` & `FW-RD Adson` 測試 `V21118H2` 於 `AIOT` `ASBI-020` 平台.
* 與廠長 `James` 討論 `35`pcs `CFast card` FA report 內容.
* 撰寫 `3TE6 AIOT Platform Compatibility` 月會報告.
* 協助新人觀看 `3MG2-P` 執行 `Write Protect` 相關操作驗證.
* TODO
  * [x] 協助 `PM-Davis` & `FW-RD Adson` 測試 `V21118H2` 於 `AIOT` `ASBI-020` 平台.
  * [x] 與 `EU-FAE` 討論 `35`pcs `CFast card` FA report 內容.
  * [x] 協助 `EU-Sales` 追蹤 `3TE7` 補上相關 `FW` bin file.
  * [x] 協助 `EU-FAE` 架設 `Fedora` 平台.

# 2023-04-27
* 協助 `PM-Davis` & `FW-RD Adson` 測試 `V21118H2` 於 `AIOT` `ASBI-020` 平台.
* 與 `EU-FAE` 討論 `35`pcs `CFast card` FA report 內容.
* 協助 `EU-Sales` 追蹤 `3TE7` 補上相關 `FW` bin file.
* 協助 `EU-FAE` 架設 `Fedora` 平台.
* TODO
  * [x] 參與 `FAE` 月會.
  * [x] 分享 `3TE6 AIOT Platform Compatibility issues​` 案例以及測試手法.
  * [x] 協助 `FW-RD Adson` 測試 `V21118H2` 於 `AIOT` `ASBI-020` 平台. 
  * [x] 協助 `PM-Davis` 確認 `AIOT` `ASBI-020` 平台 `CPU` 型號.
  * [x] 請教 `Jay` 關於 `SMI` device 開卡失敗的問題.
  * [x] 架設 `Fedora` 平台於 `3TE6` `1TB` & `256GB` device.
  * [x] 協助 `EU-Sales Patrik` 回答關於 `DLMC` tool 問題.
  * [x] 協助 `Sales-Jessica` 找尋 `FED221209005` 之 device.

# 2023-04-28
* 參與 `FAE` 月會.
* 分享 `3TE6 AIOT Platform Compatibility issues​` 案例以及測試手法.
* 協助 `FW-RD Adson` 測試 `V21118H2` 於 `AIOT` `ASBI-020` 平台, `TEST 4` 依然有問題. 
* 協助 `PM-Davis` 確認 `AIOT` `ASBI-020` 平台 `CPU` 型號.
* 請教 `Jay` 關於 `SMI` device 開卡失敗的問題.
  * 因 `SMI` 開卡包都是搭配容量去做設計, 不能不同容量混著用, 如須混著用, 須將 `Parameter` 內的 `Setting Capacity manually` 改為 `Default`, 即可正常開卡.
* 架設 `Fedora` 平台於 `3TE6` `1TB` & `256GB` device.
  * 架設過程中遇到黑屏問題, 後須將 `MB` 整個斷電後就可正常運行.
  * 修改 `Grub` 相關設定, 發生無法進入 `OS` 問題.
  * 懷疑是 `UUID` 衝突問題, 需要將 `2` pcs device 安裝完成後, 做進一步釐清.
* 協助 `EU-Sales Patrik` 回答關於 `DLMC` tool 問題.
* 協助 `Sales-Jessica` 找尋 `FED221209005` 之 device.
* TODO
  * [x] 寄出 `Vector` `RAID` 於 ` 3TG8-P` 測試結果.
  * [x] 協助 `EU-Sales Patrik` 回答關於 `DLMC` tool 問題, 並寄出.
  * [x] 觀看 `Fedora` 平台於 `3TE6` `1TB` & `256GB` device 之 `UUID`.
  * [x] 協助 `Rosch computer` 人員回答相關 `DLMC` tool 問題.
  * [x] 協助新人觀看 `SMI` device 相關問題.

# 2023-05-02
* 寄出 `Vector` `RAID` 於 ` 3TG8-P` 測試結果.
* 協助 `EU-Sales Patrik` 回答關於 `DLMC` tool 問題, 並寄出.
* 觀看 `Fedora` 平台於 `3TE6` `1TB` & `256GB` device 之 `UUID`.
* 協助 `Rosch computer` 人員回答相關 `DLMC` tool 問題.
* 協助新人觀看 `SMI` device 相關問題.
* TODO
  * [x] 協助 `EU Sales-Sylvia` 處理 `SIMOS` `35`pcs 相關客訴報告.
  * [x] 與 `EU-FAE` 討論相關客訴進度.
    * [x] `Rosch computer` DLMC tool 狀況.
    * [x] `Fedora` OS 認不到 `3TE6`.
  * [x] 協助 `EU-FAE` 測試 `3TE7` 相關 `DLMC v3.8.0` 功能.
    * [x] `DEM24-A28DK1KCADF`.
    * [x] `DEM24-B56DK1KCAQF`.

# 2023-05-03
* 協助 `EU Sales-Sylvia` 處理 `SIMOS` `35`pcs 相關客訴報告, 已寄出.
* 與 `EU-FAE` 討論相關客訴進度.
  * `Rosch computer` DLMC tool 狀況.
  * `Fedora` OS 認不到 `3TE6`.
* 協助 `EU-FAE` 測試 `3TE7` 相關 `DLMC v3.8.0` 功能.
  * `DLMC v3.8.0` 有增加 `controller` 辨識功能.
  * `DEM24-A28DK1KCADF` -> `已完成`.
  * `DEM24-B56DK1KCAQF` -> `等待 sample`.
* TODO
  * [x] 協助新人觀看 `innoworks` `3TE6` led 相關顯示問題.
  * [x] 協助 `EU-FAE` 測試 `Fedora` OS 認不到 `3TE6` 狀況.
  * [x] 協助 `Kiwi` 觀看 `dmesg` 相關操作.
  * [x] 協助新人操作 `mkmp` tool.
  * [x] 與 `EU-FAE` 更新客訴案進度.

# 2023-05-04
* 協助新人觀看 `innoworks` `3TE6` led 相關顯示問題.
* 協助 `EU-FAE` 測試 `Fedora` OS 認不到 `3TE6` 狀況, 發現透過相同開卡包, 修改 `SN`, 皆無法認碟.
* 協助 `Kiwi` 觀看 `dmesg` 相關操作.
* 協助新人操作 `mkmp` tool.
* 與 `EU-FAE` 更新客訴案進度.
* TODO
  * [x] 協助測試 `Fedora` OS 認不到 `3TE6` 狀況.
  * [x] 協助測試 `Fedora` OS 認 `4TG2-P` 狀況.
  * [x] 提供 `SIMOS` `35`pcs `CFast` card 測速結果.
  * [x] 協助新人測試於 `3TE7` 安裝 `Windows embedded`, 並執行 `DLMC`, 觀看是否可正常運作.
  * [x] 與 `EU-FAE` 更新客訴案進度.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `EU-FAE` 驗證 `3TE7` `256`GB DLMC 功能.

# 2023-05-05
* 協助測試 `Fedora` OS 認不到 `3TE6` 狀況, 並將結果提供給 `EU-FAE`.
  * 透過不同開卡包開卡( `V21118N1`, `V22620N1` ), 皆可認碟.(修改 `SN` 保留前四碼, 修改第 `7` 碼, 修改尾碼 ).
  * 透過相同開卡包開卡( `V21118N1`, `V22620N1` ), 皆不可認碟.(修改 `SN` 保留前四碼, 修改第 `7` 碼, 修改尾碼, `SN` -> `0000000000000`, `1111111111111` ).
* 協助測試 `Fedora` OS 認 `4TG2-P` 狀況, 結果只能辨識到 `1`pcs.
* 提供 `SIMOS` `35`pcs `CFast` card 測速結果.
* 協助新人測試於 `3TE7` 安裝 `Windows embedded`, 並執行 `DLMC`, 可正常運作.
* 與 `EU-FAE` 更新客訴案進度.
* 參與 `EU-FAE` 週會.
* 協助 `EU-FAE` 驗證 `3TE7` `256`GB DLMC 功能, 並錄製影片.
* TODO
  * [x] 協助 `EU-FAE` 討論 `SIMOS` `35`pcs `CFast` card FA report.
  * [x] 協助 `EU-FAE` 驗證 `DEM28-B56DK1GCAQF-Z71` `3TE7` `128GB` & `256GB` `DLMC` tool & `non Raid` `FW` bin file( `S22831` <-> `S21606` ). 
  * [x] 協助 `EU-FAE` 驗證 `Rosch Computer` `3TE7` `256GB` `DLMC` tool & `FW` bin file( `S22831` -> `S21606` ).
  * [x] 與 `EU-Sales Nancy` 討論 `DLMC` tool 進度.
  * [x] 協助 `PM-Jack` 測試 `39`pcs `3TE7`.
    * [x] `WD 128G` `10pcs`.
    * [x] `WD 256G` `10pcs`.
    * [x] `gTLC 128G` `10pcs`.
    * [x] `cTLC 128G` `9pcs`.

# 2023-05-08
* 協助 `EU-FAE` 討論 `SIMOS` `35`pcs `CFast` card FA report, 提供 `1`pcs 測速結果.
* 協助 `EU-FAE` 驗證 `DEM28-B56DK1GCAQF-Z71` `3TE7` `128GB` & `256GB` `DLMC` tool & `non Raid` `FW` bin file, 皆沒問題( `S22831` <-> `S21606` ). 
* 協助 `EU-FAE` 驗證 `Rosch Computer` `3TE7` `256GB` `DLMC` tool & `FW` bin file, 皆沒問題( `S22831` -> `S21606` ). 
* 與 `EU-Sales Nancy` 討論 `DLMC` tool 進度, 因 `3TE7` 發生 `SLC` & `TLC` 身份判斷問題, 故無法提供相關 `FW` bin file.
* 協助 `PM-Jack` 測試 `39`pcs `3TE7`, 分別測試 `初始化` & `初始化` & `Baking` `1` hr.
  * `WD 128G` `10pcs` -> `ok`.
  * `WD 256G` `10pcs` -> `ok`.
  * `gTLC 128G` `10pcs` -> `ok`.
  * `cTLC 128G` `9pcs` -> `Baking` `1` hr `2`pcs `Assert`.
* TODO
  * [x] 參與 `FAE-Team 2` 週會.
  * [x] 修復 `UART` 線針腳.
  * [x] 協助測試 `3TE6`, 分別測試 `初始化`.
    * [x] `WD` `10`pcs.
      * [x] `128`GB `1`PCS.
      * [x] `256`GB `3`PCS.
      * [x] `512`GB `4`PCS.
      * [x] `1`TB `2`PCS.
    * [x] `gTLC` `10`pcs.
      * [x] `P42` `128`GB `3`PCS.
      * [x] `P80` `128`GB `3`PCS.
      * [x] `P42` `1`TB `2`PCS.
      * [x] `P80` `2`TB `2`PCS.
    * [x] `cTLC` `10`pcs.
      * [x] `P42` `128`GB `1`PCS.
      * [x] `P42` `256`GB `1`PCS.
      * [x] `P80` `128`GB `1`PCS.
      * [x] `P42` `1`TB `3`PCS.
      * [x] `P80` `2`TB `4`PCS.
  * [x] 與 `PM-Davis` & `PM-Jack` 討論 `3TE6` 測試流程.
  * [x] 協助新人詢問 `SMI` 原廠相關問題.
  * [x] 協助 `FW RD-Adson` 處理 `3TE6` 於 `AIOT` 平台掉碟問題復現手法.

# 2023-05-09
* 參與 `FAE-Team 2` 週會.
* 修復 `UART` 線針腳.
* 協助測試 `3TE6`, 分別測試 `初始化`, 皆無遇到問題, 並將結果整理寄出.
  * `WD` `10`pcs.
    * `128`GB `1`PCS.
    * `256`GB `3`PCS.
    * `512`GB `4`PCS.
    * `1`TB `2`PCS.
  * `gTLC` `10`pcs.
    * `P42` `128`GB `3`PCS.
    * `P80` `128`GB `3`PCS.
    * `P42` `1`TB `2`PCS.
    * `P80` `2`TB `2`PCS.
  * `cTLC` `10`pcs.
    * `P42` `128`GB `1`PCS.
    * `P42` `256`GB `1`PCS.
    * `P80` `128`GB `1`PCS.
    * `P42` `1`TB `3`PCS.
    * `P80` `2`TB `4`PCS.
* 與 `PM-Davis` & `PM-Jack` 討論 `3TE6` 測試流程, 發現與 `3TE7` 現象不太相同, `3TE6` 會發生 `initalize` 資料消失, 需特別注意觀看是否會消失.
* 協助新人詢問 `SMI` 原廠相關問題.
* 協助 `FW RD-Adson` 處理 `3TE6` 於 `AIOT` 平台掉碟問題復現手法.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 與 `EU-FAE` 討論 `3TE7` DLMC 失敗問題.
  * [x] 協助 `EU-FAE` 處理 `Vector` 相關資訊提供.
  * [x] 重灌 `ubuntu` 平台.
  * [x] 協助 `FW RD-Allen` 了解 `3TE7` `DLMC` tool 相關問題.
  * [x] 協助 `Sales-MJ` 提供 `SATADOM` 電源相關問題.

# 2023-05-10
* 參與 `FAE` 週會.
* 與 `EU-FAE` 討論 `3TE7` DLMC 失敗問題.
* 協助 `EU-FAE` 處理 `Vector` 相關資訊提供.
* 重灌 `ubuntu` 平台.
* 協助 `FW RD-Allen` 了解 `3TE7` `DLMC` tool 相關問題.
  * 客戶因 `DLMC` tool 更新完成後, 會向 `device` 再次發送 `identify` 指令, 取得 device 相關資訊, 但因 device 已經進入 idle 狀態, 所以導致更新過程中, 需等待許多時間.
  * `SW RD-Allen` 會協助將第二次發送 `identify` 指令移除, 以及錯誤訊息, 解決等待時間過久問題.
* 協助 `Sales-MJ` 提供 `SATADOM` 電源相關問題.
* TODO
  * [x] 架設 `Vector` `RAID` 測試平台.
  * [x] 協助 `PM-Davis` 驗證 `3TE6` `V23501` 於 `AIOT` 平台 ( `ASBI 020`, `ASCI-120` ).
  * [x] 協助 `Sales-Jolie` 觀看 `3SE` `SMART` 內的 `Health` 資訊欄位.
  * [x] 協助 `Sales-Jolie` 觀看 `3TG6-P` 進入 `Loader` mode 問題.
  * [x] 協助 `EU-FAE` 觀看 `ATA Security command` 相關問題.
  * [x] 參與 `EU-FAE` 週會.

# 2023-05-11
* 架設 `Vector` `RAID` 測試平台.
* 協助 `PM-Davis` 驗證 `3TE6` `V23501` 於 `AIOT` 平台 ( `ASBI 020`, `ASCI-120` ).
  * `ASCI-120` -> 測試 `30` 次都沒遇到異常.
* 協助 `Sales-Jolie` 觀看 `3SE` `SMART` 內的 `Health` 資訊欄位.
* 協助 `Sales-Jolie` 觀看 `3TG6-P` 進入 `Loader` mode 問題.
* 協助 `EU-FAE` 觀看 `ATA Security command` 相關問題.
* 參與 `EU-FAE` 週會.
* TODO
  * [x] 協助 `PM-Davis` 驗證 `3TE6` `V23501` 於 `AIOT` 平台 ( `ASBI 020`, `ASCI-120` ), 測試 `50`次.
  * [x] 協助 `EU-Sales` 測試 `ATA Security Command`.
  * [x] 與 `SW-RD  Allen` & `FW-RD Thomas` 討論如何解除 `Freeze` 狀態, 以及如何 `set password`.
  * [x] 協助新人操作 `3TE7` FW 更新.

# 2023-05-12
* 協助 `PM-Davis` 驗證 `3TE6` `V23501` 於 `AIOT` 平台 ( `ASBI 020`, `ASCI-120` ), 測試 `50`次.
  * `ASBI 020` -> 第 `33` 次發生異常, 已將狀況回報給 `FW-RD Adson`.
* 協助 `EU-Sales` 測試 `ATA Security Command`, 並將其結果回報.
  * 於 `Windows` 平台內, 只要 `detect` 到 `disk` 都會將其 `mode` 設定為 `Freeze`( 無論 `disk` 上斷電 / OS suspend ).
  * 於 `Linux` 平台內, 第一次上電都會將 `disk` 都會將其 `mode` 設定為 `Freeze`, 重新上斷電後, `mode` 就會切為 `unFreeze`.
  * `Windows` 平台下 `ATA Security Command`, 需透過 `客製 FW` & `ATA CMD`( `command` -> `0xFA` ) 將 disk 解除 `Freeze` 狀態, 才可透過 `iSMART` 設定 `Security password`.
* 與 `SW-RD  Allen` & `FW-RD Thomas` 討論如何解除 `Freeze` 狀態, 以及如何 `set password`.
* 協助新人操作 `3TE7` FW 更新.
* TODO
  * [x] 協助 `EU-Sales` 回覆 `ATA Security Command` 相關問題.
  * [x] 協助 `EU-FAE` 提供 `Vector` RAID 測速相關資料.
  * [x] 協助新人觀看 `3MG2-P` & `3ME4` 電路相關問題.
  * [x] 與 `Miller` & `Kiwi` 討論 `ATA Security Command` 相關問題.
  * [x] 協助新人觀看 `DLMC` & `MKMP` tool 操作相關問題.

# 2023-05-15
* 協助 `EU-Sales` 回覆 `ATA Security Command` 相關問題.
* 協助 `EU-FAE` 提供 `Vector` RAID 測速相關資料.
* 協助新人觀看 `3MG2-P` & `3ME4` 電路相關問題.
* 與 `Miller` & `Kiwi` 討論 `ATA Security Command` 相關問題.
* 協助新人觀看 `DLMC` & `MKMP` tool 操作相關問題.
* TODO
  * [x] 參與 `FAE-Team2` 週會.
  * [x] 協助 `Kiwi` 觀看 `3ME2 Micro SD` card 開卡問題.
  * [x] 與 `EU-FAE` 討論相關客訴問題.
  * [x] 協助 `EU-FAE` 測試並整理 `Rosch computer` `Fedora` 同時放入 `2`pcs `3TE6` device 無法認碟問題.

# 2023-05-16
* 參與 `FAE-Team2` 週會.
* 協助 `Kiwi` 觀看 `3ME2 Micro SD` card 開卡問題.
* 與 `EU-FAE` 討論相關客訴問題.
* 協助 `EU-FAE` 測試並整理 `Rosch computer` `Fedora` 同時放入 `2`pcs `3TE6` device 無法認碟問題.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `EU-PM Alfie` 回覆 `TCG OPAL` 內 `biospba` image 如何取得.
  * [x] 協助 `Kiwi` 架設 `sedutil` 測試環境.
  * [x] 詢問 `FW-RD Allen` 關於 `CFast 3SE3` 於 `APdata` 平台訊號相關問題.

