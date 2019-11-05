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

# Функции
# -------------------------------

def cooky():
    # Опрашиваем куки
    # --------------------------------
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    name = cookie.get("name")
    if name is not None:
        name = int(name.value)
        return name
    else:
        Html.head_html()
        Html.error()


def lut_random(*row):
    j_str = list(range(1, 29))
    i_str = []
    for i in row[0]:
        i_str.append(i[3])
    for i in i_str: 
        j_str.remove(i)
    return random.choice(j_str)

def sql_app(name, number_lut, idlut):
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


# Работа с базой
# -------------------------------
con = sqlite3.connect('qvest2.db')
cursor = con.cursor()

# Работа с формой
# -------------------------------
form = cgi.FieldStorage()
idlut = form.getfirst("idLut")              # После тестирования исправить
cashUlika = form.getfirst("cashLut", "1")   # После тестирования исправить


# Проверяю форму
# -------------------------------
if not idlut: 
	Html.head_html()
	Html.error()



# Присваиваем пользователя из куки
name = cooky()

# Проверить наличие этого qr у юзера
# -------------------------------
cursor.execute('select * from inventaTable where idQr= ? and idComand = ?', (idlut, name))
if cursor.fetchone() is not None:
    content = '<p>Ничего интересного, всякий мусор </p>'
else:
    # Проверить наличие этого лута у юзера
    # -------------------------------
    cursor.execute('select * from inventaTable where idComand = ?', (name, ))
    number_lut = lut_random(cursor.fetchall())
    
    sql_app(name, number_lut, idlut)
    cursor.execute('select * from lutTable where id = ?', (number_lut, ))
    idlut = cursor.fetchone()
    
    cursor.close
    con.close
    if number_lut > 16:
        content = '<p>Ничего интересного, всякий мусор </p>'
    else:
        content = '<p>Вы что то нашли {} </p>'.format(idlut[1])


Html.head_html("Находка", name)
print("<br><br><br><br><br>") 
print('<div class="ulika_all">')
print(content)
print('</div>')
Html.footer_html()
