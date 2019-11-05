#!/usr/bin/env python3
# -*- coding: utf-8

import html
import http.cookies
import os
import cgi
import random
import sqlite3
import time
from datetime import datetime

from _sell import *

number_lut = random.randint(1, 28)

# Функции 
# -------------------------------


# Работа с базой
# -------------------------------
db_user = Database(filename = 'qvest2.db', table = 'comandTable')

# Работа с формой
# -------------------------------
form = cgi.FieldStorage()
idlut = form.getfirst("idLut", "1") # После тестирования исправить
cashUlika = form.getfirst("cashLut", "1") # После тестирования исправить

# Присваение для тестирования
# -------------------------------

# Опрашиваем куки
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
if name is not None: 
    name = name.value
else: name = 1 # Выдать ошибку, что вы не найдены как зарегестрированный пользователь

# Присваиваем пользователя из куки
user = db_user.retrieve(name)

con = sqlite3.connect('qvest2.db')
cursor = con.cursor()

# Проверить наличие этого qr у юзера
# -------------------------------
cursor.execute('select * from inventaTable where idQr= ? and idComand = ?', (idlut, name))
if cursor.fetchone() is not None or number_lut > 14:
	content = '<p>Ничего интересного, всякий мусор </p>'
else:
	# Проверить наличие этого лута у юзера
	# -------------------------------
	cursor.execute('select * from inventaTable where idComand = ? and idLut = ?', (name, number_lut))

	while cursor.fetchone() is not None:
		number_lut =+1
		if number_lut > 28: number_lut = 1
		cursor.execute('select * from inventaTable where idComand = ? and idLut = ?', (name, number_lut))

	dt = datetime.now()
	date = str(dt.strftime("%d.%m.%Y %H:%M:%S"))

	base = (date, name, number_lut, idlut)
	sql = "INSERT INTO inventaTable (time, idComand, idLut, idQr) VALUES (?, ?, ?, ?)"

	try:
		cursor.execute(sql, base)

	except sqlite3.DatabaseError as err:
		print('Ошибка базы: ', err)

	else:
		con.commit()

	cursor.execute('select * from lutTable where id = ?', (number_lut))
	idlut = cursor.fetchone()

	cursor.close
	con.close
	content = '<p>Вы что то нашли {} </p>'.format(idlut[1])


Html.head_html("Находка", user['NameComand'])
print("<br><br><br><br><br>")
print('<div class="ulika_all">')
print(content)
print('</div>')
Html.footer_html()


