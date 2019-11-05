#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os
import sqlite3

ulika = dict()

form = cgi.FieldStorage()
idUlika = form.getfirst("idUlika", "0")
idUlika = html.escape(idUlika)


con = sqlite3.connect('/var/www/qvest/qvest2.db')
cur = con.cursor() # Создание объекта курсора для взаимодействия с БД.

def user_base(idUlika):
    user_cur = con.cursor() # Создание объекта курсора для взаимодействия с БД.
    id = (idUlika, )
    return user_cur.execute('SELECT * FROM ulikaTable1 WHERE idUlika = ?', id)
    user_cur.close


data = user_base(idUlika)
for lis in data:
	print(lis)

for i in range(8):
	print(i)
	if data[i] == None:
		ulika[i] = ' '
	else: 
		ulika[i] = data[i]

# Добавить проверку наме групп если нет взять из куки, а если и там нет то отправить на регестрацию.
# незабыть после регестрации переслать название улики в форме.

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="../style.css">
<title>Улика</title>
</head>
<body>
	<h2>Улика №{id} / 17</h2>
	<p class="bold">Название улики: {name}</p>
	<p class="bold">Местонахождение улики: {mesto}</p>
	<p>{Text}</p>
	<p>{Lupa}</p>
	<p>{Photo}</p>
	<p>{Him}</p>
	<p>{Dictofon}</p>
</body>
</html>
'''



print('Content-type: text/html\n')

print(pattern.format(id=ulika[0], name=ulika[1], mesto=ulika[2], Text=ulika[3], Lupa=ulika[4], Photo=ulika[5], Him=ulika[6], Dictofon=ulika[7]))


cur.close()
con.close()
