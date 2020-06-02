#-*- coding = utf-8 -*-
#@Time: 2020/5/30 
#@Software: PyCharm

import urllib.request

#获取get请求
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode('utf-8'))

# 获取post请求
import urllib.parse

# data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data = data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode("utf-8"))
#
# except urllib.error.URLError as e:
#     print("Time out!")

#状态
# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)

#user-agent伪装
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name":"eric"}), encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


#访问豆瓣
url = "https://douban.com"

#用户代理
headers = {
    #模拟浏览器头部信息，向豆瓣服务器发送信息
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
