import csv
import numpy as np
import time

filepath ="./csv_files/channel2.csv"
while True:
    with open(filepath,'r') as f:
        cutboard = f.read().split(',')
    cutboard = list(np.float_(cutboard))
    cutboard = np.array(cutboard)
    print(cutboard[0])
    time.sleep(3)