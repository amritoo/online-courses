from sys import argv, exit
from cs50 import SQL

# Checking argument
if len(argv) != 2:
    print('Usage: python roster.py house_name')
    exit()

# Get database
db = SQL("sqlite:///students.db")

# Selecting rows from table
rows = db.execute("SELECT * FROM students WHERE house=? ORDER BY last, first", argv[1])

for row in rows:
    middle = row['middle']
    if middle == None:
        print(row['first'], row['last'] + ", born", row['birth'])
    else:
        print(row['first'], middle, row['last'] + ", born", row['birth'])
