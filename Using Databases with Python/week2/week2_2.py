# This application will read the mailbox data (mbox.txt) and
# count the number of email messages per organization
# (i.e. domain name of the email address) using a database
# with the following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)

import sqlite3

# Opens a connection to database if exists, otherwise creates it
conn = sqlite3.connect('week2_2.sqlite')
cur = conn.cursor()

# Drop table if exits and then create a new one
cur.execute('DROP TABLE IF EXISTS counts')
cur.execute('CREATE TABLE counts (org TEXT, count INTEGER)')

fh = open('mbox.txt')
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    org = pieces[1].split('@')[1]
    cur.execute('SELECT count FROM counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('''UPDATE counts SET count = count + 1 
                WHERE org = ?''', (org,))

# Commiiting all changes made to database
conn.commit()

# Closing the database cursor
cur.close()
