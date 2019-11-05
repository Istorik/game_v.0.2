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



class Database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')
    
    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()
    
    def insert(self, row):
        self._db.execute('insert into {} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1']))
        self._db.commit()
    
    def retrieve_ulika(self, key):
        '''Достаем улику'''
        cursor = self._db.execute('select * from {} where idUlika = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())

    def retrieve_comand(self, key):
        '''Достаем команду'''
        cursor = self._db.execute('select * from {} where idName = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())
    
    def update(self, row):
        self._db.execute(
            'update {} set i1 = ? where t1 = ?'.format(self._table),
            (row['i1'], row['t1']))
        self._db.commit()
    
    def delete(self, key):
        self._db.execute('delete from {} where t1 = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row['t1'], row['i1']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
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
