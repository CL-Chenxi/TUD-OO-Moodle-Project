import random
import datetime as dt
import string
import csv

# create super class
class User():
    num_user = 0

    #Constructor
    def __init__(self, email_address, name):

        if not email_address.__contains__("@") or not email_address.endswith(".com"):
            raise Exception("Email address is not valid.")
        if len(name) == 0:
            raise Exception("Name cannot be empty.")

        self.email_address = email_address
        self.name= name
        self.password = random.randint(0,10000)      
        self.dpt = " "          
        self.date_registered = dt.date.today()
        self.num_user += 1 

  
    #create print definition to display User details
    def print(self):
        print("*********************************") 
        print("               Users             ") 
        print("*********************************") 
        print("User Name: ", self.name) 
        print("User Email : ", self.email_address) 
        print("User Password : ", self.password) 
        print("User Department : ", self.dpt) 
        print("Date Registered : ", self.date_registered)
        print()

# create sub class
class Student(User):

    def __init__(self, email_address, name, stu_num, program_code, program_year, stu_type):
        super().__init__(email_address, name)
        if len(stu_num) != 9 or not stu_num.isdigit():  
            raise Exception("Student number invalid.")        
        if program_code == None:
            raise Exception("Program Code Cannot be empty.")
        if program_year not in range(0,6):
            raise Exception("Program year must be between Y1 to Y6.")
        if stu_type.strip() not in ["FT","PT"]:
            raise Exception("Student can only be FT(full time) or PT(part time).")

        self.stu_num = stu_num
        self.program_code = program_code
        self.program_year = program_year
        self.stu_type = stu_type

    def set_department(self, dpt):
        self.dpt = dpt

    #create print definition to display Student details   
    def print(self):
        super().print()
        print("Student Number:", self.stu_num)
        print("Program Code:", self.program_code) 
        print("Program Year", self.program_year) 
        print("Student Type :", self.stu_type) 
        print()
       

# create sub class
class Lecturer(User):   
    def __init__(self,email_address,name, staff_id, speciality, qualification):
        super().__init__(email_address, name)
        if len(staff_id) != 6 or not staff_id.isdigit(): 
            raise Exception("Staff ID invalid.")
        if speciality == None:
           raise Exception("Program Code Cannot be empty.")
        qualificationList = ["BA", "BSC", "MA", "MSC", "PHD"]
        if qualification not in qualificationList:
            raise Exception("Lecturer qualification is invalid.")
            
        self.staff_id = staff_id
        self.speciality = speciality
        self.qualification = qualification

    #create print definition to display Lecturer details
    def print(self):
        super().print()
        print("Staff ID :", self.staff_id)
        print("Lecturer Speciality :", self.speciality) 
        print("Lecturer Qualification :", self.qualification) 
        print()



# create Static Class
class GradeCalculator:
    @staticmethod
    def percentage_to_grade(percentage_in):
        if percentage_in >= 80 and percentage_in <= 100:
            return "A"
        if percentage_in >= 70 and percentage_in <= 79:
            return "B+"
        if percentage_in >= 60 and percentage_in <= 69:
            return "B"
        if percentage_in >= 55 and percentage_in <= 59:
            return "B-"
        if percentage_in >= 50 and percentage_in <= 54:
            return "C+"
        if percentage_in >= 40 and percentage_in <= 49:
            return "C"
        if percentage_in >= 35 and percentage_in <= 39:
            return "D"
        if percentage_in <= 34:
            return "F"


#create Module class
class Module():
    
    def __init__(self, module_id = "", module_name = "Unknown", course_code = " ", dpt = "Computing", lecturer = ""):

        dptList = ["Computing", "Science", "Marketing", "Business", "Art"]
        
        if len(module_id) == 0 :
            raise print("Module ID cannot be blank.")
        if dpt not in dptList:
            raise Exception("Department choice is invalid.")  
        #lecturer must be a Lecturer object     
        if not isinstance(lecturer, Lecturer):
            raise Exception("Lectuer choice is invalid.")

        lecturer.dpt = dpt
        self.__module_id = module_id
        self.__module_name = module_name
        self.__course_code = course_code
        self.__dpt = dpt
        self.__lecturer = lecturer
        self.__class_list = [] 
        self.__assessment_list = []


 # getters and setters
    def get_department(self):
        return self.__dpt
    def set_department(self, dept):
        self.dpt = dept
    def get_module_id(self):
        return self.__module_id
    def set_module_id(self, module_id):
        self.__module_id = module_id
    def get_module_name(self):
        return self.__module_name
    def get_course_code(self):
        return self.__course_code 
    def get_lecturer(self):
        return self.__lecturer
    def get_assessment_list(self):
        return self.__assessment_list
    def set_assessment_list(self):
        self.__assessment_list = assessment_list
    def get_class_list(self):
        return self.__class_list
    def set_class_list(self):
        self.__class_list = class_list

    # create auto add classlist    
    def auto_add_classlist(self,student_file):
        file = open(student_file)
        students = file.readlines()
        students.pop(0)
        for line in students:
            stu_values = line.split(",")
            #create a dictionary for student
            student = Student(stu_values[0], stu_values[1], stu_values[2], stu_values[3], int(stu_values[4]), stu_values[5])
            student.set_department(self.__dpt)
            self.__class_list.append(student)
        file.close()
    #create append to class list           
    def append_to_class_list(self, new_student):
        new_student.set_department(self.__dpt)
        self.__class_list.append(new_student)
       #create append to assessment list   
    def append_to_assessment_list(self, assessment):
        self.__assessment_list.append(assessment)

    #create print definition to print module details      
    def print_module_details(self):
        print('*'*49)
        print("*********************************") 
        print("              Module             ") 
        print("*********************************") 
        print("Module ID :", self.__module_id)
        print("Module Name :", self.__module_name) 
        print("Course Code :", self.__course_code) 
        print("Department :", self.__dpt) 
        self.__lecturer.print()
        print("Class list")
        for s in self.__class_list:
            s.print()
        print('*'*49)
        print()

###############################################
#main program body
# a)
def display_menu():
    print('*'*49)
    print('*\t\t\tMenu\t\t\t*')
    print('*\t 1. Add Module\t\t\t\t*')
    print('*\t 2. Add Student to Module\t\t*')
    print('*\t 3. Add Student Grades to Module\t*')
    print('*\t 4. Display List of Modules\t\t*')
    print('*\t 5. Display list of Students\t\t*')
    print('*\t 6. Display list of Students of Grades\t*')
    print('*\t 7. Exit\t\t\t\t*')
    print('*'*49)


module_list = []
file = open(r"modules.csv")
modules = file.readlines()
modules.pop(0)
for line in modules:
    m_value = line.strip().split(",")
    #create a dictionary for lecturer
    lecturer = Lecturer(m_value[4], m_value[5], m_value[6], m_value[7], m_value[8])
    module = Module(m_value[0], m_value[1], m_value[2], m_value[3], lecturer)
    module_list.append(module)
file.close()

# b)
while(True):
    display_menu()
    user_input = input("Enter option : ")

    if user_input == "1":
        id = input("Enter Module id : ")
        id_exists = False
        for module in module_list:
            if id == module.get_module_id():
                id_exists = True
                print(f"Module {id} already exists!")
                break
        if id_exists == False:
            course_name = input("Enter course name : ")
            code  = input("Enter course code : ")
            dept = input("Enter department : ")
            email = input("Enter lecturer's email address : ")
            name = input("Enter lecturer's name : ")
            staff_id = input("Enter lecturer's id : ")
            spec = input("Enter lecturer's spec : ")
            level = input("Enter lecturer's qualification : ")
            lecturer = Lecturer(email,name,staff_id,spec,level)
            module = Module(id,course_name,code, dept, lecturer)
            module_list.append(module)

    if user_input == "2":
        id = input("Enter Module id : ")
        for module in module_list:
            if id == module.get_module_id():
                by_file = input("Enter Student by using file? y/n ")
                if by_file == "y":
                    path = input("Enter file path : ")
                    module.auto_add_classlist(path)
                else:
                    email = input("Enter student's email address : ")
                    name = input("Enter student's name : ")
                    student_id = input("Enter student's id : ")
                    code = input("Enter student's programme's code : ")
                    year = int(input("Enter student's year : "))
                    type = input("Enter type (PT/FT) : ")
                    new_student  = Student(email,name,student_id, code,year, type)
                    module.append_to_class_list(new_student)

    if user_input == "3":
        id = input("Enter Module id :")
        for module in module_list:
            if id == module.get_module_id():
                nb_grades = int(input("Enter number of grades : "))
                for i in range(0,nb_grades):
                    student_id = input("Enter student's id : ")
                    assessment_name = input("Enter assessment name : ")
                    percentage = int(input("Enter percentage achived : "))
                    print()
                    grade = GradeCalculator.percentage_to_grade(percentage)
                    module.append_to_assessment_list([student_id,assessment_name,percentage,grade] )
                

    if user_input == "4":
        nb_students = 0
        module_d = {"Computing":0, "Science":0, "Marketing":0, "Business":0, "Art":0}
        for m in module_list:
            m.print_module_details()
            nb_students += len(m.get_class_list())
            module_d[m.get_department()] += 1
        print(f"Total number of Modules : {len(module_list)}")
        print(f"Total number of students in the system : {nb_students}")
        print("Modules by departments :")
        print(f"Computing : ", module_d["Computing"])
        print(f"Science : ", module_d["Science"])
        print(f"Marketing : ", module_d["Marketing"])
        print(f"Business : ", module_d["Business"])
        print(f"Art : ", module_d["Art"])

    if user_input == "5":
        id = input("Enter Module id : ")
        for module in module_list:
            if id == module.get_module_id():
                class_list = module.get_class_list()
                for s in class_list:
                    s.print()
                print(f"Total number of students in this module : {len(class_list)} ")


    if user_input == "6":
        id = input("Enter Module id : ")
        for module in module_list:
            if id == module.get_module_id() and len(module.get_assessment_list()) > 0 :
                grades_d = {"A":0,"B+":0,"B":0,"B-":0,"C+":0,"C":0,"D":0,"F":0}
                assessment_list = module.get_assessment_list()
                avg = 0
                highest = 0
                lowest = 100
                for a in assessment_list:
                    print(f"Student id {a[0]}; Assessment name: {a[1]}; Percentage {a[2]}%; Grade {a[3]}")
                    if a[2] > highest:
                        highest = a[2]
                    if a[2] < lowest:
                        lowest = a[2]
                    avg += a[2]
                    grades_d[a[3]] += 1
                avg = int(avg / len(assessment_list))
                print("________________________________")
                print("|","Toal\t\t","|",nb_grades,"\t\t|")
                print("________________________________")
                print("|","Highest\t","|",highest,"\t\t|")
                print("________________________________")
                print("|","Lowest\t","|", lowest,"\t\t|")
                print("________________________________")
                print("|","Average\t","|",avg,"\t\t|")
                print("________________________________")
                print("|","A\t\t","|",grades_d["A"],"\t\t|")
                print("________________________________")
                print("|","B+\t\t","|",grades_d["B+"],"\t\t|")
                print("________________________________")
                print("|","B\t\t","|",grades_d["B"],"\t\t|")
                print("________________________________")
                print("|","B-\t\t","|",grades_d["B-"],"\t\t|")
                print("________________________________")
                print("|","C+\t\t","|",grades_d["C+"],"\t\t|")
                print("________________________________")
                print("|","C\t\t","|",grades_d["C"],"\t\t|")
                print("________________________________")
                print("|","D\t\t", "|",grades_d["D"],"\t\t|")
                print("________________________________")
                print("|","F\t\t","|",grades_d["F"],"\t\t|")
                print("________________________________")
                print()

    if user_input == "7":
        with open("modules.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["ModuleId","ModuleName","CourseCode",
            "Department","Lecturer_Email","Lecturer_Name","Lecturer_StaffId",
            "Lecturer_Speciality","Lecturer_Qualification"])
            for m in module_list:
                lecturer = m.get_lecturer()
                row = [m.get_module_id(), m.get_module_name(), m.get_course_code(), m.get_department(),
                        lecturer.email_address, lecturer.name, lecturer.staff_id, lecturer.speciality, 
                        lecturer.qualification]
                writer.writerow(row)
        break


# might need to enter full path for .csv files for option 2. sorry for incoveniences.