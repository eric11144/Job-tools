import csv
import os
import shutil
import sys


channel_list = [
    '0000_00',
    '0000_01',
    '0000_02',
    '0000_03',
    '0000_04',
    '0000_05',
    '0000_06',
    '0000_07',
    '0000_08',
    '0000_09',
    '0000_10',
    '0000_11',
    '0000_12',
    '0000_13',
    '0000_14',
    '0000_15',
    '0002_08',
    '0003_14',
    '0009_00',
    '0009_01',
    '0009_02',
    '0009_03',
    '0009_04',
    '0009_05',
    '0009_06',
    '0009_07',
    '0012_07',
    '0013_00',
    '0013_01',
    '0013_02',
    '0013_03',
    '0013_04',
    '0013_05',
    '0013_06',
    '0013_07',
    '0023_12',
    '0025_08',
    '0025_10',
    '00002_02',
    '00003_09',
    '00003_10',
    '00003_11',
    '00003_12',
    '00003_13',
    '00003_14',
    '00003_15',
    '00005_06',
    '00005_07',
    '00006_04',
    '00006_12',
    '00025_15',
    '00026_00',
    '00026_01',
    '00026_09',
    '00026_10'
]

list_csv = []


def get_csv_file_list(file_dir):
    file_list = []

    for files in os.listdir(file_dir):
        file_list.append(files)

    file_list.sort(reverse=False)

    return file_list

def transfer_csv_file(path, csv_name_list):
    os.makedirs('modify', exist_ok=True)
    total = len(csv_name_list)
    count = 0

    for csv_name in csv_name_list:
        list_headers = []
        with open(path + csv_name, newline='', encoding='utf-8') as csvfile:
            date, device, file_type = csv_name.split('.') # Get old file name
            
            device = device.replace("-", "_")
            
            filename = date + '.' + device + '.' + file_type
            
            if os.path.isfile('modify/' + filename): # If file already exists, it will be remove.
                os.remove('modify/' + filename)

            rows = csv.reader(csvfile)
            headers = next(rows) # Get csv headers.

            print(device + "  " + str(len(headers)))

            for header in headers:
                header = header.replace("-", "_") # Replace "-" in header to "_".
                if header in channel_list :
                    list_headers.append( "Q" + header)
                else:
                    list_headers.append(header)

            with open(filename, "a+", encoding='utf-8') as outfile:
                csvwriter = csv.writer(outfile)
                csvwriter.writerow(list_headers)  # Write header in first row.

                for row in rows:
                    row[1] = row[1].replace("-", "_")
                    csvwriter = csv.writer(outfile)
                    csvwriter.writerow(row)
                
                outfile.close()
            
            shutil.move(filename, 'modify') # Move file to modify folder.

        count += 1
        print(str(count) + "/" + str(total))

def main():
    csv_path = sys.argv[1:] # Get csv file path.
    csv_path_str = str(csv_path[0])
    csv_name_list = get_csv_file_list(csv_path_str)
    transfer_csv_file(csv_path_str, csv_name_list) # Check file name & file content.

if __name__ == "__main__":
    main()
