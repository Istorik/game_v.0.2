#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os
import sqlite3

from _sell import *

db_ulika = Database(filename = 'qvest2.db', table = 'ulikaTable1')
db_user = Database(filename = 'qvest2.db', table = 'comandTable')

ulika = dict()

form = cgi.FieldStorage()
idUlika = form.getfirst("idUlika", "1")

if idUlika is not None:
    idUlika = html.escape(idUlika)

# Проверяем улику в базе 
ulika = db_ulika.retrieve(idUlika)

# Опрашиваем куки
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")

if name is not None: name = name.value
name = '1'
if name is None or db_user.retrieve(name) is None:
	Html.head_html(ulika['id'])
	print(name)
	print('''
		<h1>Комананда не найдена</h1>
		<p><a href=http://qvest.sch438.loc>Зарегестрируйтесь</a></p>
		<p>Удобнее всего это сделать в кабинете информатики, за одно пройдете вводный курс</p>
		<p>Место преступления тоже находится на 4 этаже</p>
		'''
		)
else:
	Html.head_html(ulika['id'])
	print(len(ulika))
	Html.content(dict(ulika))



Html.footer_html()





