import csv
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime

def SaveCapLogPNG(fname):

    with open(fname,'r') as f:
        reader = csv.reader(f)
        temps_list = list(reader)

    data = []

    for temp_line in temps_list:
        if len(temp_line)>0:
          #print(cap_line)
          dte  = temp_line[0] # date
          t  = temp_line[1] # cap in
          data.append([dte, t])


    fig = plt.figure()
    ax = fig.add_subplot(111)
    dtes = []
    dtes_str = []
    ts = []
    for l in data:
        dtes.append(date2num(datetime.strptime(l[0], '%Y-%m-%d %H:%M:%S.%f')))
        dtes_str.append(datetime.strptime(l[0], '%Y-%m-%d %H:%M:%S.%f'))
        ts.append(float(l[1]))

    ax.set_xticks(dtes[1::20])
    ax.set_xticklabels([d.strftime('%H:%M') for d in dtes_str[1::20]])
    ax.plot(dtes, ts,'--', label='Temperature on '+ d.strftime("%y%m%d"))

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc=2)
    ax.set_ylabel('Temperature, deg C')
    ax.set_xlabel('Date')

    fig.autofmt_xdate()

    fig.savefig(fname+".png")


if __name__ == "__main__":
    SaveCapLogPNG('')
