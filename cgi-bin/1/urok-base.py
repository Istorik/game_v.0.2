#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('urok.db')
cur = con.cursor()
sql = """\
CREATE TABLE IF NOT EXISTS comp (
	id INTEGER PRIMARY KEY,
	schoolboy TEXT,
	Titul TEXT,
	Text_tip TEXT,
	Poly TEXT,
	Zagolovok_1 TEXT,
	Zagolovok_2 TEXT,
	Text TEXT,
	Zagolovok_1_tip TEXT,
	Zagolovok_2_tip TEXT,
	Klontitul TEXT,
	Oglavlenie TEXT
);

"""

try:
	cur.executescript(sql)

except sqlite3.DatabaseError as err:
	print('Ошибка: ', err)

else:
	print('База удачно созадана')


arr = [
		('Комп 1',),
		('Комп 2',),
		('Комп 3',),
		('Комп 4',),
		('Комп 5',),
		('Комп 6',),
		('Комп 7',),
		('Комп 8',),
		('Комп 9',),
		('Комп 10',)
]


sql_data2 = """\
INSERT INTO comp (schoolboy)
VALUES (?)
"""


try:
	cur.executemany(sql_data2, arr) # несколько строчек данных


except sqlite3.DatabaseError as err:
	print('Ошибка: ', err)

else:
	print('База удачно заполнена')
	con.commit()



cur.close()
con.close()
