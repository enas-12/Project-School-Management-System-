from student_manager import Manager
from database_setup import Base, engine

# Create the database tables
Base.metadata.create_all(engine)

# Create a manager instance
manager = Manager()

# Add a new student
student = manager.add(Name='John Doe', Gender='M', Grade=[85, 90, 88], Student_class=9, Age=15)
print(f"Added student: {student.Name}, ID: {student.ID}")

# Find a student by ID
found_student = manager.find(uuid=student.ID)
if found_student:
    found_student.display()

# Calculate the student's status
status = manager.calculate_status(student.ID)
print(status)

# Remove a student
remove_msg = manager.remove(student.ID)
print(remove_msg)
