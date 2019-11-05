#!/usr/bin/env python3
# -*- coding: utf-8

import html
import http.cookies
import random
import sqlite3
import os
from datetime import datetime
import time
import cgi, sys, json

from _sell import *

# Работа с базой
# -------------------------------
db_ulika = Database(filename = 'qvest2.db', table = 'ulikaTable')
db_user = Database(filename = 'qvest2.db', table = 'comandTable')
db_lut = Database(filename = 'qvest2.db', table = 'UlikaLutTable')

# Работа с формой
# -------------------------------
form = cgi.FieldStorage()

#if sys.argv[1]:
#  id_ulika = sys.argv[1]
#else:
#  id_ulika = "1"

idUlika = form.getfirst("idUlika") # После тестирования исправить
cashUlika = form.getfirst("cashUlika", "1") # После тестирования исправить
button = form.getfirst("button")

# Присваение для тестирования
# -------------------------------
#ulika = db_ulika.retrieve('1') # переехало на строку 53
#user = db_user.retrieve('1')


# Проверить наличие этой улики
# -------------------------------
if idUlika:
    idUlika = html.escape(idUlika)
else:
    Html.head_html(ulika['idUlika'])
    print('''
            <h1>Комананда не найдена</h1>
            <p><a href=http://qvest.sch438.loc>Зарегестрируйтесь</a></p>
            <p>Удобнее всего это сделать в кабинете информатики, за одно пройдете вводный курс</p>
            <p>Место преступления тоже находится на 4 этаже</p>
            '''
    )

#print("--[1] idulika:", idUlika)
    
ulika = db_ulika.retrieve(idUlika) # грузим улику
#print("--[2] ulika:", ulika)

if ulika is None:
    # Пишем в лог "Попытка взлома" время куки
    # Еще добавить проверку контрольной суммы
    print('Тревога')
    

# Опрашиваем куки
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
if name is not None: 
    name = name.value
else: 
    name = 1 # Удалить else
    wall.head_html(ulika['idUlika'])
    print('''
            <h1>Комананда не найдена</h1>
            <p><a href=http://qvest.sch438.loc>Зарегестрируйтесь</a></p>
            <p>Удобнее всего это сделать в кабинете информатики, за одно пройдете вводный курс</p>
            <p>Место преступления тоже находится на 4 этаже</p>
            '''
    )

# Присваиваем пользователя из куки
user = db_user.retrieve(name)

# Проверяем наличие улики у группы, если нет, добавляем
if not db_lut.ulika_find(ulika['id'], user['id']):
#if ulikaLut is None:
    dt = datetime.now()
    date = str(dt.strftime("%d.%m.%Y %H:%M:%S"))
    con = sqlite3.connect('qvest2.db')
    cur = con.cursor()
    base = (date, ulika['id'], user['id'])
    sql = "INSERT INTO UlikaLutTable (time, idComand, idUlika) VALUES (?, ?, ?)"
    try:
        cur.execute(sql, base)

    except sqlite3.DatabaseError as err:
        print('Ошибка базы: ', err)

    else:
        con.commit()
        cur.close
        con.close
 
search_ulika = dict()       
search_ulika = db_lut.ulika_find(ulika['id'], user['id'])

#button = "Lupa"

if button:
    dt = datetime.now()
    date = str(dt.strftime("%d.%m.%Y %H:%M:%S"))
    con = sqlite3.connect('qvest2.db')
    cur = con.cursor()
    base = (date, search_ulika.get('id'))
    sql = "update UlikaLutTable set {}  = ? where id = ?".format(button)
    try:
        cur.execute(sql, base)

    except sqlite3.DatabaseError as err:
        print('Ошибка базы: ', err)

    else:
        con.commit()
        cur.close
        con.close

for row in 'Lupa', 'Photo', 'Him', 'Dictofon':
    if ulika[row] == None or user[row] is None:
        ulika[row] = ""
    else:
        if ulika[row] is not None and search_ulika[row] is None:
            ulika[row] = '<p>Кнопка</p>'
#    print('-'*10)
#    print(search_ulika[row])

Html.head_html("Улика №1", user['NameComand'])
Html.content(ulika)
Html.footer_html()


