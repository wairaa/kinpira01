import sun_position
import math
import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート ラズパイでしかinstall不可？
import time                         #時間制御用のモジュールをインポート　使用しないかも？
import sys                          #sysモジュールをインポート   使用しないかも？
"""家のモータはＭＩＣＲＯ／２ＢＢＭＧ。PWM不明、制御パルス不明"""
a = sun_position.houi('2020/12/3',7,12,135.28,34.41)
a[2] = math.floor(a[2])  #角度を整数に変更
a[4] = math.floor(a[4])
ang = 0
if a[1]=="東":
    ang = -90 + a[2]
else:
    ang = 90 - a[2]

"""サーボを水平方向に動かす　-90°は右回り、90°は左回り前提　"""
#ポート番号の定義
Servo_pin = 18                      #変数"Servo_pin"に18を格納
#GPIOの設定
GPIO.setmode(GPIO.BCM)              #GPIOのモードを"GPIO.BCM"に設定
GPIO.setup(Servo_pin, GPIO.OUT)     #GPIO18を出力モードに設定

#PWMの設定
#サーボモータSG90の周波数は50[Hz]　pwm =20ms(ミリセカンド) 
#パルス幅が20ms⇛１秒で何回パルスが発生するか⇛1000(1秒) ÷　20 = 50
Servo = GPIO.PWM(Servo_pin, 50)     #GPIO.PWM(ポート番号, 周波数[Hz])
Servo.start(0)                      #Servo.start(デューティ比[0-100%])

#角度からデューティ比を求める関数
#制御パルス0.5ms～2.4ms pwm =20ms
#0.5÷20=0.025⇛2.5%    2.4÷20=0.12⇛12% ⇛デューティ比率は2.5%(-90°)〜12%(90°)
#Micro/2BBmgが-90°〜90°までか？制御パルスがどれくらいか不明？
def servo_angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180   #角度からデューティ比を求める
    Servo.ChangeDutyCycle(duty)     #デューティ比を変更
    
"""サーボを垂直方向に動かす　0°〜90°　サーボモータは未決定のため、Servo変数の50等は別数字"""
vertical = a[4]
Servo_pin = 24                     #変数"Servo_pin"に24を格納
#GPIOの設定
GPIO.setmode(GPIO.BCM)              #GPIOのモードを"GPIO.BCM"に設定
GPIO.setup(Servo_pin, GPIO.OUT)     #GPIO18を出力モードに設定
Servo = GPIO.PWM(Servo_pin, 50)     #GPIO.PWM(ポート番号, 周波数[Hz])
Servo.start(0)                      #Servo.start(デューティ比[0-100%])
def servo_angle2(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180   #角度からデューティ比を求める
    Servo.ChangeDutyCycle(duty)     #デューティ比を変更

    
 
    
servo_angle(ang)
servo_angle2(vertical)


