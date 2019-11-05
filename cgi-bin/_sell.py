#!/usr/bin/env python3
# -*- coding: utf-8

import sqlite3

class baseQvest:
	def __init__(self):
		connect = sqlite3.connect('qvest2.db')
		cursor = connect.cursor()
	def retrieve(self, key):
		print(key)
		cursor = self.cursor.execute('select * from comandTable where NameComand = ?', (key,))
		cursor.close
		return cursor.fetchone()
	def close():
		connect.close()




class Database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')
    
    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

    def retrieve(self, key):
        '''Достаем по id'''
        cursor = self._db.execute('select * from {} where id = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())

    def retrieve_user(self, key):
        '''Достаем по name'''
        cursor = self._db.execute('select * from {} where NameComand = ?'.format(self._table), (key,))
        return cursor.fetchone()

    def ulika_find(self, ulika_id, user_id):
        cursor = self._db.execute('select * from {} where idUlika = ? and idComand = ?'.format(self._table), (ulika_id, user_id))
        return cursor.fetchone()
        
    def ulika_find_all(self, user_id):
        cursor = self._db.execute('select * from {} where idComand = ?'.format(self._table), (user_id,))
        return cursor.fetchall()

    def update(self, row):
        self._db.execute('update {} set id = ? where Lupa = ?'.format(self._table),
            (row['i1'], row['t1']))
        self._db.commit()
    
    def delete(self, key):
        self._db.execute('delete from {} where id = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['t1'], row['i1']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by id'.format(self._table))
        for row in cursor:
            yield dict(row)

    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t
    @table.deleter
    def table(self): self._table = 'test'

    def close(self):
        self._db.close()
        del self._filename


class Html():
	def head_html(title="Дело о похищенном празднике", group=None, meta=''):
		db_user = Database(filename = 'qvest2.db', table = 'comandTable')
		if group is not None: group = db_user.retrieve(group)['NameComand']
		head = '''\
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">
<head>
	<title>{}</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	{}
	<link rel="stylesheet" href="../style.css">
</head>
<header>
	<div class='who'>
		дело ведут {}
	</div>
</header>
<body>
	<div class='all'>
'''	
		print('Content-type: text/html\n')
		print(head.format(title, meta, group))
		
	def footer_html():
		footer='''\
        <center><a href='/cgi-bin/info-ulika.py'>Блокнот</a></center>
	</div>
</body>
</html>'''
		print(footer)

	def error():
		print('''
	<div class='ulika_all'>
		<div class='ulika_info'>
			<p><b>Что то пошло не так, зайдите в 41 кабинет.</b></p>
			<p><a href=http://qvest.sch438.loc>Зарегестрируйтесь</a></p>
			<p>Удобнее всего это сделать в кабинете информатики, за одно пройдете вводный курс</p>
			<p>Место преступления тоже находится на 4 этаже</p>
		</div>
	</div>
		''')

	def content(row, content=None):
		pattern = '''
	<h2>Улика № {id}/14</h2>
	<div class='ulika_all'>
		<div class='ulika_img'>
		  <img src={ulikaImg} alt='avatar'>
		</div>
		<div class='ulika_info'>
			<p><b>Местонахождение улики:</b> {ulikaMesto}</p>
			<p><b>Улика изучена на: </b></p>
			<div class="progress-bar orange shine">
				<span style="width: {status}%"><center>{status}%</center></span>
			</div>
		</div>
	</div>	
	<div class='ulika_txt'>
		<h1>{ulikaName}</h1>
		<p>{ulikaText}</p>
		<p>{Lupa}</p>
		<p>{Photo}</p>
		<p>{Him}</p>
		<p>{Dictofon}</p>
	</div>
'''
		print(pattern.format(**row))
