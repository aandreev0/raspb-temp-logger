# RaspnberryPi-based temperature recorder with web-interface

RaspberryPi temperature logger with web-interface

Wiring is copied from [Konstantin Dimitrov](https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806)

# Components:

- [RaspberryPi 3 model B+](https://www.digikey.com/products/en?keywords=1690-1025-ND)
- [Prototyping Pi Plate Kit for Raspberry Pi](https://www.digikey.com/products/en?keywords=1528-1414-ND)
- [JST-SM Pigtail connector (3-pin)](https://www.digikey.com/product-detail/en/sparkfun-electronics/CAB-14575/1568-1831-ND/8543395)
- [Waterproof DS18B20 Digital Temperature Sensor](https://www.digikey.com/products/en?keywords=1528-1592-ND)

# Installation and set-up

  1. Download the recent code to a home folder on Pi, e.g. `~/raspb-temp-logger/`
  2. Create cron job task to run the `report_temp.py` script with desired frequency. See [documentation on crontab for Debian](https://vitux.com/how-to-setup-a-cron-job-in-debian-10/) for more information

At this point you will have logs of temperature accessible, for example at `~/raspb-temp-logger/20200901.txt` in CSV format and `~/raspb-temp-logger/20200901.txt.png` in image (plot) format.

Now we can make content it web-accessible:

  3. Setup nginx web server to serve content of the `~/raspb-temp-logger/` (need more detail)
  4. Change firewall rules for external access of `*.txt` and `*.png` files (need more details)
  5. Work with your IT department in order for making this interface safe for the organization
