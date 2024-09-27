class Responder:
    def response(self, point):
        return''
    
class LuckyResponse(Responder):
    def response(self, point):
        return['モンスターにダメージを与えた', point]
    
class DrawResponse(Responder):
    def response(self, point):
        point = 0
        return['モンスターは身を守っている', point]
    
class BadResponse(Responder):
    def response(self, point):
        return['モンスターが反撃した', -point]
    
if __name__ == '__main__':
    
    
    point = 3
    responder = LuckyResponse()
    res = responder.response(point)
    print(res)
    
    responder = DrawResponse()
    res = responder.response(point)
    print(res)
    
    responder = BadResponse()
    res = responder.response(point)
    print(res)
    
    
    
    
    



