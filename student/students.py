import shortuuid
import random

class Student:
    students_data = []
    def __init__(self, Name, Gender, Grade,Student_class, ID, Age, min_length=6, max_length=10):
        self.name = Name
        self.age = Age
        self.Student_class = Student_class
        uuid_length = random.randint(min_length, max_length)
        self.ID = str(shortuuid.ShortUUID().random(length=uuid_length))
        self.Gender = Gender
        self.Grade = Grade  # Assuming Grade is a list of numbers representing grades

    def Calculate_Average(self):
        if len(self.Grade) == 0:
            return 0
        return sum(self.Grade) / len(self.Grade)

    # Example grade list
    def display(self):
        print(f"The details of Student1 are ({self.name},{self.age} years old ,in {self.Student_class}th , her ID is {self.ID} and {self.Gender})")
        print(f"Average Grade: {self.Calculate_Average()}")


