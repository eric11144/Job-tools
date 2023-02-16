with gzip.open('20180927-000000.T2C_Cu12_A_Line.csv.gz', 'rt') as f:
    # print(f.read())
    reader = csv.DictReader(f)
    for row in reader:
        del row['device_id']
        del row['datetime']
        print(row)
    #     # for channel_id, channel_value in row.items():
    #     #     print(channel_id)
    #     #     print(channel_value)
