import shortuuid
import random
import mysql.connector

# MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="enas",
        database="student"
    )


class Student:
    def __init__(self, Name, Gender, Grade, Student_class, ID=None, Age=None):
        self.name = Name
        self.age = Age
        self.Student_class = Student_class
        self.ID = ID or str(shortuuid.ShortUUID().random(length=random.randint(6, 10)))
        self.Gender = Gender
        self.Grade = Grade  # Assuming Grade is a list of numbers representing grades

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the student record into the database
        query = ("INSERT INTO students (ID, Name, Gender, Age, Student_class, Grade) "
                 "VALUES (%s, %s, %s, %s, %s, %s)")
        values = (self.ID, self.name, self.Gender, self.age, self.Student_class, ','.join(map(str, self.Grade)))

        cursor.execute(query, values)
        conn.commit()
        conn.close()

    @staticmethod
    def from_db(uuid=None, name=None):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        if uuid:
            cursor.execute("SELECT * FROM students WHERE ID = %s", (uuid,))
        else:
            cursor.execute("SELECT * FROM students WHERE Name = %s", (name,))

        student_data = cursor.fetchone()
        conn.close()

        if student_data:
            # Convert the comma-separated grade string back into a list of integers
            grades = list(map(int, student_data['Grade'].split(',')))
            return Student(
                Name=student_data['Name'],
                Gender=student_data['Gender'],
                Grade=grades,
                Student_class=student_data['Student_class'],
                ID=student_data['ID'],
                Age=student_data['Age']
            )
        return None

    def Calculate_Average(self):
        if len(self.Grade) == 0:
            return 0
        return sum(self.Grade) / len(self.Grade)

    def display(self):
        print(f"Student: {self.name}, {self.age} years old, Class: {self.Student_class}, ID: {self.ID}, Gender: {self.Gender}")
        print(f"Average Grade: {self.Calculate_Average()}")
