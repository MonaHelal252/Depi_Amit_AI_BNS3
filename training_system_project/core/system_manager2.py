from ..model.student2 import Student
from ..model.course2 import Course
class SystemManager:

    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self , name):
        student = Student(name)
        self.students[student.student_id] = student
        print("Student added Successfully.")

        return student.student_id
    
    def remove_student(self , student_id):
        if student_id in self.students:
            student = self.students[student_id]
            if not student.enrolled_courses:
                del self.students[student_id] 
                print("Student removed successfully.")

            else:
                print("Student has enrolled courses. cannot remove him")

        else:
            print("Invalid Student ID.")
    
    def add_course(self , name):
        course = Course(name)
        self.courses[course.course_id] = course
        print("Course added Successfully.")

        return course.course_id
    
    def remove_course(self , course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            if not course.enrolled_students:
                del self.courses[course_id]
                print("Course removed successfully.")
            else:
                print("Course has enrolled students. cannot remove")

        else:
            print("Invalid Course ID.")

    def search_courses(self , search_name):
        result = []
        for course in self.courses.values():
            if search_name.lower() == course.name.lower():
                result.append(course.name)
            else:
                print("Invalid course name.")
        return result

    def enroll_course(self , course_id , student_id):
        if course_id in self.courses and student_id in self.students:
            student = self.students[student_id]
            course = self.courses[course_id]

            if course.name not in student.enrolled_courses:
                student.enrolled_in_course(course)
                course.enroll_student(student)
                print("Student enrolled in course successfully.")

            else:
                print("Student is already enrolled in the course.")

        else:
            print("Invalid student or course ID.")

    def record_grade(self , student_id , course_id , grade):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.add_grade(course.name , grade)
            print("grade recorded successfully.")
        else:
            print("Invalid Student ID or Course ID")


    def get_all_students(self):
        return list(self.students.values())
    
    def get_all_courses(self):
        return list(self.courses.values())