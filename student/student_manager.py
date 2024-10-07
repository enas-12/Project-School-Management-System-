from students import Student, get_db_connection

class Manager:
    def add(self, name, gender, grades, student_class, age):
        new_student = Student(name, gender, grades, student_class, age=age)
        new_student.save()
        return new_student

    def find(self, uuid=None, name=None):
        student = Student.from_db(uuid=uuid, name=name)
        if student:
            student.display()
        else:
            print("No student found")
        return student

    def remove(self, uuid):
        conn = get_db_connection()
        cursor = conn.cursor()

        # Remove student from the database
        cursor.execute("DELETE FROM students WHERE ID = %s", (uuid,))
        conn.commit()

        if cursor.rowcount > 0:
            message = f"Student with ID {uuid} has been removed."
        else:
            message = "No student found with that ID."

        conn.close()
        return message

    def calculate_status(self, uuid):
        student = self.find(uuid=uuid)
        if student:
            avg = student.Calculate_Average()
            if avg < 50:
                self.remove(uuid)
                return f"{student.name} failed and was removed."
            elif 50 <= avg <= 60:
                return f"{student.name} will stay in the same class."
            else:
                return f"{student.name} passed to the next class."
        return "Student not found."
