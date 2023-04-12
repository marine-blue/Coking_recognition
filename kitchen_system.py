import csv
import matplotlib.pyplot as plt
import numpy as np
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
i = 0

if __name__ == '__main__':
    key_prev = 1000
    key_in =1000
    path_index = 0
    model = load_model('./kitchen_model.h5')
    while True:
        cutboard = []
        filepath ="./csv_files/channel2.csv"  
        with open(filepath,'r') as f:
            cutboard = f.read().split(',')
        cutboard = list(np.float_(cutboard))
        cutboard = np.array(cutboard)
        img_x = []
        for i in range(4):
            sta = 1800*i                      
            end = 1800*(i+1)                  
            cutboard_w = cutboard[sta:end]
            f,t,Sxx = signal.spectrogram(cutboard_w,1800)
            plt.pcolormesh(t, f, 10*np.log(Sxx)) #intensityを修正
            plt.axis('off')
            plt.savefig("./realtime"+str(i)+".png")

            #data preprocessing from image to array
            img = cv2.imread("./realtime"+str(i)+".png")
            img = cv2.resize(img,(224,224))
            img_x.append(img)

        img_x = np.array(img_x)
        img_x = img_x.astype('float32')
        img_x /= 255

        result=model.predict(img_x)[3]              #last window
        
        key_in = result.argmax()
        if key_in != key_prev:
            path = "C:/Users/81702/OneDrive/デスクトップ/NAIST_Ubi/sample_html/sample"+str(path_index)+".html"
        driver.get(path)
        time.sleep(10)
        key_prev = key_in
driver.close()