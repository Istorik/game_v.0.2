#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import html
import http.cookies
import cgi
import sqlite3
import pyqrcode # sudo pip3 install pyqrcode
import png      # sudo pip3 install pypng


from _sell import *

form = cgi.FieldStorage()
Id_group = form.getfirst("Id_group")

def main(Id_group):
	connect = sqlite3.connect('qvest2.db')
	cursor = connect.cursor()
	cursor = cursor.execute('select * from comandTable where id = ?', (Id_group,))
	user = cursor.fetchone()
	if user: 
		content = '''\
			Добро пожаловать в игру.
			Теперь вашь телефон настроен и вы стали детективом
			Вам нужно найти 4 инструмента и 17 улик что бы ракрыть это дело.
			Кажду улику можно изучить одним или несколькими инструментами.
			На данный момент Вам доступны следующие инструменты
		'''
		html_cookie = "Set-cookie: name={}; expires=Sat, 01 Apr 2018 20:59:59 GMT"
		print(html_cookie.format(user[0]))
		Html.head_html(group=user[0])
	else:
		content = 'Пользователь не найден'
	cursor.close()
	connect.close()
	return content

if Id_group:
    print(main(Id_group))
    code = pyqrcode.create('http://qvest.asspo.ru/cgi-bin/cookie.py?Id_group={}'.format(Id_group))
    image_as_str = code.png_as_base64_str(scale=6)
    print('<div class="layer1"><img width="200" height="200"  src="data:image/png;base64,{}">'.format(image_as_str))
    Html.footer_html()

else:
    Html.head_html(group='__')
    Html.error()
    Html.footer_html()

