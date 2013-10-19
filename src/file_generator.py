#!/usr/bin/env python

import sqlite3
import sys

try:
    connection = sqlite3.connect('../database/database.db')
    query = connection.cursor()    
    query.execute('SELECT * from locations')
    data = query.fetchall()
    for column in data:
        print "%s\t%s" % (column[0], [column[2], column[3]])
        
except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
