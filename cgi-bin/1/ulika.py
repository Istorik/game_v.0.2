#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os
import sqlite3

from _wall import *
wall = Html()

db = Database(filename = 'qvest2.db', table = 'ulikaTable1')

ulika = dict()

form = cgi.FieldStorage()
idUlika = form.getfirst("idUlika", "1")

if idUlika is not None:
    idUlika = html.escape(idUlika)

# Проверяем улику в базе 
ulika = db.retrieve(idUlika)
# ulika = db.instrument(idUlika)


# Опрашиваем куки
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")

pattern = '''
	<h2>Улика №{idUlika} / 17</h2>
	<div class='ulika_all'>
		<div class='ulika_img'>
		  <img src='../pics/ulika1.jpg' alt='avatar'>
		</div>
		<div class='ulika_info'>
			<p><b>Местонахождение улики:</b> {ulikaMesto}</p>
			<p><b>Улика изучена на: </b></p>
			<div class="progress-bar orange shine">
				<span style="width: 39%"><center>39%</center></span>
			</div>
		</div>
	</div>	
	<div class='ulika_txt'>
		<h1>{ulikaName}</h1>
		<p>{ulikaText}</p>
		<p>{ulikaLupa}</p>
		<p>{ulikaPhoto}</p>
		<p>{ulikaHim}</p>
		<p>{ulikaDictofon}</p>
	</div>
'''

if name is not None:
	name = name.value
	wall.head_html(ulika['idUlika'])
	print(pattern.format(**ulika))
	
else:
	wall.head_html(ulika['idUlika'])
	print(name)
	print('''
		<h1>Комананда не найдена</h1>
		<p><a href=http://qvest.sch438.loc>Зарегестрируйтесь</a></p>
		<p>Удобнее всего это сделать в кабинете информатики, за одно пройдете вводный курс</p>
		<p>Место преступления тоже находится на 4 этаже</p>
		'''
		)	

wall.footer_html()





