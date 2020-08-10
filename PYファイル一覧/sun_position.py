import math
from datetime import datetime, date, timedelta
import time

"""太陽高度の計算式:太陽光線と地球の赤道面との角度、±23°27'の範囲で変化"""
#sinh = sinφ sinδ + cosφ cosδ cost
def sinh(ido,sekii,jikaku):
    sinhigh = math.sin(math.radians(ido))*math.sin(math.radians(sekii)) + math.cos(math.radians(ido))*math.cos(math.radians(sekii))*math.cos(math.radians(jikaku))
    sinhigh = math.asin(sinhigh)
    deg = round(math.degrees(sinhigh),2)
    return deg

#θo=2π(dn-1)/365の計算
def angle(date):
    timestamp_str = date
    t = datetime.strptime(timestamp_str, '%Y/%m/%d') 
    dayofyear = t.timetuple().tm_yday #元旦からの経過日数
    ang = ((2 * math.pi) / 365) * (dayofyear+0.5)
    return ang

#太陽赤緯の計算 sekii
def sunline(date):
    ang = angle(date)
    line_ang = 0.33281-22.984*math.cos(ang)-0.34990*math.cos(2*ang)-0.13980*math.cos(3*ang)+3.7872*math.sin(ang)
    line_ang2 = 0.03250*math.sin(2*ang)+0.07187*math.sin(3*ang)
    line_final =line_ang+line_ang2
    return line_final

"""時角の計算   t = (th -12) × 15  (t：時角[°]、th：(地方)真太陽時[時:分])"""
#th = tm + e (th：地方真太陽時[時:分]、tm：地方平均太陽時[時:分]、e：均時差[時:分])
#th = Tm + (L -135[°])×4 + e
#均時差：　e（天球上を一定な速さで動くと考えた平均太陽と、実際の太陽との移動の差、17分未満）　[単位： 時間]
#e = 0.0072 cos(ωJ ) - 0.0528 cos(2ωJ ) - 0.0012 cos(3ωJ )- 0.1229 sin(ωJ ) - 0.1565 sin(2ωJ ) - 0.0041 sin(3ωJ )
def kinjisa(date):
    ang = angle(date)
    kinji = 0.0072*math.cos(ang)-0.0528*math.cos(2*ang)-0.0012*math.cos(3*ang)-0.1229*math.sin(ang)-0.1565*math.sin(2*ang)-0.0041*math.sin(3*ang)
    kinji = math.floor(kinji*60)
    return kinji #単位：分
   
    
#現在時刻を分に直し、均時差を足して、分計算後、時間表示
#kinjisa('2020/6/1') 
def th (hour,minutes,date,keido):
    thhours = hour*60+minutes+kinjisa(date) #単位:分
    keidosabunn = (keido-135)*4 #単位:分
    time = thhours+keidosabunn
    a =round(time/60,3) #時間換算
    return a  
#時角計算
def jikaku(hour,minutes,date,keido):
    a = th(hour,minutes,date,keido)
    ta = (a-12)*15
    return(ta)
#太陽高度の計算
#sinh = sinφ sinδ + cosφ cosδ cost  h：太陽高度[°]、φ：ある地点の緯度[°]、δ：太陽赤緯[°]、t：時角(真太陽時)[°]
def taiyoukoudo(date,hour,minutes,keido,ido):
    sekii = sunline(date)
    ido = ido
    jikaku1 = jikaku(hour,minutes,date,keido)
    sinhigh = math.sin(math.radians(ido))*math.sin(math.radians(sekii)) + math.cos(math.radians(ido))*math.cos(math.radians(sekii))*math.cos(math.radians(jikaku1))
    sinhigh = math.asin(sinhigh)
    deg = round(math.degrees(sinhigh),2)
    return deg
    
taiyoukoudo('2020/6/1',12,0,139.77,35.68)

"""sinA = cosδ sint / cosh
cosA = (sinh sinφ – sinδ) / cosh cosφ
(A：太陽方位角[°]、h：太陽高度[°]、φ：ある地点の緯度[°]、δ：太陽赤緯[°]、t：時角(真太陽時)[°])"""
def houi(date,hour,minutes,keido,ido):
    h = taiyoukoudo(date,hour,minutes,keido,ido)
    ido = ido
    sekii = sunline(date)
    jikaku1 = jikaku(hour,minutes,date,keido)
    sinA = (math.cos(math.radians(sekii))*math.sin(math.radians(jikaku1))) / math.cos(math.radians(h))
    sinA = math.asin(sinA)
    sinA = round(math.degrees(sinA),2)
    
    
    cosAa = (math.sin(math.radians(h)))*(math.sin(math.radians(ido))) - math.sin(math.radians(sekii))
    cosAb = (math.cos(math.radians(h)))*(math.cos(math.radians(ido)))
    cosA = cosAa / cosAb
    cosA = math.acos(cosA)
    cosA = round(math.degrees(cosA),2)  
    #return (abs(cosA))    
    if cosA > 0:
        south_north = "真南"
    else:
        south_north = "真北"
        
    if sinA > 0:
        west_east = "西"
    else:
        west_east = "東"
    line ="{}より{}へ{}°".format(south_north,west_east,(abs(cosA)))
   
    return [south_north,west_east,(abs(cosA)),"高度は⇛",h]
    print(line)
    
#例文⇛houi('2020/6/1',12,0,139.77,35.68)    ⇛　　回答：真南より西へ20.21°
if __name__ == '__main__':
    houi('2020/6/22',12,0,139.77,35.68)
    taiyoukoudo('2020/6/22',12,0,139.77,35.68)
    
houi('2020/6/22',12,0,139.77,35.68)



