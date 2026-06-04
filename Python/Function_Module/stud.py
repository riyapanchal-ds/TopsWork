# Student Management System in Python

students = []

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age
    }

    students.append(student)
    print("Student Added Successfully!\n")


def view_students():
    if len(students) == 0:
        print("No Student Records Found!\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print(f"Roll No: {s['Roll']}")
            print(f"Name    : {s['Name']}")
            print(f"Age     : {s['Age']}")
            print("----------------------")
        print()


def search_student():
    roll = input("Enter Roll No to Search: ")

    for s in students:
        if s["Roll"] == roll:
            print("\nStudent Found!")
            print(f"Roll No: {s['Roll']}")
            print(f"Name   : {s['Name']}")
            print(f"Age    : {s['Age']}\n")
            return

    print("Student Not Found!\n")


def delete_student():
    roll = input("Enter Roll No to Delete: ")

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Student Deleted Successfully!\n")
            return

    print("Student Not Found!\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")