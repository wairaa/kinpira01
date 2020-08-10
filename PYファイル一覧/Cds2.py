#光センサーの日付と情報の表示とCSV出力
import csv
import serial
import datetime
import time
import re
format = "%Y.%m.%d %H:%M:%S"
tt = time.strftime(format, time.localtime())
ser = serial.Serial('/dev/ttyACM0', timeout=2000)
f = open('ArduinoRead.csv', 'w') 
csvWriter = csv.writer(f)
smoothing = 100# log 100 data to confirm stability later
Column = ['date','Light-sensor']
csvWriter.writerow(Column)
for i in range(1, 30):
    t1=time.strftime(format, time.localtime())
    aa = [ser.readline(smoothing)]
    #文字列数字を数値に変換
    listData = []
    listData.append(t1)
    listData.append(aa)
    csvWriter.writerow(listData)
    print(listData)
f.close()
    
