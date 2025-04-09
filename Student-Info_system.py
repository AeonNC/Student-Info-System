students = {}

def add_student(name, age, marks):
    students[name] = {'Age': age, 'Marks': marks}

def view_student(name):
    if name in students:
        info = students[name]
        print(f"Name: {name}\nAge: {info['Age']}\nMarks: {info['Marks']}")
    else:
        print("Student not found.")

def display_all():
    if not students:
        print("No students added yet.")
    else:
        for name, info in students.items():
            print(f"\nName: {name}\nAge: {info['Age']}\nMarks: {info['Marks']}")

while True:
    print("\n--- Student Info System ---")
    print("1. Add Student\n2. View Student\n3. View All Students\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
        add_student(name, age, marks)

    elif choice == '2':
        name = input("Enter name to view: ")
        view_student(name)

    elif choice == '3':
        display_all()

    elif choice == '4':
        print("Exiting Student Info System.")
        break

    else:
        print("Invalid choice. Try again.")
