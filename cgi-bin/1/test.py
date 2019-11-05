#!/usr/bin/env python3
# -*- coding: utf-8

import html
import http.cookies
import random
import sqlite3
import os

from _sell import Database


lut = dict()

db_ulika = Database(filename = 'qvest2.db', table = 'ulikaTable1')
db_user = Database(filename = 'qvest2.db', table = 'comandTable')


ulika = db_ulika.retrieve_ulika('1')
user = db_user.retrieve_comand('1')

print(ulika)
print(user)
