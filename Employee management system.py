#-------------------------------
# employee Management System 
#-------------------------------

#this is menu
class Employee:
    @staticmethod
    def work():
        print("===============Employee Menu==============")
        print("press 1 :add_employee")
        print("press 2 :display_employee")
        print("press 3 :search_employee")        
        print("press 4 :update_employee")
        print("press 5 :delete_employee")
        print("press 6 :calculate_salary")
        print("__________________________________________")


# Add employee
    @staticmethod
    def add_employee():
        Emp_id = int(input("Enter the Emp_id: "))
        Name = input("Enter the Name: ")
        Age = int(input("Enter the Age: "))        
        Salary = int(input("Enter the Salary: "))
        print("\n- - - - - - - Employee Added Successfully - - - - - - -")

        with open("project.txt","a") as file:
            file.write(f"{Emp_id},{Name},{Age},{Salary}\n")

# Display_employee
    @staticmethod
    def display_employee():
        print(f"\n===========show the all employees details============")
        with open("project.txt","r") as file:
            print("\n{:<8}{:<15}{:<8}{:<10}".format("ID", "NAME", "AGE", "SALARY"))
            print("-" * 40)
            for line in file:
                Emp_id, Name, Age, Salary = line.strip().split(",")
                print("{:<8}{:<15}{:<8}{:<10}".format(Emp_id, Name, Age, Salary))


# Search_employee
    @staticmethod
    def search_employee():
        ID=input("Enter your Emp_id: ")
        found=False
        with open("project.txt","r") as file:
            for line in file:
                Emp_id, Name, Age, Salary = line.strip().split(",")
                if ID == Emp_id:
                    print("================This is your details=================")
                    print("\n{:<8}{:<15}{:<8}{:<10}".format("ID", "NAME", "AGE", "SALARY"))
                    print("-"*40)
                    print("{:<8}{:<15}{:<8}{:<10}".format(Emp_id, Name, Age, Salary))
                    found=True
                    break
        if not found:
            print("There are not exist in this list")


# Update_employee
    @staticmethod
    def update_employee():
        ID=input("Enter your Emp_id: ")
        found=False        
        with open("project.txt","r") as file:
            lines=file.readlines()
        with open("project.txt","w") as file:
            for line in lines:
                Emp_id, Name, Age, Salary = line.strip().split(",")
                if ID == Emp_id:
                    Name=input("Enter your Name: ")
                    Age=input("Enetr your Age: ")
                    file.write(f"{Emp_id},{Name},{Age},{Salary}\n")
                    found=True
                else:
                    file.write(line)
            if not found:
                print("Employee does't exist")
            else:
                print("================Employee updated successfully====================")         


# Delete_employee
    @staticmethod    
    def delete_employee():
        ID=input("Enter your Emp_id: ")
        found=False        
        with open("project.txt","r") as file:
            lines=file.readlines()
        with open("project.txt","w") as file:
            for line in lines:
                if not line.strip():
                    continue
                Emp_id, Name, Age, Salary = line.strip().split(",")
                if ID == Emp_id:
                    found =True
                    continue
                file.write(line)
            if found:
                print("====================Employee Delete Sucessfully======================")
            else:
                print("Employee Does't Exsit")


# Calculate_salary
    @staticmethod
    def calculate_salary():
        total_salary = 0
        with open("project.txt", "r") as file:
            for line in file:
                if not line.strip():
                    continue
                Emp_id, Name, Age, Salary = line.strip().split(",")
                total_salary += int(Salary)
            print(f"\n================Calculated Salary==================")
            print(f"Total Salary = {total_salary}")


# Menu-Driven Control Loop
while True:
    Employee.work()

    userwork=int(input("Enter the which work are perform:- "))
    if userwork ==1:
        Employee.add_employee()
    elif userwork ==2:
        Employee.display_employee()
    elif userwork ==3:
        Employee.search_employee()
    elif userwork ==4:
        Employee.update_employee()
    elif userwork ==5:
        Employee.delete_employee()
    elif userwork == 6:
        Employee.calculate_salary()
    else:
        print("Invaild Input")
    break


