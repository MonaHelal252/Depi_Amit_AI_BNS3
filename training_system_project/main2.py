import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))

from Depi_Amit_AI_BNS3.Sources.oop.training_system_project.core.system_manager2 import SystemManager


def show_menu():
    print("1. Add student")
    print("2. Remove student")
    print("3. Add course")
    print("4. Remove course")
    print("5. Search courses")
    print("6. Record grade")
    print("7. Get all students")
    print("8. Get all courses")
    print("9. Enroll course")
    print("10. Exit")

def add_student(manager):
    name = input("Enter student name: ")
    student_id = manager.add_student(name)
    print("Student ID: ", student_id )
    print("\n" + "=" * 40)


def remove_student(manager):
    student_id = int(input("Enter Student ID: "))
    manager.remove_student(student_id)
    print("\n" + "=" * 40)

def add_course(manager):
    name = input("Enter course name: ")
    course_id = manager.add_course(name)
    print("Course ID: ", course_id)
    print("\n" + "=" * 40)

def remove_course(manager):
    course_id = int(input("Enter course ID: "))
    manager.remove_course(course_id)
    print("\n" + "=" * 40)

def search_courses(manager):
    search_name = input("Enter course name to search: ")
    courses = manager.search_courses(search_name)
    for course in courses:
        print(course)
    print("\n" + "=" * 40)

def record_grade(manager):
    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter course ID: "))
    grade = input("Enter grade: ")
    manager.record_grade(student_id , course_id , grade)
    print("\n" + "=" * 40)

def get_all_students(manager):
    students = manager.get_all_students()
    for student in students:
         print(student)
    print("\n" + "=" * 40)

def get_all_courses(manager):
    courses = manager.get_all_courses()
    for course in courses:
        print(course)
    print("\n" + "=" * 40)

def enroll_course(manager):
    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter course ID: "))
    manager.enroll_course(student_id , course_id)
    print("\n" + "=" * 40)

def core():
    manager = SystemManager()
    while True:
        show_menu()
        choice = input("Enter choice: ")

           
        if choice == '1':
            add_student(manager)

        elif choice == '2':
            remove_student(manager)

        elif choice == '3':
            add_course(manager)

        elif choice == '4':
            remove_course(manager)

        elif choice == '5':
            search_courses(manager)

        elif choice == '6':
            record_grade(manager)
  
        elif choice == '7':
            get_all_students(manager)

        elif choice == '8':
            get_all_courses(manager)

        elif choice == '9':
            enroll_course(manager)

        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice")
            print("\n" + "=" * 40)

if __name__ == "__main__":
    core()
   


