# database_setup.py

import peewee

# Configure the SQLite database (change to another database if needed)
db = peewee.SqliteDatabase('students.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


# Initialize the database
def initialize_db():
    db.connect()
    db.create_tables([Student], safe=True)  # Create tables if they don't exist
