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

connect = sqlite3.connect('qvest2.db')
cursor = connect.cursor()
cursor = cursor.execute('select * from comandTable')
user = cursor.fetchall()

#cursor = cursor.execute('select * from UlikaLutTable')
cursor = cursor.execute('select ulikaTable.ulikaName, comandTable.NameComand, UlikaLutTable.Lupa, UlikaLutTable.Photo, UlikaLutTable.Him, UlikaLutTable.Dictofon FROM UlikaLutTable, ulikaTable, comandTable WHERE UlikaLutTable.idUlika=ulikaTable.id and comandTable.id=UlikaLutTable.idComand')
ulika = cursor.fetchall()
cursor = cursor.execute('select inventaTable.time, comandTable.NameComand, lutTable.TextLut from inventaTable, comandTable, lutTable WHERE comandTable.id=inventaTable.idComand and lutTable.id=inventaTable.idLut')
inventar = cursor.fetchall()


Html.head_html(meta='<meta http-equiv="Refresh" content="30" />')

print('<h1>Юзеры</h1>')

print('<table border=1>')
print('<tr><td>ID</td><td>Время</td><td>Название</td></tr>')
for row in user:
    print('<tr>')
    print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[3], '</td>' )
    print('</tr>')
print('</table>')


print('<h1>Улики</h1>')

print('<table border=1>')
print('<tr><td>Команда</td><td>Улика</td><td>Лупа</td><td>Сканер</td><td>Крим. Набора</td><td>Диктфон</td></tr>')
for row in ulika:
    print('<tr>')
    print('<td>', row[1], '</td><td>', row[0], '</td><td>', row[2], '</td><td>', row[3], '</td><td>',row[4], '</td><td>', row[5], '</td>')
    print('</tr>')
print('</table>')

print('<h1>Инвентарь</h1>')

print('<table border=1>')
print('<tr><td>Время</td><td>Команда</td><td>Улика</td></tr>')
for row in inventar:
    print('<tr>')
    print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2], '</td>')
    print('</tr>')
print('</table>')
print('''
<a href='http://qvest.asspo.ru/cgi-bin/cookie.py?Id_group=1'>Куки</a>
<br><a href='http://qvest.asspo.ru/cgi-bin/ulika.py?idUlika=1'>Улика</a>
<br><a href='http://qvest.asspo.ru/cgi-bin/lut.py?idLut=1'>Лут</a>
<br>
<br><a href='http://qvest.asspo.ru/cgi-bin/laboratory.py'>Лаборатория</a>



''')

Html.footer_html()
cursor.close()
connect.close()

