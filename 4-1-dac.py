import RPi.GPIO as gpio
import sys
dac = [8,11,7,1,0,5,12,6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def p(a,n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]
try:
    while (True):
        a = input('Input a number from 0-255:')
        if a.lower() == 'q':
            sys.exit()
        elif a.isdigit() and int(a)%1 == 0 and 0 <= int(a) <= 255:
            gpio.output(dac, p(int(a), 8))
            print("{:.4f}".format(int(a)/256*3.3))
        elif not a.isdigit():
            print('Please, input a number from range 0-255')
except ValueError:
    print('Input a number from range [0, 255]')
except KeyboardInterrupt:
    print('Done')
finally:
    gpio.output(dac,0)
    gpio.cleanup()