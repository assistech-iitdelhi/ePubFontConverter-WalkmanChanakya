# -*- coding: utf-8 -*-
import bs4
import sys
import pdb
import requests

def api(text, font):
    url = "http://assistech.iitd.ac.in/ravi/api/text/" + font
    r = requests.post(url, data=text.encode('utf-8'))
    r.encoding = 'utf-8'
    return r.status_code, r.text

def english(s):
    classes = ['englishMeaning', 'char-style-override-6', 'char-style-override-11', 'char-style-override-5', 'char-style-override-12']
    # return true if any of the classes is present in the class list
    if s.has_attr('class'):
        for c in s['class']:
            if c in classes:
                return True
    return False

with open(sys.argv[1], 'r') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')
    for d in list(soup.body.descendants):
        if type(d) == bs4.element.NavigableString:
            if not english(d.parent):
                status, text = api(unicode(d.string), 'Walkman-Chanakya-901')
                if status == 200:
                    d.replace_with(text)

    print(soup)
