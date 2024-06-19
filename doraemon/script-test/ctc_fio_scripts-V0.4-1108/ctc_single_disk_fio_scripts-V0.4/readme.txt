1.bare ssd test
  syntax:#./bare_ssd_test.sh devname
  eg:#nohup &>/dev/null ./bare_ssd_test.sh sdb &      (for sata/sas ssd device)
     #nohup &>/dev/null ./bare_ssd_test.sh nvme0n1 &  (for nvme ssd device)

2.bare hdd test
  syntax:#./bare_hdd_test.sh devname
  eg:#nohup &>/dev/null ./bare_ssd_test.sh sdb &      (for sata/sas hdd device)

3.bare ssd stress test
  syntax:#./bare_hdd_stress_test.sh devname
  eg:#nohup &>/dev/null ./bare_ssd_stress_test.sh sdb &      (for sata/sas ssd device)
  eg:#nohup &>/dev/null ./bare_ssd_stress_test.sh nvme0n1 &      (for nvme ssd device)

4.bare hdd stress test
  syntax:#./bare_hdd_test.sh devname
  eg:#nohup &>/dev/null ./bare_hdd_stress_test.sh sdb &      (for sata/sas hdd device)

5. Log filter(***make sure log filter scripts and fio test log are same path***)
1) single ssd test log filter:
   syntax:./result_single_ssd_traversal_log_filter devname
   eg:./result_single_ssd_traversal_log_filter sdb		(for sata/sas ssd device)
   eg:./result_single_ssd_traversal_log_filter nvme0n1	(for nvme ssd device)
2) single hdd test log filter:
   syntax:./result_single_hdd_traversal_log_filter devname
   eg:./result_single_hdd_traversal_log_filter sdb		(for sata/sas hdd device)
3) final filter result saved as filter_single_xxx_Result.csv
