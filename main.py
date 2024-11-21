class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def set_details(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
    def get_details(self):
        print("NAME: %s" %(self.name))
        print("AGE: %s" %(self.age))
        print("GENDER: %s" %(self.gender))
    
class Student(person):
    def __init__(self,name,age,gender,course,s_id,grades):
        super().__init__(name,age,gender)
        self.course = course
        self.s_id = s_id
        self.grades = grades

    def set_student_details(self):
        self.s_id = input("Enter student ID: ")
        self.course = input("Enter course name: ")
    def add_grade(self):
        self.grades.append(int(input("Enter grade: ")))
    def avg(self):
        return sum(self.grades)/len(self.grades)
    def get_details(self):
        super().get_details()
        print("STUDENT ID: %s" %(self.s_id))
        print("COURSE: %s" %(self.course))
        print("AVERAGE GRADE: %d" %(self.avg()))

class Professor(person):
    def __init__(self,name,age,gender,dep,s_id,pay):
        super().__init__(name,age,gender)
        self.dep = dep
        self.s_id = s_id
        self.pay = pay
    def set_prof_details(self):
        self.s_id = input("Enter staff ID: ")
        self.dep = input("Enter department: ")
        self.pay = input("Enter salary: ")
    def feedback(self,student):
        feed = input("Enter feedback to give to %s:\n" %(student.name))
        print("FEEDBACK FOR %s: %s" %(student.name,feed))
    def increase_pay(self):
        self.pay = self.pay*1.05
    def get_details(self):
        super().get_details()
        print("STAFF ID: %s" %(self.s_id))
        print("DEPARTMENT: %s" %(self.dep))
        print("SALARY: %d" %(self.pay))

class Admin(person):
    def __init__(self,name,age,gender,s_id,office,exp):
        super().__init__(name,age,gender)
        self.s_id = s_id
        self.office = office
        self.exp = exp
    def set_admin_details(self):
        self.s_id = input("Enter staff ID: ")
        self.office = input("Enter office location: ")
        self.exp = int(input("Enter years of service: "))
    def increment_exp(self):
        self.exp += 1
    def get_details(self):
        super().get_details()
        print("ADMIN ID: %s" %(self.s_id))
        print("OFFICE: %s" %(self.office))
        print("YEARS OF SERVICE: %d" %(self.exp))

student1 = Student("Taco",17,"F","Computer Science","12345",[6,7,9,9,9])
student2 = Student("Burger",17,"F","Computer Science","21345",[8,7,8,6,9])
prof1 = Professor("Mr Apple",34,"M","Maths","32415",72000)
prof2 = Professor("Ms Carrot",32,"F","Computer Science","43251",75000)
admin1 = Admin()