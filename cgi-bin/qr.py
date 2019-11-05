#!/usr/bin/env python3
# -*- coding: utf-8

# импорт библиотеки 
import pyqrcode	# sudo pip3 install pyqrcode
import png	# sudo pip3 install pypng
import cgi
import html
from _wall import *
wall = Html()

def main():
    head = '''\
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">
<head>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
   .layer1 {

    padding: 5px; /* Поля вокруг текста */
    float: left; /* Обтекание по правому краю */
    width: 201px; /* Ширина слоя */
   }
   </style>
</head>
<body>
	<div>
'''		
    print('Content-type: text/html\n')
    print(head)

    for i in range(1,29):
        code = pyqrcode.create('http://qvest.asspo.ru/cgi-bin/lut.py?idLut={}'.format(i))
        image_as_str = code.png_as_base64_str(scale=6)
        print('<div class="layer1"><img width="200" height="200"  src="data:image/png;base64,{}">'.format(image_as_str))
        print('<p align="center">{}</p></div>'.format(i))

    wall.footer_html()

    cur.close()
    con.close()
    

if __name__ == "__main__":
    web = main()

