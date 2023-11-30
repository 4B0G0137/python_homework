class Student:
    def __init__(self,name,school_name,school_address,department,chair_name,student_id,correspondence_address,course_credits,gpa):
        self.__name=name
        self.__school_name=school_name
        self.__school_address=school_address
        self.__department=department
        self.__chair_name=chair_name
        self.__student_id=student_id
        self.__correspondence_address=correspondence_address
        self.__course_credits=course_credits
        self.__gpa=gpa
    
    #setter and getter
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name=new_name
        
    def get_school_name(self):
        return self.__school_name
    def set_school_name(self,new_school_name):
        self.__school_name=new_school_name
        
    def get_school_address(self):
        return self.__school_address
    def set_school_address(self,new_school_address):
        self.__school_address=new_school_address
        
    def get_department(self):
        return self.__department
    def set_department(self,new_department):
        self.__department=new_department
        
    def get_chair_name(self):
        return self.__chair_name
    def set_chair_name(self,new_chair_name):
        self.__chair_name=new_chair_name
        
    def get_student_id(self):
        return self.__student_id
    def set_student_id(self,new_student_id):
        self.__student_id=new_student_id
        
    def get_correspondence_address(self):
        return self.__correspondence_address
    def set_correspondence_address(self,new_correspondence_address):
        self.__correspondence_address=new_correspondence_address
    
    #another way to get and set
    @property
    def course_credits(self):
        return self.__course_credits
    @course_credits.setter
    def course_credits(self,new_course_credits):
        self.__course_credits=new_course_credits
    
    @property  
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self,new_gpa):
        self.__gpa=new_gpa

#row test data        
student01=Student("Eddie","STUST","NST#1","CSIE","Mike","4B0G0137","Kaohsiung",150,4.00)

#to test get and set
student01.set_chair_name("Tom")
print(student01.get_chair_name())

student01.set_school_name("南臺科大")
print(student01.get_school_name())

student01.set_correspondence_address("Taipei")
print(student01.get_correspondence_address())

student01.gpa=3.50
print(student01.gpa)

student01.course_credits=165
print(student01.course_credits)