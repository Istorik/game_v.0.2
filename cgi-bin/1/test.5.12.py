#!/usr/bin/env python3
# -*- coding: utf-8

import cgi # отработка html кода на странице.


from _wall import *
wall = Html()

def main():
    db = Database(filename = 'qvest2.db', table = 'ulikaTable1')

#    print('Create table test')
#    db.sql_do('drop table if exists test')
#    db.sql_do('create table test ( t1 text, i1 int )')
#
#    print('Create rows')
#    db.insert(dict(t1 = 'one', i1 = 1))
#    db.insert(dict(t1 = 'two', i1 = 2))
#    db.insert(dict(t1 = 'three', i1 = 3))
#    db.insert(dict(t1 = 'four', i1 = 4))
#    for row in db: print(row)

#    print('Retrieve rows')
#    print(db.retrieve('1'), db.retrieve('3'))

    print('Update rows')
    db.update(dict(idUlika = '1', ulikaImg = '../pics/ulika1.jpg'))
#    db.update(dict(t1 = 'three', i1 = 103))
    for row in db: print(row)
#
#    print('Delete rows')
#    db.delete('one')
#    db.delete('three')
#    for row in db: print(row)



form = cgi.FieldStorage()
id = form.getfirst("id")

#wall.head_html("А вот так")


if id is None:
	print('<p> Не пришли</p>')
	
else:
	print("<p>Пришел id=%s</p>" % id)

print("<p>Контроль</p>")


if __name__ == "__main__": main()

#wall.footer_html()
#
