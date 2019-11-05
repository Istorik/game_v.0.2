#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import html
import http.cookies
import cgi
from _wall import Html

wall = Html()


form = cgi.FieldStorage()
Name_group = form.getfirst("Name_group", "Djn")

content = '''\
Добро пожаловать в игру.
Теперь вашь телефон настроен и вы стали детективом
Вам нужно найти 4 инструмента и 17 улик что бы ракрыть это дело.
Кажду улику можно изучить одним или несколькими инструментами.

На данный момент Вам доступны следующие инструменты

'''

html_cookie = "Set-cookie: name={}; expires=Sat, 31 Dec 2016 20:59:59 GMT"
print(html_cookie.format(Name_group))


wall.head_html()

print(content)
#print(Name_group)

wall.footer_html()
