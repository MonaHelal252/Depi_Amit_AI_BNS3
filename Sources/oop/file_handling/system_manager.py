class SystemManager:

    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self , name):
        student = Student(name)
        self.students(name)
        self.students[student.student_id]
        print("student added successfully")
        return student.student_id
    
    def remove_student(self , student_id):
        if student_id in self.students:
            student = self.students[student_id]
            if not student.enrolled_courses:
                del self.students[student_id]
                print("student removed successfully")
            else:
                print("student has enrolled course. cannot remove")

        else:
            print("invalid student id")

    def enrolle_course(self , student_id , course_id):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]

            if course.name not in student.enrolled_courses:
                student.enroll_in_course(course.name)
                course.enroll_student(student.name)
                print("student enrolled in course successfully.")
            else:
                print("student is already enrolled in the course.")
        else:
            print("Invalid student or course ID.")
    
    def record_grade(self,student_id, course_id,grade):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.add_grades(course.name , grade)
            print("Grade recorded successfully.")

        else:
            print("Invalid student ID or course ID")

    def get_all_students(self):
        return list(self.students.values)
    
    def get_all_courses(self):
        return list(self.courses.values)
    