# 建立 2020 license

下載 license 程式
git clone git@gitlab.qi:qi/qalic2.licensing.git
cd III/qalic2.licensing/builder

建立 container
make CONTAINER_REGISTRY=gitlab.qi:4567/qi/registry

1. 登入 `chameleon gateway` 頁面
2. 系統設定產品金鑰.
3. 下載主機資訊.
4. `cd III/qalic2.licensing/licenses/inhouse`
5. 建立設備資料夾, 資料夾名稱為 `設備 mac address`.
6. `cp host-info.qalic2h`
7. `cd qalic2.licensing/builder`
8. `make` (產生 license image)
9. `docker run -it -v ~/reference-iii/III/qalic2.licensing:/qalic2.licensing localhost/licensing bash`
10. `cd qalic2.licensing/licenses/inhouse/000babd6cc9f`
11. `qalic2m --init`
12. `sudo vim reference-iii/III/qalic2.licensing/licenses/inhouse/000babd6cc9f/license.yaml`
13. 修改 license 欄位 -> `licensee: Inhouse`
14. 新增設備數量 ->  
    `qalic2m --add-agent-license=10` (可讀可寫)  
    `qalic2m --add-agent-license=8 --channel-count 10 --permissions readonly` (只有讀)
    `qalic2m --add-agent-license=2 --permissions virtual-r` (指定對應平台讀取)
    `qalic2m --add-agent-license 1 --channel-count 10 --permissions melsec-rw,fins-rw` (限制 10 點 某平台 讀寫)
15. commit 
```
Compeq 0090e897d2f - Add 8 readonly licenses & channel count 10.

Purchase Order #21070003
```
16. 發 pr 至 license group.
17. License 目前會直接存放於資料夾內.
18. 如在廠區, 需取得 `licenses.tgz`, 並解壓縮.
19. 至系統設定產品金鑰上傳 `license.qalic2`.
20. 重開機即可.
