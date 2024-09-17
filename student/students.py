# student.py

import peewee
import shortuuid
from database_setup import BaseModel

class Student(BaseModel):
    id = peewee.CharField(primary_key=True, default=shortuuid.uuid)
    name = peewee.CharField(max_length=50)
    gender = peewee.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    age = peewee.IntegerField()
    student_class = peewee.IntegerField()
    grades = peewee.TextField()  # Store grades as a comma-separated string

    def calculate_average(self):
        grades = list(map(int, self.grades.split(',')))
        return sum(grades) / len(grades) if grades else 0

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
