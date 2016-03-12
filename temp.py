import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

dev_dir = '/sys/bus/w1/devices/'
dev = glob.glob(dev_dir + '28*')[0]
dev_cmd = os.path.join(dev, 'w1_slave')

def read_dev():
    with open(dev_cmd) as f:
        lines = f.readlines()
    return lines

def temp():
    lines = read_dev()
    while 'YES' not in lines[0]:
        time.sleep(0.5)
        lines = read_dev()

    _, _, value = lines[1].partition('=')
    if value:
        return float(value) / 1000.0
    return None

def main():
    while True:
        print temp()
        time.sleep(1)

if __name__ == '__main__':
    main()

