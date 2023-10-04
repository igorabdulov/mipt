import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT, initial = gpio.LOW)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]
    
def fun(a):
    signal = binary(a)
    gpio.output(dac, signal)
    return signal

    
try:
    while True:
        for a in range(256):
            sleep(0.0005)
            signal = fun(a)
            voltage = a / levels * maxVoltage
            compvalue = gpio.input(comp)
            if compvalue == 1:
                print(a, "ADC value = {:^3} - > {}, input voltage = {:.2f}".format(a, signal, voltage))
                break
finally:
    gpio.output(dac, 0)
    gpio.cleanup(dac)