#!/usr/bin/env python3
# -*- coding: utf-8

# импорт библиотеки 
import pyqrcode	# sudo pip3 install pyqrcode
import png	# sudo pip3 install pypng
import cgi
import html
import time
from datetime import datetime
import sqlite3
from _wall import *
wall = Html()

def main():
    form = cgi.FieldStorage()

    Name_group = form.getfirst("Name_group", "1")
    Name_kapitan = form.getfirst("Name_kapitan")
    Name_user_1 = form.getfirst("Name_user_1")
    Name_user_2 = form.getfirst("Name_user_2", "") 

    Class_kapitan = form.getfirst("Class_kapitan")
    Class_user_1 = form.getfirst("Class_user_1")
    Class_user_2 = form.getfirst("Class_user_2", "")

    # Для безопасноти, преобразуем системные символы в код HTML
    Name_group = html.escape(Name_group)
    Name_kapitan = html.escape(Name_kapitan)
    Name_user_1 = html.escape(Name_user_1)
    Name_user_2 = html.escape(Name_user_2)

    Class_kapitan = html.escape(Class_kapitan)
    Class_user_1 = html.escape(Class_user_1)
    Class_user_2 = html.escape(Class_user_2)
    
    group = Base_users().find(Name_group)
    
    if group is not None:
        wall.head_html("Ошибка")
        print("Такая команда уже есть")
        wall.footer_html()
        return
    else:
        content = '''\
    
    <div class='text'>
	<p>- Оооо! Знаменитое детективное агенство {group}. - Воскликнул Лейтенант.</p>
	<p>Лучший детектив столетия, после Шерлока Холмса разумеется, старший детектив {CSDET} класса, {SDET}.</p>
	<p>А так же его первый помощник, детектив {CDET} класса, {DET}.</p>
    '''

    if Name_user_2 != "":
        contentpl = '<p>И я смотрю Вы ростите себе достойную замену, младший детектив ' + str(Name_user_2) + "</p></div>"
    else:
        contentpl = '</div>'

    dt = datetime.now()
    date = str(dt.strftime("%d.%m.%Y %H:%M:%S"))

    con = sqlite3.connect('qvest2.db')
    cur = con.cursor()

    base = (date, Name_group, Name_kapitan, Class_kapitan, Name_user_1, Class_user_1, Name_user_2, Class_user_2)
    sql = "INSERT INTO comandTable (timeStart, NameComand, NameSDetective, ClassSDetective, NameDetective, ClassDetective, NameMDetective, ClassMDetective) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"



    wall.head_html(Name_group)

    try:
        cur.execute(sql, base)

    except sqlite3.DatabaseError as err:
        print('Ошибка базы: ', err)
        print(contentError.format(err))

    else:
        con.commit()
        group = Base_users().find(Name_group)
        print(content.format(group=Name_group, SDET=Name_kapitan, CSDET=Class_kapitan, DET=Name_user_1, CDET=Class_user_1))
        print(contentpl)

    Id_group = str(group[0])
    code = pyqrcode.create('http://qvest.asspo.ru/cgi-bin/cookie.py?Id_group={}'.format(Id_group))
    image_as_str = code.png_as_base64_str(scale=6)
    html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
    print('<p>Для настройки телефона отсканируй первый QR код или  перейди по ссылке<p>')
    print("<center><a href='/cgi-bin/cookie.py?Id_group={0}'>{1}</a></center>".format(Id_group, html_img))

    wall.footer_html()

    cur.close()
    con.close()
    

if __name__ == "__main__":
    web = main()

