import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
comp = 14
troyka = 13
gpio.setup(led, gpio.OUT)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def binary(a):
    return [int(bit) for bit in bin(a)[2:].zfill(bits)]
    
def abc(troyka):
    a = 0
    for i in range(7, -1, -1):
        a += 2**i
        gpio.output(dac, binary(a))
        sleep(0.0008)
        compvalue = gpio.input(comp)
        if(compvalue == 1):
            a -= 2**i
    return a
    
def fun(a):
    signal = binary(a)
    gpio.output(dac,signal)
    return signal
    
try:
    while True:
        print(binary(abc(troyka)), abc(troyka)/256*3.3)
finally:
    gpio.output(dac, 0)
    gpio.cleanup(dac)