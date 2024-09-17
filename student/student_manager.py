# student_manager.py

from student import Student
from database_setup import db

class StudentManager:
    def add_student(self, name, gender, age, student_class, grades):
        student = Student(name=name, gender=gender, age=age, student_class=student_class, grades=grades)
        student.save()
        print(f"Added student: {student}")

    def list_students(self):
        students = Student.select()
        for student in students:
            print(f"{student} - Average Grade: {student.calculate_average()}")

    def find_student(self, student_id):
        try:
            student = Student.get(Student.id == student_id)
            print(f"Found student: {student}")
            print(f"Average Grade: {student.calculate_average()}")
        except Student.DoesNotExist:
            print("Student not found.")

    def remove_student(self, student_id):
        try:
            student = Student.get(Student.id == student_id)
            student.delete_instance()
            print(f"Removed student: {student}")
        except Student.DoesNotExist:
            print("Student not found.")
