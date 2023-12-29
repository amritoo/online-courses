from sys import argv, exit
from cs50 import SQL
import csv

# Checking argument
if len(argv) != 2:
    print('Usage: python import.py characters.csv')
    exit()

# Get database
db = SQL("sqlite:///students.db")

with open(argv[1], 'r') as file:
    reader = csv.DictReader(file)
    # Reading each row
    for row in reader:
        name = row['name'].split(' ')
        house = row['house']
        birth = int(row['birth'])

        # Spliting fullnames into parts
        first = name[0]
        if len(name) == 3:
            middle = name[1]
            last = name[2]
        else:
            middle = None
            last = name[1]

        # Inserting into database
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)
