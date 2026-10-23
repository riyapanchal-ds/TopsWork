import os

FILE_NAME = "student_data.txt"

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{age},{course}\n")

    print("Student Added Successfully!")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No Records Found!")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("No Records Found!")
        return

    print("\nRoll\tName\tAge\tCourse")
    print("-"*40)

    for line in data:
        roll, name, age, course = line.strip().split(",")
        print(f"{roll}\t{name}\t{age}\t{course}")

def search_student():
    roll = input("Enter Roll No: ")

    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            r, name, age, course = line.strip().split(",")

            if r == roll:
                print("\nStudent Found")
                print("Roll:", r)
                print("Name:", name)
                print("Age:", age)
                print("Course:", course)
                found = True
                break

    if not found:
        print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll No: ")

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        found = False

        for line in lines:
            if line.startswith(roll + ","):
                found = True
                continue
            file.write(line)

    if found:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

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
        print("Invalid Choice")