#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('qvest2.db')
cur = con.cursor()
sql = """\
CREATE TABLE IF NOT EXISTS ulikaTable1 (
	idUlika INTEGER PRIMARY KEY,
	ulikaName TEXT,
	ulikaMesto TEXT,
	ulikaText TEXT,
	ulikaLupa TEXT,
	ulikaPhoto TEXT,
	ulikaHim TEXT,
	ulikaDictofon TEXT,
	ulikaImg TEXT
);
CREATE TABLE IF NOT EXISTS ulikaTable2 (
	idUlika INTEGER PRIMARY KEY,
	ulikaName TEXT,
	ulikaMesto TEXT,
	ulikaText TEXT,
	ulikaLupa TEXT,
	ulikaPhoto TEXT,
	ulikaHim TEXT,
	ulikaDictofon TEXT,
	ulikaImg TEXT
);
CREATE TABLE IF NOT EXISTS ulikaTable3 (
	idUlika INTEGER PRIMARY KEY,
	ulikaName TEXT,
	ulikaMesto TEXT,
	ulikaText TEXT,
	ulikaLupa TEXT,
	ulikaPhoto TEXT,
	ulikaHim TEXT,
	ulikaDictofon TEXT,
	ulikaImg TEXT
);
CREATE TABLE IF NOT EXISTS comandTable (
	idName INTEGER PRIMARY KEY,
	timeStart TEXT,
	timeFinish TEXT,
	NameComand TEXT,
	NameSDetective TEXT,
	ClassSDetective INTEGER,
	NameDetective TEXT,
	ClassDetective INTEGER,
	NameMDetective TEXT,
	ClassMDetective INTEGER,
	instLupa TEXT,
	instPhoto TEXT,
	instHim TEXT,
	instDictofon TEXT
);
CREATE TABLE IF NOT EXISTS inventaTable (
	idInventar INTEGER PRIMARY KEY,
	timeInentar TEXT,
	idNameComand INTEGER,
	qrInventar TEXT,
	typeInventar TEXT,
	idQR INTEGER
);
CREATE TABLE IF NOT EXISTS lutTable (
	idLut INTEGER PRIMARY KEY,
	TextLut TEXT
);
"""

try:
	cur.executescript(sql)

except sqlite3.DatabaseError as err:
	print('Ошибка: ', err)

else:
	print('База удачно созадана')


sql_data = """\
	INSERT INTO ulikaTable1 (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	ulikaLupa, 
	ulikaPhoto, 
	ulikaHim, 
	ulikaDictofon, 
	ulikaImg
)
	VALUES (
	'Грязное пятно на скатерти', 
	'Кабинет 40 (гримерка). Оно же место пощищения.', 
	'Вы обнаружили странное грязное пятно на скатерти. Явно понимая, что такой звезде как Снегурочка не стали бы стелить грязную скатерть. Младший детектив предложил изучить данный след с помощью инструментов.', 
	'1. Исследовав грязное пятно с помощью лупы, Вы убедились в том что это пятно от жидкости из разлитой кружки лежащей не подалёку. </p><p>Вы как старший детектив дано догадались кто похититель, но нужно дать шанс детективам  проявить себя и исследовать эту жидкость с помощью других инструментов', 
	null, 
	'2. Исследовав грязное пятно от жидкости разлитой из неподалеку стоящего стакана с помощью химического набора Вы определили,  что в стакане была обычная вода. </p><p>Странный похититель, пьет обычную воду.', 
	null, 
	null
);
	INSERT INTO ulikaTable1 (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	ulikaLupa, 
	ulikaPhoto, 
	ulikaHim, 
	ulikaDictofon, 
	ulikaImg
)
	VALUES (
	'Ниточка на полу', 
	'Кабинет 40 (гримерка). Оно же место пощищения.', 
	'Вы обнаружили странную ниточку на полу, остальные детективы даже не задумались о её проихождении, но ваше чутьё Старшего детектива просто кричит о важности находки.', 
	'1. Изучив детально непонятную ниточку с пола, Вы заметили, что это вовсе и не ниточка ка клок шерсти какого-то животного.', 
	'2. Пробив по базе улик этот клок шестри, оказался ', 
	null, 
	null, 
	null
);

	INSERT INTO ulikaTable1 (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	ulikaLupa, 
	ulikaPhoto, 
	ulikaHim, 
	ulikaDictofon, 
	ulikaImg
)
	VALUES (
	'Брошенные красные перчатки', 
	'Коридор 3 этажа', 
	'Кем то оставленные красные перчатки. Они явно пренадлежали кому то из странных поситителей, такой размер слишком велик для любого учащегося школы', 
	'1. При детальном исследовании перчаток на них явно прослеживается след от кольца.', 
	'3. Анализ фотографии позволил перевести надпись:</p><p>3ВГ «Одно кольцо, чтоб править всеми,</p><p>Оно главнее всех,</p><p>Оно сберёт всех вместе</p><p>И заключит во тьме.»</p><p>2ВГ Кольцо всевластия</p><p>1ВГ Кольцо Всевластия Саурона и его перчатки', 
	'2. Втирев реагент вы видите надпись на кольце</p><p>«Ash nazg durbatulûk, ash nazg gimbatul,</p><p>Ash nazg thrakatulûk agh burzum-ishi krimpatul.»', 
	null, 
	null
)"""

arr = [
		('Лупа',),
		('Фотоаппарат',),
		('Набор криминалиста',),
		('Диктофон',),
		('Чай 1',),
		('Чай 2',),
		('Кофе 1',),
		('Кофе 2',),
		('Вода 1',),
		('Вода 2',),
		('Молоко 1',),
		('Молоко 2',),
		('Апельсиновый сок 1'	,),
		('Апельсиновый сок 2',)
]


sql_data2 = """\
INSERT INTO lutTable (TextLut)
VALUES (?)
"""


try:
#	cur.execute(sql_data) # Одна строка
	cur.executescript(sql_data) # Много сторк
	cur.executemany(sql_data2, arr) # несколько строчек данных


except sqlite3.DatabaseError as err:
	print('Ошибка: ', err)

else:
	print('База удачно заполнена')
	con.commit()

cur.close()
con.close()
