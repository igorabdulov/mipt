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
    
def fun(a):
    for i in range(8, 0, -1):
        if (i * 32 - 1) <= a:
            return binary(2**i - 1)
    return binary(0)
            
def abc(troyka):
    a = 0
    for i in range(7, -1, -1):
        gpio.output(dac, binary(a + 2**i))
        sleep(0.0008)
        if gpio.input(comp) == 0:
            a += 2**i
    return a
    
try:
    while True:
        gpio.output(led, fun(abc(troyka)))
finally:
    gpio.output(dac, [0] * 8)
    gpio.cleanup(dac)