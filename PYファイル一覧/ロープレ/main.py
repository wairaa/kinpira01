'''プレイヤーからの入力値を取得する関数'''
from controller import *
import random
import time
#攻撃方法を選択する関数
def choice():
    return input('[武器を使う(0) / フォースを使う(1) ]')
#武器を選択する関数
def arm_choice():
    return input('[ライトセーバー(0)/' + 'クロスガードライトセーバー(1)/'+'ダブルブレード(2)]')
#呪文を選択する関数
def magic_choize():
    return input('[テレキネシス(0)/マインドトリック(1)/フォースダッシュ(2)]')
#リスタート選択関数
def is_restart():
    return input('もう1回やる(やる(0)/やめる(1))')


