import os
import pandas as pd
from openpyxl import load_workbook

# 定義log文件路徑
folder_path = './2022-09-02_log/'

def get_log_and_txt_files(folder_path):
    # 取得資料夾內所有 .log 或 .txt 檔案
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.log') or f.endswith('.txt')]

def process_log_and_group_to_json_with_custom_tab_split(log_files):
    grouped_data = []
    current_group = {}
    group_number = 1
    lookup_table = {}

    excluded_keys = ["Ver", "OS", "DRAM Type"]

    for log_file_path in log_files:
        current_group = {}

        with open(log_file_path, 'r', encoding='ISO-8859-1') as file:
            for line in file:
                line = line.strip()

                if line == '------------------------------------------------------------':
                    if current_group:
                        # 檢查是否存在排除的欄位，如果有則不加入結果中
                        if not any("INTEL" in value.upper() or "WDC" in value.upper() for value in current_group.values()):
                            if not any(key in current_group for key in excluded_keys):
                                grouped_data.append({"Group": group_number, **current_group})
                                group_number += 1
                        current_group = {}
                    continue

                if ':' in line:
                    key, value = line.split(':', 1)
                    current_group[key.strip()] = value.strip()
                else:
                    parts = line.split('\t')
                    if len(parts[0]) == 2 and parts[0] != "--":
                        key = parts[0].strip()
                        if key in lookup_table:
                            current_group[lookup_table[key]] = parts[2].strip()
                        else:
                            lookup_table[key] = parts[1].strip()
                            current_group[lookup_table[key]] = parts[2].strip()

                    elif len(parts[0]) >= 3 and len(parts[0]) < 26:
                        # 否則，第一組資料為欄位，第二組為數值
                        key = parts[0].strip()
                        value = parts[2].strip()   
                        current_group[key] = value                     

            # Add the last group if it exists and doesn't have excluded fields
            if current_group and not any(key in current_group for key in excluded_keys):
                grouped_data.append({"Group": group_number, **current_group})
                group_number += 1

    return grouped_data

def adjust_column_width(excel_path):
    workbook = load_workbook(excel_path)
    worksheet = workbook.active

    for col in worksheet.columns:
        max_length = 0
        column = col[0].column_letter  # Get the column name
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        worksheet.column_dimensions[column].width = adjusted_width

    workbook.save(excel_path)

# 取得資料夾內所有 .log 或 .txt 檔案
log_files = get_log_and_txt_files(folder_path)

# 處理log文件並排除指定欄位，轉換為JSON格式
grouped_json_data_excluded = process_log_and_group_to_json_with_custom_tab_split(log_files)

# 將JSON數據轉換為DataFrame
df_grouped_excluded = pd.DataFrame(grouped_json_data_excluded)

# 保存DataFrame到Excel文件
output_excel_path_excluded = './transfer_smart_log.xlsx'
df_grouped_excluded.to_excel(output_excel_path_excluded, index=False)

# 調整Excel欄位的寬度
adjust_column_width(output_excel_path_excluded)

# 顯示處理結果的前20行
df_grouped_excluded.head(20)
# df_grouped_excluded.head(20)