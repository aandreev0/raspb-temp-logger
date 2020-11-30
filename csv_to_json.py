import csv
from datetime import date, timedelta

base_dir = '/home/pi/raspb-temp-logger/' # needed for calling from the crontab

def csv_to_array(fname):
    temps_list = list()
    if not isinstance(fname, list):
        fname = [fname]
    for fn in fname:
        with open(base_dir+fn,'r') as f:
            reader = csv.reader(f)
            temps_list.extend(list(reader))
    data = [[],[],[]]
    for temp_line in temps_list:
        if len(temp_line)>0:
          dte  = temp_line[0] # date
          t  = temp_line[1] # cap in
          if len(temp_line) > 2:
              light = temp_line[2]
          else:
              light = 0
          data[0].append("'"+dte+"'")
          data[1].append(t)
          data[2].append(light)
    return data

f = []
today = date.today()
s_date = date(2020,11,16)
n_days = today - s_date
for d in range(0, n_days.days+1):
  f.append('%s.txt' % (s_date + timedelta(days=d)).strftime("%Y%m%d"))

d = csv_to_array(f)

trace_temp = "var trace_temp = { \
   x: ["+",".join(d[0])+"], \
   y: ["+ ','.join(d[1]) +"], \
   mode: 'lines', \
   name: 'Temperature' \
 };"

trace_light = "var trace_light = { \
   x: ["+",".join(d[0])+"], \
   y: ["+ ','.join(d[2]) +"], \
   mode: 'lines', \
   name: 'Light', \
   yaxis: 'y2', \
 };"

fn = open(base_dir + "data.js", "w")
n = fn.write(trace_temp + "\n" +trace_light)
fn.close()
