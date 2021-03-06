import json
import re

import appex
import requests
import ui
from bs4 import BeautifulSoup


def nansu():
    url = 'https://ameblo.jp/natsukawashiinablog/'
    try:
        response = requests.get(url)
        response.encoding = 'UTF-8'

        html = BeautifulSoup(response.text, 'html5lib')
        new_title_html = html.find("a", {"class": "skinArticleTitle"})
        new_title = re.sub(' |\n', '', str(new_title_html.string))
        print(new_title)
        label = ui.Label(font=('Menlo', 20), alignment=ui.ALIGN_CENTER)
        label.text = '最新記事: ' + new_title
        appex.set_widget_view(label)
    except:
        pass


nansu()
