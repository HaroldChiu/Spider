#-*- coding = utf-8 -*-
#@Time: 2020/6/1 
#@Software: PyCharm

from bs4 import BeautifulSoup

#1. Tag 标签及其内容，拿到所找到的第一个内容
#2. NavigableString 标签里的内容（字符串）
#3. BeautifulSoup 表示整个文档
#4. Comment 是一个特殊的NavigableString，输出的内容不包含注释符号



# 文档的遍历



# 文档的搜索

#(1) find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
#t_list = bs.find_all("a")


# 正则表达式搜索：使用search()方法来匹配内容
# t_list  = bs.find_all(re.compile("a"))


# 方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists())



#(2) kwargs 参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(href="http://news.baidu.com")
# t_list = bs.find_all(class_=True)



#(3) text参数
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# for item in t_list:
#     print(item)

#(4)limit 参数
# t_list  = bs.find_all("a"， limit=3)



#css选择器
# t_list = bs.select('title')    #通过标签来查找
#
# t_list = bs.select('.mnav')    #通过类名来查找
#
# t_list = bs.select('#u1')    #通过id来查找
#
# t_list = bs.select('a[class="bri"]')    #通过属性来查找
#
# t_list = bs.select('head > title')    #通过子标签来查找