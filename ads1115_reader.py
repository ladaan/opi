#!/usr/bin/env python

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
ads.gain = 4
print(ads.gain)
print(ads.gains)
ads.data_rate = 250
print(ads.data_rate)
print(ads.rates)
#print("{0:b}".format(ads.mode))
reg0 = ads._read_register(0)
reg1 = ads._read_register(1)
print("{0:b}".format(reg0))
print("{0:b}".format(reg1))
print("{0:d}".format(reg0))
print("{0:d}".format(reg1))


# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'V'))

#while True:
#    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
#    time.sleep(0.5)
