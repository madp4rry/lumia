
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib
#inline
import numpy as np
from operator import add
import matplotlib.pyplot as plt
plt.style.use('ggplot')

csfont = {'fontname':'Lato'}
hfont = {'fontname':'Rubik'}
from operator import sub
import matplotlib.gridspec as gridspec

file = input("Insert directory path of first file.")
file_second = input("Insert directory path of second file. If there is non enter 0")
if int(file_second) == 0:
    file_second = file

df = pd.read_csv('' + (file) + '', engine='python', sep=";", header=0 ,encoding = 'unicode_escape')
df2 = pd.read_csv('' + (file_second) + '', engine='python', sep=";", header=0, encoding = 'unicode_escape')

Name_measurement = input("Name of measurement?")
file_destination = input("Path for file destination?")
pulse_time = int(input('When was was the lightpulse set [h]?'))

Luminescence = []
Luminescence2 = []
OpticalDensity = []
Experiment_Data = []
Experiment_Data2 = []
nr_measured_strain = int(input("How many strains were measured?"))
length = len(df.columns)
strain = nr_measured_strain
print(length)
for i in range(3, length):
    Luminescence.append(df.iloc[:, i].tolist())
    Luminescence2.append(df2.iloc[:, i].tolist())

for i in range(0, 3):
    Experiment_Data.append(df.iloc[:, i].tolist())
    Experiment_Data2.append(df2.iloc[:, i].tolist())
print(len(Luminescence), len(Luminescence2))
print(len(Experiment_Data), len(Experiment_Data2))

time = []
time_intervall = input("What is the intervall between each measurement [min]?")

for i in range(len(Experiment_Data[1])):
    time.append(i * int(time_intervall))
time_hours = []
for i in range(len(time)):
    time_hours.append(0)
    time_hours[i] = time[i] / 60

# Names = ['wildtype','TM02 ROC40-LUC', 'TM05 ROC15-LUC', 'strain4','strain5','strain6','strain7', 'strain8']

Names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12',
         'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12',
         'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12',
         'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12',
         'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12',
         'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
         'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12',
         'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12']

# for i in range(nr_measured_strain):
# name = input("Name of meaasured Strain Nr."+str(i+1)+"")
# Names.append(name)

calculation = []
calculation2 = []
x = int(input("How many wells were measured per strain?"))
y = x
z = len(Luminescence) / x
c = 0


#experiment_duration = df['Cycle Nr.'].tolist()

for i in range(int(z)):
    calculation.append([])
    calculation2.append([])
    for j in range(len(Luminescence[0])):
        calculation[i].append(0)
        calculation2[i].append(0)
print(len(calculation), len(calculation2))
for i in range(len(Luminescence)):
    if i == x:
        c = c + 1
        x = x + y
        # print('c was updated')
    calculation[c] = (map(add, calculation[c], Luminescence[i]))
    calculation2[c] = (map(add, calculation2[c], Luminescence2[i]))
    # print(calculation,'-----',Luminescence[i],'----',c)
print(calculation, 'Sum of all Wells for each Strain')
for i in range(len(calculation)):
    calculation[i] = [x / y for x in calculation[i]]
    calculation2[i] = [x / y for x in calculation2[i]]

m = []
lumi = np.array(Luminescence)
m = np.mean(lumi, axis=0)


# ---Subtraktion--of--wt--background-----------------------------------------------------------------------------------------------------------------------------------------


calculation_background = []
calculation2_background = []

for i in range(len(calculation)):
    calculation_background.append([])
    calculation2_background.append([])
    for j in range(len(calculation[0])):
        calculation_background[i].append(0)
        calculation2_background[i].append(0)

for i in range(1, len(calculation)):
    for j in range(len(calculation[i])):
        calculation_background[i][j] = (calculation[i][j] - calculation[0][j])
        calculation2_background[i][j] = (calculation2[i][j] - calculation2[0][j])
# -----Plotting-------------------------------------------------------------------------------------------
def plotting(list, method):
    for i in range(0, len(list)):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(time_hours, list[i], linewidth=0.8, color='tab:grey', ls='--')
        ax.set_title('' + str(Name_measurement) + '\n' + str(Names[i]) + ' ' + str(method) + '', fontsize=10, **hfont)
        ax.set_xlabel('Time [h]', fontsize=10, **hfont)
        ax.set_ylabel('Luminescence [cps]', fontsize=10, **hfont)
        tick_count = []
        tick_count_current = -0
        for j in range(1, round(max(time_hours) / 12)):
            if j % 2 == 0:
                tick_count_current = tick_count_current + 14
            else:
                tick_count_current = tick_count_current + 10
            tick_count.append(tick_count_current)
        ax.set_xticks(tick_count)
        #ax.tick_params(labelsize=10)
        # Setting Lines of Sync
        grid_count = -0
        for j in range(1, round(max(time_hours) / 12)):
            if j % 2 == 0:
                grid_count = grid_count + 14
            else:
                grid_count = grid_count + 10
            #ax.axvline(grid_count, color='black', alpha=0.5, linewidth=0.3)
        greybar = 0
        if min(list[i]) > 0 == True:
            greybar = -4
        else:
            greybar = min(list[i])
        # Darkness during measurement
        ax.broken_barh([(0, max(time_hours))], (greybar, (max(list[i]) + 100)), facecolors='tab:gray', alpha=0.2)
        ax.broken_barh([(pulse_time, 0.5)], (greybar, (max(list[i]) + 100)), facecolors='yellow', alpha=0.9)
        axes = plt.gca()
        axes.set_ylim([(min(list[i])), (max(list[i]) + 5)])
        axes.set_xlim([0, max(time_hours)])
        # plt.savefig('/home/darius/Desktop/'+str(Name_measurement)+''+str(Names[i])+''+str(method)+'.svg')
        #plt.savefig(
           # '' + str(file_destination) + '' + str(Name_measurement) + '' + str(Names[i]) + '_' + str(method) + '.svg')
        plt.savefig(
            '' + str(file_destination) + '' + str(Name_measurement) + '' + str(Names[i]) + '_' + str(method) + '.pdf')



def plotting_all_in_one(list, method):
    max_list = []
    mean_list = []
    fig, ax = plt.subplots(figsize=(6, 4))
    for i in range(0, len(list)):
        ax.plot(time_hours, list[i], linewidth=0.5, color='tab:grey', ls='--')
        max_list.append(max(list[i]))
    ax.set_title('' + str(Name_measurement) + ' ' + 'all wells' + ''  '' + str(method) + '', fontsize=12, **hfont)
    ax.set_xlabel('Time [h]', fontsize=10, **hfont)
    ax.set_ylabel('Luminescence [cps]', fontsize=10, **hfont)
    ax.plot(time_hours, list[i], linewidth=0.5, color='tab:grey', ls='--', label='Single wells')
    #plotting average
    ax.plot(time_hours, m, color='orange', linewidth=0.8, label='Average of all wells')
    #plotting special
    ax.plot(time_hours, list[10], linewidth=0.5, color='black', ls='--', label='Single well A10')
    plt.legend(loc="upper right")
    tick_count = []
    tick_count_current = -0
    for j in range(1, round(max(time_hours) / 12)):
        if j % 2 == 0:
            tick_count_current = tick_count_current + 14
        else:
            tick_count_current = tick_count_current + 10
        tick_count.append(tick_count_current)
    ax.set_xticks(tick_count)
    #ax.tick_params(labelsize=10, grid_color='white', grid_alpha=0.5)
    # Setting Lines of Sync
    grid_count = -0
    for j in range(1, round(max(time_hours) / 12)):
        if j % 2 == 0:
            grid_count = grid_count + 14
        else:
            grid_count = grid_count + 10
        #ax.axvline(grid_count, color='black', alpha=0.5, linewidth=0.1)
    greybar = 0
    if min(list[i]) > 0 == True:
        greybar = -4
    else:
        greybar = min(list[i])
    # Darkness during measurement
    #ax.broken_barh([(0, max(time_hours))], (greybar, (max(max_list) + 100)), facecolors='tab:gray', alpha=0.2)
    ax.broken_barh([(pulse_time, 0.5)], (greybar, (max(max_list) + 100)), facecolors='yellow', alpha=0.9)
    axes = plt.gca()
    axes.set_ylim([(min(list[i])), ((max(max_list)) + 20)])
    axes.set_xlim([0, max(time_hours)])

    #plt.savefig('' + str(file_destination) + '' + str(Name_measurement) + '_All_wells' + str(method) + '.svg')
    plt.savefig('' + str(file_destination) + '' + str(Name_measurement) + '_All_wells' + str(method) + '.pdf')




plotting(calculation, 'single well')
plotting_all_in_one(calculation, '')