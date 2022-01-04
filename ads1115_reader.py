#!/usr/bin/env python

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
adc = ADS.ADS1115(i2c)
adc.gain = 1  #  -   4 = +/-1.024V
print(adc.gain)
print(adc.gains)
adc.data_rate = 250
print(adc.data_rate)
print(adc.rates)
print(adc.mode)
#print("{0:b}".format(adc.mode))
reg0 = adc._read_register(0)
reg1 = adc._read_register(1)
print("{0:b}".format(reg0))
print("{0:b}".format(reg1))
print("{0:d}".format(reg0))
print("{0:d}".format(reg1))



# Create single-ended input on channel 0
chan = AnalogIn(adc, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(adc, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'V'))

while True:
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    time.sleep(0.5)
