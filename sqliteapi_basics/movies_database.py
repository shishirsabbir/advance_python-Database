import sqlite3

# connection = sqlite3.connect('movie.db')

# cursor = connection.cursor()

# cursor.execute(''' CREATE TABLE IF NOT EXISTS Movies(
# 	Title TEXT, Direction TEXT, Year INT) ''')


# cursor.execute("INSERT INTO Movies(Title, Direction, Year) VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")
# cursor.execute("SELECT * FROM Movies")

# famousFilms = [
# 	('Pulp Fiction', 'Quentin Tarantino', 1994),
# 	('Back to the Future', 'Steven Spielberg', 1985),
# 	('Moonrise Kingdom', 'Wes Anderson', 2012)
# ]

# cursor.executemany('INSERT INTO Movies VALUES (?, ?, ?)', famousFilms)
# records = cursor.execute('SELECT * FROM Movies')


# print(cursor.fetchone())
# print(cursor.fetchall())

# another way

# for record in records:
# 	print(record)


# release_year = (1985, )

# cursor.execute("SELECT * FROM Movies WHERE Year=?", release_year)

# print(cursor.fetchall())

# connection = sqlite3.connect('contacts.db')

# cursor = connection.cursor()

# cursor.execute(''' CREATE TABLE IF NOT EXISTS Contacts
#     (first_name TEXT, last_name TEXT, phone TEXT, email TEXT) ''')

# connection.commit()
# connection.close()



def insert_contact(first_name, last_name, phone, email):
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()

    query_script = f"INSERT INTO Contacts(first_name, last_name, phone, email) VALUES('{first_name}', '{last_name}', '{phone}', '{email}')"

    cursor.execute(query_script)
    print(query_script)

    connection.commit()
    connection.close()


def read_contact():
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Contacts")
    records = cursor.fetchall()

    connection.commit()
    connection.close()

    return records


insert_contact('Sabbir Ahamed', 'Shishir', '01883061280', 'shishir.sabbir@gmail.com')
insert_contact('Shahriar Ahamed', 'Shaishob', '01747155954', 'shaishob.shahriar@gmail.com')

result = read_contact()
print(result)








