# -*- coding: utf-8 -*-
import urllib.request
import json
import base64

API_KEY = ""

with open("api.data","r") as f:
    ecrypt = base64.b64decode(f.read().encode("utf-8"))
    API_KEY = ecrypt.decode("utf-8")
    
CONSTURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY

class Robot(object):

    def __init__(self,key):
        self.__apiKey = key

    def getAnswer(self,question):
        tulinUrl = "%s%s" % (CONSTURL,urllib.parse.quote(queryStr))
        req = urllib.request.Request(url=tulinUrl)
        result = urllib.request.urlopen(req).read()
        hjson=json.loads(result.decode("utf-8"))
        if hjson["code"] == 40004:
            return "小小叽今天已经累了，改天再玩吧"
        else:
            length=len(hjson.keys())
            content=hjson["text"]
            if length==3:
                return "小小叽:" + content+ "\r\n" + hjson["url"]
            elif length==2:
                return "小小叽:" + content

    

if __name__=='__main__':
    littleG = Robot(API_KEY)
    print( "你好，请输入内容: [输入exit 退出程序]")
    while True:
        queryStr = input("我:")
        if queryStr == "exit" :
           break
           
        answer = littleG.getAnswer(queryStr)
        print (answer)
