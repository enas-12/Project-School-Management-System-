# main.py

from student.student_manager import Manager

def main():
    manager = Manager()
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Find Student")
        print("3. Remove Student")
        print("4. Calculate Status")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            gender = input("Enter gender (M/F): ")
            age = int(input("Enter age: "))
            student_class = int(input("Enter class: "))
            grades = list(map(int, input("Enter grades (comma-separated): ").split(',')))
            manager.add(name, gender, grades, student_class, age)
            print(f"Student {name} added successfully!")
            
        elif choice == '2':
            search_by = input("Search by (1. ID, 2. Name): ")
            if search_by == '1':
                uuid = input("Enter student ID: ")
                student = manager.find(uuid=uuid)
            else:
                name = input("Enter student name: ")
                student = manager.find(name=name)
            print(student)
        
        elif choice == '3':
            uuid = input("Enter student ID to remove: ")
            message = manager.remove(uuid)
            print(message)
            
        elif choice == '4':
            uuid = input("Enter student ID: ")
            status = manager.calculate_status(uuid)
            print(status)
        
        elif choice == '5':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
