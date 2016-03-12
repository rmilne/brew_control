import os
import time
import sys

import RPi.GPIO as gpio

from datetime import datetime
from temp import *

SLEEP = 60
TARGET = 20.0

def heat(val):
    gpio.output(21, val)

def main():
    gpio.setmode(gpio.BCM)
    gpio.setup(21, gpio.OUT)
    heat(False)

    while True:
        curr = temp()
        relay = curr < TARGET
        heat(relay)
        file_name = datetime.now().strftime('%Y_%m_%d.log')
	with open(file_name, 'a') as f:
            f.write('%s:  %f\t %s\n' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), curr, relay))
        time.sleep(SLEEP)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print '\nExiting\n'
    except Exception as e:
        print 'exception: %s' % e
    gpio.cleanup()
