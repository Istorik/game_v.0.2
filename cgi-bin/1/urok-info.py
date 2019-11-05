#!/usr/bin/env python3
# -*- coding: utf-8

import html
import sqlite3
import os
from datetime import datetime
import time
import cgi

from _sell import *

now = datetime.now()

time_chek = (1 - ((50 - now.minute)/20)) * 100
if time_chek > 100 or time_chek < 0: time_chek = 49
#time_chek = (1 - ((50 - 32)/20)) * 100

connect = sqlite3.connect('urok.db')
cursor = connect.cursor()
cursor = cursor.execute('select * from comp')
user = cursor.fetchall()

print('Content-type: text/html\n')

print('''\
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">
<head>
	<title>Открытый Урок</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="Refresh" content="10" />
	<link rel="stylesheet" href="../style.css">
</head>
<body>
''')

print('''\
<div class="progress-bar orange shine">
	<span style="width: {0}%"><center>{0}%</center></span>
</div>
'''.format(int(time_chek)))

print('''<table border=1>
<tr><td>Комп</td><td>Фамилия Имя</td>
<td>Титул</td>
<td>Тип Текста</td>
<td>Поля</td>
<td>Заголовок 1 уровня</td>
<td>Заголовок 2 уровня</td>
<td>Текст</td>
<td>Тип загол. 1 уровня</td>
<td>Тип загол. 2 уровня</td>
<td>Колонтитул</td>
<td>Оглавление</td>
</tr>''')

for row in user:
    print('<tr>')
    print('<td>', row[0], '</td><td>', row[1], '</td>')
    for i in range(2,12):
        if row[i]:
            print('<td bgcolor=#00ff00>Готово</td>')
        else: print('<td align=center bgcolor=#000000><font color=#fff>False</font></td>')
    print('</tr>')
print('</table>')


Html.footer_html()
cursor.close()
connect.close()

