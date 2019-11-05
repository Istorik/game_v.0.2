#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os
import sqlite3

from _wall import Html
wall = Html()

ulika = dict()
ulika_progress="30%"

form = cgi.FieldStorage()
idUlika = form.getfirst("idUlika", "1")
Name_group = form.getfirst("Name_group")

if idUlika is not None:
    idUlika = html.escape(idUlika)

id_= (idUlika,)

con = sqlite3.connect('qvest2.db')
cur = con.cursor() # Создание объекта курсора для взаимодействия с БД.

# Проверяем улику в базе 
cur.execute('SELECT * FROM ulikaTable1 WHERE idUlika = ?', id_)
ulika = cur.fetchone()
cur.close()
con.close()

# Опрашиваем куки
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")

if name is not None:
	name = name.value

# Проверка куки на наличие команды в базе
if Base_users().find(name) is None:
	print('Set-cookie: name={}; expires=Friday, 31-Dec-99 23:59:59 GMT')
	print('Content-type: text/html\n')
	print("Команда не найдена")
	

if name is None and Name_group is None:
	wall.head_html(ulika[1])
	content = '''\
    <div class='start_form'>
        <h1>Комананда не найдена</h1>
        <form action="/cgi-bin/ulika.py" autocomplete="off">
        <p>Название детективного агенства</p>
        <input type="text" name="Name_group" required placeholder="Название агенства">
        <input type="radio" name="idUlika" value="{}" checked><br>
        <input type="submit" class="body_start" value="Представиться">
    </div>
'''

	print(content.format(idUlika))

else:
	html_cookie = "Set-cookie: name={}; expires=Sat, 31 Dec 2016 23:59:59 GMT"
	print(html_cookie.format(Name_group))
	wall.head_html(ulika[1])

pattern = '''
	<h2>Улика №{id} / 17</h2>
	<div class='ulika_all'>
		<div class='ulika_img'>
		  <img src='../pics/ulika1.jpg' alt='avatar'>
		</div>
		<div class='ulika_info'>
			<p><b>Местонахождение улики:</b> {mesto}</p>
			<p><b>Улика изучена на: </b></p>
			<div class="progress-bar orange shine">
				<span style="width: {progress}"><center>{progress}</center></span>
			</div>
		</div>
	</div>	
	<div class='ulika_txt'>
		<h1>{name}</h1>
		<p>{Text}</p>
		<p>{Lupa}</p>
		<p>{Photo}</p>
		<p>{Him}</p>
		<p>{Dictofon}</p>
	</div>
'''
  
print(pattern.format(id=ulika[0], name=ulika[1], mesto=ulika[2], Text=ulika[3], Lupa=ulika[4], Photo=ulika[5], Him=ulika[6], Dictofon=ulika[7], progress=ulika_progress))
wall.footer_html()


