#-*- coding = utf-8 -*-
#@Time: 2020/5/30 
#@Software: PyCharm

from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error  #指定URL，获取网页数据
import xlwt    #进行Excel操作
import sqlite3  #进行SQLite数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = "douban_movie_top250.xls"
    # 3.保存数据
    saveData(savepath)

    # askURL("https://movie.douban.com/top250?start=0")

#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串的模式）
#影片图片
findImageSrc = re.compile(r'<img.*src="(.*?)"', re.S)   #re.S 让换行符包含在字符中
#影片名
findTitle = re.compile(r'span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

datalist = []

#1.爬取网页
def getData(baseurl):
    for i in range(0,10):           #调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url)          #保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div',class_="item"):     #查找符合要求的字符串，形成列表
            #print(item)                            #测试，查看电影item全部信息
            data = []                               #保存一步电影的所有信息
            item = str(item)

            # 获取影片详情的链接
            link = re.findall(findLink, item)[0]    #re库用来通过正则表达式查找指定的字符串
            data.append(link)                       #添加链接

            imgSrc = re.findall(findImageSrc, item)[0]
            data.append(imgSrc)                     #添加图片

            titles = re.findall(findTitle, item)    #片名可能只有一个中文名
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)                 #添加中文名
                otitle = titles[1].replace("/", "")  #去掉无关的符号
                data.append(otitle)                 #添加外文名
            else:
                data.append(titles[0])
                data.append(" ")                    #外国名字留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)                     #添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)                   #添加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")      #去掉句号
                data.append(inq)                    #添加概述
            else:
                data.append(" ")                    #留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)    #去掉<br/>
            bd = re.sub('/', " ", bd)              #替换/
            data.append(bd.strip())                #去掉前后的空格

            datalist.append(data)                  #把处理好的信息放入datalist

    return datalist


#得到指定一个URL的网页内容
def askURL(url):
    headers = {
        # 模拟浏览器头部信息，向豆瓣服务器发送信息
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html  = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


 #3.保存数据
def saveData(savepath):
    print("saving...")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)  #创建workbook对象
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)    #创建工作表
    col = ("电影详情概述", "图片链接", "影片中文名", "影片外文名", "评分", "评分数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])   #列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j]) #数据

    book.save(savepath)     #保存


if __name__ == "__main__":
    main()
    print("爬取完毕！")
