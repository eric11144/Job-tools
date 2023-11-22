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
  * [x] 修改 `ansible` 相關安裝流程.
  * [x] 協助 `EU-FAE` 整理 `Fedora` 測試相關過程.

# 2023-05-17
* 參與 `FAE` 週會.
* 協助 `EU-PM Alfie` 回覆 `TCG OPAL` 內 `biospba` image 如何取得.
* 協助 `Kiwi` 架設 `sedutil` 測試環境.
* 詢問 `FW-RD Allen` 關於 `CFast 3SE3` 於 `APdata` 平台訊號相關問題.
* 修改 `ansible` 相關安裝流程.
* 協助 `EU-FAE` 整理 `Fedora` 測試相關過程.
* TODO
  * [x] 參與 `3TE7` 身份認證問題討論會議.
  * [x] 協助 `PM-Davis` 測試 `ASBI-020` `100` 次, 並錄製 `PCIe` analyzer.
  * [x] 修改 `ansible` 相關安裝流程.
  * [x] 協助新人觀看客訴案相關問題.
  * [x] 與 `EU-PM Alfie` 討論 `Winsystem` 母片準備相關問題.
  * [x] 協助新人更換 `Flash`.

# 2023-05-18
* 參與 `3TE7` 身份認證問題討論會議.
* 協助 `PM-Davis` 測試 `ASBI-020` `100` 次, 並錄製 `PCIe` analyzer.
* 修改 `ansible` 相關安裝流程, 處理 `install package version latest` 問題.
* 協助新人觀看客訴案相關問題.
* 與 `EU-PM Alfie` 討論 `Winsystem` 母片準備相關問題.
* 協助新人更換 `Flash`.
* TODO
  * [x] 協助新人觀看 `3TE6` LED 顯示問題.
  * [x] 協助新人開卡(`3TE7`).
  * [x] 協助 `PM-Becky` 準備及測試 `3TG6-P` pcie `DLMC` tool.
  * [x] 歸還 `Ericission` 客訴品, 共 `9`pcs 於 `EU-Sales Jessica`.
  * [x] 測試 `ansible` 相關安裝流程.

# 2023-05-19
* 協助新人觀看 `3TE6` LED 顯示問題.
* 協助新人開卡(`3TE7`).
* 協助 `PM-Becky` 準備及測試 `3TG6-P` pcie `DLMC` tool.
* 歸還 `Ericission` 客訴品, 共 `9`pcs 於 `EU-Sales Jessica`.
* 測試 `ansible` 相關安裝流程.
* TODO
  * [x] 協助 `EU-FAE` 測試 `Hanel` 平台, 以及錄製 `UART` log.
  * [x] 測試 `ansible` 相關流程(`中文輸入法`).
  * [x] 協助新人觀看 `3MG2-P` 相關客訴問題.
  * [x] 協助 `Danny` 觀看 `ubuntu` 操作相關問題.
  * [x] 將 `Hanel` 客訴品(`3SE3`)送於 `RMA` 做 `controller` 更換. 

# 2023-05-22
* 協助 `EU-FAE` 測試 `Hanel` 平台, 以及錄製 `UART` log.
* 測試 `ansible` 相關流程(`中文輸入法`).
* 協助新人觀看 `3MG2-P` 相關客訴問題.
* 協助 `Danny` 觀看 `ubuntu` 操作相關問題.
* 將 `Hanel` 客訴品(`3SE3`)送於 `RMA` 做 `controller` 更換. 
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 測試 `ansible` 相關安裝流程.
  * [x] 協助新人觀看 `3TE7` DLMC 問題, 以及 `3MG2-P` 客訴問題.
  * [x] 協助新人回答 `RRD` 發生情境.

# 2023-05-23
* 參與 `FAE-team2` 週會.
* 測試 `ansible` 相關安裝流程.
* 協助新人觀看 `3TE7` DLMC 問題, 以及 `3MG2-P` 客訴問題.
* 協助新人回答 `RRD` 發生情境.
  * device 放入資料, 一段時間未上電使用.
  * 在資料寫入過程中, 異常斷電.
  * 當資料寫入一段時間, 後續只有讀取未寫入時.
* TODO
  * [x] 協助 `PM-Jack` 處理 `3TE7` `AES` 造成之問題.
  * [x] 參與 `FAE` 週會.
  * [x] 從 `RMA` 取回 `Hanel` 客訴品, 並做相關測試.
  * [x] 與 `EU-PM Alfie` & `PM Jack` 討論 `Winsystem` 母片製作問題.
  * [x] 協助 `FAE-Nick` 提供 `USB-analyzer` tool.
  * [x] 將另外 `1`pcs `Hanel` 客訴品送置產線照 `X-ray`. 

# 2023-05-24
* 協助 `PM-Jack` 處理 `3TE7` `AES` 造成之問題.
* 參與 `FAE` 週會.
* 從 `RMA` 取回 `Hanel` 客訴品, 並做相關測試, 經過 `10`次上斷電測試, 並無看到相關異常.
* 與 `EU-PM Alfie` & `PM Jack` 討論 `Winsystem` 母片製作問題.
* 協助 `FAE-Nick` 提供 `USB-analyzer` tool.
* 將另外 `1`pcs `Hanel` 客訴品送置產線照 `X-ray`, 經由測試, 並無看到相關異常狀況. 
* TODO
  * [x] 協助 `PM-Jack` 製作 `Winsystem` 母片以及錄製相關影片.
  * [x] 協助 `PM-Jack` 處理 `3TE7` `AES` 問題.
  * [x] 測試 `ansible` 相關流程(`var environment`).
  * [x] 協助 `EU-Sales` 將 `SIMOS` 客訴品送至 `RMA`( `mSATA 3TG6-P`* 1pcs & `CFast card 3SE3`* 35pcs ).
  * [x] 轉交母片於 `PE-Peiwen`.

# 2023-05-25
* 協助 `PM-Jack` 製作 `Winsystem` 母片以及錄製相關影片.
* 協助 `PM-Jack` 處理 `3TE7` `AES` 問題.
* 測試 `ansible` 相關流程(`var environment`).
* 協助 `EU-Sales` 將 `SIMOS` 客訴品送至 `RMA`( `mSATA 3TG6-P`* 1pcs & `CFast card 3SE3`* 35pcs ).
* 轉交母片於 `PE-Peiwen`.
* TODO
  * [x] 協助 `Kiwi` 將 `Doby` 客訴品 `USB 3SE` 送至產線照 `X-ray`.
  * [x] 新增 `ansible` 相關流程( Add `gparted` `generate the file with right click` & update environment ).
  * [x] 協助新人測試 `3TE7` 關於 `S21606` & `S23505` DLMC 過程.
  * [x] 測試 `Hanel` 客訴案.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 與 `FW-RD Adson` 討論 `Fedora` 異常功能修改狀況.
  * [x] 與 `SW-RD` Allen 討論 `DLMC V3.9.0` 相關修改功能(`Get id table by 4 options`).

# 2023-05-26
* 協助 `Kiwi` 將 `Doby` 客訴品 `USB 3SE` 送至產線照 `X-ray`.
* 新增 `ansible` 相關流程( Add `gparted` `generate the file with right click` & update environment ).
* 協助新人測試 `3TE7` 關於 `S21606` & `S23505` DLMC 過程.
* 測試 `Hanel` 客訴案, 並無看到異常現象.
* 參與 `EU-FAE` 週會.
* 與 `FW-RD Adson` 討論 `Fedora` 異常功能修改狀況.
* 與 `SW-RD` Allen 討論 `DLMC V3.9.0` 相關修改功能(`Get id table by 4 options`).
* TODO
  * [x] 協助 `FW-RD Allen` 測試 `Avionics` 客訴案.
  * [x] 協助 `EU-FAE` 提供 `Vector` 相關測速結果.
  * [x] 教導 `工讀生` 測試 `3TE6` FW `V23505` 於 `AIOT` 平台認碟測試手法.
  * [x] 協助新人與 `FW-RD Adson` 討論 `SBC booting` 過慢問題.
  * [x] 協助 `EU-FAE` 撰寫 `DLMC V3.9.0` 相關操作流程以及差異.
  * [x] 與 `SW-RD` Allen 討論 `DLMC V3.9.0` 相關修改功能.
  * [x] 與 `EU-FAE YingXiang` & `PM-Jack` 討論 `AES` 開啟造成 `Disk` 無法被 access 相關問題及操作流程.

# 2023-05-29
* 協助 `FW-RD Allen` 測試 `Avionics` 客訴案.
* 協助 `EU-FAE` 提供 `Vector` 相關測速結果.
* 教導 `工讀生` 測試 `3TE6` FW `V23505` 於 `AIOT` 平台認碟測試手法.
* 協助新人與 `FW-RD Adson` 討論 `SBC booting` 過慢問題.
* 協助 `EU-FAE` 撰寫 `DLMC V3.9.0` 相關操作流程以及差異.
* 與 `SW-RD` Allen 討論 `DLMC V3.9.0` 相關修改功能.
* 與 `EU-FAE YingXiang` & `PM-Jack` 討論 `AES` 開啟造成 `Disk` 無法被 access 相關問題及操作流程.
* TODO
  * [x] 協助 `Sales-Walt` 提供 `Kontron` 客訴案相關報告.
  * [x] 參與 `FAE` team 實驗室搬遷.
  * [x] 與 `Kiwi` 討論目前客訴案進度.
  * [x] 協助新人詢問 `FW-RD Adson` 關於 UART log 顯示相關內容( `NvmeCreate:id:1 size:7f` & `SetfFid:7,DW11:0 sv:0` ).
  * [x] 處理 `Hanel` 客訴案之 `device` 焊接 `power sequence`.

# 2023-05-30
* 協助 `Sales-Walt` 提供 `Kontron` 客訴案相關報告.
* 參與 `FAE` team 實驗室搬遷.
* 與 `Kiwi` 討論目前客訴案進度.
* 協助新人詢問 `FW-RD Adson` 關於 UART log 顯示相關內容( `NvmeCreate:id:1 size:7f` & `SetfFid:7,DW11:0 sv:0` ).
  * `NvmeCreate:id:1 size:7f` -> 連到 `bridge`.
  * `SetfFid:7,DW11:0 sv:0` -> 連到 `host` 端 `bios`.
* 處理 `Hanel` 客訴案之 `device` 焊接 `power sequence`, 過程中發生短路問題, 導致 `device` 無法被讀取.
* TODO
  * [x] 轉送 `Hanel` 客訴案之 `device` 於 `RMA` 維修.
  * [x] 協助 `PE-Peiwen` 將 `mSATA` 開為 `ext4`.
  * [x] 協助 `FW-RD Allen` 架設 `FED230126002` `3TE7 SATA Slim` 測試環境.
  * [x] 協助新人觀看 `DLMC` tool 相關修改內容.
  * [x] 協助 `FAE` team 整理實驗室相關物品.
  * [x] 協助 `PM-Jack` 製作 `Winsystem` 相關母碟.

# 2023-05-31
* 轉送 `Hanel` 客訴案之 `device` 於 `RMA` 維修.
* 協助 `PE-Peiwen` 將 `mSATA` 開為 `ext4`.
* 協助 `FW-RD Allen` 架設 `FED230126002` `3TE7 SATA Slim` 測試環境.
* 協助新人觀看 `DLMC` tool 相關修改內容.
* 協助 `FAE` team 整理實驗室相關物品.
* 協助 `PM-Jack` 製作 `Winsystem` 相關母碟.
* TODO
  * [x] 協助 `William` 觀看安裝 `SATA analyzer` 相關問題.
  * [x] 量測 `Hanel` 客訴案之 `device`, 並將 `power sequence` 相關訊號線焊上.
  * [x] 請教 `Jay` 關於 `CFast 3SE3` 線路圖相關問題.
  * [x] 協助新人觀看 `EU-FAE` 對於 `DLMC` tool 相關問題, 以及釐清各個工具的差異性. 
  * [x] 透過 `FIO` 測試 `EU` `FED230126002` `3TE7 SATA Slim` 客訴案相關流程.

# 2023-06-01
* 協助 `William` 觀看安裝 `SATA analyzer` 相關問題.
* 量測 `Hanel` 客訴案之 `device`, 並將 `power sequence` 相關訊號線焊上.
* 請教 `Jay` 關於 `CFast 3SE3` 線路圖相關問題.
* 協助新人觀看 `EU-FAE` 對於 `DLMC` tool 相關問題, 以及釐清各個工具的差異性. 
* 透過 `FIO` 測試 `EU` `FED230126002` `3TE7 SATA Slim` 客訴案相關流程, 尚未看到相同異常現象.
* TODO
  * [x] 協助 `PM-Jack` 測試 `3TE7` 設定 `AES` password 後, 無法讀取檔案現象.
  * [x] 協助 `Danny` 觀看 `Linux` 相關問題.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助新人詢問關於 `DLMC` tool 操作手冊相關問題.
  * [x] 協助新人測試 `3ME4` 透過 `DLMC` tool 更新 `FW`( `L17606` -> `L20420` ).
  * [x] 協助新人回覆 `智邦` 提出相關之問題.
  * [x] 量測 `Hanel` 客訴案之 `device` `power sequence`, 並將其結果截圖.

# 2023-06-02
* 協助 `PM-Jack` 測試 `3TE7` 設定 `AES` password 後, 無法讀取檔案現象, 現象複製後, `FW RD` 回覆關於 `AES` unlocked 邏輯有錯誤, 並做後續修正.
* 協助 `Danny` 觀看 `Linux` 相關問題.
* 參與 `EU-FAE` 週會.
* 協助新人詢問關於 `DLMC` tool 操作手冊相關問題.
* 協助新人測試 `3ME4` 透過 `DLMC` tool 更新 `FW`( `L17606` -> `L20420` ).
* 協助新人回覆 `智邦` 提出相關之問題.
* 量測 `Hanel` 客訴案之 `device` `power sequence`, 並將其結果截圖, 後續發現 `RESET` 訊號不能量測 `CD` 點位, 故需重量.
* TODO
  * [x] 量測 `Hanel` 客訴案新退回之 `3pcs` `device`.
  * [x] 量測 `Hanel` 客訴案新退回之 `device`, 並將 `power sequence` 相關訊號線焊上.
  * [x] 協助 `EP-Peiwen` 處理 `USB` type( `ext3 128K` ).
  * [x] 協助 `EU-FAE Jason` 提供 `3TE6-DEM28-02TDD1KCAQF` 相關 `FW` bin file.
  * [x] 協助新人 setting Linux OS 於 `3TE6` device.
  * [x] 教導新人操作 `COPY` mechine.
  * [x] 與新人討論 `DLMC` tool 手冊, 並將其文件提供給 `EU-FAE`.
  * [x] 領取 `SMI` 送分析知客訴品.
  * [x] 協助 `EU-Sales` 回覆關於 `SIMOS` `CFast` 35pcs 之客訴問題.

# 2023-06-05
* 量測 `Hanel` 客訴案新退回之 `3pcs` `device`.
* 量測 `Hanel` 客訴案新退回之 `device`, 並將 `power sequence` 相關訊號線焊上.
* 協助 `EP-Peiwen` 處理 `USB` type( `ext3 128K` ).
* 協助 `EU-FAE Jason` 提供 `3TE6-DEM28-02TDD1KCAQF` 相關 `FW` bin file.
* 協助新人 setting Linux OS 於 `3TE6` device.
* 教導新人操作 `COPY` mechine.
* 與新人討論 `DLMC` tool 手冊, 並將其文件提供給 `EU-FAE`.
* 領取 `SMI` 送分析知客訴品, 後續發現產品寄錯.
* 協助 `EU-Sales` 回覆關於 `SIMOS` `CFast` 35pcs 之客訴問題.
* TODO 
  * [x] 量測 `Hanel` 客訴案新退回之 `device` `power sequence`.
  * [x] 協助 `EU-FAE` 測試 `3TE6` `V2262001` 關於 `Fedora` `NSID` 重複任不到碟之問題.
  * [x] 參加 `FAE-team2` 週會.
  * [x] 協助 `Kiwi` 觀看 `喬鼎` `3ME4` 客訴品.
  * [x] 協助新人觀看測試平台相關問題.
  * [x] 處理 `Ericssion` `USB` 送至 `SMI` 分析品領回.
  * [x] 協助新人送修 `CPU`.

# 2023-06-06
* 量測 `Hanel` 客訴案新退回之 `device` `power sequence`.
* 協助 `EU-FAE` 測試 `3TE6` `V2262001` 關於 `Fedora` `NSID` 重複任不到碟之問題.
* 參加 `FAE-team2` 週會.
* 協助 `Kiwi` 觀看 `喬鼎` `3ME4` 客訴品, 已請業務幫忙詢問相關問題.
* 協助新人觀看測試平台相關問題, 後續發現為 `CPU` 問題.
* 處理 `Ericssion` `USB` 送至 `SMI` 分析品領回.
* 協助新人送修 `CPU`.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `PM-Jack` 處理 `EU` `Winsystem` 母片製作 `2` pcs.
  * [x] 錄製 `喬鼎` `3ME4` 客訴品 `Elog`.
  * [x] 提供送修 `CPU` 以及相關風扇. 
  * [x] 協助 `EU-FAE` 測試 `3TE6` `V22620Z1` 於 `Fedora` OS, 是否解決 `NSID` 相同造成無法辨識問題.
  * [x] 測試實驗平台異常狀況.
  * [x] 協助新人 setting `Ubuntu 22.04` 於 `3TE6` `4` pcs.
  * [x] 協助新人詢問 `FW-RD Adson` 關於 `3TE6` `DLMC` `action commit` 問題.
  * [x] 協助新人將 `3TE6` 測試相關結果影片上傳至 `Google Drive`.

# 2023-06-07
* 參與 `FAE` 週會.
* 協助 `PM-Jack` 處理 `EU` `Winsystem` 母片製作 `2` pcs, 並轉交給 `EP` 相關人員.
* 錄製 `喬鼎` `3ME4` 客訴品 `Elog`.
* 提供送修 `CPU` 以及相關風扇. 
* 協助 `EU-FAE` 測試 `3TE6` `V22620Z1` 於 `Fedora` OS, 是否解決 `NSID` 相同造成無法辨識問題, 經由測試, 並無看到相關問題, 已將結果整理並提供給 `EU-FAE`.
* 測試實驗平台異常狀況, 後續發現為主機板供電於 `CPU` 有異常, 另外一片測試平台為 `CPU` 不支援 `內顯`, 需額外裝顯示卡.
* 協助新人 setting `Ubuntu 22.04` 於 `3TE6` `4` pcs.
* 協助新人詢問 `FW-RD Adson` 關於 `3TE6` `DLMC` `action commit` 問題, 經由討論後, 只能對 `device` 下 `action commit` `0` & `1`.
* 協助新人將 `3TE6` 測試相關結果影片上傳至 `Google Drive`. 
* TODO
  * [x] 建立 `TTS` 請 `FW-RD` 協助觀看 `喬鼎` `3ME4` 客訴品 `Elog`.
  * [x] 架設以及撰寫 `3TE7` 每次寫入 `4GB` file 測試環境, 觀看是否可看到與客戶相同之問題.
  * [x] 於 `RMA` 取回 `Hanel` 客訴案之 `device`, 並透過 `copy mechine` 於客戶平台測試.
  * [x] 協助新人使用 `copy mechine` 於 `3TE6`.
  * [x] 協助新人執行 `3TE7` `Burnintest`.
  * [ ] 協助 `Kiwi` 更新 `3TG8-P` FW version.

# 2023-06-08
* 建立 `TTS` 請 `FW-RD` 協助觀看 `喬鼎` `3ME4` 客訴品 `Elog`.
* 架設以及撰寫 `3TE7` 每次寫入 `4GB` file 測試環境, 觀看是否可看到與客戶相同之問題.
* 於 `RMA` 取回 `Hanel` 客訴案之 `device`, 並透過 `copy mechine` 於客戶平台測試, 測試上斷 `10`次, 並無看到相同問題.
* 協助新人使用 `copy mechine` 於 `3TE6`.
* 協助新人執行 `3TE7` `Burnintest`.
* TODO  
  * [x] 測試 `喬鼎` `3ME4` 客訴品, 看是否與客戶遇到之問題相同.
  * [x] 測試 `3TE7` 每次寫入 `4GB` file, 觀看是否可看到與客戶相同之問題.
  * [x] 協助 `Danny` 觀看 `ubuntu 16.04` kernel 更新問題.
  * [x] 參與 `EU-FAE` 週會.

# 2023-06-09
* 測試 `喬鼎` `3ME4` 客訴品, 看是否與客戶遇到之問題相同, 經由測試開關機 `10` 次, 皆無看到問題, 已錄製影片於 `Sales-Leslie`.
* 測試 `3TE7` 每次寫入 `4GB` file, 觀看是否可看到與客戶相同之問題, 全碟寫滿放置一段時間後, `disk` 進入 `Loader mode`.
* 協助 `Danny` 觀看 `ubuntu 16.04` kernel 更新問題.
* 參與 `EU-FAE` 週會.
* TODO
  * [x] 錄製 `3TE7` 每次寫入 `4GB` file `UART` log.
  * [x] 協助 `Kiwi` 更新 `3TG8-P` FW version.
  * [x] 測試並撰寫 `3TG8-P` FW update 操作手冊.
  * [x] 協助 `EU` 詢問 `Neousys-Tech` 遇到之客訴案測試手法.
  * [x] 向 `Sales-Leslie` 回報 `3ME4` 測試狀況.
  * [x] 協助 `Danny` 查找 `sd card` controller.

# 2023-06-12
* 錄製 `3TE7` 每次寫入 `4GB` file `UART` log.
* 協助 `Kiwi` 更新 `3TG8-P` FW version.
* 測試並撰寫 `3TG8-P` FW update 操作手冊.
* 協助 `EU` 詢問 `Neousys-Tech` 遇到之客訴案測試手法.
* 向 `Sales-Leslie` 回報 `3ME4` 測試狀況.
* 協助 `Danny` 查找 `sd card` controller.
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 觀看 `THALES` 提供測試 `3TE7 SATA Slim` 之 shell script.
  * [x] 詢問原廠 `MK` 關於 `Hanel` 平台認碟相關問題.
  * [x] 觀看 `GLYN` 客訴品 `SATADOM 3ME3` 狀況.
  * [x] 幫忙 `EU-FAE` 詢問 `FW-RD Adson` 關於 `Fedora` 平台 FW 問題.

# 2023-06-13
* 參與 `FAE-team2` 週會.
* 觀看 `THALES` 提供測試 `3TE7 SATA Slim` 之 shell script, 但後續發生平台問題, 導致無法驗證, 已經平台送修.
* 詢問原廠 `MK` 關於 `Hanel` 平台認碟相關問題.
* 觀看 `GLYN` 客訴品 `SATADOM 3ME3` 狀況.
* 幫忙 `EU-FAE` 詢問 `FW-RD Adson` 關於 `Fedora` 平台 FW 問題.
* TODO
  * [x] 回報 `喬鼎` `3ME4` 測試狀況, 並將 `device` 轉交於業務.
  * [x] 測試 `THALES` 提供測試 `3TE7 SATA Slim` 之 shell script 於客戶平台.
  * [x] 處理 `Hanel` 客訴案, 須將客戶平台與 `device` 送於原廠分析, 並整理相關實驗過程.
  * [x] 詢問 `FW-RD` 關於 `Hanel` 客訴案之 `FW` 相關測試.
  * [x] 統整採購清單.
  * [x] 協助新人處理 `mSATA` 轉接相關問題.

# 2023-06-14
* 回報 `喬鼎` `3ME4` 測試狀況, 並將 `device` 轉交於業務.
* 測試 `THALES` 提供測試 `3TE7 SATA Slim` 之 shell script 於客戶平台, 但因平台發生問題, 無法開機進行驗證, 故將平台送修, 準備 `Samsung 970` & `M.2 3TE7` 來做實驗對照組.
* 處理 `Hanel` 客訴案, 須將客戶平台與 `device` 送於原廠分析, 並整理相關實驗過程.
* 詢問 `FW-RD` 關於 `Hanel` 客訴案之 `FW` 相關測試, 並將其整理提供給原廠人員.
* 統整採購清單.
* 協助新人處理 `mSATA` 轉接相關問題.
* TODO
  * [x] 準備 `THALES` 客訴案所需之 `2`pcs `3TE7 BiCS5` device, 並執行客戶提供之 `script`.
  * [x] 整理 `THALES` 客訴案所做的實驗過程, 並參與 `EU` 討論會議.
  * [x] 與 `Jason` 討論 `Vector` RAID 測試結果.
  * [x] 協助新人處理 `Redhat` 安裝, `Windows IOT` 安裝於 `3TE6` & `AIOT` 平台, 以及回覆相關問題.
  * [x] 統整採購清單.
  * [x] 前往 `RMA` 取回送修之 `3TE7`, 並重開卡.
  * [x] 協助 `Jay` 查找提供給 `超恩` 之 `FW` bin file.

# 2023-06-15
* 準備 `THALES` 客訴案所需之 `2`pcs `3TE7 BiCS5` device, 並執行客戶提供之 `script`.
* 整理 `THALES` 客訴案所做的實驗過程, 並參與 `EU` 討論會議, 後續須將測試流程整理出來.
* 與 `Jason` 討論 `Vector` RAID 測試結果, 後續發現 `Write` 測試參數以及 `RAID` capacity 需做修改, 並重起測試.
* 協助新人處理 `Redhat` 安裝, `Windows IOT` 安裝於 `3TE6` & `AIOT` 平台, 以及回覆相關問題.
* 統整採購清單.
* 前往 `RMA` 取回送修之 `3TE7`, 並重開卡.
* 協助 `Jay` 查找提供給 `超恩` 之 `FW` bin file.
* TODO
  * [x] 觀看 `Vector` RAID 測試結果.
  * [x] 觀看 `THALES` 客訴案於兩個測試平台狀況.
  * [x] 協助 `EU` 處理 `Ericssion` USB 客訴案.
  * [x] 參與 `FAE-team2` 績效討論會議.
  * [x] 協助新人處理 `CFast` & `AIOT` 平台客訴測試案.
  * [x] 填寫績效考核內容.

# 2023-06-16
* 觀看 `Vector` RAID 測試結果, 後續 `EU-FAE` 回報客戶測試參數需進行調整, 經過調整後, 已開始測試.
  * `Initialzation Method` -> `Quick init`.
  * `Capacity` -> `14495514` MB.
  * `Disk Cache Policy` -> `Enable`.
  * `Select All` -> Select.
* 觀看 `THALES` 客訴案於兩個測試平台狀況, 目前皆正常.
* 協助 `EU` 處理 `Ericssion` USB 客訴案, 可正常辨識, `SMART` 已撈取, 並請 `SMI` 相關人員協助照 `X-ray`( `Controller`, `Flash`, `Controller` ).
* 參與 `FAE-team2` 績效討論會議.
* 協助新人處理 `CFast` & `AIOT` 平台客訴測試案.
* 填寫績效考核內容.
* TODO
  * [x] 觀看 `Vector` RAID 測試結果.
  * [x] 前往 `RMA` 取回 `Ericssion` 送回之 `device`, 與相關人員討論 `Connector` 問題, 並整理初步分析相關結果.
  * [x] 觀看 `THALES` 客訴案於兩個測試平台狀況.
  * [x] 持續追蹤 `MK` 原廠是否可以協助分析 `Hanel` 平台.
  * [x] 協助 `Sales-Jolie` 透過 `cmd-diskpart` 將 `3TG6-P` 做 `Initialize format`.
  * [x] 協助新人錄製 `3SE2-P` 相關測試影片.

# 2023-06-19
* 觀看 `Vector` RAID 測試結果.
* 前往 `RMA` 取回 `Ericssion` 送回之 `device`, 與相關人員討論 `Connector` 問題, 並整理初步分析相關結果.
* 觀看 `THALES` 客訴案於兩個測試平台狀況.
* 持續追蹤 `MK` 原廠是否可以協助分析 `Hanel` 平台.
* 協助 `Sales-Jolie` 透過 `cmd-diskpart` 將 `3TG6-P` 做 `Initialize format`.
* 協助新人錄製 `3SE2-P` 相關測試影片.
* TODO  
  * [x] 回覆原廠 `MK` 關於 `Hanel` 平台相關問題.
  * [x] 協助 `福哥` 將 `Neousys` 平台取回, 並送回原廠更換 `CPU`.
  * [x] 參與 `FAE-team2` 週會.
  * [x] 協助新人處理 `3SE2-P` `JTAG` 訊號線.
  * [x] 觀看 `THALES` 客訴案於兩個測試平台狀況.
  * [x] 協助 `EU-FAE` 回報 `Vector` RAID 測試結果.
  * [x] 與 `EU-FAE` & `EU-PM` 討論 `Ericssion` USB 分析進度.
  * [x] 協助組內處理採購清單.

# 2023-06-20
* 回覆原廠 `MK` 關於 `Hanel` 平台相關問題.
* 協助 `福哥` 將 `Neousys` 平台取回, 並送回原廠更換 `CPU`.
* 參與 `FAE-team2` 週會.
* 協助新人處理 `3SE2-P` `JTAG` 訊號線.
* 觀看 `THALES` 客訴案於兩個測試平台狀況, 尚未看到異常.
* 協助 `EU-FAE` 回報 `Vector` RAID 測試結果.
* 與 `EU-FAE` & `EU-PM` 討論 `Ericssion` USB 分析進度.
* 協助組內處理採購清單.
* TODO
  * [x] 撰寫 `Ericssion` USB 分析報告.
  * [x] 協助 `EU-PM` 詢問 `Ericssion` USB `date code` & `controller date code`.
  * [x] 回報 `EU-Sales Sylvain` 關於 `THALES` 客訴案於兩個測試平台狀況.
  * [x] 協助新人測試 `3TE6` FW `V20B09` & `V22620` 於 `ASCI-020` 平台.
  * [x] 協助新人處理 `3MG2-P` 焊接 `EYES` 點位訊號線.
  * [x] 參與 `FAE` 週會.
  * [x] 與 `MK-Vector` 討論 `Hanel` 平台分析狀況.
  * [x] 協助 `EU-FAE` 處理 `Rosch computer` 關於 `Fedora` 平台 `3TE6` `2` pcs 同時插上辨識問題.
  * [x] 請教 `Jay` 關於 `WinPE` & `WinIOT` image 相關問題.

# 2023-06-21
* 撰寫 `Ericssion` USB 分析報告, 已寄出一版, 事後補上 `BurninTest`.
* 協助 `EU-PM` 詢問 `Ericssion` USB `date code` & `controller date code`, 詢問完 `Toby`, 已將結果提供.
* 回報 `EU-Sales Sylvain` 關於 `THALES` 客訴案於兩個測試平台狀況, 皆無看到異常, 目前等待平台維修回來.
* 協助新人測試 `3TE6` FW `V20B09` & `V22620` 於 `ASCI-020` 平台, 發現為 `warm boot` 造成 `SW reset` & `HW reset` 相沖問題.
* 協助新人處理 `3MG2-P` 焊接 `EYES` 點位訊號線.
* 參與 `FAE` 週會.
* 與 `MK-Vector` 討論 `Hanel` 平台分析狀況, 討論結果為無法分析平台訊號, 對於 `MK` 來說是平台訊號過弱, 於一般平台測試是沒問題的.
* 協助 `EU-FAE` 處理 `Rosch computer` 關於 `Fedora` 平台 `3TE6` `2` pcs 同時插上辨識問題, 已將結果錄製影片, 並將 `device` 轉接於業助送回.
* 請教 `Jay` 關於 `WinPE` & `WinIOT` image 相關問題.
* TODO
  * [x] 借出 `3TE7` `2.5 SATA` & `SATA Slim` & `mSATA` 3 種 type.
  * [x] 補上 `BurninTest` 結果圖於 `Ericssion` USB 分析報告.
  * [x] 整理歷年客訴案件處理狀況, 以及開發相關軟體清單.
  * [x] 協助 `Sales-Jamie` 回答關於 `宸曜` 平台測試狀況.
  * [x] 參與 `FAE` 月會.
  * [x] 協助新人詢問 `RD-Ray` 處理 `3TE7` FW Bin 調整為 `SATA 1.5G`.
  * [x] 協助新人測試 `3TE6` FW `V22620X1` & `V22620` 於 `ASCI-020` 平台.

# 2023-06-26
* 借出 `3TE7` `2.5 SATA` & `SATA Slim` & `mSATA` 3 種 type.
* 補上 `BurninTest` 結果圖於 `Ericssion` USB 分析報告.
* 整理歷年客訴案件處理狀況, 以及開發相關軟體清單.
* 協助 `Sales-Jamie` 回答關於 `宸曜` 平台測試狀況.
* 參與 `FAE` 月會.
* 協助新人詢問 `RD-Ray` 處理 `3TE7` FW Bin 調整為 `SATA 1.5G`.
* 協助新人測試 `3TE6` FW `V22620X1` & `V22620` 於 `ASCI-020` 平台.
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 整理每筆客訴案進度.
  * [x] 與 `EU-FAE` 討論 `Ericssion` `EDC USB` 相關測試內容, 以及提供轉板 `PIN` 針規格.
  * [x] 與 `HW-RD` 討論如何錄製 `CFast 3SE3` SATA analyzer, 以及相關訊號線如何製作.
  * [x] 協助新人觀看 `DLMC` tool 相關執行問題, 以及測試 `V3.9.0` 於 `Windows 7` 執行狀況.
  * [x] 測試 `Ericssion` `EDC USB` 第 `2` pcs 相關測試, 並將 device 送至 `RMA` 照 `X-ray`.

# 2023-06-27
* 參與 `FAE-team2` 週會.
* 整理每筆客訴案進度.
* 與 `EU-FAE` 討論 `Ericssion` `EDC USB` 相關測試內容, 以及提供轉板 `PIN` 針規格.
* 與 `HW-RD` 討論如何錄製 `CFast 3SE3` SATA analyzer, 以及相關訊號線如何製作.
* 協助新人觀看 `DLMC` tool 相關執行問題, 以及測試 `V3.9.0` 於 `Windows 7` 執行狀況.
* 測試 `Ericssion` `EDC USB` 第 `2` pcs 相關測試, 並將 device 送至 `RMA` 照 `X-ray`.
* TODO
  * [x] 協助新人製作 `Auto DLMC` tool for `3TE7`.
  * [x] 整理 `Ericssion` `EDC USB` 第 `2` pcs 相關測試結果, 以及 `X-ray` 照片.
  * [x] 參與 `FAE` 週會.
  * [x] 與 `EU-Sales Jessica` 討論 `Ericssion` `EDC USB` 相關測試內容.
  * [x] 詢問 `宸曜` 平台維修狀態. 
  * [x] 架設 `SATA analyzer` 錄製 `Hanel` 平台訊號過程.

# 2023-06-28
* 協助新人製作 `Auto DLMC` tool for `3TE7`.
* 整理 `Ericssion` `EDC USB` 第 `2` pcs 相關測試結果, 以及 `X-ray` 照片.
* 參與 `FAE` 週會.
* 與 `EU-Sales Jessica` 討論 `Ericssion` `EDC USB` 相關測試內容, 並將測試結果寫入報告內提供出來.
* 詢問 `宸曜` 平台維修狀態, 目前在業務手中, 尚未寄回.
* 架設 `SATA analyzer` 錄製 `Hanel` 平台訊號過程, 發現訊號卡在 `COMMON RESET`, 無法往下執行.
*  TODO
   * [x] 協助新人製作 `Auto DLMC` tool for `3TE7`.
   * [x] 與 `Miller` 討論關於採購相關事項.
   * [x] 協助新人準備測試平台於 `VN-Sales Lam`.
   * [x] 協助 `Kiwi` 測試 `3TE7 SATA Slim` FW 更新於 `Windows 10` ( `S21606 nonRaid` <-> `S23505 nonRaid` ).
   * [x] 取得 `3TE7 SATA Slim` device, 將 FW 更換為 `S22831`, 再執行 `THALES` 客訴案之 `Shell script`.
   * [x] 架設 `SATA analyzer` 錄製 `Hanel` 平台訊號過程, 觀看 `COMMON RESET` 動作內容.
   * [x] 與 `Kiwi` 討論 `EU` 客訴案( `FEC230209011` ) 測試內容, 並討論後續說法.

# 2023-06-29
* 協助新人製作 `Auto DLMC` tool for `3TE7`.
* 與 `Miller` 討論關於採購相關事項.
* 協助新人準備測試平台於 `VN-Sales Lam`.
* 協助 `Kiwi` 測試 `3TE7 SATA Slim` FW 更新於 `Windows 10` ( `S21606 nonRaid` <-> `S23505 nonRaid` ).
* 取得 `3TE7 SATA Slim` device, 將 FW 更換為 `S22831`, 再執行 `THALES` 客訴案之 `Shell script`.
* 架設 `SATA analyzer` 錄製 `Hanel` 平台訊號過程, 觀看 `COMMON RESET` 動作內容.
* 與 `Kiwi` 討論 `EU` 客訴案( `FEC230209011` ) 測試內容, 並討論後續說法.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `EU-Sales` 處理 `FEC230606009` `SATADOM` 送至 `RMA`.
  * [x] 協助 `EU` 討論 `Hanel` 出貨測試流程.
  * [x] 協助新人測試 `一對多 DLMC tool`.
  * [x] 協助 `EU-FAE` 回覆 `4TG2-P` 關於 `TS1` 訊號修改.

# 2023-06-30
* 參與 `EU-FAE` 週會.
* 協助 `EU-Sales` 處理 `FEC230606009` `SATADOM` 送至 `RMA`.
* 協助 `EU` 討論 `Hanel` 出貨測試流程.
* 協助新人測試 `一對多 DLMC tool`.
  * `3TE7 P42 128GB` `S21606` -> `S23505`.
  * `3TE7 P42 256GB` `S21606` -> `S23505`.
  * `3TE7 P42 512GB` `S22831` -> `S23505`.
* 協助 `EU-FAE` 回覆 `4TG2-P` 關於 `TS1` 訊號修改.
* TODO
  * [x] 協助 `EU-Sales` 回覆 `4TG2-P` 相關問題.
  * [x] 協助新人修改 `一對多 DLMC tool`.
  * [x] 協助 `Sales-Jamie` 詢問 `Xavier` 平台維修進度.
  * [x] 詢問 `4TG2-P` `FW-RD` 關於 `DGM28-01TDP1KCAEF` 使用之解決 `FW` 是否可以運行於 `DGM28-01TDP1KCCEF`.
  * [x] 參與 `PCIe Gen4` 相關客訴討論會議.
  * [x] 觀察 `Thales` 測試狀況.

# 2023-07-03
* 協助 `EU-Sales` 回覆 `4TG2-P` 相關問題.
* 協助新人修改 `一對多 DLMC tool`.
 * 新增換行.
 * 執行過程相關文字呈現.
* 協助 `Sales-Jamie` 詢問 `Xavier` 平台維修進度, 目前尚未回覆.
* 詢問 `4TG2-P` `FW-RD` 關於 `DGM28-01TDP1KCAEF` 使用之解決 `FW` 是否可以運行於 `DGM28-01TDP1KCCEF`.
* 參與 `PCIe Gen4` 相關客訴討論會議.
* 觀察 `Thales` 測試狀況, 目前已將碟寫滿, 並將其重新啟動, 並未看到相關問題.
* TODO
   * [x] 觀察 `Thales` 測試狀況.
   * [x] 觀察 `Xavier` 測試狀況.
   * [x] 協助 `Kiwi` 分析 `Simms International` `3ME2` 客訴問題.
   * [x] 協助 `FW` 工讀生處理如何進入 `bios` `shell mode`.
   * [x] 詢問 `Sales-Leslie` 關於 `喬鼎` 測試狀況.
   * [x] 與 `EU-FAE Jason` 討論 `Ericsson` 關於 `EDC USB` 客訴報告內容.
   * [x] 參與 `FAE team2` 週會.

# 2023-07-04
* 觀察 `Thales` 測試狀況, 皆正常.
* 觀察 `Xavier` 測試狀況, 皆正常.
* 協助 `Kiwi` 分析 `Simms International` `3ME2` 客訴問題, 並錄製 `UART` log.
* 協助 `FW` 工讀生處理如何進入 `bios` `shell mode`.
* 詢問 `Sales-Leslie` 關於 `喬鼎` 測試狀況.
* 與 `EU-FAE Jason` 討論 `Ericsson` 關於 `EDC USB` 客訴報告內容.
* 參與 `FAE team2` 週會.
 * TODO
   * [x] 取得借出 `device`( `Thales` ), 並重新測試.
   * [x] 詢問 `FW-RD` 關於 `Simms International` `3ME2` 客訴問題.
   * [x] 協助新人觀看 `達明機器人` 客訴報告.
   * [x] 協助新人架設 `Korea` AMD 平台( 透過 `RS232` to `USB` ).
   * [x] 撰寫 `Ericsson` `EDC USB` 客訴報告.
   * [x] 參與 `FAE` 週會.

# 2023-07-05
* 取得借出 `device`( `Thales` ), 並重新測試.
* 詢問 `FW-RD` 關於 `Simms International` `3ME2` 客訴問題.
* 協助新人觀看 `達明機器人` 客訴報告.
* 協助新人架設 `Korea` AMD 平台( 透過 `RS232` to `USB` ).
* 撰寫 `Ericsson` `EDC USB` 客訴報告.
* 參與 `FAE` 週會.
* TODO
   * [x] 觀察 `Thales` 測試狀況.
   * [x] 觀察 `Xavier` 測試狀況.
   * [x] 協助 `FAE-Leo` 架設 `Carmera` 相關環境.
   * [x] 協助　`EU-Sales` 照射 `X-ray` 處理 `Ericsson` `EDC USB` connector 孔徑問題.
   * [x] 協助新人回覆 `innoworks` 相關客訴問題. 
   * [x] 協助新人觀看 `達明機器人` FA report.
   * [x] 協助 `FAE-Danny` 處理 `3TG6-P` 開卡問題.
   * [x] 發信詢問 `Simms International` 相關測試手法問題.

# 2023-07-06
* 觀察 `Thales` 測試狀況, 測試過程中發現平台重新開機, 目前加入 `systemctl` 相關 log 來做觀察.
* 觀察 `Xavier` 測試狀況, 目前正常.
* 協助 `FAE-Leo` 架設 `Carmera` 相關環境, 以及燒錄 `image`.
* 協助　`EU-Sales` 照射 `X-ray` 處理 `Ericsson` `EDC USB` connector 孔徑問題, 九孔上下孔徑皆超過 `0.532mm`, 並將結果整理寄出.
* 協助新人回覆 `innoworks` 相關客訴問題. 
* 協助新人觀看 `達明機器人` FA report.
* 協助 `FAE-Danny` 處理 `3TG6-P` 開卡問題.
* 發信詢問 `Simms International` 相關測試手法問題.
* TODO
  * [x] 觀察 `Thales` 測試狀況.
  * [x] 觀察 `Xavier` 測試狀況.
  * [x] 撰寫 `Hanel` FA report.
  * [x] 協助新人觀看 `innoWorks` 相關客訴問題.
  * [x] 參與 `EU-FAE` 週會.

# 2023-07-07
* 觀察 `Thales` 測試狀況, 皆正常無異常.
* 觀察 `Xavier` 測試狀況, 皆正常無異常.
* 撰寫 `Hanel` FA report.
* 協助新人觀看 `innoWorks` 相關客訴問題.
* 參與 `EU-FAE` 週會.
* TODO
  * [x] 觀察 `Thales` 測試狀況.
  * [x] 觀察 `Xavier` 測試狀況, 將測試 `device` 移至 `宸曜` 平台.
  * [x] 協助 `Sales-Jesse` 處理 `3TG6-P` FW bin file.
  * [x] 協助 `EU-Sales` 回答 `FA` report 內 ISO 日期相關問題.
  * [x] 協助新人觀看 `innoWorks` 相關客訴問題.
  * [x] 詢問 `宸曜-Mona` 關於測試平台相關問題.
  * [x] 協助 `Leo` 觀看 `Camera` 相關平台架設問題.

# 2023-07-10
* 觀察 `Thales` 測試狀況.
* 觀察 `Xavier` 測試狀況, 將測試 `device` 移至 `宸曜` 平台.
* 協助 `Sales-Jesse` 處理 `3TG6-P` FW bin file.
* 協助 `EU-Sales` 回答 `FA` report 內 ISO 日期相關問題.
* 協助新人觀看 `innoWorks` 相關客訴問題.
* 詢問 `宸曜-Mona` 關於測試平台相關問題.
* 協助 `Leo` 觀看 `Camera` 相關平台架設問題.
* TODO
  * [x] 架設 `Asrock` 測試平台, 並詢問測試相關條件.
  * [x] 測試 `3TE2` 客人提供之測試環境.
  * [x] 協助新人處理 `3SE3 CFast` 相關客訴問題.
  * [x] 與 `PM-Jack` 討論料件借出問題.
  * [x] 回報 `Thales` 測試狀況.
  * [x] 與 `EU-PM Alfie` 討論 `Ericssion` `USE` 相關測試問題. 
  * [x] 參與 `FAE-team2` 週會.
  * [x] 詢問 `Sales-Leslie` 關於 `喬鼎` 測試狀況.
  * [x] 與 `宸曜-Mona` 討論平台無法開機相關問題.

# 2023-07-11
* 架設 `Asrock` 測試平台, 並詢問測試相關條件.
* 測試 `3TE2` 客人提供之測試環境, 需架設 `Windows10`, 並執行 `BurninTest`, cpu 需設定至 `70%`~`80%`, 重開機 `1000` cycle.
* 協助新人處理 `3SE3 CFast` 相關客訴問題.
* 與 `PM-Jack` 討論料件借出問題, 已請佩佩協助領料.
* 回報 `Thales` 測試狀況, 測試皆正常.
* 與 `EU-PM Alfie` 討論 `Ericssion` `USE` 相關測試問題, 需想辦法透過 `USB 3.0` 認碟. 
* 參與 `FAE-team2` 週會.
* 詢問 `Sales-Leslie` 關於 `喬鼎` 測試狀況, 等待客戶回覆.
* 與 `宸曜-Mona` 討論平台無法開機相關問題, 需重新安裝 `OS`, 因 `eMMC` 寫滿, 導致無法開機.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助新人操作 `SATA analyzer` 錄製 `3ME4 mSATA` 相關訊號.
  * [x] 查找 `reboot` 自動執行 `BurninTest`( `Asrock` ).
  * [x] 重新安裝 `宸曜` 平台 `os`.
  * [x] 撰寫每秒寫入 `30KB` 檔案測試程式( `FEA230621002-Issue with 3TE2 M.2` ).
  * [x] 觀看 `Thales` 測試狀況.

# 2023-07-12
* 參與 `FAE` 週會.
* 協助新人操作 `SATA analyzer` 錄製 `3ME4 mSATA` 相關訊號.
* 查找 `reboot` 自動執行 `BurninTest`( `Asrock` ).
* 重新安裝 `宸曜` 平台 `os`, 與 `Mona` 討論需架設 `ubuntu 18.04` 平台, 並安裝 `Nvidia SDK Manager` tool.
* 撰寫每秒寫入 `30KB` 檔案測試程式( `FEA230621002-Issue with 3TE2 M.2` ).
* 觀看 `Thales` 測試狀況, 皆正常.
* TODO
  * [x] 架設 `ubuntu 18.04` 平台, 並安裝 `Nvidia SDK Manager` tool, 重新安裝 `宸曜` 平台.
  * [x] 協助新人操作 `SATA analyzer` 錄製 `3ME4 mSATA` 相關訊號.
  * [x] 協助新人焊接 `3ME4 mSATA` UART log 訊號線.
  * [x] 觀看 `Thales` 測試狀況.
  * [x] 處理每秒寫入 `30KB` 檔案並自動重新開機啟動測試( `FEA230621002-Issue with 3TE2 M.2` ).
  * [x] 處理 `Asrock` 於 `reboot` 自動執行 `BurninTest`
  * [x] 與 `EU-FAE` 回報 `宸曜` 平台測試狀況.

# 2023-07-13
* 架設 `ubuntu 18.04` 平台, 並安裝 `Nvidia SDK Manager` tool, 重新安裝 `宸曜` 平台, 目前卡在 `JetPack` 版本無法選定 `4.6.1`.
* 協助新人操作 `SATA analyzer` 錄製 `3ME4 mSATA` 相關訊號.
* 協助新人焊接 `3ME4 mSATA` UART log 訊號線.
* 觀看 `Thales` 測試狀況, 並無看到問題.
* 處理每秒寫入 `30KB` 檔案並自動重新開機啟動測試( `FEA230621002-Issue with 3TE2 M.2` ), 已進行相關測試.
* 處理 `Asrock` 於 `reboot` 自動執行 `BurninTest`
* 與 `EU-FAE` 回報 `宸曜` 平台測試狀況, 目前卡在系統無法重新刷機.
* TODO
  * [x] 處理 `Asrock` 於 `reboot` 自動執行 `BurninTest`.
  * [x] 處理每秒寫入 `30KB` 檔案並自動重新開機啟動測試.
  * [x] 協助 `EU-FAE Jason` 查找 `3TE6-DEM28-C12DD1KCAQF` 對應之 bin file.
  * [x] 協助 `EU-FAE Jason` 歸還 `Vector` 測試平台, 並轉交給 `Sandra`.
  * [x] 將 `mSATA 3MG2-P` 送至 `RMA` 照 `X-ray`.
  * [x] 參與 `EU-FAE` 週會.

# 2023-07-14
* 處理 `Asrock` 於 `reboot` 自動執行 `BurninTest`, 已找出方法測試, 需透過 `rebooter` tool 來進行.
* 處理每秒寫入 `30KB` 檔案並自動重新開機啟動測試, 目前卡在無法開機進入 `OS`.
* 協助 `EU-FAE Jason` 查找 `3TE6-DEM28-C12DD1KCAQF` 對應之 bin file, 並提供相關資訊.
* 協助 `EU-FAE Jason` 歸還 `Vector` 測試平台, 並轉交給 `Sandra`.
* 將 `mSATA 3MG2-P` 送至 `RMA` 照 `X-ray`.
* 參與 `EU-FAE` 週會.
* TODO
  * [x] 觀看 `Asrock` 於 `reboot` 自動執行 `BurninTest` 測試結果.
  * [x] 參與 `EU-Ericssion` 討論會議.
  * [x] 協助 `PH-Lam` 準備測試用平台.
  * [x] 協助新人觀看 `3MG2-P` 客訴案件( 更換 `Crystal`, 清除焊接線 ).
  * [x] 觀看 `Thales` 測試狀況.

# 2023-07-17
* 觀看 `Asrock` 於 `reboot` 自動執行 `BurninTest` 測試結果.
  * 後續因權限問題, 不能在重開機時, 執行 `BurninTest`, 故執行 `1000` reboot.
* 參與 `EU-Ericssion` 討論會議.
* 協助 `PH-Lam` 準備測試用平台.
* 協助新人觀看 `3MG2-P` 客訴案件( 更換 `Crystal`, 清除焊接線 ).
* 觀看 `Thales` 測試狀況.
* TODO
  * [x] 觀看以及回報 `Asrock` 於 `reboot` 自動執行測試結果.
  * [x] 協助新人調整 `Crystal` (`3MG2-P` 客訴案件).
  * [x] 協助新人量測 `3MG2-P` 供電狀況.
  * [x] 回覆 `EU-Ericssion` 相關資訊.
  * [x] 回報 `Thales` 測試相關狀況.
  * [x] 與 `PM-Shao` 討論送修 `宸曜` 平台問題.
  * [x] 重新安裝 `FEA230621002-Issue with 3TE2 M.2`  測試環境.

# 2023-07-18
* 觀看以及回報 `Asrock` 於 `reboot` 自動執行測試結果, 皆正常, 接下來執行 `Burnintest` `3~4` days.
* 協助新人調整 `Crystal` (`3MG2-P` 客訴案件), 依然有認碟問題.
* 協助新人量測 `3MG2-P` 供電狀況, 後續發現 `Power IC U8` 電源輸出有異常( 正常 `3.3V`, 量測 `0.6V` ).
* 回覆 `EU-Ericssion` 相關資訊.
  * 提供轉板照片, 以及 `hardware id` 資訊.
  * 提供 `20` 次插拔結果.
  * 送至 `RMA` 更換 connector.
* 回報 `Thales` 測試相關狀況, 皆正常.
* 與 `PM-Shao` 討論送修 `宸曜` 平台問題.
* 重新安裝 `FEA230621002-Issue with 3TE2 M.2` 測試環境.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 詢問 `喬鼎` 客戶測試狀況.
  * [x] 詢問 `Kerry` 關於 `Kontron` 對 `3TE6` 做 `DLMC` 後, 發生 `Assert` 狀況過程. 
  * [x] 測試並修改每秒寫入 `30KB` 檔案並自動重新開機啟動測試
  * [x] 協助新人處理 `Auto Format` 程式處理.
 
# 2023-07-19
* 參與 `FAE` 週會.
* 詢問 `喬鼎` 客戶測試狀況.
* 詢問 `Kerry` 關於 `Kontron` 對 `3TE6` 做 `DLMC` 後, 發生 `Assert` 狀況過程. 
* 測試並修改每秒寫入 `30KB` 檔案並自動重新開機啟動測試, 尚未處理完成.
* 協助新人處理 `Auto Format` 程式處理.
* TODO
  * [x] 測試 `Ericssion eUSB` 更換 connector 相關狀況.
  * [x] 測試 `3TE6` FW 更換為 `V211180A`, 於 `Asrock` 平台測次 `1000`次 `reboot`.
  * [x] 參與 `EU-PM Missie` 討論 `Ericssion eUSB` 狀況.
  * [x] 從 `RMA` 取回並測試 `mSATA 3TG2-P`.
  * [x] 協助新人架設 `Power Relay tool`. 
  * [x] 與 `Kiwi` sync `3TE6` 測試 `Burnintest` `2hr` 以及 `idle` 一段時間後, 會發生 `CPU` `100%` 現象.
  * [x] 協助新人照 `X-ray` (`3MG2-P` `2`pcs).

# 2023-07-20
* 測試 `Ericssion eUSB` 更換 connector 相關狀況, 於 `USB 3.0` 皆無法被辨識.
* 測試 `3TE6` FW 更換為 `V211180A`, 於 `Asrock` 平台測次 `1000`次 `reboot`.
* 參與 `EU-PM Missie` 討論 `Ericssion eUSB` 狀況.
* 從 `RMA` 取回並測試 `mSATA 3TG2-P`, 依然無法辨識.
* 協助新人架設 `Power Relay tool`, 中間發生 `cmd` 視窗控制權傳送訊號問題, 以及程式執行相關問題, 需使用 `teraterm 4.101` & 安裝 `TTL editor`, 執行程式檔名不能有中文. 
* 與 `Kiwi` sync `3TE6` 測試 `Burnintest` `2hr` 以及 `idle` 一段時間後, 會發生 `CPU` `100%` 現象.
* 協助新人照 `X-ray` (`3MG2-P` `2`pcs), 並無異常.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 回報 `Power Relay tool` 測試狀況, 共執行 `18` hr.
  * [x] 回報 `3TE6` FW 更換為 `V211180A`, 於 `Asrock` 平台測試 `1000`次 `reboot` 狀況.
  * [x] 回覆 `Sales-Joan` 關於 `Kontron` 新舊版本 `FW` 更新問題.
  * [x] 回報 `Ericssion` `eUSB` 相關測試狀況.
  * [x] 修改每秒寫入 `30KB` 檔案並自動重新開機啟動測試程式.
  * [x] 回報 `FEA230621002-Issue with 3TE2` 測試狀況.
  * [x] 回覆 `EU-FAE` 關於 `Neousys` 測試相關狀況.
  * [x] 觀看 `mSATA 3TG2-P` 無法辨識問題.

# 2023-07-21
* 參與 `EU-FAE` 週會.
* 回報 `Power Relay tool` 測試狀況( `mSATA 3ME4` ), 共執行 `18` hr, 並未看到問題.
* 回報 `3TE6` FW 更換為 `V211180A`, 於 `Asrock` 平台測試 `1000`次 `reboot` 狀況, 並未看到問題.
* 回覆 `Sales-Joan` 關於 `Kontron` 新舊版本 `FW` 更新問題.
* 回報 `Ericssion` `eUSB` 相關測試狀況, `BurninTest` pass, 並錄製 `SMART`, `USB 3.0` 依然認不到.
* 修改每秒寫入 `30KB` 檔案並自動重新開機啟動測試程式, 目前已修正完成.
* 回報 `FEA230621002-Issue with 3TE2` 測試狀況.
* 回覆 `EU-FAE` 關於 `Neousys` 測試相關狀況.
* 觀看 `mSATA 3TG2-P` 無法辨識問題, 從 `UART` log 觀看到 `FW hang up`, 已詢問原廠.
* TODO
  * [x] 觀看 `FEA230621002-Issue with 3TE2` 測試狀況.
  * [x] 追蹤原廠回覆 `mSATA 3TG2-P` 無法辨識問題.
  * [x] 參與 `EU-PM` 討論 `Ericssion eUSB` 客訴問題.
  * [x] 觀看 `3TE6` `FW_V211180A` 經由 `BurninTest` `18` 小時後, `UART` log 是否會出現 `merge` 現象造成 `CPU` 過載.
  * [x] 協助新人測試 `SMI` `DLMC` image.
  * [x] 協助新人操作 `power cycle` 測試 tool.
  * [x] 詢問 `Hyperstone` 人員是否能協助分析 `eUSB` `controller`.
  * [x] 協助 `EU-PM` 回報 `Ericssion` `eUSB` 辨識狀況.
  * [x] 協助 `EU` 測試 `3TE6` FW 更換為 `V22620_20220914`, 於 `Asrock` 平台測試 `1000`次 `reboot`.

# 2023-07-24
* 觀看 `FEA230621002-Issue with 3TE2` 測試狀況, 並無異常.
* 追蹤原廠回覆 `mSATA 3TG2-P` 無法辨識問題, 暫無回應.
* 參與 `EU-PM` 討論 `Ericssion eUSB` 客訴問題, 討論先將 `device` 寄送至 `Hyperstone` 協助分析.
* 觀看 `3TE6` `FW_V211180A` 經由 `BurninTest` `18` 小時後, `UART` log 是否會出現 `merge` 現象造成 `CPU` 過載, 並無異常.
* 協助新人測試 `SMI` `DLMC` image.
* 協助新人操作 `power cycle` 測試 tool.
* 詢問 `Hyperstone` 人員是否能協助分析 `eUSB` `controller`.
* 協助 `EU-PM` 回報 `Ericssion` `eUSB` 辨識狀況, 有複製出 `2` 種辨識狀況, 但皆無法撈取 `SMART`.
* 協助 `EU` 測試 `3TE6` FW 更換為 `V22620_20220914`, 於 `Asrock` 平台測試 `1000`次 `reboot`, 已架設完成.
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 觀看 `FEA230621002-Issue with 3TE2` 測試狀況.
  * [x] 觀看 `3TE6` FW 更換為 `V22620_20220914`, 於 `Asrock` 平台測試 `1000`次 `reboot` 狀況.
  * [x] 協助 `EU-PM` 觀看 `Ericssion` 客訴案實驗整理.
  * [x] 協助 `EU-PM` 回覆 `Hyperstone` 相關問題.
  * [x] 協助新人觀看 `Micro USB` 相關客訴問題, 以及回應 `3ME4` `FW` 外顯設定.
  * [x] 協助 `Danny` 觀看 `Cfast card 3ME4` 開卡相關問題.
  * [x] 協助 `Miller` 回覆 `Hanel` 平台客訴案狀況.
  * [x] 協助 `Sales-Joan` 詢問關於 `3TE2` 問題復現狀況, 並與 `RD-Jian` 討論相關問題.

# 2023-07-25
* 參與 `FAE-team2` 週會.
* 觀看 `FEA230621002-Issue with 3TE2` 測試狀況, 皆正常, 並將狀況回覆( `Reboot` : `85`, `File count` : `499985` ).
* 觀看 `3TE6` FW 更換為 `V22620_20220914`, 於 `Asrock` 平台測試 `1000`次 `reboot` 狀況, 皆正常, 已將狀況回覆給 `EU-Sales`.
* 協助 `EU-PM` 觀看 `Ericssion` 客訴案實驗整理, 並寄出給 `EU-PM Missie`.
* 協助 `EU-PM` 回覆 `Hyperstone` 相關問題.
* 協助新人觀看 `Micro USB` 相關客訴問題, 以及回應 `3ME4` `FW` 外顯設定.
* 協助 `Danny` 觀看 `Cfast card 3ME4` 開卡相關問題, 發現可能為 `Controller` 異常.
* 協助 `Miller` 回覆 `Hanel` 平台客訴案狀況, 目前已停止測試, 告知 `EU-Sales` 可透過 `copy machine`` 來做篩選條件.
* 協助 `Sales-Joan` 詢問關於 `3TE2` 問題復現狀況, 並與 `RD-Jian` 討論相關問題.
  * 主要原因為 `get flash temperature` 的機制導致異常! `get flash temperature` 在 `idle` 和 `RT` 階段更新時, 會切換 `flash mode`, 假設在切換過程還有 `Flash` 操作正在執行的話! 會導致資料錯誤而後引發`defect block` 產生.
  * 目前告知 `Sales-Joan` 的說法為異常斷電導致 `System data` lose, 導致認不到碟.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 於 `FEA230621002-Issue with 3TE2` 測試中加入 `5` ~ `10` mins `idle` 狀態, 並將 `OS` 更換成 `CentOS 7.X`.
  * [x] 協助 `新竹` `FW-RD` 更新 `3TE6` FW -> ` V22620X2`, 並透過 `BurninTest` 測試.
  * [x] 將 `Ericssion eUSB` 送至 `RMA` 更換 `Connector`.
  * [x] 參與 `Kontron` 討論 `3TE6` `FW-V211180A, V2111804` -> `V226220X1` 差異.
  * [x] 處理 `mSATA 3MG2-P` 客訴案.
  * [x] 協助新人處理 `iTracker` `mSATA 3ME4` 相關操作.
  * [x] 修改 `3TE2` 測試程式, 加入 `reboot count` & `datetime` 紀錄.

# 2023-07-26
* 參與 `FAE` 週會.
* 於 `FEA230621002-Issue with 3TE2` 測試中加入 `5` ~ `10` mins `idle` 狀態, 並將 `OS` 更換成 `CentOS 7.X`.
* 協助 `新竹` `FW-RD` 更新 `3TE6` FW -> ` V22620X2`, 並透過 `BurninTest` 測試, 已架設完成.
* 將 `Ericssion eUSB` 送至 `RMA` 更換 `Connector`.
* 參與 `Kontron` 討論 `3TE6` `FW-V211180A, V2111804` -> `V226220X1` 差異.
* 處理 `mSATA 3MG2-P` 客訴案, 後續發現為 `Later bad` 過多導致開卡有相關問題.
  * 第一次開卡需先將容量降低( `IDEMA` -> `Disk Size` ).
  * 不參考之前紀錄之 `Later bad` ( `PreTest` -> `1. Don't Reference Original Bad` ).
* 協助新人處理 `iTracker` `mSATA 3ME4` 相關操作.
* 修改 `3TE2` 測試程式, 加入 `reboot count` & `datetime` 紀錄, 還再修改中.
* TODO
  * [x] 修改 `3TE2` 測試程式, 加入 `reboot count` & `datetime` 紀錄.
  * [x] 架設 `FRA` system, 觀看客訴問題.
  * [x] 與 `EU-FAE` 討論 `FEB230608005` 於 `宸曜` 平台相關測試.
  * [x] 測試 `mSATA 3MG2-P` 客訴案, 並提供相關資訊於 `EU-FAE`.
  * [x] 針對 `mSATA 3MG2-P` 執行 `BurninTest`.

# 2023-07-27
* 修改 `3TE2` 測試程式, 加入 `reboot count` & `datetime` 紀錄, 目前已修改完成, 並進行相關測試.
* 架設 `FRA` system, 觀看客訴問題.
* 與 `EU-FAE` 討論 `FEB230608005` 於 `宸曜` 平台相關測試, 並追蹤維修狀況.
* 測試 `mSATA 3MG2-P` 客訴案, 並提供相關資訊於 `EU-FAE`.
* 針對 `mSATA 3MG2-P` 執行 `BurninTest`.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 觀看 `FRA` system 客訴問題.
  * [x] 協助新人處理 `3IE4` 開卡問題.
  * [x] 協助新人回覆 `micro sd card` 相關信件問題.
  * [x] 協助 `EU-Sales` 處理 `Hanel` sorting 問題.

# 2023-07-28
* 參與 `EU-FAE` 週會.
* 觀看 `FRA` system 客訴問題.
  * 1. MOP12302230020012 -> Can enter the OS normally, but takes about 2 minutes.
  * 2. MOP12302230020028 -> Unrecognizable, preliminarily determined to be a power issue.
  * 3. MOP12302230020016 -> Can enter the OS normally, no abnormal phenomena observed.
  * 4. MOP12302230020046 -> Recognizable normally.
* 協助新人處理 `3IE4` 開卡問題.
* 協助新人回覆 `micro sd card` 相關信件問題.
* 協助 `EU-Sales` 處理 `Hanel` sorting 問題.
* TODO
  * [x] 查找 `MOP12302230020028` power issue.
  * [x] 錄製 `MOP12302230020016` & `MOP12302230020012` UART log.
  * [x] 協助 `Alan` 查找 `電路圖` & `位置圖`.
  * [x] 詢問 `Adson` 關於 `AIOT` 平台問題.
  * [x] 協助新人處理 `越南-Sales` 相關平台操作問題.

# 2023-07-31
* 查找 `MOP12302230020028` power issue, 透過分析, 發現為 `U21` powere IC 破損.
* 錄製 `MOP12302230020016` & `MOP12302230020012` UART log.
* 協助 `Alan` 查找 `電路圖` & `位置圖`.
* 詢問 `Adson` 關於 `AIOT` 平台問題.
* 協助新人處理 `越南-Sales` 相關平台操作問題.
* TODO
  * [x] 建立 `FRA` system 客訴於 `TTS`, 並提供相關 `SMART` & `UART`.
  * [x] 將 `MOP12302230020028` 送至 `RMA` 更換料件.
  * [x] 協助 `EU-Sales` 處理 `Hanel` sorting 相關問題, 並透過 `EU-Sales` 詢問取得相關 `HW` & `SW` 資源.
  * [x] 參與 `FAE-team1` 週會.
  * [x] 協助分析 `融程電子` 客訴品( `mSATA 3TG6-P` ).
  * [x] 協助 `EU-Sales` 處理 `Ericssion` 銷帳相關問題.
  * [x] 回報 `3TE2` 客訴案測試結果.

# 2023-08-01
* 建立 `FRA` system 客訴於 `TTS`, 並提供相關 `SMART` & `UART`, 並無看到相關異常訊息.
* 將 `MOP12302230020028` 送至 `RMA` 更換料件.
* 協助 `EU-Sales` 處理 `Hanel` sorting 相關問題, 並透過 `EU-Sales` 詢問取得相關 `HW` & `SW` 資源.
* 參與 `FAE-team1` 週會.
* 協助分析 `融程電子` 客訴品( `mSATA 3TG6-P` ), 並錄製 `UART` log 提供於 `FW-RD` 分析, 後續發現為 `read retry` 過多, 導致 `performance` 下降.
* 協助 `EU-Sales` 處理 `Ericssion` 銷帳相關問題.
* 回報 `3TE2` 客訴案測試結果.
* TODO
  * [x] 將 `融程電子` 客訴品( `mSATA 3TG6-P` ) 透過 `DLMC` 更新 `FW`.
  * [x] 協助 `EU-PM` 追蹤 `Ericssion` 送回原廠分析進度.
  * [x] 與 `FW-RD SID` 討論 `4TG2-P` `開機` & `重開機` 速度過慢問題.
  * [x] 與 `宸曜` 人員討論平台狀況.
  * [x] 協助 `Hyperstone` 人員寄送轉接板.

# 2023-08-02
* 將 `融程電子` 客訴品( `mSATA 3TG6-P` ) 透過 `DLMC` 更新 `FW`.
* 協助 `EU-PM` 追蹤 `Ericssion` 送回原廠分析進度.
* 與 `FW-RD SID` 討論 `4TG2-P` `開機` & `重開機` 速度過慢問題.
* 與 `宸曜` 人員討論平台狀況.
* 協助 `Hyperstone` 人員寄送轉接板.
* TODO
  * [x] 參與 `EU` `Ericssion eUSB` 客訴案討論會議.
  * [x] 測試 `Asrock` 執行 `3TE6 2TB`( `FW -> V211180A` ), 是否可以正常.
  * [x] 協助 `EU-FAE` 詢問銅柱相關問題.
  * [x] 觀看 `3TE2` 客訴案測試結果, 並與 `Sales-Joan` 討論.
  * [x] 協助 `Sales-Vivian` 處理 `融程` `mSATA 3TG6-P` 客訴案分析.

# 2023-08-03
* 參與 `EU` `Ericssion eUSB` 客訴案討論會議, 詢問 `Hyperstone` 關於分析的狀況, 並領取 `Controller` 料件.
* 測試 `Asrock` 執行 `3TE6 2TB`( `FW -> V211180A` ), 是否可以正常, 測試後續發現平台有問題, 已將平台送修.
* 協助 `EU-FAE` 詢問銅柱相關問題.
* 觀看 `3TE2` 客訴案測試結果, 並與 `Sales-Joan` 討論.
* 協助 `Sales-Vivian` 處理 `融程` `mSATA 3TG6-P` 客訴案分析, 需要 `Sales` 幫忙詢問當時處理客訴的 `China-FAE`.
* TODO
  * [x] 颱風天放假.

# 2023-08-04
* 颱風天放假.
* TODO
  * [x] 協助 `FAE-Danny` 處理 `FA230711001` `3SE4` 客訴案.
  * [x] 取回 `宸曜` 送回之平台.
  * [x] 撰寫 `融程` `mSATA 3TG6-P` 客訴案分析報告, 並與 `Jay` 討論.
  * [x] 架設 `Supermicro` 測試環境, `4TG2-P`( `FW -> E23609` ) 第一次開機會辨識, `reboot` 後, 認不到 `device`.
  * [x] 與 `EU-PM` 討論 `Ericssion eUSB` 分析狀況.
  * [x] 詢問 `FW-RD Jason` 關於 `mSATA 3TG6-P` `read retry` 機制修改流程.
  * [x] 詢問機構組 `Jason` 關於 `銅柱` 查訊相關問題.

# 2023-08-07
* 協助 `FAE-Danny` 處理 `FA230711001` `3SE4` 客訴案.
* 取回 `宸曜` 送回之平台.
* 撰寫 `融程` `mSATA 3TG6-P` 客訴案分析報告, 並與 `Jay` 討論, 並將報告寄出給 `Sales-Vivian`.
* 架設 `Supermicro` 測試環境, `4TG2-P`( `FW -> E23609` ) 第一次開機會辨識, `reboot` 後, 認不到 `device`.
* 與 `EU-PM` 討論 `Ericssion eUSB` 分析狀況.
  * `Hyperstone` office 並無 `USB analyzer`.
  * 初步檢查電性相關狀況.
  * 已聯絡相關人員將 `Device` 寄回.
* 詢問 `FW-RD Jason` 關於 `mSATA 3TG6-P` `read retry` 機制修改流程, 並將其畫成流程圖.
* 詢問機構組 `Jason` 關於 `銅柱` 查訊相關問題, 經由系統查詢, 並未有 `EU-FAE` 所需之規格, 後續會再提供相關資訊給 `EU-FAE`.
* TODO
  * [x] 協助 `EU` 領出 `Ericssion` `eUSB` controller.
  * [x] 整理 `Ericssion` `eUSB` 量測結果m, 並與 `EU-PM` 討論.
  * [x] 架設 `Supermicro` 測試環境並錄製 `UART` log 提供給 `FW-RD Sid`.
  * [x] 修改 `融程` `mSATA 3TG6-P` 客訴案分析報告.
  * [x] 協助新人量測 `mSATA 3ME3` 客訴品.

# 2023-08-08
* 協助 `EU` 領出 `Ericssion` `eUSB` controller.
* 整理 `Ericssion` `eUSB` 量測結果m, 並與 `EU-PM` 討論.
* 架設 `Supermicro` 測試環境並錄製 `UART` log 提供給 `FW-RD Sid`.
* 修改 `融程` `mSATA 3TG6-P` 客訴案分析報告, 後續討論將 `FW`.
* 協助新人量測 `mSATA 3ME3` 客訴品.
* TODO
  * [x] 回覆送修主機板相關問題.
  * [x] 參與 `FAE` 週會.
  * [x] 參與 `EU` 討論 `Ericssion` `eUSB` 客訴會議.
  * [x] 協助新人觀看 `3ME3` 量測 `Flash` 相關狀況.
  * [x] 從 `RMA` 領回 `Ericssion` `eUSB` 更換為新 `controller`, 並做 `20` 次插拔實驗.
  * [x] 撰寫 `3TE2` 客訴案報告, 並與 `Sales` 討論.
  * [x] 架設 `Neousys` 平台, 並觀察是否可以正常運行.

# 2023-08-09
* 回覆送修主機板相關問題.
* 參與 `FAE` 週會.
* 參與 `EU` 討論 `Ericssion` `eUSB` 客訴會議.
* 協助新人觀看 `3ME3` 量測 `Flash` 相關狀況.
* 從 `RMA` 領回 `Ericssion` `eUSB` 更換為新 `controller`, 並做 `20` 次插拔實驗, 並回報測試狀況.
* 撰寫 `3TE2` 客訴案報告, 並與 `Sales` 討論, 回覆客戶相關問題.
* 架設 `Neousys` 平台, 確認平台可以正常運行.
* TODO
  * [x] 協助 `FW-RD Jason` 回覆 `TTS` 測試狀況.
  * [x] 回報 `Ericssion` `eUSB` 處理狀況.
  * [x] 協助新人處理 `notebook` 問題.
  * [x] 將 `Ericssion` `eUSB` 送至 `RMA` 更換為新品 `Controller`.
  * [x] 回覆 `3TE2` 客訴案客戶相關問題.
  * [x] 協助新人觀看 `Digi` 客訴案報告.
  * [x] 參與 `EU-FAE` 週會.

# 2023-08-10
* 協助 `FW-RD Jason` 回覆 `TTS` 測試狀況.
* 回報 `Ericssion` `eUSB` 處理狀況.
* 協助新人處理 `notebook` 問題.
* 將 `Ericssion` `eUSB` 送至 `RMA` 更換為新品 `Controller`.
* 回覆 `Concurrent` `3TE2` 客訴案客戶相關問題.
* 協助新人觀看 `Digi` 客訴案報告.
* TODO
  * [x] 回報 `Ericssion` `eUSB` 處理狀況.
  * [x] 參與 `EU` 討論 `Ericssion` `eUSB` 客訴會議.
  * [x] 於 `Supermicro` 測試 `4TG2-P` 執行 `DLMC`( `FW` `E23609` -> `E23810` ).
  * [x] 詢問 `Jay` 關於 `4TG2-P` 開卡操作流程.
  * [x] 至 `RMA` 領取 `Ericssion` `eUSB`, 並做插拔測試.
  * [x] 回覆 `EU-FAE` 關於如何從 `iSMART` 觀看歷史 `高溫` & `低溫`.
  * [x] 參與 `Concurrent ` `3TE2` 討論會議.
  * [x] 詢問 `FW-RD Jian` 關於 `3TE2` `data lose` 產生條件, 以及進入 `idle` 相關方式.

# 2023-08-11
* 回報 `Ericssion` `eUSB` 處理狀況.
* 參與 `EU` 討論 `Ericssion` `eUSB` 客訴會議.
* 於 `Supermicro` 測試 `4TG2-P` 執行 `DLMC`( `FW` `E23609` -> `E23810` ), 可正常運行, 並錄製影片.
  * 因 `FW` 版本限制無法跨版本 `DLMC`, 故須將 `Device` 重新開卡.
* 詢問 `Jay` 關於 `4TG2-P` 開卡操作流程.
  * 須將 `mode` 改為 `open card`.
  * `EUI64` 設定需修改 `config.ini`.
* 至 `RMA` 領取 `Ericssion` `eUSB`, 並做插拔測試, 換回異常品 `controller` 後, 無法被 `USB3.0` 被辨識, 初步判斷 `controller` 有異常.
* 回覆 `EU-FAE` 關於如何從 `iSMART` 觀看歷史 `高溫` & `低溫`.
* 參與 `Concurrent ` `3TE2` 討論會議, 後續需要提供 `DLMC` tool.
* 詢問 `FW-RD Jian` 關於 `3TE2` `data lose` 產生條件, 以及進入 `idle` 相關方式.
* 協助新人處理 `mSATA 3ME3` 更換 `Flash`.
* TODO
  * [x] 協助新人觀看 `SATA Slim 3ME3` 客訴報告.
  * [x] 量測 `Ericssion` `eUSB` `TX & RX` 阻抗數值.
  * [x] 將 `Ericssion` `eUSB`  送至 `RMA` 與新品對調 `controller`.
  * [x] 測試 `FRA SYS` `4TG2-P` `20046` BurninTest.
  * [x] 詢問關於 `3TE7` 於 `DLMC` 情況下, 不 `reset` 進行更新之工具.
  * [x] 協助新人回覆 `VN-Sales` 相關技術問題.

# 2023-08-14
* 協助新人觀看 `SATA Slim 3ME3` 客訴報告.
* 量測 `Ericssion` `eUSB` `TX & RX` 阻抗數值.
* 將 `Ericssion` `eUSB`  送至 `RMA` 與新品對調 `controller`.
* 測試 `FRA SYS` `4TG2-P` `20046` BurninTest.
* 詢問關於 `3TE7` 於 `DLMC` 情況下, 不 `reset` 進行更新之工具.
* 協助新人回覆 `VN-Sales` 相關技術問題.
* TODO
  * [x] 參與 `FAE-Team2` 週會.
  * [x] 架設 `FRA` System 執行 `BurninTest`( `20046` ).
  * [x] 至 `RMA` 領取 `Ericssion` `eUSB`, 並做 `20` 次插拔測試( 異常品 `controller` -> `DEUH2-08GY91SWADB-G58B` ), 並回報進度.
  * [x] 更新 `FA` case 進度於 `eFAE` system.
  * [x] 協助 `PM-Becky` 測試 `4TE3` 於 `Supermicro` MB.
  * [ ] 撰寫 `3TE2` DLMC tool 操作手冊.
  * [x] 協助新人觀看 `mSATA 3ME3` & `CFast 3ME4` 客訴案.

# 2023-08-15
* 參與 `FAE-Team2` 週會.
* 架設 `FRA` System 執行 `BurninTest`( `20046` ).
* 至 `RMA` 領取 `Ericssion` `eUSB`, 並做 `20` 次插拔測試( 異常品 `controller` -> `DEUH2-08GY91SWADB-G58B` ), 並回報進度.
* 更新 `FA` case 進度於 `eFAE` system.
* 協助 `PM-Becky` 測試 `4TE3` 於 `Supermicro` MB.
* 協助新人觀看 `mSATA 3ME3` & `CFast 3ME4` 客訴案.
* TODO
  * [x] 參與 `FAE team` 週會.
  * [x] 協助 `EU-PM` 詢問 `CN` 使用 `analyzer` 相關時間. 
  * [x] 觀看海洋淨灘影片.
  * [x] 測試送修之測試 `MSI` 主機板.
  * [x] 協助 `Benson` 處理 `Ericssion` 相關分析, 並提供相關資訊.
  * [x] 詢問 `Hyperstone` 關於 `set bit 24 deactivate U1 mode` 設定功能.
  * [x] 提供 `EU-FAE` 關於 `Neousys'` platform 測試狀況.
  * [x] 提供 `EU-FAE` `ASRock` platform 關於 `reboot` `1000` cycle 測試結果.

# 2023-08-16
* 參與 `FAE team` 週會.
* 協助 `EU-PM` 詢問 `CN` 使用 `analyzer` 相關時間. 
* 觀看海洋淨灘影片.
* 測試送修之測試 `MSI` 主機板.
* 協助 `Benson` 處理 `Ericssion` 相關分析, 並提供相關資訊.
* 詢問 `Hyperstone` 關於 `set bit 24 deactivate U1 mode` 設定功能.
* 提供 `EU-FAE` 關於 `Neousys'` platform 測試狀況.
* 提供 `EU-FAE` `ASRock` platform 關於 `reboot` `1000` cycle 測試結果.
* TODO
  * [x] 協助拍攝測試平台 `MSI` 故障影片.
  * [x] 協助 `EU-FAE` 架設 `Supermicro` 測試 `4TG2-P` 關於 `Event log` 相關 `warning` message 問題.
  * [x] 與 `FW-RD` 討論關於 `3TE7` 透過 `WinPE` 安裝之相關流程.
  * [x] 與 `EU-FAE` 討論客訴案相關狀況.
  * [x] 參與 `EU` 討論 `Ericssion` 客訴處理會議.
  * [x] 協助新人量測透過 `Chamber` 於 `-40` 度情況下, `SATA Slim 3ME3-S21804` `reboot` & `cold boot` 時間.
  * [x] 與新竹 `FW-RD` ＆ `Fred` 討論 `3TE2` DLMC 狀況.

# 2023-08-17
* 協助拍攝測試平台 `MSI` 故障影片.
* 協助 `EU-FAE` 架設 `Supermicro` 測試 `4TG2-P` 關於 `Event log` 相關 `warning` message 問題.
* 與 `FW-RD` 討論關於 `3TE7` 透過 `WinPE` 安裝之相關流程.
* 與 `EU-FAE` 討論客訴案相關狀況.
* 參與 `EU` 討論 `Ericssion` 客訴處理會議.
* 協助新人量測透過 `Chamber` 於 `-40` 度情況下, `SATA Slim 3ME3-S21804` `reboot` & `cold boot` 時間.
* 與新竹 `FW-RD` ＆ `Fred` 討論 `3TE2` DLMC 狀況.
* TODO  
  * [x] 協助 `PM-Becky` 回報 `4TE3` `warm boot` 測試狀況.
  * [x] 拍攝 `MSI` 主機板異常證明影片.
  * [x] 架設 `WinPE` 環境.
  * [x] 協助新竹 `FW-RD` 查詢 `3TE2` 客訴品 `FW` version, 並討論如何進行 `DLMC`.
  * [x] 協助新人架設 `電源供應器` 量測 `CFast card 3ME4` 訊號變化.
  * [x] 協助新人詢問 `DQE` 人員是否有空的 `chamber` 可進行低溫測試.
  * [x] 查找 `FRA` SYS 螢幕輸出問題.

# 2023-08-18
* 協助 `PM-Becky` 回報 `4TE3` `warm boot` 測試狀況.
* 拍攝 `MSI` 主機板異常證明影片.
* 架設 `WinPE` 環境.
* 協助新竹 `FW-RD` 查詢 `3TE2` 客訴品 `FW` version, 並討論如何進行 `DLMC`.
* 協助新人架設 `電源供應器` 量測 `CFast card 3ME4` 訊號變化.
* 協助新人詢問 `DQE` 人員是否有空的 `chamber` 可進行低溫測試.
* 查找 `FRA` SYS 螢幕輸出問題, 後續發現為 `power cable` 不能用 `EU`.
* TODO
  * [x] 協助新人架設 `Windows 7 embededd` 環境.
  * [x] 架設 `WinPE` 環境.
  * [x] 協助 `EU-PM` 回答 `Ericssion` 技術問題.
  * [x] 與 `EU-FAE` 討論 `Rosch computer` DLMC tool 流程.
  * [x] 測試 `4TG2-P` 於 `Supermicro` 平台是否會出現 `ID 17 Warning` message, 並回報初步測試狀況.
  * [x] 協助新人架設 `電源供應器` 量測 `CFast card 3ME4` 訊號變化.

# 2023-08-21
* 協助新人架設 `Windows 7 embededd` 環境.
* 架設 `WinPE` 環境.
* 協助 `EU-PM` 回答 `Ericssion` 技術問題.
* 與 `EU-FAE` 討論 `Rosch computer` DLMC tool 流程.
* 測試 `4TG2-P` 於 `Supermicro` 平台是否會出現 `ID 17 Warning` message, 並回報初步測試狀況.
* 協助新人架設 `電源供應器` 量測 `CFast card 3ME4` 訊號變化.
* TODO
  * [x] 協助 `Kiwi` 參與 `Asia` `3TE7` 進行測試, reboot後無法進入系統之客訴討論會議.
  * [x] 修改 `Ericssion` `FA` report.
  * [x] 參與 `FAE-team2` 週會.
  * [x] 測試 `EU-FAE` 需要之 `DLMC` tool (without `reset`).
  * [x] 回報 `Supermicro` `reboot` 測試結果.

# 2023-08-22
* 協助 `Kiwi` 參與 `Asia` `3TE7` 進行測試, reboot後無法進入系統之客訴討論會議.
* 修改 `Ericssion` `FA` report, 並回覆相關問題.
* 參與 `FAE-team2` 週會.
* 測試 `EU-FAE` 需要之 `DLMC` tool (without `reset`), 後續測試發現需要 `reset` 才可更新 `FW`.
* 回報 `Supermicro` `reboot` 測試結果.
* TODO
  * [x] 測試 `EU-FAE` 需要之 `DLMC` tool (without `reset`).
  * [x] 與 `Arlen` 討論 `DLMC` tool (without `reset`).
  * [x] 詢問 `PE` 關於清潔劑領取相關問題.
  * [x] 協助 `Sales-Vivian` 處理 `融程` 客訴品( Update FW -> `S23707` )
  * [x] 協助 `Celia` 處理團購物品.
  * [x] 參與 `4TG2-P` 於 `Supermicro` 測試討論會議( `Windows` `Event log` -> `ID:17` warning ).
  * [x] 與 `EU-YingXiang` 討論 `Rosch computer` 需要之 `DLMC` tool.
  * [x] 詢問 `Jay` 關於 `3TG6-P` `write code` 相關操作.

# 2023-08-23
* 測試 `EU-FAE` 需要之 `DLMC` tool (without `reset`).
* 與 `Arlen` 討論 `DLMC` tool (without `reset`).
* 詢問 `PE` 關於清潔劑領取相關問題.
* 協助 `Sales-Vivian` 處理 `融程` 客訴品( Update FW -> `S23707` )
* 協助 `Celia` 處理團購物品.
* 參與 `4TG2-P` 於 `Supermicro` 測試討論會議( `Windows` `Event log` -> `ID:17` warning ).
* 與 `EU-YingXiang` 討論 `Rosch computer` 需要之 `DLMC` tool.
* 詢問 `Jay` 關於 `3TG6-P` `write code` 相關操作.
* TODO
  * [x] 測試 `3TE2` `FW` update tool( `K19603` -> `K19603e1` ).
  * [x] 詢問 `Kiwi` 關於 `3TE2` 開卡相關問題.
  * [x] 提供 `銅柱` 相關領料資訊於 `EU-Jason`.
  * [x] 與 `Sales-Joan` 討論 `3TE2` 狀況處理.
  * [x] 觀察 `FRA sys` 測試 `20016` reboot 狀況.
  * [x] 撰寫 `3TE2` DLMC tool 操作手冊.
  * [x] 協助新人觀看 `CFast 3ME4` & `mSATA 3ME3` 相關客訴問題.

# 2023-08-24
* 測試 `3TE2` `FW` update tool( `K19603` -> `K19603e1` ), 已測試完成, 並提供相關 `bin file`.
* 詢問 `Kiwi` 關於 `3TE2` 開卡相關問題.
* 提供 `銅柱` 相關領料資訊於 `EU-Jason`.
* 與 `Sales-Joan` 討論 `3TE2` 狀況處理.
* 觀察 `FRA sys` 測試 `20016` reboot 狀況, 發現掉碟現象, 已回報給 `FW-RD Sid`.
* 撰寫 `3TE2` DLMC tool 操作手冊, 並提供給 `Sales-Joan`.
* 協助新人觀看 `CFast 3ME4` & `mSATA 3ME3` 相關客訴問題.
* TODO
  * [x] 測試 `FRA sys` 測試 `20016` reboot.
  * [x] 與 `Sales-Joan` 討論 `3TE2` 客戶問題回覆內容.
  * [x] 回報 `FRA SYS` 測試狀況, 以及環境執行狀態.
  * [x] 協助新人回覆 `CFast  3ME4` & `SATADOM 3ME3` 客戶相關提問.
  * [x] 協助 `EU-FAE` 觀看 `3MR3-P` 客訴問題.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助新人參與 `innoworks` & `VN` 客訴討論會議.

# 2023-08-25
* 測試 `FRA sys` 測試 `20016` reboot.
* 與 `Sales-Joan` 討論 `3TE2` 客戶問題回覆內容.
* 回報 `FRA SYS` 測試狀況, 以及環境執行狀態.
* 協助新人回覆 `CFast  3ME4` & `SATADOM 3ME3` 客戶相關提問.
* 協助 `EU-FAE` 觀看 `3MR3-P` 客訴問題, 其中 `1`pcs 確實無法認碟.
* 參與 `EU-FAE` 週會.
* 協助新人參與 `innoworks` & `VN` 客訴討論會議.
* TODO
  * [x] 測試 `CFast card 3IE7` 更新 `S23809i` 狀況, 並錄製相關證明影片.
  * [x] 協助 `EU-FAE` 更新 `Supermicro` bios -> `2.7` & 更新 `OS` -> `Windows 10 pro`.
  * [x] 更新 `FRA SYS` 內 `OS` kernel & 執行 `reboot` `3000` 次.
  * [x] 觀看 `3MR3-P` 客訴品其餘 `7` pcs.
  * [x] 協助新人回覆 `innoworks` & `VN` 客訴問題.
  * [x] 將 `3MG2-P` device 送至 `RMA`.
  * [x] 協助組內人員發送訂購設備.

# 2023-08-28
* 測試 `CFast card 3IE7` 更新 `S23809i` 狀況, 並錄製相關證明影片.
* 協助 `EU-FAE` 更新 `Supermicro` bios -> `2.7` & 更新 `OS` -> `Windows 10 pro`.
* 更新 `FRA SYS` 內 `OS` kernel & 執行 `reboot` `3000` 次.
* 觀看 `3MR3-P` 客訴品其餘 `7` pcs.
* 協助新人回覆 `innoworks` & `VN` 客訴問題.
* 將 `3MG2-P` device 送至 `RMA`.
* 協助組內人員發送訂購設備.
* TODO
  * [x] 參與 `FAE team2` 週會.
  * [x] 整理 `3MR3-P` 客訴品 `8` pcs 相關資訊以及 `Log`.
  * [x] 協助 `Jay` 查找 `PCIe` analyzer 安裝包.
  * [x] 詢問 `China-FAE` 是否能協助錄製 `eUSB` analyzer.
  * [x] 協助 `FW RD-Mike` 處理 `Nexcom` 平台.
  * [x] 詢問 `Sales-Joan` 關於 `FEA230804005` `3TE7` 客訴案處理後續狀況.
  * [x] 協助新人撰寫 `3ME3` 透過 `ssh` 更新 `FW` 相關操作手冊.
  * [x] 觀察 `FRA SYS` 測試狀況.
  * [x] 觀看 `Supermicro` 更新 `Bios` & `Windows 10 pro` 測試狀況.
  * [x] 協助新人與 `Jay` 討論 `CFast 3ME4` 客訴案處理.

# 2023-08-29
* 參與 `FAE team2` 週會.
* 整理 `3MR3-P` 客訴品 `8` pcs 相關資訊以及 `Log`, 並寄給 `EU-FAE`.
* 協助 `Jay` 查找 `PCIe` analyzer 安裝包.
* 詢問 `China-FAE` 是否能協助錄製 `eUSB` analyzer.
* 協助 `FW RD-Mike` 處理 `Nexcom` 平台.
* 詢問 `Sales-Joan` 關於 `FEA230804005` `3TE7` 客訴案處理後續狀況.
* 協助新人撰寫 `3ME3` 透過 `ssh` 更新 `FW` 相關操作手冊.
* 觀察 `FRA SYS` 測試狀況, 目前測試 `4000` cycle reboot, 尚未看到掉碟問題, 會持續加測.
* 觀看 `Supermicro` 更新 `Bios` & `Windows 10 pro` 測試狀況, 經過 `3000` cycle reboot 測試, 尚未看到客戶反應之 `Event ID 17` 問題.
* 協助新人與 `Jay` 討論 `CFast 3ME4` 客訴案處理.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 回報 `SARL` 客訴案測試狀況.
  * [x] 與 `FW RD-Sid` 討論 `FRA SYS` 測試狀況, 以及 `FW` 修改內容.
  * [x] 協助新人錄製 `3ME3` 透過 `ssh` 更新 `FW` 相關影片.
  * [x] 協助 `Kiwi` 觀看 `Joanne` 客訴品 `CFast card 3ME4` 狀況.
  * [x] 撰寫 `FAE` 月會報告(關於 `4TG2-P` DLMC 更新 tool & `Supermicro` 平台 `warm boot` 案例分享 ).
  * [x] 與 `FW-RD Allen` 討論 `FEB230811006 FACTORY-SYS` 關於 `InnoOSR 3TO7` 相關客訴問題.
  * [x] 送 `FA230828007-Aristocrat Tech` 之客訴品 `CFast card 3ME4` 至 `RMA` 協助量測 `controller` & `Flash` `X-ray`.

# 2023-08-30
* 參與 `FAE` 週會.
* 回報 `SARL` 客訴案測試狀況.
* 與 `FW RD-Sid` 討論 `FRA SYS` 測試狀況, 以及 `FW` 修改內容.
* 協助新人錄製 `3ME3` 透過 `ssh` 更新 `FW` 相關影片.
* 協助 `Kiwi` 觀看 `Joanne` 客訴品 `CFast card 3ME4` 狀況.
* 撰寫 `FAE` 月會報告(關於 `4TG2-P` DLMC 更新 tool & `Supermicro` 平台 `warm boot` 案例分享 ).
* 與 `FW-RD Allen` 討論 `FEB230811006 FACTORY-SYS` 關於 `InnoOSR 3TO7` 相關客訴問題.
* 送 `FA230828007-Aristocrat Tech` 之客訴品 `CFast card 3ME4` 至 `RMA` 協助量測 `controller` & `Flash` `X-ray`, 並無發現異常.
* TODO
  * [x] 與 `EU-FAE` 討論 `3MR3-P` 相關分析結果.
  * [x] 修改 `FAE` 月會分享之報告.
  * [x] 協助 `Kiwi` 觀看 `FA230828007-Aristocrat Tech` 之客訴品 `CFast card 3ME4` 狀況, 並進行相關量測實驗.
  * [x] 參加 `FAE` 月會.
  * [x] 協助新人觀看 `Innoworks` 相關客訴問題.

# 2023-08-31
* 與 `EU-FAE` 討論 `3MR3-P` 相關分析結果.
* 修改 `FAE` 月會分享之報告.
* 協助 `Kiwi` 觀看 `FA230828007-Aristocrat Tech` 之客訴品 `CFast card 3ME4` 狀況, 並進行相關量測實驗.
  * 與正常品交換 `Power IC` -> `Failed`.
  * 送至 `RMA` 更換 controller -> `Pass`.
* 參加 `FAE` 月會.
* 協助新人觀看 `Innoworks` 相關客訴問題.
* TODO
  * [x] 與 `Jay` 討論關於 `融程` 客訴案之 `mSATA 3TG6-P` 掉速相關問題.
  * [x] 修改到班時間.
  * [x] 與 `Sales-Vivian` 討論 `融程` 反應之掉速問題, 並詢問客戶相關操作狀況.
  * [x] 至 `工程部` 借取 `eUSB` 組裝治具, 並與 `EU-PM Alfie` 討論.
  * [x] 與 `Miller` 討論 `Ericssion` 相關測試 `SOP` 流程問題.
  * [x] 協助 `Joanne` 關於 `3ME4` `controller` 異常相關問題.
  * [x] 參加淨灘說明會.
  * [x] 協助新人觀看 `Innoworks` 相關客訴問題.
  * [x] 觀看 `FRA SYS` 客訴品 `4TG2-P` 隨機認不到碟問題.

# 2023-09-01
* 與 `Jay` 討論關於 `融程` 客訴案之 `mSATA 3TG6-P` 掉速相關問題.
* 修改到班時間.
* 與 `Sales-Vivian` 討論 `融程` 反應之掉速問題, 並詢問客戶相關操作狀況.
* 至 `工程部` 借取 `eUSB` 組裝治具, 並與 `EU-PM Alfie` 討論.
* 與 `Miller` 討論 `Ericssion` 相關測試 `SOP` 流程問題.
* 協助 `Joanne` 關於 `3ME4` `controller` 異常相關問題, 並將異常品做 `controller` 交叉驗證.
* 參加淨灘說明會.
* 協助新人觀看 `Innoworks` 相關客訴問題.
* 觀看 `FRA SYS` 客訴品 `4TG2-P` 隨機認不到碟問題, 並與 `FW-RD Sid` 討論.
* TODO
  * [x] 重新錄製 `FRA SYS` 客訴品 `4TG2-P` 隨機認不到碟 `UART` log.
  * [x] 至 `RMA` 取回 `3ME4` (將異常品 `controller` 換回異常品, 觀看認碟進度).
  * [x] 量測 `Ericssion` `eUSB` `8`pcs 認碟狀況, 並整理.
  * [x] 測試 `Rosch computer` 需要之 `DLMC` tool( `V3.11.0` -> `ROM  mocd` ).
  * [x] 關於 `3ME4` `controller` 異常相關問題.
  * [x] 協助新人錄製 `3TE7` `DLMC` 透過 `ssh` 更新 `FW` 相關影片.
  * [x] 協助新人錄製 `3TE7` `DLMC` 透過 `ssh` 更新 `FW` 相關影片, 並提供工具於 `EU-FAE`.

# 2023-09-04
* 重新錄製 `FRA SYS` 客訴品 `4TG2-P` 隨機認不到碟 `UART` log.
* 至 `RMA` 取回 `3ME4` (將異常品 `controller` 換回異常品, 觀看認碟進度).
* 量測 `Ericssion` `eUSB` `8`pcs 認碟狀況, 並整理.
* 測試 `Rosch computer` 需要之 `DLMC` tool( `V3.11.0` -> `ROM  mocd` ).
* 關於 `3ME4` `controller` 異常相關問題. 
* 提供 `Sales-Joanne` 相關 `X-ray` 照片.
* 協助新人錄製 `3TE7` `DLMC` 透過 `ssh` 更新 `FW` 相關影片, 並提供工具於 `EU-FAE`.
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 架設 `3MR3-P` 執行環境, 並上電錄製 `UART` log,觀看是否可以辨識到.
  * [x] 量測 `Ericssion` `eUSB` `3` pcs 異常品電性量測.
  * [x] 填寫 `3ME4` `controller` 送至原廠分析單, 並回覆原廠相關問題.
  * [x] 觀看 `FRA SYS` 測試狀況.
  * [x] 協助 `EU-FAE` 領取 `CFast card 3IE7`.
  * [x] 協助 `採購` 回覆 `Marvell` 送修相關問題.

# 2023-09-05
* 參與 `FAE-team2` 週會.
* 架設 `3MR3-P` 執行環境, 並上電錄製 `UART` log,觀看是否可以辨識到.
* 量測 `Ericssion` `eUSB` `3` pcs 異常品電性量測.
* 填寫 `3ME4` `controller` 送至原廠分析單, 並回覆原廠相關問題.
* 觀看 `FRA SYS` 測試狀況, 結果與 `JP-PFU` 客訴問題相同, 並將問題回報給 `EU`.
* 協助 `EU-FAE` 領取 `CFast card 3IE7`.
* 協助 `採購` 回覆 `Marvell` 送修相關問題.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `採購` 回覆 `Marvell` 送修相關問題.
  * [x] 與 `Kiwi` 前往 `RMA` 借取 `Marvell` controller sorting board, 並做相關交叉測試驗證.
  * [x] 協助新人回覆 `innoWorks` 相關客訴問題.
  * [x] 協助新人架設 `Ubuntu 16.04` `reboot count` 測試程式.
  * [x] 協助 `FW-RD Allen` 錄製 `SCN` `5` pcs `3MR3-P` 相關 `SMART` info.
  * [x] 協助新人觀看 `3TG6-P` 相關客訴問題.
  * [x] 協助 `EU` 量測 `1`pcs `Ericssion` `eUSB` 之 `Power sequence` `Open short` `Crystal`. 

# 2023-09-06
* 參與 `FAE` 週會.
* 協助 `採購` 回覆 `Marvell` 送修相關問題.
* 與 `Kiwi` 前往 `RMA` 借取 `Marvell` controller sorting board, 並做相關交叉測試驗證.
* 協助新人回覆 `innoWorks` 相關客訴問題.
* 協助新人架設 `Ubuntu 16.04` `reboot count` 測試程式.
* 協助 `FW-RD Allen` 錄製 `SCN` `5` pcs `3MR3-P` 相關 `SMART` info.
* 協助新人觀看 `3TG6-P` 相關客訴問題.
* 協助 `EU` 量測 `1`pcs `Ericssion` `eUSB` 之 `Power sequence` `Open short` `Crystal`. 
* TODO
  * [x] 協助 `EU` 量測 `3`pcs `Ericssion` `eUSB` 之 `Power sequence` `Open short` `Crystal`. 
  * [x] 整理 `3`pcs `Ericssion` `eUSB` 相關測試結果.
  * [x] 協助新人觀看 `innoWorks` 關於 `ssh` 遠端更新操作, 以及 `CFast` 相關問題.
  * [x] 與 `FW-RD Allen` 討論 `3MR3-P` 其中一片無法認碟問題.
  * [x] 詢問 `HW-RD Chiyang` 關於 `eUSB` `1.8V` 的量測.
  * [x] 與 `EU-FAE` 討論客訴案進度狀況.

# 2023-09-07
* 協助 `EU` 量測 `3`pcs `Ericssion` `eUSB` 之 `Power sequence` `Open short` `Crystal`. 
* 整理 `3`pcs `Ericssion` `eUSB` 相關測試結果, 並回報給 `EU`.
* 協助新人觀看 `innoWorks` 關於 `ssh` 遠端更新操作, 以及 `CFast` 相關問題.
* 與 `FW-RD Allen` 討論 `3MR3-P` 其中一片無法認碟問題.
* 詢問 `HW-RD Chiyang` 關於 `eUSB` `1.8V` 的量測.
* 與 `EU-FAE` 討論客訴案進度狀況.
* TODO
  * [x] 撰寫 `Aristacrat` `FA` report.
  * [x] 測試 `3IE7` `80GB` `DLMC` tool.
  * [x] 協助 `FW-RD Allen` 測試 `3MR3-P` `5` pcs 成功進入系統時間(建表完成).
  * [x] 參與 `EU-FAE` 週會.
  * [x] 測試 `Hanel` 平台 usb cable 功能, 以及是否能進入 `bios`.
  * [x] 協助新人觀看 `innoWorks` `CFast card` 相關問題.
  * [x] 協助新人透過烤箱測試 `3MR2-P` 老化驗證.
  * [x] 透過顯微鏡觀看 `Ericssion` `eUSB` `Crystal` 外觀狀況.

# 2023-09-08
* 撰寫 `Aristacrat` `FA` report, 已將初步報告寄出.
* 測試 `3IE7` `80GB` `DLMC` tool, 可正常運行( `S21606i -> S23809i` ).
* 協助 `FW-RD Allen` 測試 `3MR3-P` `5` pcs 成功進入系統時間(建表完成).
* 參與 `EU-FAE` 週會.
* 測試 `Hanel` 平台 usb cable 功能, 以及是否能進入 `bios`, 經過驗證後, 是沒有問題的, 並將結果回覆給 `EU`.
* 協助新人觀看 `innoWorks` `CFast card` 相關問題.
* 協助新人透過烤箱測試 `3MR2-P` 老化驗證.
* 透過顯微鏡觀看 `Ericssion` `eUSB` `Crystal` 外觀狀況.
* TODO
  * [x] 協助 `Alex` 提供透過 `DLMC` tool 進入 `ROM` mode 的資訊.
  * [x] 協助 `Kerry` 提供關於 `3TE6` 2pcs 同時接上認不到碟的問題, 以及解法.
  * [x] 與 `EU-FAE` 討論 `3MR3-P` 後續處理狀況.
  * [x] 協助新人架設 `Power Cycling` 環境.
  * [x] 將 `Ericssion` `eUSB` `BCA12206150155234` 送至 `RMA` 更換 `Crystal`.

# 2023-09-11
* 協助 `Alex` 提供透過 `DLMC` tool 進入 `ROM` mode 的資訊.
* 協助 `Kerry` 提供關於 `3TE6` 2pcs 同時接上認不到碟的問題, 以及解法.
* 與 `EU-FAE` 討論 `3MR3-P` 後續處理狀況.
* 協助新人架設 `Power Cycling` 環境.
* 將 `Ericssion` `eUSB` `BCA12206150155234` 送至 `RMA` 更換 `Crystal`.
* TODO
  * [x] 修改 `FEA230804005` `3TE7` `FA` report.
  * [x] 參與 `FAE-team2` 週會.
  * [x] 協助新人觀看 `innoWorks` `CFast 3ME4` 火車平台客訴案.
  * [x] 詢問 `CN-FAE Rowand` 關於 `USB` analyzer 使用進度.
  * [x] 量測 `FA230828007` `Aristocrat Tech` `3ME4` controller 透過 sorting board 量測 `SATA` analyzer.
  * [x] 協助 `Sales-Vivian` 找尋 `融程科技` 測試平台.

# 2023-09-12
* 修改 `FEA230804005` `3TE7` `FA` report.
* 參與 `FAE-team2` 週會.
* 協助新人觀看 `innoWorks` `CFast 3ME4` 火車平台客訴案.
* 詢問 `CN-FAE Rowand` 關於 `USB` analyzer 使用進度, 預計下週會寄回.
* 量測 `FA230828007` `Aristocrat Tech` `3ME4` controller 透過 sorting board 量測 `SATA` analyzer, 並提供給原廠分析.
* 協助 `Sales-Vivian` 找尋 `融程科技` 測試平台, 並將其歸還給客戶.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 追蹤 `FA230828007` `Aristocrat Tech` 分析進度.
  * [x] 協助新人觀看 `innoWorks` `CFast 3ME4` 火車平台客訴案.
  * [x] 與 `EU-FAE` 討論 `SARL` 客訴案狀況.
  * [x] 協助 `EU-FAE` 查找 `3TE6` `V2111804` & `V2111806` DLMC 相關限制.
  * [x] 協助新人針對 `CFast 3ME4` `2`pcs 執行 `ReMP`.
  * [x] 協助 `Kiwi` 測試 `VN` `3TE7` 於 `UEFI` & `Legacy` mode warm boot 隨機無法認碟問題.
  * [x] 與 `EP Kevin` 討論 `Hanel` 後續出貨驗證流程.
  * [x] 協助 `Sales-Joanne` 將 `Aristocrat Tech` `CFast 3ME4` 送至維修部觀看是否有客戶資料.
  * [x] 與 `Edom-Chad` 討論 `controller` 分析處理狀況.

# 2023-09-13
* 參與 `FAE` 週會.
* 追蹤 `FA230828007` `Aristocrat Tech` 分析進度.
* 協助新人觀看 `innoWorks` `CFast 3ME4` 火車平台客訴案.
* 與 `EU-FAE` 討論 `SARL` 客訴案狀況.
* 協助 `EU-FAE` 查找 `3TE6` `V2111804` & `V2111806` DLMC 相關限制.
* 協助新人針對 `CFast 3ME4` `2`pcs 執行 `ReMP`.
* 協助 `Kiwi` 測試 `VN` `3TE7` 於 `UEFI` & `Legacy` mode warm boot 隨機無法認碟問題.
* 與 `EP Kevin` 討論 `Hanel` 後續出貨驗證流程.
* 協助 `Sales-Joanne` 將 `Aristocrat Tech` `CFast 3ME4` 送至維修部觀看是否有客戶資料.
* 與 `Edom-Chad` 討論 `controller` 分析處理狀況.
* TODO
  * [x] 與 `EU-FAE` 討論 `Hanel` 送至 `RMA` 維修狀況.
  * [x] 協助 `Kiwi` 處理 `M.2` 訊號線焊接(詢問 `RMA` 人員).
  * [x] 協助新人回覆 `innoWokrs` 關於 `mSATA` image 內容相關問題.
  * [x] 取回並測試 `Aristocrat Tech` `CFast 3ME4` 資料內容.
  * [x] 測試 `Ericssion` `3SE eSUB` only `USB 2.0` 辨識問題(更換 `connector`).
  * [x] 協助新人測試 `3ME4` `dd` image 功能.

# 2023-09-14
* 與 `EU-FAE` 討論 `Hanel` 送至 `RMA` 維修狀況.
* 協助 `Kiwi` 處理 `M.2` 訊號線焊接(詢問 `RMA` 人員).
* 協助新人回覆 `innoWokrs` 關於 `mSATA` image 內容相關問題.
* 取回並測試 `Aristocrat Tech` `CFast 3ME4` 資料內容.
* 測試 `Ericssion` `3SE eSUB` only `USB 2.0` 辨識問題(更換 `connector`).
* 協助新人測試 `3ME4` `dd` image 功能.
* TODO
  * [x] 參與 `Ericssion` `eUSB` 分析狀況討論.
  * [x] 與 `Marvell` 代理商討論送驗相關問題, 並將狀況回報給 `Sales-Joanne`.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助新人回覆 `innoWorks` 關於 `GC` & `sector 0` 相關問題.
  * [x] 更新 `eFAE` 客訴案相關進度.

# 2023-09-15
* 參與 `Ericssion` `eUSB` 分析狀況討論.
* 與 `Marvell` 代理商討論送驗相關問題, 並將狀況回報給 `Sales-Joanne`.
* 參與 `EU-FAE` 週會.
* 協助新人回覆 `innoWorks` 關於 `GC` & `sector 0` 相關問題.
* 更新 `eFAE` 客訴案相關進度.
* TODO  
  * [x] 針對 `Ericssion` `eUSB` `BCA12205190324191` 備份資料後, 重新 `Format`, 進行 `50` 次認碟時間.
  * [x] 提供 `Marvell` 代理商相關送驗資訊.
  * [x] 與新人討論 `innoWorks` `3ME4` `FW` `Gen2 & Gen3` 相關問題.
  * [x] 寄送 `Ericssion` `eUSB` `2`pcs 至 `CN` 錄製 `analyzer`.

# 2023-09-18
* 針對 `Ericssion` `eUSB` `BCA12205190324191` 備份資料後, 重新 `Format`, 進行 `50` 次認碟時間.
* 提供 `Marvell` 代理商相關送驗資訊.
* 與新人討論 `innoWorks` `3ME4` `FW` `Gen2 & Gen3` 相關問題.
* 寄送 `Ericssion` `eUSB` `2`pcs 至 `CN` 錄製 `analyzer`.
* 更新 `eFAE` 系統客訴案相關進度.
* TODO
  * [x] 與 `Sales-Joan` 討論 `Simms` 客訴案 `FA` report.
  * [x] 協助新人回答 `innoWorks` 關於 `Sector 0` `GC & wear leveling` 相關問題.
  * [x] 協助新人回答 `innoWorks` 關於 `Ubuntu` `dmesg` 內的 `ATA` command 相關問題.
  * [x] 參與 `EU` 討論 `Ericssion` `eUSB` `BCA12205190324191` 認碟速度較慢的問題.
  * [x] 協助 `EU-FAE` 提供 `DES25-A28D08BC1QC` 開卡包.
  * [x] 將 `BCA12203290522077` 送至 `RMA` 更換回 `old` `Controller`.

# 2023-09-19
* 與 `Sales-Joan` 討論 `Simms` 客訴案 `FA` report, 需修改日期, 以及 `In charge` & `Date`.
* 協助新人回答 `innoWorks` 關於 `Sector 0` `GC & wear leveling` 相關問題.
* 協助新人回答 `innoWorks` 關於 `Ubuntu` `dmesg` 內的 `ATA` command 相關問題.
* 參與 `EU` 討論 `Ericssion` `eUSB` `BCA12205190324191` 認碟速度較慢的問題.
* 協助 `EU-FAE` 提供 `DES25-A28D08BC1QC` 開卡包.
* 將 `BCA12203290522077` 送至 `RMA` 更換回 `old` `Controller`.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 測試 `BCA12203290522077` 更換回 `old` `Controller` 辨識狀況.
  * [x] 將 `Aristocrat Tech` `CFast 3ME4` 欲分析 `Controller` 交至採購寄往原廠分析.
  * [x] 練習 `C++` 相關 function 使用.

# 2023-09-20
* 參與 `FAE` 週會.
* 測試 `BCA12203290522077` 更換回 `old` `Controller` 辨識狀況.
* 將 `Aristocrat Tech` `CFast 3ME4` 欲分析 `Controller` 交至採購寄往原廠分析.
* 練習 `C++` 相關 function 使用.
* TODO
  * [x] 協助新人處理 `VN-Sales` `3TE7` `ReMP` 相關操作.
  * [x] 協助新人回覆 `innoWorks` `mSATA 3SE3` 相關問題.
  * [x] 協助新人處理 `SATADOM` 相關接線問題.
  * [x] 協助組內領出轉板料件.
  * [x] 回報 `EU` `Ericssion` `eUSB` 測試分析狀況.
  * [x] 與 `EU-FAE` 討論 `3ME3` 客訴案處理狀況.

# 2023-09-21
* 協助新人處理 `VN-Sales` `3TE7` `ReMP` 相關操作.
* 協助新人回覆 `innoWorks` `mSATA 3SE3` 相關問題.
* 協助新人處理 `SATADOM` 相關接線問題.
* 協助組內領出轉板料件.
* 回報 `EU` `Ericssion` `eUSB` 測試分析狀況.
* 與 `EU-FAE` 討論 `3ME3` 客訴案處理狀況.
* TODO
  * [x] 協助 `Alan` 觀看 `CIFX 90-E2CO` 相關資訊.
  * [x] 協助新人驗證 `innoWorks` 關於 `hexdump` 資料顯示.
    * [x] `A` device image copy to `B` device.
    * [x] Use same `Ubuntu 22.04` image to install OS in `A` & `B` device. 
  * [x] 協助查找 `innoWorks` 關於 `wear leveling` & `Garbage collection` 動作執行解說影片.
  * [x] 查找 `SODDIMM` 相關 `DRAM`.

# 2023-09-22
* 協助 `Alan` 觀看 `CIFX 90-E2CO` 相關資訊.
* 協助新人驗證 `innoWorks` 關於 `hexdump` 資料顯示.
  * `A` device image copy to `B` device.
  * Use same `Ubuntu 22.04` image to install OS in `A` & `B` device. 
* 協助查找 `innoWorks` 關於 `wear leveling` & `Garbage collection` 動作執行解說影片.
* 查找 `SODDIMM` 相關 `DRAM`.
* TODO
  * [x] 詢問 `Rowand` 關於 `eUSB` 錄製 `analyzer` 相關資訊.
  * [x] 詢問 `Mickey` 關於 `SATADOM` power cable 相關料號.
  * [x] 協助新人觀看 `3TE7` 無法認碟問題.
  * [x] 觀看 `3TG6-P P80` 無法認碟問題.

# 2023-09-23
* 詢問 `Rowand` 關於 `eUSB` 錄製 `analyzer` 相關資訊, 經過討論後, 需寄出信件告知需要量測的動作.
* 詢問 `Mickey` 關於 `SATADOM` power cable 相關料號, 並進行照片查找.
* 協助新人觀看 `3TE7` 無法認碟問題, 經由電路查找, 發現為 `U41` power IC 異常.
* 觀看 `3TG6-P P80` 無法認碟問題, 問題為 `ASSERT: M(3)F(21)L(10506)`, 目前等待 `FW` 驗證.
* TODO
  * [x] 協助新人觀看 `innoWorks` 關於 `wear leveling` & `Garbage collection` 相關問題.
  * [x] 協助 `VN-Sales` 處理 `3TE7` 在當 `OS` System 使用時, 能否進行 `DLMC`(透過 `-j`).
  * [x] 協助新人錄製 `3TE7` `DLMC` tool 操作影片.
  * [x] 與 `Sales-Joan` 討論 `UK004` `3MG2-P` 無法認碟問題.

# 2023-09-25
* 協助新人觀看 `innoWorks` 關於 `wear leveling` & `Garbage collection` 相關問題.
* 協助 `VN-Sales` 處理 `3TE7` 在當 `OS` System 使用時, 能否進行 `DLMC`(透過 `-j`).
* 協助新人錄製 `3TE7` `DLMC` tool 操作影片.
* 與 `Sales-Joan` 討論 `UK004` `3MG2-P` 無法認碟問題.
* TODO
  * [x] 參與 `FAE team2` 週會.
  * [x] 協助 `Sales-Vincent` 討論 `3TG6-P (P80)` 處理狀況以及分享相關異常資訊.
  * [x] 與 `FW-RD Mike` 討論異常資訊處理狀況, 並詢問相關更新流程.
  * [x] 測試 `3TG6-P (P80)` 透過 `DLMC V3.11.0` 更新 `FW`( `C22822` -> `C22822E` ).
  * [x] 與 `CN-FAE` 討論 `eUSB` 錄製之 `analyzer`.
  * [x] 追蹤 `Marvell` 原廠分析進度.

# 2023-09-26
* 參與 `FAE team2` 週會.
* 協助 `Sales-Vincent` 討論 `3TG6-P (P80)` 處理狀況以及分享相關異常資訊.
* 與 `FW-RD Mike` 討論異常資訊處理狀況, 並詢問相關更新流程.
* 測試 `3TG6-P (P80)` 透過 `DLMC V3.11.0` 更新 `FW`( `C22822` -> `C22822E` ).
* 撰寫 `3TG6-P (P80)` 透過 `DLMC V3.11.0` 更新 `FW` 操作文件, 並提供給 `Sales-Vincent`.
* 與 `CN-FAE` 討論 `eUSB` 錄製之 `analyzer`.
* 追蹤 `Marvell` 原廠分析進度, 目前已經異常品 `controller` 送至國外做分析.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 提供 `eUSB` 錄製之 `analyzer` 於 `Hyperstone` 原廠協助分析.
  * [x] 與 `Sales-Vincent` 討論 `3TG6-P (P80)` `FW` 更新相關事項.
  * [x] 協助新人測試 `teamviewer` 遠端更新 `SSD`.

# 2023-09-27
* 參與 `FAE` 週會.
* 提供 `eUSB` 錄製之 `analyzer` 於 `Hyperstone` 原廠協助分析.
* 與 `Sales-Vincent` 討論 `3TG6-P (P80)` `FW` 更新相關事項.
* 協助新人測試 `teamviewer` 遠端更新 `SSD`.
* TODO
  * [x] 協助 `Sales-Vincent` 查找 `FTB221125007` 客訴案內容.
  * [x] 協助 `Kiwi` 查找 `Blue screen` 相關客訴報告.
  * [x] 協助 `Alan` 查找 `Remove PHYID checking` 相關資訊.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助新人 copy `3TE7`.
  * [x] 錄製 `eUSB 3SE` analyzer 於 `hyperstone`.

# 2023-09-28
* 協助 `Sales-Vincent` 查找 `FTB221125007` 客訴案內容.
* 協助 `Kiwi` 查找 `Blue screen` 相關客訴報告.
* 協助 `Alan` 查找 `Remove PHYID checking` 相關資訊.
* 參與 `EU-FAE` 週會.
* 協助新人 copy `3TE7`.
* 錄製 `eUSB 3SE` analyzer 於 `hyperstone`.
* TODO
  * [x] 參與 `FAE` 月會.
  * [x] 協助 `Sales-Joan` 處理 `3MG2-P M.2 SATA SSD (256G) failures (HW-490)` 客戶問題.
  * [x] 與 `CN-Lyle` & `hyperstone Elvis` 討論 `eUSB` analyzer 相關問題.
  * [x] 協助新人處理相關客訴問題.

# 2023-10-02
* 參與 `FAE` 月會.
* 協助 `Sales-Joan` 處理 `3MG2-P M.2 SATA SSD (256G) failures (HW-490)` 客戶問題.
* 與 `CN-Lyle` & `hyperstone Elvis` 討論 `eUSB` analyzer 相關問題.
* 協助新人處理相關客訴問題.
* TODO
  * [x] 撰寫 `Ericssion` 8pcs 客訴案報告.
  * [x] 協助新人處理 `iCF 9000` 客訴問題.
  * [x] 觀看 `B&R` 客訴案( `FEB230911016 - 3MV2-P`).
  * [x] 參與 `FAE-team2` 週會.
  * [x] 請 `CN-Rowand` 協助寄回 `2`pcs devices.

# 2023-10-03
* 撰寫 `Ericssion` 8pcs 客訴案報告.
* 協助新人處理相關客訴問題.
* 觀看 `B&R` 客訴案( `FEB230911016 - 3MV2-P`).
* 參與 `FAE-team2` 週會.
* 請 `CN-Rowand` 協助寄回 `2`pcs devices.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 將 `8`pcs `eUSB` 送至 `RMA` 透過 `X-ray` 觀看 connector.
  * [x] 撰寫 `B&R` 客訴案報告.
  * [x] 撰寫 `Ericssion` 8pcs 客訴案報告.
  * [x] 與 `Kiwi` 討論 `FEA230526003` 相關客戶問題回覆.
  * [x] 協助 `Sales-Vincent` 提供 `DLMC` tool.

# 2023-10-04
* 參與 `FAE` 週會.
* 將 `8`pcs `eUSB` 送至 `RMA` 透過 `X-ray` 觀看 connector.
* 撰寫 `B&R` 客訴案報告.
* 撰寫 `Ericssion` 8pcs 客訴案報告.
* 與 `Kiwi` 討論 `FEA230526003` 相關客戶問題回覆.
* 協助 `Sales-Vincent` 提供 `DLMC` tool.
* TODO
  * [x] 協助 `Sales-Joan` 回覆 `FEA230526003` 客訴案問題.
  * [x] 協助 `Sales-Vincent` 處理 `PCIe 3TG6-P` 無法 `DLMC` 問題.
  * [x] 通知 `CN-FAE` 將 `Ericssion` `eUSB` 送回 `HQ`.
  * [x] 協助 `Sales-Joan` 與 `PM-Jack` 詢問 `PCN` 相關修改事項.
  * [x] 測試 `EU` `SATA 3ME3` `controller` 重新回焊認碟狀況.

# 2023-10-05
* 協助 `Sales-Joan` 回覆 `FEA230526003` 客訴案問題.
* 協助 `Sales-Vincent` 處理 `PCIe 3TG6-P` 無法 `DLMC` 問題, 經過詢問後, 發現原因應該為客戶端 `OS` 為客製化 `OS`, 可能就會造成 `DLMC` 出現異常.
* 通知 `CN-FAE` 將 `Ericssion` `eUSB` 送回 `HQ`, 預計連假後寄回 `HQ`.
* 協助 `Sales-Joan` 與 `PM-Jack` 詢問 `PCN` 相關修改事項, 卻只修改 `power IC`.
* 測試 `EU` `SATA 3ME3` `controller` 重新回焊認碟狀況, 有出現假性認碟狀況, 後續已將 `device` 送至 `RMA` 更換新 `controller`.
* TODO
  * [x] 協助 `Sales-Vincent` 錄製 `3TG6-P` 當 `OS` disk 執行 `DLMC` 狀況.
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `EU-FAE` 詢問關於 `NCQ` 相關問題.
  * [x] 協助新人觀看 `innoWorks` 客訴問題.

# 2023-10-06
* 協助 `Sales-Vincent` 錄製 `3TG6-P` 當 `OS` disk 執行 `DLMC` 狀況.
* 參與 `EU-FAE` 週會.
* 協助 `EU-FAE` 詢問關於 `NCQ` 相關問題.
* 協助新人觀看 `innoWorks` 客訴問題.
* 測試 `Windows 7` OS 安裝.
* TODO
  * [x] 協助新人測試 `mSATA 3ME3` `invalid count = 2048`, 造成 `data lose` 相關實驗.
  * [x] 測試 `Windows 7` OS 安裝.
  * [x] 協助 `Kiwi` 觀看 `TCG opal` 相關架設.
  * [x] 協助 `EU-FAE` 借出樣品.
  * [x] 協助新人架設 `SATADOM` 測試環境.
  * [x] 協助 `EU-FAE` 回覆 `4TG2-P` `Thermal Throttling` `FW` update 問題.
  * [x] 協助新人製作 `Ubuntu 22.04 Server` 安裝 disk.

# 2023-10-11
* 協助新人測試 `mSATA 3ME3` `invalid count = 2048`, 造成 `data lose` 相關實驗.
* 測試 `Windows 7` OS 安裝.
* 協助 `Kiwi` 觀看 `TCG opal` 相關架設.
* 協助 `EU-FAE` 借出樣品.
* 協助新人架設 `SATADOM` 測試環境.
* 協助 `EU-FAE` 回覆 `4TG2-P` `Thermal Throttling` `FW` update 問題.
* 協助新人製作 `Ubuntu 22.04 Server` 安裝 disk.
* TODO
  * [x] 協助 `EU-FAE` 處理 `4TG2-P` 樣品借出 & `DLMC` tool.
  * [x] 協助 `EU-FAE` 查找 `FED230609011` `3TE6` 客訴品位置( `YCA12302020080032` ).
  * [x] 協助 `Sales-Cindy` 處理 `CFast 3IE7` `DLMC` tool.
  * [x] 協助新人於 `SATADOM` 安裝 `Ubuntu 22.04 Server`.
  * [x] 協助新人詢問關於每版 `FW` 相關驗證報告. 

# 2023-10-12
* 協助 `EU-FAE` 處理 `4TG2-P` 樣品借出 & `DLMC` tool, 並提供相關影片, `U.2` 於 `Ubuntu` 執行 `DLMC` tool 缺少相關轉板, 暫無法執行.
* 協助 `EU-FAE` 查找 `FED230609011` `3TE6` 客訴品位置( `YCA12302020080032` ).
* 協助 `Sales-Cindy` 處理 `CFast 3IE7` `DLMC` tool.
* 協助新人於 `SATADOM` 安裝 `Ubuntu 22.04 Server`.
* 協助新人詢問關於每版 `FW` 相關驗證報告. 
* TODO
  * [x] 協助 `EU-FAE` 詢問關於 `4TG2-P` 於 `Ubuntu` 透過 `nvme-cli` 執行 `DLMC` 相關指令, 以及更新步驟.
  * [x] 協助 `EU-FAE` 提供 `4TG2-P` 於 `Ubuntu` 透過 `nvme-cli` 執行 `DLMC` 驗證影片.
  * [x] 取回 `RMA` 維修之 `SATA 2.5 3ME3`, 並執行相關測試.
  * [x] 觀看 `艾東` 客訴案(`mSATA 3IE4`).
  * [x] 參與 `EU-FAE` 週會.

# 2023-10-13
* 協助 `EU-FAE` 詢問關於 `4TG2-P` 於 `Ubuntu` 透過 `nvme-cli` 執行 `DLMC` 相關指令, 以及更新步驟.
* 協助 `EU-FAE` 提供 `4TG2-P` 於 `Ubuntu` 透過 `nvme-cli` 執行 `DLMC` 驗證影片.
* 取回 `RMA` 維修之 `SATA 2.5 3ME3`, 並執行相關測試.
* 觀看 `艾東` 客訴案(`mSATA 3IE4`).
* 參與 `EU-FAE` 週會.
* TODO
  * [x] 建立 `艾東` 客訴案(`mSATA 3IE4`) 於 `TTS`.
  * [x] 協助新人觀看 `SATADOM` 安裝 `Ubuntu Server` 問題.
  * [x] 測試 `SATA 2.5 3ME3` 不同版 `FW`(`Mode: Legacy`), 觀看 `log`.
  * [x] 提供並回覆 `eUSB` 相關資訊於 `Hyperstone` 人員.
  * [x] 寄送良品 `eUSB` 於 `Hyperstone` 人員.

# 2023-10-16
* 建立 `艾東` 客訴案(`mSATA 3IE4`) 於 `TTS`.
* 協助新人觀看 `SATADOM` 安裝 `Ubuntu Server` 問題.
* 測試 `SATA 2.5 3ME3` 不同版 `FW`(`Mode: Legacy`), 觀看 `log`.
* 提供並回覆 `eUSB` 相關資訊於 `Hyperstone` 人員.
* 寄送良品 `eUSB` 於 `Hyperstone` 人員.
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 協助 `Sales-Vincent` 處理 `特裁申請`.
  * [x] 協助 `Sales-Vivian` 回覆 `艾夏` 客訴案分析進度.
  * [x] 協助 `FW RD-Eddie` dump `艾夏` 客訴品相關 `UART` log.
  * [x] 協助詢問 `Sales-Joan` 關於兩筆客訴案後續處理.
  * [x] 協助 `PM-Jack` & `EU` 量測 `Winsys` `4999`pcs 客退品使用問題.

# 2023-10-17
* 參與 `FAE-team2` 週會.
* 協助 `Sales-Vincent` 處理 `特裁申請`.
* 協助 `Sales-Vivian` 回覆 `艾夏` 客訴案分析進度.
* 協助 `FW RD-Eddie` dump `艾夏` 客訴品相關 `UART` log.
* 協助詢問 `Sales-Joan` 關於兩筆客訴案後續處理.
* 協助 `PM-Jack` & `EU` 量測 `Winsys` `4999`pcs 客退品使用問題.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 整理 `Winsys` `8pcs` 量測結果.
  * [x] 詢問 `FW RD-Eddie` 關於 `艾夏` 客訴品分析結果.
  * [x] 參與 `EU` 會議討論 `Winsys` 量測.
  * [x] 協助 `Kiwi` 測試 `3TE6` 開卡包 `EUI64` 功能.
  * [x] 協助新人觀看 `Innoworks` `3ME3` 客訴報告.

# 2023-10-18
* 參與 `FAE` 週會.
* 整理 `Winsys` `8pcs` 量測結果.
* 詢問 `FW RD-Eddie` 關於 `艾夏` 客訴品分析結果.
* 參與 `EU` 會議討論 `Winsys` 量測.
* 協助 `Kiwi` 測試 `3TE6` 開卡包 `EUI64` 功能.
* 協助新人觀看 `Innoworks` `3ME3` 客訴報告.
* TODO
  * [x] 整理並測試 `Winsys` 退回客訴品( 8箱內所有的 `device` 盒子, 各取一片出來, 共 `76`pcs ).
  * [x] 協助新人觀看 `Innoworks` 客訴案.
  * [x] 協助 `Jason` 查詢 `Vector` `RAID` 量測相關紀錄.

# 2023-10-19
* 整理並測試 `Winsys` 退回客訴品( 8箱內所有的 `device` 盒子, 各取一片出來, 共 `76`pcs ), 目前已量測 `26`pcs, 並錄製相關影片.
* 協助新人觀看 `Innoworks` 客訴案.
* 協助 `Jason` 查詢 `Vector` `RAID` 量測相關紀錄.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 協助 `PM-Jack` & `PM-Alfie` 繼續量測 `Winsys` 退回客訴品剩餘 `50`pcs.
  * [x] 整理 `Winsys` 退回客訴品測試結果.
  * [x] 協助 `RD-Ray` 錄製 `Winsys` 退回客訴品( `Normal` & `Fail` sample ) `SATA analyzer`.
  * [x] 協助新人安裝 `Fedora` OS 於 `SATADOM`.
  * [x] 協助新人量測 `3TE6` `ReMP`( `V211180A` -> `V22620` ).
  * [x] 協助新人觀看 `innoWorks` 客訴案報告.
  * [x] 處理 `SATA 2.5 3TG6-P` 更新 `FW`. 
  * [x] 追蹤 `Ericssion` 分析狀況.

# 2023-10-20
* 參與 `EU-FAE` 週會.
* 協助 `PM-Jack` & `PM-Alfie` 繼續量測 `Winsys` 退回客訴品剩餘 `50`pcs.
* 整理 `Winsys` 退回客訴品測試結果, 並提供給相關人員.
* 協助 `RD-Ray` 錄製 `Winsys` 退回客訴品( `Normal` & `Fail` sample ) `SATA analyzer`.
* 協助新人安裝 `Fedora` OS 於 `SATADOM`, 目前尚未完成.
* 協助新人量測 `3TE6` `ReMP`( `V211180A` -> `V22620` ).
* 協助新人觀看 `innoWorks` 客訴案報告.
* 處理 `SATA 2.5 3TG6-P` 更新 `FW`, 目前尚未處理完成. 
* 追蹤 `Ericssion` 分析狀況.
* TODO
  * [x] 與 `FW RD-Allen` sync `3TE7` `DLMC` `Jump ROM` 相關問題.
  * [x] 協助新人將 `iCF Card` 送至 `RMA`.
  * [x] 協助新人安裝 `Fedora` OS 於 `SATADOM`.
  * [x] 協助新人將 `SATADOM` 送至 `RMA` 照 `X-ray`.
  * [x] 處理 `SATA 2.5 3TG6-P` 更新 `FW`.
  * [x] 詢問補打卡相關問題.
  * [x] 追蹤 `Ericssion` 分析狀況, 並回覆 `Hyperstone` 人員相關問題.

# 2023-10-23
* 與 `FW RD-Allen` sync `3TE7` `DLMC` `Jump ROM` 相關問題.
* 協助新人將 `iCF Card` 送至 `RMA`.
* 協助新人安裝 `Fedora` OS 於 `SATADOM`, 安裝完成後, 觀看 `partition` 皆為 `unknow partition`, 後續需錄製相關 `UART` log.
* 協助新人將 `SATADOM` 送至 `RMA` 照 `X-ray`.
* 處理 `SATA 2.5 3TG6-P` 更新 `FW`, 已完成更新(需要使用舊平台更新).
* 詢問補打卡相關問題.
* 追蹤 `Ericssion` 分析狀況, 並回覆 `Hyperstone` 人員相關問題.
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 協助新人觀看 `SATADOM` 問題.
  * [x] 查找轉板裝上開關電路.
  * [x] 與 `FW-RD` 討論 `Winsys` 系統擋相關差異, 並與 `PM-Alfie` & `PM-Jack` 討論.

# 2023-10-24
* 參與 `FAE-team2` 週會.
* 協助新人觀看 `SATADOM` 問題.
* 查找轉板裝上開關電路.
* 與 `FW-RD` 討論 `Winsys` 系統擋相關差異, 並與 `PM-Alfie` & `PM-Jack` 討論.
* TODO
  * [x] 與 `PM-Alfie` & `PM-Jack` 討論 `Winsys` 客訴案.
  * [x] 協助 `FW-RD` 測試 `Winsys` 解鎖過程斷電相關現象.
  * [x] 與 `Sales-Joan` 討論 `Simms` 客訴案( `M.2 (P42) 3TE7` & `M.2 (P42) 3TE2` ) 後續處理.
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `Kiwi` 建立 `3ME4` `power cycle count` issue 於 `TTS`.

# 2023-10-25
* 與 `PM-Alfie` & `PM-Jack` 討論 `Winsys` 客訴案.
* 協助 `FW-RD` 測試 `Winsys` 解鎖過程斷電相關現象.
* 與 `Sales-Joan` 討論 `Simms` 客訴案( `M.2 (P42) 3TE7` & `M.2 (P42) 3TE2` ) 後續處理.
* 參與 `FAE` 週會.
* 協助 `Kiwi` 建立 `3ME4` `power cycle count` issue 於 `TTS`.
* TODO
  * [x] 協助 `Kiwi` 架設 `鼎通盛` 測試環境, 並錄製 `UART` log.
  * [x] 協助 `Eva` 驗證及打包 `DLMC` 流程工具.
  * [x] 協助 `Sales-Joan` 處理 `3TE7` `Re-MP` 到 `iSLC 160GB`, 並修改 `Disk Label`.
  * [x] 與 `FW-RD Weiting` 討論 `3ME4` `power cycle count` issue 測試手法.
  * [x] 參與 `FAE` 月會.
  * [x] 協助 `Sales-Joan` 詢問 `SATA 3TE7` 掉速相關問題.
  * [x] 分析 `Ericssion` `eUSB` `辨識` ＆ `電性量測`, 並將 `Device` 送至 `SMT` 照 `Controller` & `Flash` `X-ray`.
  * [x] 協助 `Jay` 修改 `DLMC` 根據 `Capacity` 判斷 `FW` bin file 之 `Shell script`.

# 2023-10-26
* 協助 `Kiwi` 架設 `鼎通盛` 測試環境, 並錄製 `UART` log.
* 協助 `Eva` 驗證及打包 `DLMC` 流程工具.
* 協助 `Sales-Joan` 處理 `3TE7` `Re-MP` 到 `iSLC 160GB`, 並修改 `Disk Label`.
* 與 `FW-RD Weiting` 討論 `3ME4` `power cycle count` issue 測試手法.
* 參與 `FAE` 月會.
* 協助 `Sales-Joan` 詢問 `SATA 3TE7` 掉速相關問題.
* 分析 `Ericssion` `eUSB` `辨識` ＆ `電性量測`, 並將 `Device` 送至 `SMT` 照 `Controller` & `Flash` `X-ray`.
* 協助 `Jay` 修改 `DLMC` 根據 `Capacity` 判斷 `FW` bin file 之 `Shell script`.
* TODO
  * [x] 整理 `Ericssion` `eUSB` 相關實驗數據.
  * [x] 協助 `Sales-Joan` 觀看 `solidstatedisks` 關於 `3TE7` 同時插上 `2`pcs `Device`, 無法認碟問題. 
  * [x] 撰寫 `艾夏` `mSATA 3TE7` `FA report`.
  * [x] 協助 `EU FAE` 詢問廠區是否有熱成像儀.
  * [x] 與 `EU FAE` 討論關於 `DLMC` `V3.9.0(Mode 7 + WP)` 上鎖相關資訊.
  * [x] 詢問 `FW RD` 關於　`3TE7` 掉速相關可能.

# 2023-10-27
* 整理 `Ericssion` `eUSB` 相關實驗數據.
* 協助 `Sales-Joan` 觀看 `solidstatedisks` 關於 `3TE7` 同時插上 `2`pcs `Device`, 無法認碟問題. 
* 撰寫 `艾夏` `mSATA 3TE7` `FA report`, 並提供給 `Sales-Vivian`.
* 協助 `EU FAE` 詢問廠區是否有熱成像儀, 結果是沒有.
* 與 `EU FAE` 討論關於 `DLMC` `V3.9.0(Mode 7 + WP)` 上鎖相關資訊, 只適用於 `3ME4`.
* 詢問 `FW RD` 關於　`3TE7` 掉速相關可能.
* TODO
  * [x] 參與公司運動會.

# 2023-10-30
* 參與公司運動會.
* TODO
  * [x] 協助了解 `3TE7` 同時插上 `2`pcs `Device`, 無法認碟問題, 並與 `Sales` 討論後續處理方式.
  * [x] 撰寫 `Ericssion` `10`pcs 初步報告.
  * [x] 撰寫 `Ericssion` `8`pcs `FA` report 結論.
  * [x] 協助回覆 `Sales-Vivian` 關於 `艾夏` `mSATA 3TE7` `FA report` 問題.
  * [x] 與 `FW RD Eddie` 討論 `3ME4` `Erase error` 分析進度, 並協助詢問破壞性實驗手法.
  * [x] 與 `Sales-Joanne` 討論 `Aristocrat CFast 3ME4` 無法辨識問題原廠分析報告.
  * [x] 協助 `Kiwi` 傳送 `週會報告`.
  * [x] 協助 `Alex` 回覆關於 `DLMC` `FW Verify` 相關操作.
  * [x] 協助新人觀看 `3TE6` 更新相關客訴問題.

# 2023-10-31
* 協助了解 `3TE7` 同時插上 `2`pcs `Device`, 無法認碟問題, 並與 `Sales` 討論後續處理方式.
* 撰寫 `Ericssion` `10`pcs 初步報告.
* 撰寫 `Ericssion` `8`pcs `FA` report 結論.
* 協助回覆 `Sales-Vivian` 關於 `艾夏` `mSATA 3TE7` `FA report` 問題.
* 與 `FW RD Eddie` 討論 `3ME4` `Erase error` 分析進度, 並協助詢問破壞性實驗手法.
* 與 `Sales-Joanne` 討論 `Aristocrat CFast 3ME4` 無法辨識問題原廠分析報告.
* 協助 `Kiwi` 傳送 `週會報告`.
* 協助 `Alex` 回覆關於 `DLMC` `FW Verify` 相關操作.
* 協助新人觀看 `3TE6` 更新相關客訴問題.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `Sales-Joan` 回覆 `3TE7` 掉速客訴問題.
  * [x] 撰寫 `Ericssion` `8`pcs `FA` report & `10`pcs `first` draft `FA` report.
  * [x] 與 `Miller` & `EU-FAE` 討論 `Ericssion` 2筆 `FA` report.
  * [x] 協助新人架設 `Fedora` Server 於 `SATADOM`.
  * [x] 與 `Alex` 討論 `DLMC` tool 中的 `FW Verify` 相關功能.
  * [x] 參與研發部月會.
  * [x] 參與 `EU` 關於 `Eurcompus` `Winsys` 討論會議.

# 2023-11-01
* 參與 `FAE` 週會.
* 協助 `Sales-Joan` 回覆 `3TE7` 掉速客訴問題.
* 撰寫 `Ericssion` `8`pcs `FA` report & `10`pcs `first` draft `FA` report.
* 與 `Miller` & `EU-FAE` 討論 `Ericssion` 2筆 `FA` report.
* 協助新人架設 `Fedora` Server 於 `SATADOM`.
* 與 `Alex` 討論 `DLMC` tool 中的 `FW Verify` 相關功能.
* 參與研發部月會.
* 參與 `EU` 關於 `Eurcompus` `Winsys` 討論會議.
* TODO
  * [x] 協助 `PM-Jack` 測試 `mSATA 3TE7 Bisc5` 於 `Winsys` 進行異常上斷電測試.
  * [x] 與 `EU-PM` 討論 `Winsys` 測試相關流程.
  * [x] 與 `EU-FAE` 討論 `Ericssion` 後續分析動作.
  * [x] 於 `RMA` 取回 `Ericssion` `3`pcs 異常品, 並做相關驗證測試.
  * [x] 與 `Sales-Joanne` 討論 `Aristocrat CFast 3ME4` 原廠報告.
  * [x] 詢問 `Jay` 關於 `3TE2` 開卡相關操作.

# 2023-11-02
* 協助 `PM-Jack` 測試 `mSATA 3TE7 Bisc5` 於 `Winsys` 進行異常上斷電測試.
* 與 `EU-PM` 討論 `Winsys` 測試相關流程.
* 與 `EU-FAE` 討論 `Ericssion` 後續分析動作.
* 於 `RMA` 取回 `Ericssion` `3`pcs 異常品, 並做相關驗證測試.
* 與 `Sales-Joanne` 討論 `Aristocrat CFast 3ME4` 原廠報告.
* 詢問 `Jay` 關於 `3TE2` 開卡相關操作.
* TODO
  * [x] 上午請假 `3` 小時.
  * [x] 協助 `Danny` 觀看示波器操作.
  * [x] 協助 `Kiwi` 觀看 `3MG2-P` 出現 `SMART` error 相關異常訊息問題.
  * [x] 協助 `FW RD Weiting` 測試 `3ME4` `Abnormal power cycle count` fix bin file.
  * [x] 協助新人製作 `3ME4` `DLMC` ro `L23721` image.

# 2023-11-03
* 上午請假 `3` 小時.
* 協助 `Danny` 觀看示波器操作.
* 協助 `Kiwi` 觀看 `3MG2-P` 出現 `SMART` error 相關異常訊息問題.
* 協助 `FW RD Weiting` 測試 `3ME4` `Abnormal power cycle count` fix bin file.
* 協助新人製作 `3ME4` `DLMC` ro `L23721` image.
* TODO
  * [x] 與 `EU-FAE` sync 目前 `Ericssion` 分析狀況.
  * [x] 與 `Weiting` 討論 `3ME4` 修正 `Abnormal power cycle count` 外顯名稱.
  * [x] 與 `EU-PM` 討論 `Winsys` 測試內容.
  * [x] 協助 `Jay` 測試 `2SE2` USB 電性測試, 以及故障零件電路查找.
  * [x] 進行 `Ericssion` 客退品電路相關分析( `short` & `crystal` ).

# 2023-11-06
* 與 `EU-FAE` sync 目前 `Ericssion` 分析狀況.
* 與 `Weiting` 討論 `3ME4` 修正 `Abnormal power cycle count` 外顯名稱.
* 與 `EU-PM` 討論 `Winsys` 測試內容.
* 協助 `Jay` 測試 `2SE2` USB 電性測試, 以及故障零件電路查找.
* 進行 `Ericssion` 客退品電路相關分析( `short` & `crystal` ).
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 協助新人安裝 `Fedora` 於 `SATADOM`.
  * [x] 觀看 `Windows IOT` 更新 `NVME controller` driver.
  * [x] 觀看 `M.2 3MG2-P` 於 Linux 發生 `SMART` error 相關問題.
  * [x] 處理 `3ME4` `FW` 客製申請單.  

# 2023-11-07
* 參與 `FAE-team2` 週會.
* 協助新人安裝 `Fedora` 於 `SATADOM`.
* 觀看 `Windows IOT` 更新 `NVME controller` driver.
* 觀看 `M.2 3MG2-P` 於 Linux 發生 `SMART` error 相關問題.
* 處理 `3ME4` `FW` 客製申請單.  
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `Danny` 處理 `FIO` 相關測試.
  * [x] 透過 `Ubuntu` 相關 disk health check tool 測試 disk 相關狀況.
  * [x] 與 `FW RD` 討論 `3ME4` `erase error` 相關分析狀況.
  * [x] 協助新人架設 `nano SSD 3TE7` 客戶平台低溫測試( `-35` ).
  * [x] 協助新人錄製 `SATADOM 3TE7` 關於 `SSH` 相關驗證影片.

# 2023-11-08
* 參與 `FAE` 週會.
* 協助 `Danny` 處理 `FIO` 相關測試.
* 透過 `Ubuntu` 相關 disk health check tool 測試 disk 相關狀況, 並發信給 `SMI` 原廠詢問此異常現象問題產生, 原廠回覆是 `Hardware ECC` 過高, 導致的告警現象.
* 與 `FW RD` 討論 `3ME4` `erase error` 相關分析狀況.
* 協助新人架設 `nano SSD 3TE7` 客戶平台低溫測試( `-35` ).
* 協助新人錄製 `SATADOM 3TE7` 關於 `SSH` 相關驗證影片.
* TODO
  * [x] 回覆 `鼎通盛` 關於 `3TE7` 降速相關問題, 並做相關測試.
  * [x] 將 `Ericssion` 2pcs 異常品送至 `RMA` 更換零件( `Crystal` & `Controller` ).
  * [x] 協助新人測試 `nano SSD 3TE7` 於客戶平台錄製相關 `UART` log.
  * [x] 協助 `Sales-Vivian` 處理 `艾夏` 相關客訴, 並協助回覆客戶相關問題.
  * [x] 與 `FW RD` 了解 `3ME4` 發生 `erase error` 相關原理.
  * [x] 撰寫 `艾夏` `3ME4` `erase error` `FA` report.
  * [x] 依照 `SMI` 原廠回覆, 對 `3MG2-P` 進行相關老化測試, 驗證 `Hardware ECC` 產生過多造成的 error message. 

# 2023-11-09
* 回覆 `鼎通盛` 關於 `3TE7` 降速相關問題, 並做相關測試.
* 將 `Ericssion` 2pcs 異常品送至 `RMA` 更換零件( `Crystal` & `Controller` ).
* 協助新人測試 `nano SSD 3TE7` 於客戶平台錄製相關 `UART` log, 因不知客戶 `buadrate` 相關設定, 故無法錄製 log.
* 協助 `Sales-Vivian` 處理 `艾夏` 相關客訴, 並協助回覆客戶相關問題.
* 與 `FW RD` 了解 `3ME4` 發生 `erase error` 相關原理.
* 撰寫 `艾夏` `3ME4` `erase error` `FA` report.
* 依照 `SMI` 原廠回覆, 對 `3MG2-P` 進行相關老化測試, 驗證 `Hardware ECC` 產生過多造成的 error message.
* TODO
  * [x] 參與 `EU-FAE` 週會.
  * [x] 測試 `鼎通盛` 關於 `3TE7` 降速驗證.
  * [x] 觀看 `3MG2-P` 寫入測試狀況, 並觀察 `Hardware ECC` 是否有大量增加.
  * [x] 協助 `Sales-Lisa` 轉送 `FAE` 案件.
  * [x] 測試 `Ericssion` `eUSB` 更換 `controller` 後狀況.
  * [x] 撰寫 `艾夏` `3ME4` 客訴案 `FA` report.

# 2023-11-10
* 參與 `EU-FAE` 週會.
* 測試 `鼎通盛` 關於 `3TE7` 降速驗證.
* 觀看 `3MG2-P` 寫入測試狀況, 並觀察 `Hardware ECC` 是否有大量增加.
* 協助 `Sales-Lisa` 轉送 `FAE` 案件.
* 測試 `Ericssion` `eUSB` 更換 `controller` 後狀況.
* 撰寫 `艾夏` `3ME4` 客訴案 `FA` report.
* TODO
  * [x] 協助 `Sales-Joan` 處理 `3MG2-P` `Hardware ECC` 相關客戶問題.
  * [x] 協助新人測試 `nano SSD 3TE7` 錄製 `UART` log.
  * [x] 協助新人查找 `Windows 10 LTSC 1809` 更新至 `21H2` 相關方法.
  * [x] 協助 `EP-Peiwen` 觀看 `eUSB` partition table 切割問題.
  * [x] 撰寫 `Ericssion` `10`pcs `FA` report, 並提供給 `EU`. 

# 2023-11-13
* 協助 `Sales-Joan` 處理 `3MG2-P` `Hardware ECC` 相關客戶問題.
* 協助新人測試 `nano SSD 3TE7` 錄製 `UART` log.
* 協助新人查找 `Windows 10 LTSC 1809` 更新至 `21H2` 相關方法.
* 協助 `EP-Peiwen` 觀看 `eUSB` partition table 切割問題.
* 撰寫 `Ericssion` `10`pcs `FA` report, 並提供給 `EU`. 
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 協助回覆 `鼎通盛-May` 相關測速問題.
  * [x] 協助詢問 `EU-Simon` 關於 `3MG2-P` `Hardware ECC` 相關操作, 以及回報目前測試狀況.
  * [x] 協助 `PM-Micky` 回覆關於 `Ericssion` `eUSB` 相關問題.
  * [x] 協助 `Sales-Vivian` 提供 `InnoOSR` 相關工具.
  * [x] 協助 `Danny` 操作 `3TG6-P` `write code` 功能.
  * [x] 請教 `Kiwi` 關於 `3IE4` 開卡相關設定.

# 2023-11-14
* 參與 `FAE-team2` 週會.
* 協助回覆 `鼎通盛-May` 相關測速問題.
* 協助詢問 `EU-Simon` 關於 `3MG2-P` `Hardware ECC` 相關操作, 以及回報目前測試狀況.
* 協助 `PM-Micky` 回覆關於 `Ericssion` `eUSB` 相關問題.
* 協助 `Sales-Vivian` 提供 `InnoOSR` 相關工具.
* 協助 `Danny` 操作 `3TG6-P` `write code` 功能.
* 請教 `Kiwi` 關於 `3IE4` 開卡相關設定.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助新人測試 `nano SSD 3TE7` 錄製 `UART` log 相關測試.
  * [x] 詢問 `FW RD` 關於 `3TE7` `512GB` 於高溫無法恢復速度問題.
  * [x] 協助 `EP-Peiwen` 觀看 `eUSB` partition table 切割問題.
  * [x] 協助處理 `3TE2` DLMC `FW` 外顯問題.
  * [x] 與 `EU-FAE` 討論 `eUSB` partition table 問題.
  * [x] 協助 `Sales-Joan` 回答客戶相關問題, 以及進度.

# 2023-11-15
* 參與 `FAE` 週會.
* 協助新人測試 `nano SSD 3TE7` 錄製 `UART` log 相關測試, 發現版端上的 `pin` 都無法錄製相關訊息, 後續會在詢問客戶線路圖資訊.
* 詢問 `FW RD` 關於 `3TE7` `512GB` 於高溫無法恢復速度問題, 目前還再詢問 `FW RD`.
* 協助 `EP-Peiwen` 觀看 `eUSB` partition table 切割問題.
* 協助處理 `3TE2` DLMC `FW` 外顯問題, 已確定完畢, 需要 `FW RD` 協助修改外顯.
* 與 `EU-FAE` 討論 `eUSB` partition table 問題.
* 協助 `Sales-Joan` 回答客戶相關問題, 以及進度, 已全部回覆.
* TODO
  * [x] 協助處理 `eUSB` partition table 切割問題.
  * [x] 測試 `3TE2` `DLMC` 相關功能.
  * [x] 協助 `EU` 發信詢問 `Hyperstone` 關於後續問題分析狀況. 
  * [x] 協助新人詢問客戶關於 `Korea` `NANO SSD` 相關 `UART` 錄製問題.
  * [x] 與 `EP-Peiwen` sync `eUSB` partition table 問題.
  * [x] 詢問客戶關於 `3SE2-P` 上斷電時間相關測試參數.
  * [x] 詢問 `FW RD` 關於 `3TE7` `512GB` 於高溫無法恢復速度問題, 並回覆給客戶.
  * [x] 協助新人前往 `SW RD` 討論 `3TE6` `04 & 0A` `DLMC` 相關流程.
  * [x] 與 `EU FAE` 討論 `eUSB` partition table 問題.

# 2023-11-16
* 協助處理 `eUSB` partition table 切割問題.
* 測試 `3TE2` `DLMC` 相關功能.
* 協助 `EU` 發信詢問 `Hyperstone` 關於後續問題分析狀況. 
* 協助新人詢問客戶關於 `Korea` `NANO SSD` 相關 `UART` 錄製問題.
* 與 `EP-Peiwen` sync `eUSB` partition table 問題.
* 詢問客戶關於 `3SE2-P` 上斷電時間相關測試參數.
* 詢問 `FW RD` 關於 `3TE7` `512GB` 於高溫無法恢復速度問題, 並回覆給客戶.
* 協助新人前往 `SW RD` 討論 `3TE6` `04 & 0A` `DLMC` 相關流程.
* 與 `EU FAE` 討論 `eUSB` partition table 問題.
* TODO
  * [x] 參與 `EU FAE` 週會.
  * [x] 測試 `3SE2-P` 依照客戶上斷電時間參數, 測試認碟狀況.
  * [x] 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作.
  * [x] 協助測試 `Tritech` `3TE6` 執行 `Burnintest`, 觀看是否會掉碟.
  * [x] 協助新人撈取 `NANO SSD` 相關 `syslog` & `kernel log`.
  * [x] 協助 `EU-Sales` 歸還 `Asrock` 平台, 並查找 `Device`.

# 2023-11-17
* 參與 `EU FAE` 週會.
* 測試 `3SE2-P` 依照客戶上斷電時間參數, 測試認碟狀況, 客戶尚未回覆.
* 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作, 目前尚未拿到 `Disk`.
* 協助測試 `Tritech` `3TE6` 執行 `Burnintest`, 觀看是否會掉碟.
* 協助新人撈取 `NANO SSD` 相關 `syslog` & `kernel log`.
* 協助 `EU-Sales` 歸還 `Asrock` 平台, 並查找 `Device`, 但 `Device` 尚未找到.
* TODO
  * [x] 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作.
  * [x] 測試 `3SE2-P` 依照客戶上斷電時間參數, 測試認碟狀況.
  * [x] 觀看 `Tritech` `3TE6` 執行 `Burnintest` 結果.
  * [x] 協助 `PM-Davis` 測試 `3TO7` `innoOSR` `LED` 顯示, 以及運行功能.
  * [x] 協助 `EU-Sales` 歸還相關客訴品( `Ericssion` `20pcs` & `KEBA` `CFast 3IE7` ).

# 2023-11-20
* 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作, 目前尚未拿到 `device`.
* 測試 `3SE2-P` 依照客戶上斷電時間參數, 測試認碟狀況, 客戶尚未回覆.
* 觀看 `Tritech` `3TE6` 執行 `Burnintest` 結果.
* 協助 `PM-Davis` 測試 `3TO7` `innoOSR` `LED` 顯示, 以及運行功能.
* 協助 `EU-Sales` 歸還相關客訴品( `Ericssion` `20pcs` & `KEBA` `CFast 3IE7` ).
* TODO
  * [x] 參與 `FAE-team2` 週會.
  * [x] 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作.
  * [x] 測試 `3SE2-P` 依照客戶上斷電時間參數, 測試認碟狀況.
  * [x] 測試 `Astute` `3MG2-P` 客訴品, 重新開卡, 並進行老化測試, 觀看 `Hardware ECC` 是否會增加.
  * [x] 協助 `Sales-Vincent` 詢問關於 `3TG6-P` `PCIe` `FW-C23803` 修改內容.
  * [x] 協助 `Sales-Vivian` 處理 `innoOSR` 相關 demo.
  * [x] 協助 `EU-FAE` 處理 `Hyperstone` 提供的相關回覆, 以及 `white paper`.

# 2023-11-21
* 參與 `FAE-team2` 週會.
* 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作, 尚未拿到樣品.
* 測試 `3SE2-P` 依照客戶上斷電時間參數, 測試認碟狀況.
* 測試 `Astute` `3MG2-P` 客訴品, 重新開卡( `M151112` ), 並進行老化測試, 觀看 `Hardware ECC` 是否會增加.
* 協助 `Sales-Vincent` 詢問關於 `3TG6-P` `PCIe` `FW-C23803` 修改內容.
* 協助 `Sales-Vivian` 處理 `innoOSR` 相關 demo.
* 協助 `EU-FAE` 處理 `Hyperstone` 提供的相關回覆, 以及 `white paper`.
* TODO
  * [x] 參與 `FAE` 週會.
  * [x] 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作, 透過客戶提供之異常樣品做相關驗證.
  * [x] 協助 `Sales-Vivian` 遠端提供 `iCAP` tool.
  * [x] 紀錄 `Astute` `3MG2-P` 客訴品進行 `BurninTest` 測試, 並紀錄 `Hardware ECC` 數值.
  * [x] 紀錄 `3SE2-P` 依照客戶上斷電時間參數, `SMART` 內的 `power cycle count`.
  * [x] 協助 `Sales-Joan` 回覆 `鼎通盛` 相關測速問題.
  * [x] 詢問 `FW-RD Allen` 關於 `3IE7` `640GB` `thermal throttling` 相關機制.
  * [x] 協助 `EU` 申請領取測試樣品.

# 2023-11-22
* 參與 `FAE` 週會.
* 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作, 透過客戶提供之異常樣品做相關驗證.
* 協助 `Sales-Vivian` 遠端提供 `iCAP` tool.
* 紀錄 `Astute` `3MG2-P` 客訴品進行 `BurninTest` 測試, 並紀錄 `Hardware ECC` 數值, 進行 `48` hr 測試, `Hardware ECC` 數值增加到 `1972`.
* 紀錄 `3SE2-P` 依照客戶上斷電時間參數, `SMART` 內的 `power cycle count`.
* 協助 `Sales-Joan` 回覆 `鼎通盛` 相關測速問題.
* 詢問 `FW-RD Allen` 關於 `3IE7` `640GB` `thermal throttling` 相關機制.
* 協助 `EU` 申請領取測試樣品.
* TODO
  * [x] 提供 `3SE2-P` 依照客戶上斷電時間參數測試驗證相關影片.
  * [x] `Astute` `3MG2-P` 客訴品進行重新開卡( `M161125` ), 再 `BurninTest` 測試, 並紀錄 `Hardware ECC` 數值.
  * [x] 協助 `Sales-Joan` 整理 `鼎通盛` 相關測速條件.
  * [x] 協助 `Sales-Joan` 回覆 `鼎通盛` 相關測速問題.
  * [x] 協助 `PM-Davis` 處理 `innoOSR` 關於新料 `bottom` 相關驗證影片.
  * [x] 協助 `EU-FAE` 驗證 `mSATA 3TE7` 進行 `DLMC` 相關驗證影片( `S21606` -> `S23505` ).
  * [x] 與 `EU-FAE` 討論 `eUSB` partition table 切割操作後續處理方式.
  * [x] 協助新人錄製 `3TE7` `DLMC` 相關驗證影片.
  * [x] 協助 `Sales-Eric` 驗證 `3TE6` 安裝 `Redhat` OS 相關流程.

# 2023-11-23
* 提供 `3SE2-P` 依照客戶上斷電時間參數測試驗證相關影片.
* `Astute` `3MG2-P` 客訴品進行重新開卡( `M161125` ), 再 `BurninTest` 測試, 並紀錄 `Hardware ECC` 數值.
* 協助 `Sales-Joan` 整理 `鼎通盛` 相關測速條件.
  * `Device`: `DES25-C12DK1KCCQF`
    * 溫度 `70` 度 & `90`度
    * 1. 測試 `Re-MP` 狀態, 執行 `CDM`.
    * 2. 延續測試 `1`, 透過 `burnintest 2hr`後, 測試 `CDM`.
    * 3. 延續測試 `2`, `device` 靜置( `5`, `10`, `15` min ), 測試 `CDM`.
  * `Device`: `DHS25-F4GDK1KCCQF`
    * 溫度 `70` 度 & `90` 度.
    * 測試 `CDM`.
* 協助 `Sales-Joan` 回覆 `鼎通盛` 相關測速問題.
* 協助 `PM-Davis` 處理 `innoOSR` 關於新料 `bottom` 相關驗證影片.
* 協助 `EU-FAE` 驗證 `mSATA 3TE7` 進行 `DLMC` 相關驗證影片( `S21606` -> `S23505` ).
* 與 `EU-FAE` 討論 `eUSB` partition table 切割操作後續處理方式.
* 協助新人錄製 `3TE7` `DLMC` 相關驗證影片.
* 協助 `Sales-Eric` 驗證 `3TE6` 安裝 `Redhat` OS 相關流程, 目前驗證 `Redhat 8.7` 無異常.
* TODO
  * [ ] 協助 `Sales-Eric` 驗證 `3TE6` 安裝 `Redhat 7.6` OS 相關流.
  * [ ] 參與 `EU-FAE` 週會.
  * [ ] 協助 `EP-Peiwen` 測試 `eUSB` partition table 切割操作, 透過客戶寄回之新樣品.
  * [ ] 紀錄 `Astute` `3MG2-P` ( `M161125` ) 客訴品進行 `BurninTest` 測試, 並紀錄 `Hardware ECC` 數值.
  * [ ] 測試 `3MG2-P` 依照客戶上斷電時間參數, `SMART` 內的 `power cycle count`( 等待領料樣品 ).
