# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re

penalty_title_pattern = re.compile("[\u4e00-\u9fa5]+")

download_url = "http://www.csrc.gov.cn/pub/zjhpublic/G00306212/201903/t20190319_352989.htm"
head = {}
head[
    'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
download_req = request.Request(url=download_url, headers=head)
download_response = request.urlopen(download_req)
download_html = download_response.read().decode('UTF-8', 'ignore')
soup_texts = BeautifulSoup(download_html, 'lxml')
penalty_title=soup_texts.find_all("script")
penalty_texts = soup_texts.find_all("p",attrs={"class":"p0"})

penalty_title_result=penalty_title_pattern.findall(str(penalty_title))
penalty_texts_result=""
for i in penalty_texts:
    penalty_texts_result=penalty_texts_result+i.text+"\n"
print(penalty_title_result[0]+"\n"+penalty_title_result[1]+penalty_texts_result)





# 抓取正文





# download_url = 'http://www.biqukan.com/1_1094/5403177.html'
# head = {}
# head[
#     'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
# download_req = request.Request(url=download_url, headers=head)
# download_response = request.urlopen(download_req)
# download_html = download_response.read().decode('gbk', 'ignore')
# soup_texts = BeautifulSoup(download_html, 'lxml')
# texts = soup_texts.find_all(id='content', class_='showtxt')
# soup_text = BeautifulSoup(str(texts), 'lxml')
# # 将\xa0无法解码的字符删除
# print(soup_text.div.text.replace('\xa0', ''))
