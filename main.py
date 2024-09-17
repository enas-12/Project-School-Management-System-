# main.py

from database_setup import initialize_db
from student_manager import StudentManager

def main():
    initialize_db()  # Set up the database
    manager = StudentManager()

    # Uncomment below to add students
    # manager.add_student('Alice', 'F', 20, 2, '85,90,78')
    # manager.add_student('Bob', 'M', 22, 3, '70,75,80')

    print("Student List:")
    manager.list_students()

    print("Finding Student with ID 1:")
    manager.find_student('1')  # Replace with a valid student ID

    print("Removing Student with ID 1:")
    manager.remove_student('1')  # Replace with a valid student ID

if __name__ == '__main__':
    main()
