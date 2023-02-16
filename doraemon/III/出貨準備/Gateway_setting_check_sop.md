# 出貨流程 #
* 修改 bios 相關設定.
    * 上電自動開機設定  
        * `[System Management] -> [Power Up] -> [Power-Up Mode]` should be `[Tuen On]`.  

    * `CPU Configuration` 設定  
        * `[Advanced] -> [CPU Configuration] -> [PPM Configuration] -> [CPU C state Report]` should be `[Disabled]`.  

        * `[Execute Disable Bit]` should be `[Disabled]`.  
        * `[Power Technology]` should be `[Disabled]`.  

    * `ACPI Settings` 設定  
        * `[Advanced] -> [ACPI Settings] -> [Enable ACPI Auto Configuration]` should be `[Enabled]`.  

    * `Miscellaneous Configuration` 設定  
        * `[Advanced] -> [Miscellaneous Configuration] -> [OS Selection]` should be `[Monn Island 3.1]`.  
    * `Serial` 設定
        * `Baytrail Features Configuration -> HSUART Port Mode` should be `rs232`, `rs422`, `rs485`.

* 安裝完 os 後, 需再開機安裝 Chameleon Gateway, 直至關機才算完成安裝( 總共關機 `2` 次 ).

* 申請 Licenses 數量以及單號.

* 放入 License 重開機後, 透過 `Chameleon Gateway` 內的產品金鑰, 確認數量是否正確.

* 需連上外網, 將 IPC 時間做校正.

* 讀取一台設備, 看 gateway 是否可正常運作.

* 反覆開關機五次, 確保設備可正常啟動, 以及開機鈕是否正常.

* 上電開機測試五次.

* 根據硬體規格須做一些參數調整.
    * `DL20` : `sudo /venv/bin/python3 install.py --metal hpe-dl20gen10 --extra-node-red-count 7`.
    * `Grafana` 同時觀看數量 : `INFLUXDB_COORDINATOR_MAX_CONCURRENT_QUERIES = 8`
