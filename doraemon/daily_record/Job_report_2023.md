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
  * [ ] 參與 `EU-FAE` 週會.

