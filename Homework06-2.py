class Employee:

    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.name = emp_name
        self.id = emp_id
        self.salary = emp_salary
        self.department = emp_department

    def calculate_emp_salary(self, hours_worked):
        overtime = hours_worked - 50
        if overtime > 0:
            overtime_amount = (overtime * (self.salary / 50))
            self.salary += overtime_amount
            return self.salary
        else:
            return self.salary

    def emp_assign_department(self, changed_department):
        self.department = changed_department
        return self.department

    def print_employee_details(self):
        print(
            f"Name : {self.name}\nID : {self.id}\nSalary : {self.salary}\nDepartment : {self.department}\n"
        )


#original data
person1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
person2 = Employee("JONES", "E7499", 45000, "RESEARCH")
person3 = Employee("MARTIN", "E7900", 50000, "SALES")
person4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

emp_list = [person1, person2, person3, person4]

#To print original data
print("------original data------")
for num in emp_list:
    num.print_employee_details()

#test To calcluate salary
person1.calculate_emp_salary(100)
person2.calculate_emp_salary(50)
person3.calculate_emp_salary(20)
person4.calculate_emp_salary(60)

#test To assign department
person2.emp_assign_department("ACCOUNTING")
person3.emp_assign_department("RESEAECH")

# To print changed data
print("------changed data------")
for num in emp_list:
    num.print_employee_details()
