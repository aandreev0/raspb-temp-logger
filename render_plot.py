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
          if len(temp_line) > 2:
              light = temp_line[2]
          else:
              light = 0
          data.append([dte, t, light])

    plt.rcParams.update({'font.size': 6})
    fig, ax = plt.subplots()

    dtes = []
    dtes_str = []
    ts = []
    ls = []
    for li in data:
        dtes.append(date2num(datetime.strptime(li[0], '%Y-%m-%d %H:%M:%S.%f')))
        dtes_str.append(datetime.strptime(li[0], '%Y-%m-%d %H:%M:%S.%f'))
        ts.append(float(li[1]))
        ls.append(float(li[2]))
    color = 'tab:blue'
    tick_interval = int(len(dtes)/20)
    ax.set_xticks(dtes[0::tick_interval])
    ax.set_xticklabels([d.strftime('%H:%M') for d in dtes_str[0::tick_interval]])
    d = dtes_str[0]
    ax.plot(dtes, ts,'-',linewidth=1, label='Temperature on '+ d.strftime("%y%m%d"),color=color)

    handles, labels = ax.get_legend_handles_labels()
    ax.set_ylabel('Temperature, deg C',color=color)
    ax.set_xlabel('Time')
    ax.tick_params(axis='y', labelcolor=color)

    color = 'tab:red'
    ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Light level, a.u.', color=color)  # we already handled the x-label with ax1
    ax2.plot(dtes, ls,'-',linewidth=1, label='Light on '+ d.strftime("%y%m%d"),color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Recording date: '+ d.strftime("%y/%m/%d"))

    fig.autofmt_xdate()

    fig.savefig(fname+".png", dpi=600)


if __name__ == "__main__":
    SaveCapLogPNG('')
