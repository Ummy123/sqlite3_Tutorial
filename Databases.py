__author__ = 'A. Sangha'
"""
Date: January 31, 2022
File Name: Databases
Description: Create a database and use simple commands to edit it
"""

import sqlite3

# For short term data, you can store it in RAM
# con = sqlite3.connect(':memory:')

# run the command "python Databases.py" in terminal to create the database
con = sqlite3.connect('Books.db')

# create cursor
curs = con.cursor()

# create a table
curs.execute("""CREATE TABLE books (
        book_name text,
        author text,
        publication_date text
    )""")

# create data for the table
book_list = [('The Catcher in the Rye', 'J. D. Salinger', '1951'),
             ('To Kill a Mockingbird', 'Harper Lee', '1960'),
             ('The Great Gatsby', 'F. Scott Fitzgerald', '1925'),
             ('The Lord of the Rings', 'J. R. R. Tolkien', '1954'),
             ('The Alchemist', 'Paulo Coelho', '1988')
             ]

# Update record
# curs.execute("""UPDATE books SET publication_date = '2000' WHERE publication_date = '1960'""")
# con.commit()



# insert data into the table
#curs.executemany("INSERT INTO books VALUES (?,?,?)", book_list)



# see what is in database
# print(curs.fetchone()) will print the first item in the database
# print(curs.fetchmany(3)) will print the first 3 items in the database
# get all items from the table including primary key
curs.execute("SELECT rowid, * FROM books")
books = curs.fetchall()

# in the square brackets, 0 prints the book names, 1 prints the author, 2 prints the publication date
for item in books:
    print(item)#[])

# The "where" clause helps search for specific items, this instance searches for authors that begin with "J"
# curs.execute("SELECT rowid, * FROM books WHERE author LIKE 'J%'")
# books = curs.fetchall()
#for item in books:
    #print(item)

# commit command
con.commit()

# close the connection
con.close()