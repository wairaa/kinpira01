
from responder import *
import random

"""応答オブジェクトを呼び分けるクラス"""
class Controller:
    #応答オブジェクトを生成してインスタンス変数に格納
    def __init__(self):
        self.lucky = LuckyResponse() #luckyがインスタンス変数
        self.draw = DrawResponse()
        self.bad = BadResponse()
     #サブクラスのresponseを呼び出して応答文字列と変動値を取得する   
    def attack(self, point):
        x = random.randint(0, 100)
        if x <= 30:
            self.responder = self.lucky
        elif 31 <= x <= 60:
            self.responder = self.draw
        else :
            self.responder = self.bad
        #response()を実行し、戻り値をそのまま返す
        return self.responder.response(point)

#プログラム実行ブロック
if __name__ == '__main__':
    
    
    point = 3
    ctr = Controller()
    res = ctr.attack(point)
    print(res)


