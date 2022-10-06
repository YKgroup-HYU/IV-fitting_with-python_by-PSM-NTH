import pandas as pd
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm


def bestplot(A, B, C,D,E,F):
    file_path = '.\dat\%s*.csv'%C
    file_path1 = '.\dat\%s*.csv' % D
    file_path2 = '.\dat\%s*.csv' % E
    file_path3 = '.\dat\%s*.csv' % F
    # file_path4 = '.\dat\%s*.csv' % G
    # file_path5 = '.\dat\%s*.csv' % H
    # file_path6 = '.\dat\%s*.csv' % I
    # file_path7 = '.\dat\%s*.csv' % J

    csv = []
    for filename in glob.glob(file_path, recursive=True):
        csv.append(filename)
    for filename in glob.glob(file_path1, recursive=True):
        csv.append(filename)
    for filename in glob.glob(file_path2, recursive=True):
        csv.append(filename)
    for filename in glob.glob(file_path3, recursive=True):
        csv.append(filename)
    # for filename in glob.glob(file_path4, recursive=True):
    #     csv.append(filename)
    # for filename in glob.glob(file_path5, recursive=True):
    #     csv.append(filename)
    # for filename in glob.glob(file_path6, recursive=True):
    #     csv.append(filename)
    # for filename in glob.glob(file_path7, recursive=True):
    #     csv.append(filename)

    csv_tqdm = tqdm(csv)
    voltage = []
    current_lin = []
    current_abs = []
    voltage_2 = []
    current_lin_2 = []
    current_abs_2 = []
    for i in csv_tqdm:
        filename = i.split('\\')[-1][:-4]
        # filename_1 = i.split('\\')[-1][:-4].split('_')[1]
        csv_tqdm.set_description(f'Processing {filename}')

        Data = pd.read_csv(".\dat\%s" % filename + '.csv', names=['Value', 'Voltage', 'Current', 'four', 'five', 'six'])

        Value = "DataValue"

        find_row = Data.loc[(Data['Value'] == Value)]
        # find_row = find_row.iloc[:,1:3]
        # print(find_row)

        find_columns_v = find_row['Voltage']
        find_columns_c = find_row['Current']
        Voltage = list(map(float, find_columns_v.values.tolist()))
        voltage.append(Voltage)
        Current_abs = list(map(abs, map(float, find_columns_c.values.tolist())))
        current_abs.append(Current_abs)
        Current_lin = list(map(float, find_columns_c.values.tolist()))
        current_lin.append(Current_lin)
        # print(Voltage)
        # print(Current_lin)
        Voltage_2 = []
        for i in range(0, len(Voltage), 10):
            Voltage_2.append(Voltage[i])
        Current_lin_2 = []
        for i in range(0, len(Current_lin), 10):
            Current_lin_2.append(Current_lin[i])
        Current_abs_2 = []
        for i in range(0, len(Current_abs), 10):
            Current_abs_2.append(Current_abs[i])
        voltage_2.append(Voltage_2)
        current_lin_2.append(Current_lin_2)
        current_abs_x2.append(Current_abs_2)

    plt.rc('font', size=15)
    plt.figure(figsize=(30, 15))
    plt.subplot(121)
    plt.plot(voltage[0], current_lin[0], label='%s' % csv[0].split('_')[-1][:-4])
    plt.plot(voltage[1], current_lin[1], label='%s' % csv[1].split('_')[-1][:-4])
    plt.plot(voltage[2], current_lin[2], label='%s' % csv[2].split('_')[-1][:-4])
    plt.plot(voltage[3], current_lin[3], label='%s' % csv[3].split('_')[-1][:-4])
    # plt.plot(voltage[4], current_lin[4], label='%s' % csv[4].split('\\')[-1][:-4])
    # plt.plot(voltage[5], current_lin[5], label='%s' % csv[5].split('\\')[-1][:-4])
    # plt.plot(voltage[6], current_lin[6], label='%s' % csv[6].split('\\')[-1][:-4])
    # plt.plot(voltage[7], current_lin[7], label='%s' % csv[7].split('\\')[-1][:-4])
    plt.plot(voltage_2[0], current_lin_2[0], ">")
    plt.plot(voltage_2[1], current_lin_2[1], ">")
    plt.plot(voltage_2[2], current_lin_2[2], ">")
    plt.plot(voltage_2[3], current_lin_2[3], ">")
    # plt.plot(voltage_2[4], current_lin_2[4], ">")
    # plt.plot(voltage_2[5], current_lin_2[5], ">")
    # plt.plot(voltage_2[6], current_lin_2[6], ">")
    # plt.plot(voltage_2[7], current_lin_2[7], ">")
    plt.title('I-V graph_linear')
    plt.xlabel('Voltage [V]', labelpad=10)
    plt.ylabel('Current [A]', labelpad=10)
    plt.legend()
    plt.grid(True)

    plt.subplot(122)
    plt.plot(voltage[0], current_abs[0], label='%s' % csv[0].split('_')[-1][:-4])
    plt.plot(voltage[1], current_abs[1], label='%s' % csv[1].split('_')[-1][:-4])
    plt.plot(voltage[2], current_abs[2], label='%s' % csv[2].split('_')[-1][:-4])
    plt.plot(voltage[3], current_abs[3], label='%s' % csv[3].split('_')[-1][:-4])
    # plt.plot(voltage[4], current_abs[4], label='%s' % csv[4].split('\\')[-1][:-4])
    # plt.plot(voltage[5], current_abs[5], label='%s' % csv[5].split('\\')[-1][:-4])
    # plt.plot(voltage[6], current_abs[6], label='%s' % csv[6].split('\\')[-1][:-4])
    # plt.plot(voltage[7], current_abs[7], label='%s' % csv[7].split('\\')[-1][:-4])
    plt.plot(voltage_2[0], current_abs_2[0], ">")
    plt.plot(voltage_2[1], current_abs_2[1], ">")
    plt.plot(voltage_2[2], current_abs_2[2], ">")
    plt.plot(voltage_2[3], current_abs_2[3], ">")
    # plt.plot(voltage_2[4], current_abs_2[4], ">")
    # plt.plot(voltage_2[5], current_abs_2[5], ">")
    # plt.plot(voltage_2[6], current_abs_2[6], ">")
    # plt.plot(voltage_2[7], current_abs_2[7], ">")
    plt.yscale('log')
    plt.title('I-V graph_abs')
    plt.xlabel('Voltage [V]', labelpad=10)
    plt.ylabel('Current [A]', labelpad=10)
    plt.legend(loc="lower left", bbox_to_anchor=(1.04,0))
    plt.grid(True)

    if A == 'T':
        plt.savefig('.\\res\\%s.png' % (' 4V R ALL'))

    if B == 'T':
        plt.show(block=False)
        plt.pause(1)
        plt.close()
