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

now = datetime.now()

# Работа с базой
# -------------------------------
con = sqlite3.connect('urok.db')
cur = con.cursor()

# Работа с формой
# -------------------------------
form = cgi.FieldStorage()

comp = form.getfirst("comp")
button = form.getfirst("button")

# Функции
# -------------------------------

def check_comp(number):
    but = '''
    <div class='start_form1'>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="submit" class="body_start" value="Комп № {0}">
        </form>
        </div>
        '''
    return but.format(number)

def update(number, zadanie):
    base = (now.minute, number)
    sql = "update comp set {} = ? where id = ?".format(zadanie)
    try:
        cur.execute(sql, base)
    except sqlite3.DatabaseError as err:
        return('Ошибка базы: ', err)
    else: 
        con.commit()
        return 'Номер компьютера {}. Данные об {} обновлены'.format(number, zadanie)

button_fun = '''\
    <div class='start_form1'>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Titul">
            <input type="submit" class="body_start" value="Титул">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Text_tip">
            <input type="submit" class="body_start" value="Тип Текста">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Poly">
            <input type="submit" class="body_start" value="Поля">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Zagolovok_1">
            <input type="submit" class="body_start" value="Заголовок 1 уровня">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Zagolovok_2">
            <input type="submit" class="body_start" value="Заголовок 2 уровня">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Text">
            <input type="submit" class="body_start" value="Текст">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Zagolovok_1_tip">
            <input type="submit" class="body_start" value="Тип загол. 1 уровня">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Zagolovok_2_tip">
            <input type="submit" class="body_start" value="Тип загол. 2 уровня">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Klontitul">
            <input type="submit" class="body_start" value="Колонтитул">
        </form>
        <form>
            <input type="hidden" name="comp" value="{0}">
            <input type="hidden" name="button" value="Oglavlenie">
            <input type="submit" class="body_start" value="Оглавление">
        </form>
        </div>

'''

print('Content-type: text/html\n')

print('''\
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">
<head>
	<title>Открытый Урок</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="../style.css">
</head>
<body><div>
''')

if comp and not button:
	print('Задание')
	print(button_fun.format(comp))

elif comp and button:
	print(update(comp, button))
	print('<p>Добавил, <a href=/cgi-bin/urok-chek.py>нажми сюда для возврата</a></p>')

else:
	for i in range(1,14):
		print(check_comp(i))


Html.footer_html()
cur.close()
con.close()
