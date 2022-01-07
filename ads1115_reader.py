#!/usr/bin/env python

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn
import math

# Data collection setup
RATE = 860
SAMPLES = 1000
FACTOR = 30
MULTIPLIER = 0.00187
VOLTAGE = 235

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)

# Create the ADC object using the I2C bus
adc = ADS.ADS1115(i2c)
adc.gain = 2  #  -   4 = +/-1.024V

# ADC Configuration
adc.mode = Mode.CONTINUOUS
adc.data_rate = RATE

#print("Gain: {}".format(adc.gain))
#print("Rate: {}".format(adc.data_rate))
#print("Mode: {}".format(adc.mode))
#reg0 = adc._read_register(0)
#reg1 = adc._read_register(1)
#print("{0:b}".format(reg0))
#print("{0:b}".format(reg1))
#print("{0:d}".format(reg0))
#print("{0:d}".format(reg1))

# Create single-ended input on channel 0
chan0 = AnalogIn(adc, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(adc, ADS.P0, ADS.P1)

data = [None] * SAMPLES

start = time.monotonic()
print(start)

def get_current():

    sum = 0
    counter = 0
    start = time.monotonic()
    # Read the same channel over and over
    for i in range(SAMPLES):
        #data[i] = chan0.voltage
        #voltage = chan0.value * MULTIPLIER
        current = chan0.voltage * FACTOR
        #current /= 1000
        sum += current ** 2
        

    current = math.sqrt(sum/SAMPLES)
    return current


print(get_current())
end = time.monotonic()
total_time = end - start

print("Time of capture: {}s".format(total_time))
print("Sample rate requested={} actual={}".format(RATE, SAMPLES / total_time))
#print(data)


#print("{:>5}\t{:>5}".format('raw', 'V'))
#
#out = []
#i = 1
#while True:
#    #print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
#    #print("Last result {}".format(adc.get_last_result()))
#    voltage = abs(chan.voltage)
#    #if abs(voltage) 
#    out.append(voltage)
#    time.sleep(0.005)
#    i += 1
#    if i == 500:
#        break
#
#print(round(sum(out)/len(out),3))
