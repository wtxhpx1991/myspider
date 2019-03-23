# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor
from docx.shared import Pt
from docx.shared import Cm
from docx.oxml.ns import qn

# 读取中文
penalty_title_pattern = re.compile("[\u4e00-\u9fa5]+")
# 设置头文件
head = {}
head[
    'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"

# 初始网址
start_download_url = "http://www.csrc.gov.cn/pub/zjhpublic/3300/3313/index_7401_"
# 行政处罚决定书页面数量，目前是60页
# 不知道怎么自动抓这个数字
PAGE_NUMBER=60
# 生成网页链接
download_url_set=["http://www.csrc.gov.cn/pub/zjhpublic/3300/3313/index_7401.htm"]
for i in range(PAGE_NUMBER-1):
    download_url_set.append(start_download_url+str(i+1)+".htm")

# 对每一个页面，首先抓取全部链接，然后根据链接里的内容生成word
for download_url in download_url_set:
    download_req = request.Request(url=download_url, headers=head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('UTF-8', 'ignore')
    soup_texts = BeautifulSoup(download_html, 'lxml')
    # 获取页面核心数据
    soup_core_texts_html = soup_texts.find_all("div", attrs={"class": "row"})
