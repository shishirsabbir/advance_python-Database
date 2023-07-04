import sqlalchemy as db
import sqlite3

# engine = db.create_engine('sqlite:///movie.db')
#
# connection = engine.connect()
#
# metadata = db.MetaData()
#
# movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

# query = db.select([movies])
#
# result_proxy = connection.execute(query)
#
# result_set = result_proxy.fetchall()
#
# print(result_set)

# query = db.select([movies]).where(movies.columns.Direction == 'Martin Scorsese')
#
# result_proxy = connection.execute(query)
#
# result_set = result_proxy.fetchall()
#
# print(result_set)
#
# query = movies.insert().values(Title="Psycho", Direction="Alfred Hitchcock", Year="1960")
#
# connection.execute(query)
#
# query = db.select([movies])
#
# result_proxy = connection.execute(query)
#
# result_set = result_proxy.fetchall()
#
# print(result_set)


##############################################################################################
# first sqlalchemy challenge


# connection = sqlite3.connect('users.db')
#
# cursor = connection.cursor()
#
# cursor.execute(''' CREATE TABLE IF NOT EXISTS Users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email_address TEXT) ''')
#
# users_data = [
#     ("shishir", "sabbir", "shishir.sabbir@gmail.com"),
#     ("apon", "masrur", "aponmasrur@gmail.com"),
#     ("shirin", "akter", "shishirinmarket@gmail.com"),
#     ("shaishob", "shahriar", "shaishobshahriar@gmail.com"),
#     ("mosharrof", "hossain", "mosharrof.hossain0077@gmail.com")
# ]
#
# cursor.executemany('INSERT INTO Users (first_name, last_name, email_address) VALUES (?, ?, ?)', users_data)
#
# records = cursor.execute('SELECT * FROM Users')
#
# print(records.fetchall())
#
# connection.commit()
# connection.close()

######################### sqlalchemy core way

# engine = db.create_engine('sqlite:///users.db')
#
# connection = engine.connect()
#
# metadata = db.MetaData()
#
# users = db.Table('Users', metadata, autoload=True, autoload_with=engine)
#
# query = db.select([users])
#
# result_proxy = connection.execute(query)
#
# result_set = result_proxy.fetchall()
#
# print(result_set)



####### create the table and insert data using sqlalchemy core

engine = db.create_engine('sqlite:///users.db')

connection = engine.connect()

metadata = db.MetaData()

users = db.Table('Users', metadata,
                 db.Column('user_id', db.Integer, primary_key=True),
                 db.Column('first_name', db.Text),
                 db.Column('last_name', db.Text),
                 db.Column('email_address', db.Text))

metadata.create_all(engine)

insertion_query = users.insert().values([
    {"first_name": "shishir", "last_name": "sabbir", "email_address": "shishir.sabbir@gmail.com"},
    {"first_name": "apon", "last_name": "masrur", "email_address": "aponmasrur@gmail.com"},
    {"first_name": "shirin", "last_name": "akter", "email_address": "shishirinmarket@gmail.com"},
    {"first_name": "shaishob", "last_name": "shahriar", "email_address": "shaishobshahriar@gmail.com"},
    {"first_name": "mosharrof", "last_name": "hossain", "email_address": "mosharrof.hossain0077@gmail.com"}
])

connection.execute(insertion_query)

selection_query = db.select([users.columns.email_address])

selection_result = connection.execute(selection_query)

print(selection_result.fetchall())
