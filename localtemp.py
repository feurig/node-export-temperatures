#!/usr/bin/python
with open('/var/lib/prometheus/node-exporter/temp.prom', 'r') as f:
    for line in f.readlines():
        if 'Xhome_temperature_farenheit' in ('X'+line) :
            print('%.2fF' % (float(line.split(' ')[1],)))