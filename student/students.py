import shortuuid
import random

class Student:
    def __init__(self, Name, Gender, Grade, ID, Age, min_length, max_length):
        self.name = Name
        self.age = Age
        uuid_length = random.randint(min_length, max_length)
        self.ID = str(shortuuid.ShortUUID().random(length=uuid_length))
        self.Gender = Gender
        self.Grade = Grade  # Assuming Grade is a list of numbers representing grades

    def display(self):
        print(f"The details of Student1 are ({self.name}, {self.age}, {self.ID}, {self.Grade}, and {self.Gender})")
       

Student1 = Student("Enas", "Female", "14th", 500, 16, min_length=6, max_length=10)
Student1.display()
