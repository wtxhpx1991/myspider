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

penalty_title_pattern = re.compile("[\u4e00-\u9fa5]+")

download_url = "http://www.csrc.gov.cn/pub/zjhpublic/G00306212/201903/t20190319_352989.htm"
head = {}
head[
    'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
download_req = request.Request(url=download_url, headers=head)
download_response = request.urlopen(download_req)
download_html = download_response.read().decode('UTF-8', 'ignore')
soup_texts = BeautifulSoup(download_html, 'lxml')
penalty_title = soup_texts.find_all("script")
penalty_texts = soup_texts.find_all("p", attrs={"class": "p0"})

penalty_title_result = penalty_title_pattern.findall(str(penalty_title))
penalty_texts_result = ""
for i in penalty_texts:
    penalty_texts_result = penalty_texts_result + i.text + "\n"
print(penalty_title_result[0] + "\n" + penalty_title_result[1] + penalty_texts_result)



document = Document()
title = document.add_heading(penalty_title_result[0] + "\n" + penalty_title_result[1]+ "\n" +penalty_texts[1].text, 0)  # 插入标题
title.alignment = WD_ALIGN_PARAGRAPH.CENTER  # 标题居中
title.style.font.color.rgb=RGBColor(255,0,0)
for i in penalty_texts[4:len(penalty_texts)]:
    p = document.add_paragraph(i.text)
    p.style.font.name='Times New Roman'
    p.style.element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    p.paragraph_format.first_line_indent = Cm(0.74)
    p.style.font.size = Pt(15)
documenttitle= penalty_title_result[0] + penalty_texts[1].text+penalty_title_result[1]+".docx"
document.save(documenttitle)