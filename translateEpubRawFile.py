# -*- coding: utf-8 -*-
import bs4
import sys
import requests

def api(text, font):
    url = "http://localhost:8080/api/text/" + font
    r = requests.post(url, data=text.encode('utf-8'))
    r.encoding = 'utf-8'
    return r.status_code, r.text

def english(s):
    classes = ['englishMeaning', 'char-style-override-6', 'char-style-override-11', 'char-style-override-5', 'char-style-override-12']
    # return true if any of the classes is present in the class list
    if s.has_attr('class'):
        for c in s['class']:
            if c in s['class']:
                return True
    return False

with open(sys.argv[1], 'r') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')
    for d in soup.descendants:
        if type(d) == bs4.element.NavigableString:
            print d.parent.name, type(d.parent)
            d = 'STRING'
    #for span in [s for s in soup.find_all('span') if s.string and not english(s)]:
    #    status, text = api(span.string, 'Walkman-Chanakya-901')
    #    if status == 200:
    #        span.string.replace_with(text)

    print(soup)
