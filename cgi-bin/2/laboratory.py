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

reagent = {1: ('9', '10'), 3: ('13', '14'), 5: ('7', '8'), 6: ('5', '6'), 10: ('11', '12'),10: ('15', '16')}

def cooky():
	# Опрашиваем куки
	#--------------------------------
	cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	name = cookie.get("name")
	if name is not None:
		name = int(name.value)
		return name
	else:  
		Html.head_html()
		Html.error()

def laboratory():
	connect = sqlite3.connect('qvest2.db')
	cursor = connect.cursor()

	cursor = cursor.execute('select ulikaTable.id, ulikaTable.ulikaImg FROM UlikaLutTable, ulikaTable WHERE UlikaLutTable.idUlika=ulikaTable.id and UlikaLutTable.idComand = ? and UlikaLutTable.Him = ?', (name, '1'))
	ulika = cursor.fetchall()

	cursor = cursor.execute('select inventaTable.id, lutTable.TextLut from inventaTable, lutTable WHERE inventaTable.idLut=lutTable.id and inventaTable.idComand = ? and inventaTable.idLut > 4', (name,))
	inventar = cursor.fetchall()

	print("""<p>
		Вы находитесь в крименалистической химической лаборатории и собираетесь исследовать одну из найденных улик. 
		Помните, что каждая попытка это потраченный реактив. 
		Приступайте к делу точно понимая, что вы делаете, в противном случае обратитесь к учителю Химии за подсказкой.</p>""")

	print('<p>Выберите улику, которую будете изучать</p><center>')

	for row in ulika:
		content = '''
			<label>
				<input type="radio" name="ulika" value="{0}" />
				<img width=200 height=276 src="{1}">
			</label>'''
		
		print(content.format(*row))

	print('</center><p>Выберите реактив 1</p>')
	print('<select>')
	for row in inventar:
		print('<option>')
		print(row[1])
		print('</option>')
	print('</select>')

	print('<p>Выберите химическую реакцию.</p>')
	print('''
		<select>
			<option>Нагрев</option>
			<option>Раствор</option>
			<option>Качественно перемешать</option>
			<option>4 тип реакции</option>
			<option>Давление</option>
		</select>
	''')

	print('<p>Выберите реактив 2</p>')
	print('<select>')
	for row in inventar:
		print('<option>')
		print(row[1])
		print('</option>')
	print('</select>')


	cursor.close()
	connect.close()

def otvet_True(id_):
	connect = sqlite3.connect('qvest2.db')
	cursor = cursor.execute('select Him FROM ulikaTable WHERE idUlika=?', (id_,))
	ulika = cursor.fetchall()
	print(ulika)
	print('<p>Данны доавлены ы дело</p>')
	dt = datetime.now()
	date = str(dt.strftime("%d.%m.%Y %H:%M:%S"))
	cursor = connect.cursor()
	base = (date, id_)
	sql = "update UlikaLutTable set Him  = ? where id = ?"
	try:
		cur.execute(sql, base)
	except sqlite3.DatabaseError as err:
		print('Ошибка базы: ', err)
	else:
		con.commit()
		cur.close
		con.close

def otvet_False(id_loot):
	print('''<p>Вы видите как все заискрилось, засверкало, и взарволось красивым разноцветным облаком.</p>
	<p>К сожалению это не правильная реакция и реагенты были утеряны.</p>
	<p>Попробуйте снова найти их там же где сделали это в первый раз.</p>
	''')
	print("Удалить из базы реагенты")


name = cooky() # Присваиваем пользователя из куки

Html.head_html('Лаборатория', name)
laboratory()
Html.footer_html()
