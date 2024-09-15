import shortuuid
import random

class Student:
    def __init__(self,Name,Gender,Grade,ID,Age,min_length, max_length):
        self.name = Name
        self.age = Age
        uuid_length = random.randint(min_length, max_length)
        self.ID = str(shortuuid.ShortUUID().random(length=uuid_length))
        self.Gender = Gender
        self.Grade = Grade
        

    def display(self):
            print(f"The details of Sudent1 are ( {self.name} , {self.age}, {self.ID},{self.Grade} and {self.Gender})")
    