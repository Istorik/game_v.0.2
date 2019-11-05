#!/usr/bin/env python3
# -*- coding: utf-8

import sqlite3

class Html():
	def head_html(self, title="Дело о похищенном празднике", group=None):
		if group is not None:
			group = 'Set-cookie: session=' + group
		else:
			group = ""
		head = '''\
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">
<head>
	<title>{}</title>
	{}
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="../style.css">
</head>
<body>
	<div class='all'>
'''		
		print('Content-type: text/html\n')
		print(head.format(title, group))
		
	def footer_html(self):
		footer='''\
	</div>
</body>
</html>'''
		print(footer)

	def ulika_html(self):
		print('1')

class Base_users():

	def find(self, user):
		"""Ищет пользователя по имени"""
		user = (user, )
		con = sqlite3.connect('qvest2.db')
		cur = con.cursor()
		cur.execute('SELECT * FROM comandTable WHERE NameComand = ?', user)
		user = cur.fetchone()
#		print(user)
		if user is not None:
			return user
		return None
		


class Database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')
    
    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()
    
    def insert(self, row):
        '''Добавление в инвентарь улики'''
        self._db.execute('insert into {} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1']))
        self._db.commit()
    
    def retrieve(self, key):
        '''Возращает найденую строчку улики'''
        cursor = self._db.execute('select * from {} where idUlika = ?'.format(self._table), key)
        table = dict(cursor.fetchone())
        # Убираем None
        for i in table:
            if table[i] is None:
                i = {i : "<p></p>"}
                table.update(i)
        return table
    
    def update(self, row):
        '''Внесение изменений в базу'''
        self._db.execute(
            'update {} set idUlika = ? where ulikaImg = ?'.format(self._table),
            (row['idUlika'], row['ulikaImg']))
        self._db.commit()
    
    def delete(self, key):
        '''Удаление из базы, врятли мне понадобится'''
        self._db.execute('delete from {} where t1 = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by idUlika'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['dUlika'], row['i1']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by idUlika'.format(self._table))
        for row in cursor:
            yield dict(row)

    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row


    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t


    def close(self):
            self._db.close()
            del self._filename

