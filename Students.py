class Student:
    id_name = ()
    email = ""
    grades = [()]
    courses = {}

    def __init__(self, student_id, student_name, email, grades=None, courses=None):
    # 👉 initialize attributes here
        self.student_id = student_id
        self.email = email
        self.grades = grades
        self.courses = courses

    def __str__(self):
    # 👉 return formatted string of student info
        return string.format({student_id}, {student_name},{email},{grades},{courses})

class StudentRecords:
    def __init__(self):
    # 👉 initialize empty list for students
        pass
    
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
    # 👉 create Student object and append to list
    # 👉 return "Student added successfully"
        pass

    def update_student(self, student_id, email=None, grades=None, courses=None):
    # 👉 find student by ID
    # 👉 update only provided values
    # 👉 return success or not found
        pass

    def delete_student(self, student_id):
    # 👉 remove student if found
    # 👉 return "Student deleted successfully" or "Student not found"
        pass

    def enroll_course(self, student_id, course):
    # 👉 add course to student’s set (duplicates handled automatically)
    # 👉 return success or not found
        pass

    def search_student(self, student_id):
    # 👉 return student info if found, else "Student not found"
        pass

    def calculate_gpa(self):
    # 👉 convert scores into GPA scale (A=4.0, B=3.0, etc.)
    # 👉 compute and return average GPA
        pass

    def search_by_name(self, name):
    # 👉 check if name.lower() is in student.id_name[1].lower()
    # 👉 return all matches
        pass
