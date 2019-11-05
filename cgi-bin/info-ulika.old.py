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

text_ulika = ['Первый преступник пил воду на месте преступления',
        'Второй преступник держит зебру',
        'Саурон пришел с красными перчатками',
        'Бармалей оставил свою собаку у входа на территорию школы.',
        'Хозяин зеленого плаща пьет кофе.',
        'Анонимус пьёт только чай.',
        'Кто-то в зеленом плаще зашел сразу после персонажа в белых ботинках.',
        'Любитель барбарисок разводит улиток.',
        'Тот кто пришел с желтым зонтиком был с чупа-чупсом.',
        'Тот кто пришел третим пьёт молоко.',
        'Гринч пришел первым, а сразу за ним кто в синих штанах.',
        'Тот кто пришел вместе с хозяином лошади, любитель чуп-чупсов.',
        'Любитель желатиновых мишек пьет апельсиновый сок.',
        'Снеговик ест конфеты «Коровка».']


db_user = Database(filename = 'qvest2.db', table = 'comandTable')
db_ulika = Database(filename = 'qvest2.db', table = 'ulikaTable')
db_lut = Database(filename = 'qvest2.db', table = 'UlikaLutTable')

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

ulika_find_all = db_lut.ulika_find_all(name)

connect = sqlite3.connect('qvest2.db')
cursor = connect.cursor()
cursor = cursor.execute('select * from comandTable WHERE id=?', (name,))
user = cursor.fetchall()

def sum_ulika(j):
    x= -5
    for key in db_ulika.retrieve(j):
        if db_ulika.retrieve(j)[key] is not None: x+=1
    return x

def sum_lut(j):
    x= -4
    for row in ulika_find_all:
        row = dict(row)
        if row['idUlika'] == j:
            for key in row:
                if row[key] is not None: x+=1
            return x 

#cursor = cursor.execute('select * from UlikaLutTable')
cursor = cursor.execute('select ulikaTable.ulikaName, ulikaTable.id FROM UlikaLutTable, ulikaTable, comandTable WHERE UlikaLutTable.idUlika=ulikaTable.id and comandTable.id=UlikaLutTable.idComand and comandTable.id=?', (name,))
ulika = cursor.fetchall()


# Доступные улики
menu = ''
xc = ''

# Формируем HTML страницу
#Html.head_html(meta='<meta http-equiv="Refresh" content="30" />', group=name)
Html.head_html(group=name)

for row in ulika:
	#menu = menu + '<a href=info-ulika.py?id={1}>{0}</a> {2}|{3} </br>'.format(row[0], row[1], sum_ulika(row[1]), sum_lut(row[1]))
	#print(row[1], ' ', row[0])
	#print(sum_ulika(row[1]))
	#print(sum_lut(row[1]), '<br>')
	if sum_ulika(row[1]) == sum_lut(row[1]): xc += '<li>{}</li>'.format(text_ulika[row[1]-1])

if sum_lut(user) == 15:
	print('<ul>{}</ul>'.format(xc))
else:
	print('''
<form name="form1" method="GET">
<table border="1" cellpadding="5" width="645">
<tbody>
<tr>
<td colspan="3"><center>
<h1 style="color: #FF0000;" align="center">Преступление Века</h1>
<p style="font-style: italic; color: #666666;" align="center"><br>Итак...</p><br>
<p>5 разных человек зашли в школу с разного цвета вещами, любят 5 разных сладостей, 
выращивают 5 разных видов животных, пьют 5 разных видов напитков.</p>
<span><b>Вопрос: Кто похитил Снегурочку?</b></span>
</center>
<p align="right"><input value="Очистить" class="inp" type="reset"></p>
</td>
<td colspan="3"><ol class="list">
{ulika}
</ol>
</td></tr>
<tr>
	<td width="150"><span><b>Порядок</b></span></td>
	<td width="105"><span>1</span></td>
	<td width="180"><span>2</span></td>
	<td width="170"><span>3</span></td>
	<td width="170"><span>4</span></td>
	<td width="180"><span>5</span></td>
</tr><tr>
	<td width="150"><span><b>Цвет</b></span></td>
	<td width="105" name="t1"><span>
	<select name="house1">
	<option value="nocolor">-----------&gt;</option>
	<option value="white">Белый</option>
	<option value="yellow">Желтый</option>
	<option value="green">Зеленый</option>
	<option value="red">Красный</option>
	<option value="blue">Синий</option>
	</select>
	</span></td>
	<td name="t2" width="180"><span>
	<select name="house2">
	<option value="nocolor">-----------&gt;</option>
	<option value="white">Белый</option>
	<option value="yellow">Желтый</option>
	<option value="green">Зеленый</option>
	<option value="red">Красный</option>
	<option value="blue">Синий</option>
	</select>
	</span></td>
	<td name="t3" width="200"><span>
	<select name="house3">
	<option value="nocolor">-----------&gt;</option>
	<option value="white">Белый</option>
	<option value="yellow">Желтый</option>
	<option value="green">Зеленый</option>
	<option value="red">Красный</option>
	<option value="blue">Синий</option>
	</select>
	</span></td>
	<td name="t4" width="200"><span>
	<select name="house4">
	<option value="nocolor">-----------&gt;</option>
	<option value="white">Белый</option>
	<option value="yellow">Желтый</option>
	<option value="green">Зеленый</option>
	<option value="red">Красный</option>
	<option value="blue">Синий</option>
	</select>
	</span></td>
	<td name="t5" width="200"><span>
	<select name="house5">
	<option value="nocolor">-----------&gt;</option>
	<option value="white">Белый</option>
	<option value="yellow">Желтый</option>
	<option value="green">Зеленый</option>
	<option value="red">Красный</option>
	<option value="blue">Синий</option>
	</select>
	</span></td>
</tr><tr>
<td width="150"><span><b>Напиток</b></span></td>
<td width="105"><span>
<select name="drink1">
<option value="nodrink">-----------&gt;</option>
<option value="water">Вода</option>
<option value="cafe">Кофе</option>
<option value="milk">Молоко</option>
<option value="beer">Сок</option>
<option value="tea">Чай</option>
</select>
</span></td>
<td width="180"><span>
<select name="drink2">
<option value="nodrink">-----------&gt;</option>
<option value="water">Вода</option>
<option value="cafe">Кофе</option>
<option value="milk">Молоко</option>
<option value="beer">Сок</option>
<option value="tea">Чай</option>
</select>
</span></td>
<td width="200"><span>
<select name="drink3">
<option value="nodrink">-----------&gt;</option>
<option value="water">Вода</option>
<option value="cafe">Кофе</option>
<option value="milk">Молоко</option>
<option value="beer">Сок</option>
<option value="tea">Чай</option>
</select>
</span></td>
<td width="200"><span>
  <select name="drink4">
    <option value="nodrink">-----------&gt;</option>
    <option value="water">Вода</option>
    <option value="cafe">Кофе</option>
    <option value="milk">Молоко</option>
    <option value="beer">Сок</option>
    <option value="tea">Чай</option>
  </select>
</span></td>
<td width="200"><span class="style14">
  <select name="drink5">
    <option value="nodrink">-----------&gt;</option>
    <option value="water">Вода</option>
    <option value="cafe">Кофе</option>
    <option value="milk">Молоко</option>
    <option value="beer">Сок</option>
    <option value="tea">Чай</option>
  </select>
</span></td>
</tr><tr>
<td width="150"><span><b>Животное</b></span></td>
<td width="105"><span>
  <select name="anim1">
    <option value="noanim">-----------&gt;</option>
    <option value="cat">Зебра</option>
    <option value="horse">Лошади</option>
    <option value="bird">Улитка</option>
    <option value="fish">Лиса</option>
    <option value="dog">Собаки</option>
  </select>
</span></td>
<td width="180"><span>
  <select name="anim2">
    <option value="noanim">-----------&gt;</option>
    <option value="cat">Зебра</option>
    <option value="horse">Лошади</option>
    <option value="bird">Улитка</option>
    <option value="fish">Лиса</option>
    <option value="dog">Собаки</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="anim3">
    <option value="noanim">-----------&gt;</option>
    <option value="cat">Зебра</option>
    <option value="horse">Лошади</option>
    <option value="bird">Улитка</option>
    <option value="fish">Лиса</option>
    <option value="dog">Собаки</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="anim4">
    <option value="noanim">-----------&gt;</option>
    <option value="cat">Зебра</option>
    <option value="horse">Лошади</option>
    <option value="bird">Улитка</option>
    <option value="fish">Лиса</option>
    <option value="dog">Собаки</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="anim5">
    <option value="noanim">-----------&gt;</option>
    <option value="cat">Зебра</option>
    <option value="horse">Лошади</option>
    <option value="bird">Улитка</option>
    <option value="fish">Лиса</option>
    <option value="dog">Собаки</option>
  </select>
</span></td>
</tr><tr>
<td width="150"><span><b>Сладости</b></span></td>
<td width="105"><span>
  <select name="cigar1">
    <option value="nocigaret">--------------&gt;</option>
    <option value="dunhill">Барбариска</option>
    <option value="marlboro">Жел. Мишка</option>
    <option value="pallmall">"Коровка"</option>
    <option value="philipmorris">Маршмеллоу</option>
    <option value="rothmans">Чупа-Чупс</option>
  </select>
</span></td>
<td width="180"><span>
  <select name="cigar2">
    <option value="nocigaret">--------------&gt;</option>
    <option value="dunhill">Барбариска</option>
    <option value="marlboro">Жел. Мишка</option>
    <option value="pallmall">"Коровка"</option>
    <option value="philipmorris">Маршмеллоу</option>
    <option value="rothmans">Чупа-Чупс</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="cigar3">
    <option value="nocigaret">--------------&gt;</option>
    <option value="dunhill">Барбариска</option>
    <option value="marlboro">Жел. Мишка</option>
    <option value="pallmall">"Коровка"</option>
    <option value="philipmorris">Маршмеллоу</option>
    <option value="rothmans">Чупа-Чупс</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="cigar4">
    <option value="nocigaret">--------------&gt;</option>
    <option value="dunhill">Барбариска</option>
    <option value="marlboro">Жел. Мишка</option>
    <option value="pallmall">"Коровка"</option>
    <option value="philipmorris">Маршмеллоу</option>
    <option value="rothmans">Чупа-Чупс</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="cigar5">
    <option value="nocigaret">--------------&gt;</option>
    <option value="dunhill">Барбариска</option>
    <option value="marlboro">Жел. Мишка</option>
    <option value="pallmall">"Коровка"</option>
    <option value="philipmorris">Маршмеллоу</option>
    <option value="rothmans">Чупа-Чупс</option>
  </select>
</span></td>
</tr><tr>
<td width="150"><span><b>Имя</b></span></td>
<td width="105"><span>
  <select name="nac1">
    <option value="nonac">--------------&gt;</option>
    <option value="english">Ананимус</option>
    <option value="denmark">Бармалей</option>
    <option value="german">Гринч</option>
    <option value="Norway">Саурон</option>
    <option value="Schwed">Снеговик</option>
  </select>
</span></td>
<td width="180"><span>
  <select name="nac2">
    <option value="nonac">--------------&gt;</option>
    <option value="english">Ананимус</option>
    <option value="denmark">Бармалей</option>
    <option value="german">Гринч</option>
    <option value="Norway">Саурон</option>
    <option value="Schwed">Снеговик</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="nac3">
    <option value="nonac">--------------&gt;</option>
    <option value="english">Ананимус</option>
    <option value="denmark">Бармалей</option>
    <option value="german">Гринч</option>
    <option value="Norway">Саурон</option>
    <option value="Schwed">Снеговик</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="nac4">
    <option value="nonac">--------------&gt;</option>
    <option value="english">Ананимус</option>
    <option value="denmark">Бармалей</option>
    <option value="german">Гринч</option>
    <option value="Norway">Саурон</option>
    <option value="Schwed">Снеговик</option>
  </select>
</span></td>
<td width="200"><span>
  <select name="nac5">
    <option value="nonac">--------------&gt;</option>
    <option value="english">Ананимус</option>
    <option value="denmark">Бармалей</option>
    <option value="german">Гринч</option>
    <option value="Norway">Саурон</option>
    <option value="Schwed">Снеговик</option>
  </select>
</span>
</td></tr>
</tbody></table>
<input value="Проверка"type="submit" class="body_start" >
</form>'''.format(ulika=xc))

#print('''<table width=100% border=1>
#		<tr>
#			<td></td>
#			<td width=20%>{0}</td>
#		</tr>
#	</table>'''.format(menu))

Html.footer_html()
cursor.close()
connect.close()

