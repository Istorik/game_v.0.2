#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 53 строка тип данных поменял на число

import sqlite3

con = sqlite3.connect('qvest2.db')
cur = con.cursor()
sql = """\
CREATE TABLE IF NOT EXISTS ulikaTable (
	id INTEGER PRIMARY KEY,
	ulikaName TEXT,
	ulikaMesto TEXT,
	ulikaText TEXT,
	Lupa TEXT,
	Photo TEXT,
	Him TEXT,
	Dictofon TEXT,
	ulikaImg TEXT
);

CREATE TABLE IF NOT EXISTS comandTable (
	id INTEGER PRIMARY KEY,
	timeStart TEXT,
	timeFinish TEXT,
	NameComand TEXT,
	NameSDetective TEXT,
	ClassSDetective INTEGER,
	NameDetective TEXT,
	ClassDetective INTEGER,
	NameMDetective TEXT,
	ClassMDetective INTEGER
);

CREATE TABLE IF NOT EXISTS inventaTable (
	id INTEGER PRIMARY KEY,
	time TEXT,
	idComand INTEGER,
	idLut INTEGER,
	idQR INTEGER
);

CREATE TABLE IF NOT EXISTS lutTable (
	id INTEGER PRIMARY KEY,
	TextLut TEXT
);

CREATE TABLE IF NOT EXISTS UlikaLutTable (
        id INTEGER PRIMARY KEY,
        time TEXT,
        idComand INTEGER,
        idUlika INTEGER,
        Lupa TEXT,
        Photo TEXT,
        Him TEXT,
        Dictofon TEXT
);
"""

try:
	cur.executescript(sql)

except sqlite3.DatabaseError as err:
	print('Ошибка: ', err)

else:
	print('База удачно созадана')


sql_data = """\
	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Грязное пятно на скатерти', 
	'Кабинет 40 (гримерка). Оно же место пощищения.', 
	'Вы обнаружили странное грязное пятно на скатерти. Осознаёте, что такой звезде как Снегурочка не стали бы стелить грязную скатерть. Младший детектив предложил изучить данный след с помощью инструментов.', 
	'Исследовав грязное пятно с помощью лупы, Вы убедились в том, что это пятно  жидкости  разлитой из стакана, лежащего неподалёку. </p><p>Вы, как старший детектив, дано догадались, кто похититель, но нужно дать шанс детективам  проявить себя и исследовать эту жидкость с помощью других инструментов.', 
	null, 
	'Исследовав грязное пятно  жидкости из пролитого стакана с помощью химического набора Вы определили,  что в кружке была обычная вода. </p><p>Странный похититель, пьет обычную воду.', 
	null, 
	'/pics/ulika1.jpg'
);
	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Ниточка на полу', 
	'Кабинет 40 (гримерка). Оно же место пощищения.', 
	'Вы обнаружили странную ниточку на полу, остальные детективы даже не задумались о её происхождении, но ваше чутьё Старшего детектива просто кричит о важности находки.', 
	'Изучив детально непонятную ниточку с пола, Вы заметили, что это вовсе и не ниточка, а клок шерсти какого-то животного.', 
	'Пробиваете по базе улику. Клок шерсти принадлежит зебре.', 
	null,
	null,
	'/pics/ulika2.jpg'
);

	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Брошенные красные перчатки', 
	'Пушкинская рекреация', 
	'Оставленные кем-то красные перчатки. Они явно пренадлежали кому-то из странных поситителей, такой размер слишком велик для любого учащегося школы.', 
	'При детальном исследовании перчаток вы замечаете, что на них явно виден след от кольца ', 
	'Анализ фотографии позволил перевести надпись:</p><p>«Одно кольцо, чтоб править всеми,</p><p>Оно главнее всех,</p><p>Оно сберёт всех вместе</p><p>И заключит во тьме.»</p><p>Кольцо всевластия</p><p>1ВГ Кольцо Всевластия Саурона и его перчатки', 
	null,
	null,
	'/pics/ulika3.jpg'
);

	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Шевеление у забора', 
	'Окно с видом на калитку.', 
	'Вы видите, как вдалеке возле ворот что-то или кто-то шевелится.',
	'С помощью хитро поставленных луп вы смогли приблизить картинку и увидеть собаку на привязи.	',
	'Пробив по базе улик собаку и привязь, вы узнаете, что это животное Бармалея',
	null,
	null, 
	'/pics/ulika4.jpg'
);

	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Тряпка', 
	'Кабинет Литературы',
	'На спинке стула в кабинете висит какая-то ткань, она явно принадлежит одному из подозрительных личностей.', 
	'С помощью лупы Вы разглядели, что перед вами не просто грязный кусок ткани, а чей-то плащ, более детальный анализ плаща показывает, что он имеет определенный цвет и какое-то выделяющееся пятно в районе живота', 
	'Да, Вы так и думали, а черно-белая фотография это доказала, улика имеет зеленый цвет.', 
	'Исследовав в лаборатории пробы пятна, Вы пришли к выводу, что оно оставлено от пролитого на себя Кофе.', 
	null, 
	'/pics/ulika5.jpg'
);
	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Чашка', 
	'Рекреация Математиков', 
	'На столе стоит чашка.', 
	'Рядом с чашкой лежит маска и явно видно, что ее сняли для того, что бы насладиться напитком из этой самой чашки.', 
	'Наша база, а так же память по прошлому делу показывает, что данная маска принадлежит Анонимусу.',
	'Исследовав в лаборатории пробы жидкости из чашки, Вы пришли к выводу, что это обычный чай.', 
	null, 
	'/pics/ulika6.jpg'
);

	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Two old ladies’ talk', 
	'Кабинет Английского языка 1', 
	'Вы услышали разговор двух человек и, если у Вас есть диктофон, Вы сможете его записать и разобрать, а если нет, то ничего страшного, они еще долго будут тут сплетничать.', 
	null, 
	null, 
	null, 
	'<p>– The weather is nice today! It’s not raining.</p><p>– You don’t like rain?</p><p>– No, I don’t. I can’t see what happens in the street, what people do, where they go.</p><p>– I see, you are a real spy!</p><p>– Yes, I am! By the way, do you remember that white school at the end of the street?</p><p>– Exactly! There are always strange people there. Did you see anything strange near that building?</p><p>– In the morning many people came into the school one by one. They all were silent.</p><p>– Do you remember these people?</p><p>– Yeah, somebody in a green coat (raincoat) went in just after one man in white boots.</p><p>– Is it strange?</p><p>– I just don’t like a lot of bright colours!</p>',
	'/pics/ulika7.jpg'
);
	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Брошенный  на пол фантик', 
	'Гидрант 2 этаж',
	'Кто-то бросил фантик мимо урны, это явно был не ученик нашей школы. Ведь мы все аккуратные и не бросаем мусор, где попало.', 
	null,
	'Поискав в базе совпадений, Вы выявили, что это фантик от "барбариски"', 
	'Взяв пробы с улики и проанализировав их в химической лаборатории, Вы  получили странные результаты. Это оказалась слизь улитки.',
	null,
	'/pics/ulika8.jpg'
);

	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Камера №2', 
	'Стенд "МИФ"', 
	'Ваш взгляд зацепляется за мусор у стенда', 
	'С помощью лупы Вы разобрали, что мусор, это фантик от Чупа-Чупса', 
	'Подключившись к камере Вы видете, что фантик бросил кто-то с желтым зонтиком', 
	null, 
	'Тот кто пришел с желтым зонтиком был с чупа-чупсом.',
	'/pics/ulika9.jpg'
);
	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)

	VALUES (
	'Кружка',
	'Столовая', 
	'На столе стоит кружка.',
	null, 
	null, 
	'Исследовав в лаборатории пробы жидкости из кружки, Вы пришли к выводу, что в ней недавно было молоко.', 
	'По свидетельским показаниям очевидцев, Вы узнаете, что эта кружка  осталась после посещения данного помещения третьим странным гостем школы',
	'/pics/ulika10.jpg'
);

	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)

	VALUES (
	'Две дамы разгаваривают с полицейским',
	'Кабинет Английского языка 2',
	'Вы услышали разговор двух человек и если у Вас есть диктофон, Вы сможете его записать и разобрать, а если нет ничего страшного, они еще долго будут тут сплетничать.',
	null, 
	null, 
	null,
	'<p>– Mr. Black I want to share with you some useful information!</p>
	<p>– Yes, I am all in attention! How many homeless cats and dogs did you see today?</p>
	<p>– You are joking at me?</p>
	<p>– No, I am not. You just often give me these facts!</p>
	<p>– This time it was that strange school! And strange people coming in and out of it.</p>
	<p>– Yes, I also saw that Grinch was the first. Somebody in blue trousers came just after him. </p>
	<p>– Did anyone else come inside after?</p>
	<p>– No, they were the last. And they didn’t go out. That’s I think, strange!</p>',
	'/pics/ulika11.jpg'
);

	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Допрос Алексея', 
	'Центральный вход', 
	'Алексей рассказал Вам, что видел как в школу зашли…', 
	null, 
	null,
	null, 
	'В двери вошли двое. "Так чем ты кормишь свою лошадь? А морковь она любит? А сахар?" - интересовался один из них. Потом достал из кармана чупа-чупс и с наслаждением принялся за сладость.',
	'/pics/ulika12.jpg'
);


	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Столик в столовой', 
	'Столовая', 
	'Один из подозрительных типов сделал заказ в столовой.', 
	null, 
	'На месте, где сидел подозрительный тип, остались желатиновые мишки',
	'На месте, где сидел подозрительный тип, в стакане остался недопитый апельсиновый сок', 
	null,
	'/pics/ulika13.jpg'
);

	INSERT INTO ulikaTable (
	ulikaName, 
	ulikaMesto, 
	ulikaText, 
	Lupa, 
	Photo, 
	Him, 
	Dictofon, 
	ulikaImg
)
	VALUES (
	'Камера №1', 
	'Коридор 2 этаж', 
	'Кусок конфеты', 
	null, 
	null,
	'Химический анализ крошек показал, что это остатки конфеты «Коровка»', 
	'Артем Сергеевич, посмотрел камеру и рассказал Вам о том, что на этом подаконнике сидел Снеговик',
	'/pics/ulika14.jpg'
)

"""

arr = [
		('Лупа',),
		('Фотоаппарат',),
		('Набор криминалиста',),
		('Диктофон',),
		('Чай',),
		('Чай',),
		('Кофе',),
		('Кофе',),
		('Вода',),
		('Вода',),
		('Молоко',),
		('Молоко',),
		('Перчатки',),
		('Перчатки',),
		('Апельсиновый сок',),
		('Апельсиновый сок',)
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
