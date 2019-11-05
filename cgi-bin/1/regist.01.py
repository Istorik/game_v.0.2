#!/usr/bin/env python3
# -*- coding: utf-8

# импорт библиотеки 
import cgi
import html
import time
import datetime
import sqlite3

def find(group):
	"""Ищет пользователя по имени или по имени"""
	group = (group, )
	Name = cur.execute('SELECT * FROM comandTable WHERE NameComand = ?', group)
	if Name:
		return False
	return True
def ok():
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
			<html>
			<head>
				<meta charset="utf-8">
				<title>Детективное агенство {}</title>
			</head>
			<body>""".format(Name_group))

	print("<h1>Позравляем! Детективное агенство создано!</h1>")
	print("<p>Название Детективного агенства: {}</p>".format(Name_group))
	print("<p>Старший детектив  {}</p>".format(Name_kapitan))
	print("<p>Детектив: {}</p>".format(Name_user_1))
	print("<p>Младший детектив: {}</p>".format(Name_user_2))


	print("""</body>
			</html>""")

form = cgi.FieldStorage()

Name_group = form.getfirst("Name_group", "null")
Name_kapitan = form.getfirst("Name_kapitan", "null")
Name_user_1 = form.getfirst("Name_user_1", "null")
Name_user_2 = form.getfirst("Name_user_2", "null") 

Class_kapitan = form.getfirst("Class_kapitan", "null")
Class_user_1 = form.getfirst("Class_user_1", "null")
Class_user_2 = form.getfirst("Class_user_2", "null")

# Для безопасноти, преобразуем системные символы в код HTML
Name_group = html.escape(Name_group)
Name_kapitan = html.escape(Name_kapitan)
Name_user_1 = html.escape(Name_user_1)
Name_user_2 = html.escape(Name_user_2)

Class_kapitan = html.escape(Class_kapitan)
Class_user_1 = html.escape(Class_user_1)
Class_user_2 = html.escape(Class_user_2)

date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

con = sqlite3.connect('/var/www/qvest/qvest2.db')
cur = con.cursor()

base = (date, Name_group, Name_kapitan, Class_kapitan, Name_user_1, Class_user_1, Name_user_2, Class_user_2)

sql = """\
INSERT INTO comandTable (
	timeStart,
	NameComand,
	NameSDetective,
	ClassSDetective,
	NameDetective,
	ClassDetective,
	NameMDetective,
	ClassMDetective,
) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

if str(Name_group) != "null":
	
	# Записать в базу
	cur.execute(, (data, ulikaName))
	con.commit()
	cur.close()
	ok()
	
else:
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
			<html>
			<head>
				<meta charset="utf-8">
				<title>Ошибка</title>
			</head>
			<body>""")
	print("<h1>Детективное агенство НЕ создано!</h1>")
	print("<p>Попробуйте еще раз</p>")
	print("<p>Название Детективного агенства: {}</p>".format(Name_group))
	print("""</body>
	</html>""")


