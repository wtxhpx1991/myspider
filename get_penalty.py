from urllib import request
from bs4 import BeautifulSoup
from datetime import datetime
import re

# 读取中文
penalty_title_pattern = re.compile("[\u4e00-\u9fa5]+")

download_url = "http://www.csrc.gov.cn/pub/zjhpublic/3300/3313/index_7401.htm"
head = {}
head[
    'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
download_req = request.Request(url=download_url, headers=head)
download_response = request.urlopen(download_req)
download_html = download_response.read().decode('UTF-8', 'ignore')
soup_texts = BeautifulSoup(download_html, 'lxml')
# 获取页面核心数据
soup_core_texts_html = soup_texts.find_all("div", attrs={"class": "row"})

for tag in soup_core_texts_html:
    print(tag.find("a").get_text())
    print(tag.find("a").attrs['href'].split("/")[-1])
    tag_datetime=tag.find("li", class_="fbrq").get_text()
    tt = datetime.strptime(tag_datetime, u"%Y年%m月%d日")
    print(datetime.strftime(tt, "%Y%m"))

