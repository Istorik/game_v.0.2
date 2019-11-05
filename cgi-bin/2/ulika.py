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
db_inventar = Database(filename = 'qvest2.db', table = 'inventaTable')
db_lutTable = Database(filename = 'qvest2.db', table = 'lutTable')

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


# Проверить наличие этой улики
# -------------------------------
if idUlika:
    idUlika = html.escape(idUlika)
else:
    Html.head_html()
    Html.error()
#idUlika = '1'
ulika = db_ulika.retrieve(idUlika) # грузим улику


# Опрашиваем куки
#--------------------------------
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
if name is not None: 
    name = int(name.value)
else: 
    Html.head_html()
    Html.error()
#name = '7'

# Присваиваем пользователя из куки
user = db_user.retrieve(name)

search_ulika = dict()
search_ulika = db_lut.ulika_find(ulika['id'], user['id'])

# Проверяем наличие улики у группы, если нет, добавляем
if not search_ulika:
#if ulikaLut is None:
    dt = datetime.now()
    date = str(dt.strftime("%d.%m.%Y %H:%M:%S"))
    con = sqlite3.connect('qvest2.db')
    cur = con.cursor()
    base = (date, user['id'], ulika['id'])
    sql = "INSERT INTO UlikaLutTable (time, idComand, idUlika) VALUES (?, ?, ?)"
    try:
        cur.execute(sql, base)
        
    except sqlite3.DatabaseError as err:
        print('Ошибка базы: ', err)
    else:
        con.commit()
        cur.close
        con.close

search_ulika = dict(db_lut.ulika_find(ulika['id'], user['id']))
#button = "Lupa"

if button:
    dt = datetime.now()
    date = str(dt.strftime("%d.%m.%Y %H:%M:%S"))
    con = sqlite3.connect('qvest2.db')
    cur = con.cursor()
    if button == 'Him': # Проверяем на сбор материалов для хим стола
        date = '1'
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


# Проверяем лут
connect = sqlite3.connect('qvest2.db')
cursor = connect.cursor()
cursor = cursor.execute('select * from inventaTable where idComand = ?', (name,))
_user = cursor.fetchall()
cursor.close

def inventar(_user, instrument):
    for row in _user:
        if int(row[3]) == instrument:
            return True
    return False

def check_button(ins, ul):
    but = '''
    <div class='start_form'>
        <form method="post">
            <input type="hidden" name="button" value="{0}">
            <input type="hidden" name="idUlika" value="{1}">
            <input type="submit" class="body_start" value="Изучить">
        </form>
        </div>
        '''
    return but.format(ins, ul)

insts = {1: 'Lupa', 2: 'Photo', 3: 'Him', 4: 'Dictofon'}
summ_status = 20 # 5-summ_status Количество объектов у улики
search_ulika = dict(db_lut.ulika_find(ulika['id'], user['id']))

for inst in (1 ,2, 3, 4):
    if ulika[insts[inst]] is not None:
        if inventar(_user, inst):
            if search_ulika[insts[inst]] is None:
                ulika[insts[inst]] = check_button(insts[inst], ulika['id'])
            else: 
                if inst == 3 and search_ulika['Him'] == '1': #Проверяем данную улику изучили на лаб столе
                    ulika['Him'] = '<b>Для изучения, нужна лаборатория и реагенты</b>'
                    summ_status += 10
                else: summ_status += 20
        else: 
            ulika[insts[inst]] = ''
    else: 
        summ_status += 20
        ulika[insts[inst]] = ''


ulika['status'] = summ_status

Html.head_html("Улика", name)
Html.content(ulika)
Html.footer_html()
