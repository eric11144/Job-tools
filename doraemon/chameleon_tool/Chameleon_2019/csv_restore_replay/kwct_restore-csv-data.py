import datetime
import os
import shutil
import sys

float_map = {
    'FX3G' : [
        'D30',
        'D32',
        'D840',
        'D842',
        'D844',
        'D846',
        'D848',
        'D850',
        'D8350',
        'D8340'
    ],
    'Cutter_Line_2' : [
        'D30',
        'D32',
        'D840',
        'D842',
        'D844',
        'D846',
        'D848',
        'D850',
        'D8350',
        'D8340'
    ],
    'Siemens' : [
        'G_ELCT',
        'G_ACTF',
        'G_ACTS',
        'G_CYCT',
        'G_FERP',
        'G_POSA_0',
        'G_POSA_1',
        'G_POSA_2',
        'G_POSA_3',
        'G_POSA_4',
        'G_POSD_0',
        'G_POSD_1',
        'G_POSD_2',
        'G_POSD_3',
        'G_POSD_4',
        'G_POSR_0',
        'G_POSR_1',
        'G_POSR_2',
        'G_POSR_3',
        'G_POSR_4',
        'G_SPSD',
        'TodayOEE_1',
        'TodayOEE_12',
        'TodayOEE_16',
        'TodayOEE_8',
        'YesterdayOEE_1',
        'YesterdayOEE_12',
        'YesterdayOEE_16',
        'YesterdayOEE_8'
    ],
    'Q00U_utilization' : ['total_utilization_hours'],
    'Q00_utilization' : ['total_utilization_hours'],
    'FX3G_utilization' : ['total_utilization_hours'],
    'Cutter_Line_2_utilization' : ['total_utilization_hours'],
    'Q00U_channels_working_time' : [
        'heating_elapsed_time_sec',
        'max_heating_elapsed_time_sec',
        'OIL-SEALED-ROTARY-PUMP-OPERATION_working_time_hours',
        'oil_sealed_rotary_pump_elasped_time_sec',
        'MECHANICAL-BOOSTER-PUMP-OPERATION_working_time_hours',
        'max_mechanical_booster_pump_elapsed_time_sec',
        'max_oil_sealed_rotary_pump_elapsed_time_sec',
        'mechanical_booster_pump_elapsed_time_sec',
        'oil_sealed_rotary_pump_elapsed_time_sec',
        'HEATER-POWER-ON_working_time_hours'
    ],
    'Q00_channels_working_time' : [
        'heating_elapsed_time_sec',
        'max_heating_elapsed_time_sec',
        'OIL-SEALED-ROTARY-PUMP-OPERATION_working_time_hours',
        'oil_sealed_rotary_pump_elasped_time_sec',
        'MECHANICAL-BOOSTER-PUMP-OPERATION_working_time_hours',
        'max_mechanical_booster_pump_elapsed_time_sec',
        'max_oil_sealed_rotary_pump_elapsed_time_sec',
        'mechanical_booster_pump_elapsed_time_sec',
        'oil_sealed_rotary_pump_elapsed_time_sec',
        'HEATER-POWER-ON_working_time_hours'
    ],
    'Power_meter_4' : [
        '40289',
        '40291',
        '40293',
        '40295',
        '40307',
        '40323',
        '40325',
        '40333',
        '40341'
    ],
    'Power_meter_3' : [
        '40289',
        '40291',
        '40293',
        '40295',
        '40307',
        '40323',
        '40325',
        '40333',
        '40341'
    ],
    'Power_meter_2' : [
        '40289',
        '40291',
        '40293',
        '40295',
        '40307',
        '40323',
        '40325',
        '40333',
        '40341'
    ],
    'Power_meter' : [
        '40289',
        '40291',
        '40293',
        '40295',
        '40307',
        '40323',
        '40325',
        '40333',
        '40341'
    ],
    'Modbus-1' : ['30003'],
    'Modbus' : [
        '30001',
        '30002'
    ],
    'meter_temp' : ['meter_temp'],
    'meter_C' : [
        'meter_X1',
        'meter_X2',
        'meter_Y1',
        'meter_Y2'
    ],
    'Grinding-2D5' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988'
    ],
    'Grinding-2D4' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988'
    ],
    'Grinding-2D3' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988'
    ],
    'Grinding-1H2' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988'
    ],
    'Grinding-1H1' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988'
    ],
    'Grinding-1G8' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988',
        'D989'
    ],
    'Grinding-1G7' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988',
        'D989'
    ],
    'Grinding-1G6' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988',
        'D989'
    ],
    'Grinding-1G5' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988',
        'D989'
    ],
    'Grinding-1G4' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988',
        'D989'
    ],
    'Grinding-1G3' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988',
        'D989'
    ],
    'Grinding-1G2' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988',
        'D989'
    ],
    'Grinding-1G1' : [
        'D202',
        'D684',
        'D700',
        'D786',
        'D788',
        'D884',
        'D900',
        'D986',
        'D988',
        'D989'
    ],
    'Grinding-1C1' : [
        'D2300',
        'D2350',
        'D2401',
        'D2451'
    ],
    'Grinding-1C2' : [
        'D2300',
        'D2350',
        'D2401',
        'D2451'
    ],
    'Grinding-1C3' : [
        'D2300',
        'D2350',
        'D2401',
        'D2451'
    ],
    'Grinding-1C6' : [
        'D2300',
        'D2350',
        'D2401',
        'D2451'
    ],
    'Grinding-1D1' : [
        'D2451',
        'D2350'
    ],
    'Grinding-1D2' : [
        'D202',
        'D2451',
        'D2350'
    ],
    'Grinding-1D3' : [
        'D2451',
        'D2350'
    ],
    'Grinding-1D4' : [
        'D2451',
        'D2350'
    ],
    'Grinding-1D5' : [
        'D2451',
        'D2350'
    ],
    'Grinding-1D6' : [
        'D2451',
        'D2350'
    ],
    'meter_temp' : [
        'room_temp',
        'room_humidity'
    ]
}

str_map = {
    'cutter-1-barcode-scanner' : ['barcode'],
    'cutter-2-barcode-scanner' : ['barcode'],
    'hot-process-barcode-scanner' : ['barcode'],
    'power-meter-wash-barcode-scanner' : ['barcode'],
    'Siemens' : [
        'G_EXEP',
        'G_SEQN ',
        'G_FRUT ',
        'G_PRGM ',
        'G_PRGR ',
        'G_PSUT ',
        'G_SRNE_0 ',
        'G_SRNE_1 ',
        'G_SRNE_2 ',
        'G_SRNE_3 ',
        'G_SRNE_4 '
    ]
}

def get_csv_list(file_dir):
    file_list = []

    for files in os.listdir(file_dir):
        file_list.append(files)

    file_list.sort(reverse=False)

    return file_list

def insert_csv_data(path, csv_name_list):
    os.makedirs('finish', exist_ok=True)
    count = len(csv_name_list)
    for csv_name in csv_name_list:
        print(datetime.datetime.now())
        print(csv_name)

        date, device, file_type = csv_name.split('.')

        force_float = ''
        force_string = ''

        if device in float_map:
            for channel_id in float_map[device]:
                force_float += ' -f ' + channel_id

        if device in str_map:
            for channel_id in str_map[device]:
                force_string += ' -s ' + channel_id

        result = os.system(
            '/tmp/venv/bin/qcsv.influxdb_feeder.inject --readings-per-request 200 --host localhost --port 7890 --dry-run '
            + force_string
            + force_float
            + ' --csv=' + path + csv_name
            + ' 2>&1 > ' + path + '_' + csv_name + '.log')

        exit_status = result >> 8

        if exit_status != 0:
            print(csv_name + '  Insert Fail !!!')
        else:
            shutil.move(path + csv_name, 'finish')

        count -= 1

        print(count)
        print(str(datetime.datetime.now())  + ' finish \n')


def main():
    csv_path = sys.argv[1:]
    csv_path_str = str(csv_path[0])
    csv_name_list = get_csv_list(csv_path_str)
    insert_csv_data(csv_path_str, csv_name_list)

    print(str(datetime.datetime.now()) + ' finish ')

if __name__ == "__main__":
    main()
