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

# Куки
#------------------------------

# Если есть вернуть True
# Куки нет есть форма куки
    # Добаввить куки на сессию user = id_coocky
# если нет Выдать регистрационную форму куки = id названия команды



def cursor(connect, table):
    cur = connect.cursor()
    cur = cur.execute('select * from {}'.format(table))
    return cur.fetchall()



#for row in cursor(connect, 'comandTable'):
#    print('<p>')
#    print(row[0])
#    print(row[1], '|')
#    print(row[3])
#    print('</p>')

Html.head_html('Команда Молодости')

    

#def menu(ulika):
#    print('<ul>')
#    for row is ulika:
#        print('<li><a href=test.py?idUlik>')
#        row['id']
#
#    print('</ul>')

start1 = '''
<body>
    <div class="top_info">
        <div class=button_info>
          <ul>
            <li><a href="1.html">Подозреваемые</a> </li>
            <li><a href="1.html">Улики</a> </li>
            <li><a href="1.html">Инструменты</a></li>
          </ul>
        </div>
    </div>
    <article><h1>Дело о</h1></article>
    <aside>'''


start2 = '</aside></body>'

print(start1)

connect = sqlite3.connect('qvest2.db')
print('<ul class="menu">')
for row in cursor(connect, 'UlikaLutTable where idComand = 8'):
    for row in cursor(connect, 'ulikaTable where id = {}'.format(row[3])):
        print('<li><a href=/cgi-bin/ulika.py?idUlika={0}>{1}</a></li>'.format(row[0], row[1]))
print('</ul>')
connect.close()

print(start2)
Html.footer_html()

