#-*- coding = utf-8 -*-
#@Time: 2020/6/3 
#@Software: PyCharm

import jieba        #分词
from jieba import analyse
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import xlrd

#准备词云所需的文字
data = xlrd.open_workbook('douban_movie_top250.xls')
table = data.sheet_by_name(u'豆瓣电影Top250')        #通过名称获取
text = ""
for item in  table.col_values(6):
    text = text + item

#分词，top50关键字
tags = jieba.analyse.extract_tags(text, topK=50, withWeight=False)
# cut = jieba.cut(text)
# print(type(cut))
string  = ' '.join(tags)
# print(len(string))
print(string)

img = Image.open(r'tree.jpg')   #打开遮罩图片
img_array = np.array(img)   #将图片转化为数组

stopwords = set('')
stopwords.update(['电影', '我们', '一个', '不会', '不要', '就是', '这样', '永远', '不是'])
# Generate a word cloud image
wc = WordCloud(
    background_color='white',
    stopwords=stopwords,
    mask=img_array,
    font_path = r"Hiragino Sans GB.ttc"      #字体
)
wc.generate(string)


# Display the generated image:
# the matplotlib way:
fig = plt.figure(1)
plt.imshow(wc)
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()