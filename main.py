# implement add() to ask users to enter information about employee records,
# including their EID, Name, Age, and Rating.  Create an index file at the same time by using EID as
# primary key and RRN as reference.


class Employee:
    def __init__(self, name, age, salary, rating):
        self.name = name
        self.age = age
        self.salary = salary
        self.rating = rating


# store the employee information in a fixed-length record file.
def add():
    eid = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    salary = input("Enter Salary: ")
    rating = input("Enter Rating: ")
    Employee(name, age, salary, rating)
    # emp.display()
    # write the employee information to the file
    with open("employee.txt", "a") as f:
        f.write(
            eid + " " + name + " " + age + " " + salary + " " + rating + "\n")
    # create an index file
    with open("index.txt", "a") as f:
        f.write(eid + " " + str(f.tell()) + "\n")


# search the index file to find the record number of the employee record
# and then use this record number to locate the employee record in the employee file.
def search():
    eid = input("Enter Employee ID: ")
    with open("index.txt", "r") as f:
        for line in f:
            if eid == line.split()[0]:
                print("Found")
                rrn = line.split()[1]
                print("RRN: ", rrn)
                with open("employee.txt", "r") as f:
                    for line in f:
                        if line.split()[0] == eid:
                            print("Employee ID: ", line.split()[0])
                            print("Name: ", line.split()[1])
                            print("Age: ", line.split()[2])
                            print("Salary: ", line.split()[3])
                            print("Rating: ", line.split()[4])
                            break
                break
            else:
                print("Not Found")


if __name__ == "__main__":
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "3":
        exit()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "3":

        def display(self):
            print("Name: ", self.name)
            print("Age: ", self.age)
            print("Salary: ", self.salary)
            print("Rating: ", self.rating)

employees = []


# def add():
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     salary = input("Enter salary: ")
#     rating = input("Enter rating: ")
#     new_employee = Employee(name, age, salary, rating)
#     employees.append(new_employee)


# def display():
#     for employee in employees:
#         employee.display()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     add()
#     display()
