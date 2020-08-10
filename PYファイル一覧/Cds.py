#光センサーの情報を出力
import csv
import serial

ser = serial.Serial('/dev/ttyACM1', timeout=2000) #timeout(秒)→処理完了できない場合、中止できる時間
smoothing = 100 # log 100 data to confirm stability later

with open('ArduinoRead.csv', 'w') as f: #withでファイルopen、処理、ファイルクローズを一連で行う。
  writer = csv.writer(f)
  a = [ser.read(smoothing)]
  writer.writerow(a) #Writerオブジェクトに、writerowで、csvファイルへ一行の書き込みが可能。
  f.close()　#f.closeは不要？
print("csv wrote")

