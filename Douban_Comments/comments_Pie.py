#-*- coding = utf-8 -*-
#@Time: 2020/6/7 
#@Software: PyCharm

from pyecharts.charts import Pie
from pyecharts.charts import Bar
from pyecharts import options as opts
import xlrd

# 读取xlsx文件
data_cn = xlrd.open_workbook(r'TheGodfather_comments.xlsx')
table_cn = data_cn.sheets()[0]
tables_cn = []

def Read_Excel(excel):
    for row in range(1, excel.nrows - 1):
        dict_ = {
            'commentator': '', 'comment_time':'', 'ranking':'', 'comments': ''
        }
        dict_['commentator'] = table_cn.cell_value(row, 0)
        dict_['comment_time'] = table_cn.cell_value(row, 1)
        dict_['ranking'] = table_cn.cell_value(row, 2)
        dict_['comments'] = table_cn.cell_value(row, 3)
        tables_cn.append(dict_)

Read_Excel(table_cn)
# for i in tables_cn:
#     print(i)

num_ranking_5 = 0
num_ranking_4 = 0
num_ranking_3 = 0
num_ranking_2 = 0
num_ranking_1 = 0
for i in tables_cn:
    score = i['ranking']
    if i['ranking'] == "力荐":
        num_ranking_5 += 1
    if i['ranking'] == "推荐":
        num_ranking_4 += 1
    if i['ranking'] == "还行":
        num_ranking_3 += 1
    if i['ranking'] == "较差":
        num_ranking_2 += 1
    if i['ranking'] == "很差":
        num_ranking_1 += 1

# print(num_ranking_5)
bar_x_axis_data = ("5星", "4星", "3星", "2星", "1星")
bar_y_axis_data = (num_ranking_5, num_ranking_4, num_ranking_3, num_ranking_2, num_ranking_1)

pie = (
    Pie(init_opts=opts.InitOpts(height="800px", width="1200px"))
    .add("评分概览",
              [list(z) for z in zip(bar_x_axis_data, bar_y_axis_data)],
              center=["35%", "38%"],
              radius="40%",
              label_opts=opts.LabelOpts(
                  formatter="{b|{b}: }{c}  {per|{d}%}  ",
                  rich={
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            }
        ))
        .set_global_opts(title_opts=opts.TitleOpts(title="TheGodfatherRanking"),
                          legend_opts=opts.LegendOpts(pos_left="0%", pos_top="65%"))
        .render("comments_Pie.html")
)

