# from https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/#:~:text=The%20DS18B20%20temperature%20sensor%20is,accurate%20and%20take%20measurements%20quickly.

import os
import glob
import time
import datetime
import sys
import requests
import render_plot
import serial

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0] # only picks 1st device
device_file = device_folder + '/w1_slave'
light_arduino = '/dev/'

def read_light():
    ser = serial.Serial('/dev/ttyACM0')  # open serial port
    avg_light = 0;
    for i in range(0,5):
       line = ser.readline()   # read a '\n' terminated line
       if i>2:
          avg_light += int(line.strip())

    avg_light = avg_light / 2.0;
    ser.close()
    print("Averaged light:" + str(avg_light))
    return avg_light

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

def watchdog_ping():
    print("Sending watchdog ping...")
    url = "http://aandreev.net/?raspberry_pi_ping"
    res = requests.get(url)
    print(res.status_code)

try:
    watchdog_ping()
    t = read_temp()
    today = datetime.datetime.today()
    light_lvl = read_light()
    v = str(today) + ", " + str(t) +', '+str(light_lvl)+ "\n"

    fname = "/home/pi/raspb-temp-logger/" + today.strftime('%Y%m%d') + ".txt"
    with open(fname, "a+") as myfile:
        myfile.write(v)
    print("["+ str(today) +"] Recorded temp: " + str(t))

    render_plot.SaveCapLogPNG(fname)


except:
    e = sys.exc_info()[0]
    print(str(e))
