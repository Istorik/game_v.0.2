#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os

#from _wall import Wall
#wall = Wall()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookie.get("session")

# Если куки не пустые, вытащить из куки значение value
if session is not None:
    session = session.value
else:

    # Вывести текст о том что для начала расследования необходимо 
    # зареестрировать собственное деетктивное агенство сделать это можно
    # по ссылке с телефона или из кабинета информатики.
    print('Content-type: text/html\n')
    print('<p>для начала расследования необходимо зареестрировать собственное деетктивное агенство.</p')
    print('<p>Cделать это можно по ссылке с телефона или из кабинета информатики.</p>')
    print('<a href=../index.html>Регистрация</a>')
    raise SystemExit

# Проверяем от куда пришел игрок и кто он такой
# http://qvest.asspo.ru/cgi-bin/form.1-1.py?idUlika=1

form = cgi.FieldStorage()
idUlika = form.getfirst("idUlika", "0")
idUlika = html.escape(idUlika)


# Добавить проверку наме групп если нет взять из куки, а если и там нет то отправить на регестрацию.
# незабыть после регестрации переслать название улики в форме.

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="style.css">
<title>Улика {posts}/17</title>
</head>
<body>
	<div class="ulika_all">
		<div class="ulika_img"><img></div>
		<div class="ulika_info">
			<div class="ulika_txt">
				<p class="bold">Название улики: {ulikaName}</p>
				<p class="bold">Местонахождение улики: {ulikaMesto}</p>
			</div
		</div>
		<div>
			{Text}
			{Lupa}
			{Photo}
			{Him}
			{Dictofon}
		</div>
		
		<form action="/cgi-bin/wall.py">
			Логин: <input type="text" name="login">
			Пароль: <input type="password" name="password">
			<input type="hidden" name="action" value="login">
			<input type="submit">
		</form>

		{posts}

		{publish}
    </div>
</body>
</html>
'''

else:

        pattern = '''

        <!DOCTYPE HTML>
        <html> 
        <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="../style.css">
        <title>Улика {posts}/17</title>
        </head>
        <body>
                <div class="for-example">
                        <p> Что то я вас не узнаю в гриме детектив. У вас точно есть допуск к этому расследованию?</p>
                        <p> Представьютесь пожалуйста</p>
                        <form action="/cgi-bin/ulika.py" autocomplete="off">
                         <div class="reg_name">
                                <p>Название детективного агенства:</p>
                                <input type="text" name="Name_group"> 
                        </div> 
                        <div class="reg_name">
                                <input type="submit" class="body_start" value=" Создать агенство "> 
                         </div>
                        </form>
                </div> 
        </body>
        </html>
        '''  

print('Content-type: text/html\n')

print(pattern.format(Text=ulikaText, Lupa=ulikaLupa, Photo=ulikaPhoto, Him=ulikaHim, Dictofon=ulikaDictofon,))

#print(pattern.format(posts=wall.html_list(), publish=pub))

