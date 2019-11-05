#!/usr/bin/env python3
# -*- coding: utf-8

import cgi
import html

form = cgi.FieldStorage()

Name_group = form.getfirst("Name_group", "не задано")
Name_kapitan = form.getfirst("Name_kapitan", "не задано")
Name_user_1 = form.getfirst("Name_user_1", "не задано")
Name_user_2 = form.getfirst("Name_user_2", "не задано")

Name_group = html.escape(Name_group)
Name_kapitan = html.escape(Name_kapitan)
Name_user_1 = html.escape(Name_user_1)
Name_user_2 = html.escape(Name_user_2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Детективное агенство {}</title>
        </head>
        <body>""".format(Name_group))

print("<h1>Позравляем! Детективное агенство создано!</h1>")
print("<p>Название Детективного агенства: {}</p>".format(Name_group))
print("<p>Старший детектив  {}</p>".format(Name_kapitan))
print("<p>Детектив: {}</p>".format(Name_user_1))
print("<p>Младший детектив: {}</p>".format(Name_user_2))


print("""</body>
        </html>""")
