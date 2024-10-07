from student import Student
from database_setup import Session

class Manager:
    def __init__(self):
        self.session = Session()

    # Add a new student
    def add(self, Name, Gender, Grade, Student_class, Age):
        new_student = Student(Name=Name, Gender=Gender, Grade=Grade, Student_class=Student_class, Age=Age)
        self.session.add(new_student)
        self.session.commit()
        return new_student

    # Search for a student by ID or Name
    def find(self, uuid=None, name=None):
        if uuid:
            return self.session.query(Student).filter_by(ID=uuid).first()
        elif name:
            return self.session.query(Student).filter_by(Name=name).first()
        return None

    # Remove a student by ID
    def remove(self, uuid):
        student = self.find(uuid=uuid)
        if student:
            self.session.delete(student)
            self.session.commit()
            return f"{student.Name} has been removed."
        return "Student not found"

    # Calculate student status
    def calculate_status(self, uuid):
        student = self.find(uuid=uuid)
        if student:
            avg = student.Calculate_Average()
            if avg < 50:
                self.remove(uuid)
                return f"{student.Name} failed and has been removed."
            elif 50 <= avg <= 60:
                return f"{student.Name} will stay in the current class."
            else:
                student.Student_class += 1
                self.session.commit()
                return f"{student.Name} has passed to class {student.Student_class}."
        return "Student not found"

    # Filter students based on their status (pass, fail, stay)
    def filter(self, status):
        students = self.session.query(Student).all()
        filtered_students = []
        for student in students:
            avg = student.Calculate_Average()
            if status == "fail" and avg < 50:
                filtered_students.append(student)
            elif status == "stay" and 50 <= avg <= 60:
                filtered_students.append(student)
            elif status == "pass" and avg > 60:
                filtered_students.append(student)
        return filtered_students
