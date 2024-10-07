from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base model class for all database models
Base = declarative_base()

# Database setup (adjust connection string as per your database)
engine = create_engine('mysql+mysqlconnector://root:password@localhost/student_management', echo=True)

# Session factory
Session = sessionmaker(bind=engine)
