import csv
from tracemalloc import start
import matplotlib.pyplot as plt
import numpy as np
from pyparsing import Or
from scipy import signal
import os
import cv2
import time
import tensorflow as tf
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.preprocessing import image
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer
from selenium import webdriver

driver = webdriver.Chrome("C:/webdriver/chromedriver_win32/chromedriver")
start_t = time.time()
cooking_files =[
    ["C:/Users/81702/OneDrive/デスクトップ/NAIST_Ubi/sample_html/sample0.html",0],
    ["C:/Users/81702/OneDrive/デスクトップ/NAIST_Ubi/sample_html/sample1.html",90],
    ["C:/Users/81702/OneDrive/デスクトップ/NAIST_Ubi/sample_html/sample2.html",240]
]
key_prev = 1000
key_in =1000
index = 0
model = load_model('./kitchen_model.h5')
while True:
    cutboard = []
    filepath ="./csv_files/Channel2.csv"
    with open(filepath,'r') as f:
        cutboard = f.read().split(',')
    cutboard = list(np.float_(cutboard))
    cutboard = np.array(cutboard)
    cutboard = cutboard[::4]
    img_x = []

    f,t,Sxx = signal.spectrogram(cutboard,1800)
    plt.pcolormesh(t, f, 10*np.log(Sxx)) #intensityを修正
    plt.axis('off')
    plt.savefig("./realtime.png")

    #data preprocessing from image to array
    img = cv2.imread("./realtime.png")
    img = cv2.resize(img,(224,224))
    img_x.append(img)

    img_x = np.array(img_x)
    img_x = img_x.astype('float32')
    img_x /= 255
    
    result=model.predict(img_x)             
    current_t = time.time()

    key_in = result.argmax()
    print(result)
    if (int(current_t- start_t) > cooking_files[index][1]  or key_in != key_prev):
        driver.get(cooking_files[index][0])
        index += 1
        start_t = current_t
        key_prev = key_in
    time.sleep(3)
driver.close()