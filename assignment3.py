import json

def load_student_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def save_student_data(json_file_path, data):
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def get_student_by_id(data, student_id):
    for student in data:
        if student["ID"] == student_id:
            return student
    return None


def get_all_students(data):
    return data



def get_students_by_major(data, major):
    students_in_major = []
    for student in data:
        if student["Major"].lower() == major.lower():
            students_in_major.append(student)
    return students_in_major



def add_student(data, name, age, major, gpa):
    new_student = {
        "ID": len(data) + 1,
        "Name": name,
        "Age": age,
        "Major": major,
        "GPA": gpa
    }
    data.append(new_student)
    save_student_data(json_file_path, data)
    
    

def find_common_majors(data1, data2):
    majors1 = set(student["Major"] for student in data1)
    majors2 = set(student["Major"] for student in data2)
    return majors1.intersection(majors2)


def delete_student(data, student_id):
    for student in data:
        if student["ID"] == student_id:
            data.remove(student)
            save_student_data(json_file_path, data)
            return


def calculate_average_gpa(data):
    total_gpa = sum(student["GPA"] for student in data)
    return total_gpa / len(data)


def get_top_performers(data, num_performers):
    sorted_students = sorted(data, key=lambda student: student["GPA"], reverse=True)
    top_students = sorted_students[:num_performers]
    return [student["Name"] for student in top_students]


def main_menu():
    while True:
        print("- - - - - - - - - - - - - - -")
        print("1. Get Student by ID")
        print("2. Get All Students")
        print("3. Get Students by Major")
        print("4. Add Student")
        print("5. Find Common Majors")
        print("6. Delete Student")
        print("7. Calculate Average GPA")
        print("8. Get Top Performers")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            student = get_student_by_id(data, student_id)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == "2":
            students = get_all_students(data)
            for student in students:
                print(student)

        elif choice == "3":
            major = input("Enter major: ")
            students = get_students_by_major(data, major)
            for student in students:
                print(student)

        elif choice == "4":
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            major = input("Enter student's major: ")
            gpa = float(input("Enter student's GPA: "))
            add_student(data, name, age, major, gpa)
            print("Student added.")

        elif choice == "5":
            data2 = load_student_data('data2.json')  # Load data from another file for comparison
            common_majors = find_common_majors(data, data2)
            if common_majors:
                print("Common majors: ", common_majors)
            else:
                print("No common majors found.")

        elif choice == "6":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(data, student_id)
            print("Student deleted.")

        elif choice == "7":
            avg_gpa = calculate_average_gpa(data)
            print(f"Average GPA: {avg_gpa:.2f}")

        elif choice == "8":
            num_performers = int(input("Enter the number of top performers to retrieve: "))
            performers = get_top_performers(data, num_performers)
            print(f"Top performers: {performers}")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    json_file_path = 'data.json'
    data = load_student_data(json_file_path)
    main_menu()
