from sqlalchemy import Column, Integer, String, Float
from database_setup import Base
import shortuuid
import random

class Student(Base):
    __tablename__ = 'students'

    ID = Column(String(10), primary_key=True)
    Name = Column(String(50), nullable=False)
    Gender = Column(String(1), nullable=False)
    Age = Column(Integer, nullable=False)
    Student_class = Column(Integer, nullable=False)
    Grade = Column(String)  # Store grades as a comma-separated string

    def __init__(self, Name, Gender, Grade, Student_class, Age, min_length=6, max_length=10):
        self.ID = str(shortuuid.ShortUUID().random(length=random.randint(min_length, max_length)))
        self.Name = Name
        self.Gender = Gender
        self.Grade = ','.join(map(str, Grade))  # Store grades as a string
        self.Student_class = Student_class
        self.Age = Age

    def Calculate_Average(self):
        grades_list = list(map(int, self.Grade.split(',')))
        if len(grades_list) == 0:
            return 0
        return sum(grades_list) / len(grades_list)

    def display(self):
        avg_grade = self.Calculate_Average()
        print(f"Student: {self.Name}, ID: {self.ID}, Age: {self.Age}, Class: {self.Student_class}")
        print(f"Gender: {self.Gender}, Average Grade: {avg_grade}")
