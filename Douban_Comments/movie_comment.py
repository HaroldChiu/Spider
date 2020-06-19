import requests
from bs4 import BeautifulSoup
import pandas as pd

#豆瓣《教父》地址
url = 'https://movie.douban.com/subject/1291841/comments?start=0&limit=20&sort=new_score&status=P'

#获取cookie值（略去cookie值则仅能爬取前二十页数据），模拟登陆
ck='ll="118238"; bid=hcbHNtzv8b4; gr_user_id=2d126497-b499-46ee-9275-15b478d0609e; _vwo_uuid_v2=D6AB96FFEF8D3BE49F1208E1EB25D60CC|0b87311fc6de84dd5f4b706249c2e57f; __gads=ID=d32ccef7e66c9bfb:T=1563062245:S=ALNI_MbzUKNVsCB0Cj_87-MG4YLb56QOAA; __yadk_uid=JKUEf8CExYOf76R1XPN903jLTjS3oVsz; viewed="4913064"; ct=y; trc_cookie_storage=taboola%2520global%253Auser-id%3Dedbcb957-d43c-475b-9ef7-4e0a24af6e4c-tuct42749ea; douban-fav-remind=1; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utma=30149280.1797971680.1563014790.1563321748.1563408714.12; __utmc=30149280; __utmz=30149280.1563408714.12.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmv=30149280.16315; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1563408735%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fsource%3Dsuggest%26q%3D%25E6%25B7%25B1%25E5%25A4%259C%25E9%25A3%259F%25E5%25A0%2582%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.1883369083.1563103010.1563321754.1563408735.4; __utmb=223695111.0.10.1563408735; __utmc=223695111; __utmz=223695111.1563408735.4.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmt=1; __utmb=30149280.7.10.1563408714; dbcl2="163150289:pcJJ8qv7vVk"; ck=ALyo; _pk_id.100001.4cf6=fb693c531fbf9f1d.1563103009.4.1563410743.1563322323.'

#将cookie放在headers中一起发送请求
headers = {
    'cookie':ck,
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

}
r = requests.get(url,headers=headers)
#打印状态码，2##表示成功获取页面
print(r.status_code)

#利用BeautifulSoup解析页面
soup = BeautifulSoup(r.text,'html.parser')
# print(r.text)

#CSS选择器指定选择元素
print('正在抽取500条短评')
comment_number = 500
n = comment_number//20

#pandas DataFrame表格,创建表格
df = pd.DataFrame([[1, 1, 1, 1]])
df.columns =['评论者', '时间', '评分','内容']
for i in range(n):
    url = 'https://movie.douban.com/subject/1291841/comments?start={}&limit=20&sort=new_score&status=P'
    url = url.format(i*20)
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    reviewer_v = soup.select('.comment .comment-info a')
    data_v = soup.select('.comment .comment-time')
    goal_v = soup.select('.comment .comment-info .rating')
    content_v = soup.select('.comment .short')
    print(len(goal_v))
    #如果第i页没有数据，则跳出循环
    if len(goal_v)==0:
        break
    #修改表格内容
    for j in range(len(goal_v)):
        r = reviewer_v[j].get_text()
        d = data_v[j].get_text().replace(' ', '').replace('\n', '')
        g = goal_v[j]['title']
        c = content_v[j].get_text()
        df.loc[i*20+j] = [r, d, g, c]
    print('正在导出第%d页' % i)
#to_csv导出为.csv文件；to_excel导出为.xls或.xlsx文件
df.to_excel('TheGodfather_comments.xlsx',index=False)
print('导出完成！')
