#!/usr/bin/env python3
# -*- coding: utf-8

import html
import http.cookies
import random
import sqlite3
import os
from datetime import datetime
import time
import cgi

from _sell import *

def qr(id_qr, user):
	'''Проверка сканировал он уже этот QR '''
	if id_qr > 28: return "Error"
	for row in user:
		if row[4] == id_qr:
			return row
	return False

def group(id_lut, user):
	''' Проверка есть ли у него этот лут'''
	for row in user:
		if int(row[3]) == id_lut:
			return row
	return False

def form_get(_f):
	'''возращаем данные из формы'''
	form = cgi.FieldStorage()
	_f = form.getfirst(_f)
	if _f: return html.escape(_f)
	return False

def cookie_get(_f):
	cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	name = cookie.get(_f)
	if name: 
		name = name.value
		return name
	else: 
		Html.head_html()
		Html.error()
		return False

id_group = int(cookie_get('name'))
id_qr = int(form_get('idQr'))
#id_group = 7
#id_qr = 2

connect = sqlite3.connect('qvest2.db')
cursor = connect.cursor()
cursor = cursor.execute('select * from inventaTable where idComand = ?', (id_group,))
user = cursor.fetchall()


if id_qr and id_group:
	id_lut = random.randint(1, 28)
	Html.head_html(id_group)
	if not qr(id_qr, user):
		while group(id_lut, user):
			id_lut = id_lut + 1
			if id_lut > 28: id_lut = 1
		'''Цикл закончился и выдал нам id улики'''
		dt = datetime.now()
		date = str(dt.strftime("%d.%m.%Y %H:%M:%S"))
		base = (date, id_group, id_qr, id_lut)
		inventaTable = "INSERT INTO inventaTable (time, idComand, idQR, idLut) VALUES (?, ?, ?, ?)"
		
		try:
			cursor.execute(inventaTable, base)
		except sqlite3.DatabaseError as err:
			print('Ошибка базы: ', err)
		else:
			connect.commit()
		'''Все что идет дальше хорошобы перенести в функцию '''
		cursor.execute('select * from lutTable where id = ?', (id_lut,))
		name_lut = cursor.fetchone()
		cursor.close
		if name_lut:
			print("<p>Вы нашли {} </p>".format(name_lut[1]))
		else: print('<p>Ничего интересного Вы не нашли</p>')
	else:
		print('<p>Ничего интересного Вы не нашли</p>')
else:
	Html.head_html()
	Html.error()


Html.footer_html()
cursor.close()
connect.close()

