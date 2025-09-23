class Student:

    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.name_id = (student_id, student_name) #Put the student and id inside 1 attribute to call easily since I use tuple
        self.email = email 
        self.grades = grades if grades is not None else {} #Used ternary operator to set the disctionary as emptry since no value has been provided yet
        self.courses = courses if courses is not None else set() 

    def __str__(self):
        return (f"Student ID: {self.name_id[0]}, " # Accessing the tuple by index
                f"Student Name: {self.name_id[1]}, Email: {self.email}, " # Accessing the tuple by index
                f"Student Grades: {self.grades if self.grades is not None else "None"}, " # Ternary operator to check if grades is None
                f"Courses: {self.courses if self.courses is not None else "None"}") 
    
    def calculate_gpa(self):
        # GPA scale: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
        if not self.grades:
            return None
        total = 0 #initializing total and count variable
        count = 0 #initializing count variable

        for score in self.grades.values(): #iterating through the values of the grades dictionary
            if isinstance(score, str): #checking if the score is a string
                grade = score.upper() # converting the grade to uppercase to handle case insensitivity
                gpa = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}.get(grade, 0.0) #using dictionary to map letter grades to GPA values
            else:
                # If score is numeric, convert to letter grade
                if score >= 90:
                    gpa = 4.0
                elif score >= 80:
                    gpa = 3.0
                elif score >= 70:
                    gpa = 2.0
                elif score >= 60:
                    gpa = 1.0
                else:
                    gpa = 0.0
            total += gpa #adding the gpa to total
            count += 1 #incrementing the count for each grade processed
        return round(total / count, 2) if count else None #returning the gpa rounded to 2 decimal places

class StudentRecords:
    def __init__(self):
        self.students = [] # empty set where all the student objects will be stored
    
    def add_student(self, student_id, student_name, email, grades=None, courses=None):

        newstudent = Student(student_id, student_name, email, grades, courses) #This is the object
        self.students.append(newstudent) #Using the append function, added the object to the empty list
        
        return "Student added successfully"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.name_id[0] == student_id: #checks if the student id matches
                if email:
                    student.email = email #updates the email if provided
                if grades:
                    student.grades = grades #updates the grades if provided
                if courses:
                    student.courses = courses #updates the courses if provided
                return "Student updated successfully"
            return "Student not found"

    def delete_student(self, student_id):
        for i, student in enumerate(self.students): #using enumerate() function to get the index
            if student.name_id[0] == student_id: #checks if the student id matches
                del self.students[i]
                return "Student deleted successfully"
        return "Student not found"

    def enroll_course(self, student_id, course):
        for student in self.students: #iterates through the list of students
            if student.name_id[0] == student_id:  #checks if the student id matches
                student.courses.add(course)
                return "Course added successfully"
            return "Student not found"

    def search_student(self, student_id):
        for student in self.students: 
            if student.name_id[0] == student_id:
                return str(student)
            return "Student not found"

    def search_by_name(self, name):
        for student in self.students:
            if student.name_id[0] == name:
                student.courses.add(self.course)
                return "Course enrolled successfully"
        return "Student not found"

    def search_student(self, student_id):
        for student in self.students:
            if student.name_id[0] == student_id:
                return str(student)
        return "Student not found"

    def search_by_name(self, name):
        name = name.lower() # used the lower() function to make the search case-insensitive
        matches = [str(s) for s in self.students if name in s.name_id[1].lower()] # List comprehension to find all matching names
        return matches if matches else ["No matching students found"]
    
if __name__ == "__main__": #this is  to test the output of the code
    records = StudentRecords() #Created an object of the StudentRecords class
    print(records.add_student(33739, "Justin", "33739@gmail.com")) #Added a student
    print(records.update_student(33739,
    email="justin_new@gmail.com",
    grades={"ACP": "A", "OOP": "A","PATHfit": "A"},
    courses={"ACP", "OOP", "PATHFit"})) #updated the student
    print(records.search_student(33739)) #searched the student
    print(records.add_student(12345, "Hazel", "Hazel@gmail.com", {"ACP": "A", "OOP": "D"}, {"ACP", "OOP"})) #Added another student
    print("Justin's GPA:", [student.calculate_gpa() for student in records.students if student.name_id[0] == 33739][0]) #Print Justin's GPA
    print("Hazel's GPA:", [student.calculate_gpa() for student in records.students if student.name_id[0] == 12345][0]) #Print Hazel's GPA
    print(records.delete_student(12345)) #Deleted the student
