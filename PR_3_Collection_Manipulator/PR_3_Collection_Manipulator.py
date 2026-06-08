# Student Data Organizer

students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")

    subjects_input = input("Enter Subjects (comma separated): ")
    subjects_list = [subject.strip() for subject in subjects_input.split(",")]

    # Tuple (Immutable)
    student_info = (student_id, dob)

    # Set (Unique subjects)
    subjects_set = set(subjects_list)

    # Dictionary
    student = {
        "id_info": student_info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects_set
    }

    students.append(student)

    print("\nStudent added successfully!")


def display_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:

        student_id = student["id_info"][0]
        dob = student["id_info"][1]

        subjects = ", ".join(student["subjects"])

        # String Formatting using f-string
        print(
            f"""
Student ID : {student_id}
Name       : {student['name']}
Age        : {student['age']}
Grade      : {student['grade']}
DOB        : {dob}
Subjects   : {subjects}
-----------------------------------
"""
        )


def update_student():
    print("\n--- Update Student ---")

    search_id = int(input("Enter Student ID: "))

    for student in students:

        if student["id_info"][0] == search_id:

            print("Student Found!")

            student["name"] = input("Enter New Name: ")
            student["age"] = int(input("Enter New Age: "))
            student["grade"] = input("Enter New Grade: ")

            subjects = input(
                "Enter New Subjects (comma separated): "
            )

            student["subjects"] = set(
                subject.strip()
                for subject in subjects.split(",")
            )

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    search_id = int(input("Enter Student ID: "))

    for i in range(len(students)):

        if students[i]["id_info"][0] == search_id:

            # del keyword
            del students[i]

            print("Student deleted successfully!")
            return

    print("Student not found.")


def display_subjects():
    print("\n--- Subjects Offered ---")

    all_subjects = set()

    for student in students:
        all_subjects.update(student["subjects"])

    if len(all_subjects) == 0:
        print("No subjects available.")
    else:
        for subject in sorted(all_subjects):
            print(subject)


def main():

    print("=" * 50)
    print("WELCOME TO STUDENT DATA ORGANIZER")
    print("=" * 50)

    while True:

        print("""
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            display_subjects()

        elif choice == "6":
            print("\nThank you for using Student Data Organizer.")
            print("Good Bye!")
            break

        else:
            print("Invalid choice. Try again.")


main()
