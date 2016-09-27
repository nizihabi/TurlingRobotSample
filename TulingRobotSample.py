# -*- coding: utf-8 -*-
import urllib.request
import json
import base64

API_KEY = "**************************"
 
CONSTURL = "http://www.tuling123.com/openapi/api?key=%s&userid=toby&info=" % API_KEY

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
            content="小小叽：" + hjson["text"]
            if  "list" in hjson:
                for i in hjson["list"]:
                    for (lsk ,lsv) in i.items():
                        if lsk == "icon":
                            continue
                        content = content + "\r\n"
                        content = content + str(lsv)
            if "url" in hjson:
                content = content + "\r\n"+ hjson["url"]
            return content

    

if __name__=='__main__':
    littleG = Robot(API_KEY)
    print( "你好，请输入内容: [输入exit 退出程序]")
    while True:
        queryStr = input("我:")
        if queryStr == "exit" :
           break
           
        answer = littleG.getAnswer(queryStr)
        print (answer)
