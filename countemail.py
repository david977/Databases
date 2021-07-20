#Demonstrate CRUD

import sqlite3

conn = sqlite3.connect('mbox.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (domain TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE domain = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (domain, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE domain = ?',
                    (domain,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr0 = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 10'
#sqlstr = 'SELECT COUNT (DISTINCT domain)  FROM Counts'

for row in cur.execute(sqlstr0):
    #print(str(row))
    print(str(row[0]), row[1])

cur.close()
