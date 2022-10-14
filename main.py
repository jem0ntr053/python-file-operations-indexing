__author__ = "Jonathan Montrose"
__version__ = "1.0.1"
__maintainer__ = "Jonathan Montrose"
__email__ = "jem118@shsu.edu"

# This program will allow the user to add, search, and delete employee records.


class Employee:
    def __init__(self, name, age, salary, rating):
        self.name = name
        self.age = age
        self.salary = salary
        self.rating = rating


def add():
    eid = input("Enter Employee ID: ").ljust(5)[:5]
    name = input("Enter Name: ").ljust(20)[:20]
    age = input("Enter Age: ").ljust(2)[:2]
    salary = input("Enter Salary: ").ljust(7)[:7]
    rating = input("Enter Rating: ").ljust(2)[:2]
    Employee(name, age, salary, rating)

    # write the employee information to the file in fixed-length record format
    with open("employee.txt", "a") as f:
        f.write(
            eid + " " + name + " " + age + " " + salary + " " + rating + "\n")
    # create an index file
    with open("index.txt", "a") as f:
        f.write(eid + " " + str(f.tell()) + "\n")


# implement search() to search for an employee record in the employee file using
# the index file
def search():
    search_eid: str = input("Enter Employee ID: ")
    with open("index.txt", "r") as f:
        for line in f:
            if search_eid == line.split()[0]:
                print("Found")
                rrn = line.split()[1]
                print("RRN: ", rrn)
                with open("employee.txt", "r") as f:
                    for line in f:
                        if line.split()[0] == search_eid:
                            print("Employee ID: ", line.split()[0])
                            print("Name: ", line.split()[1])
                            print("Age: ", line.split()[2])
                            print("Salary: ", line.split()[3])
                            print("Rating: ", line.split()[4])
                            break
                break
        else:
            print("Not Found")


# implement delete() to delete an employee record from the employee file using
# the index file
def delete():
    delete_eid = input("Enter Employee ID: ")
    index = []
    with open("index.txt", "r") as f:
        for line in f:
            if delete_eid == line.split()[0]:
                print("Found")
                rrn = line.split()[1]
                print("RRN: ", rrn)
                with open("employee.txt", "r") as f:
                    for line in f:
                        if line.split()[0] == delete_eid:
                            print("Employee ID: ", line.split()[0])
                            print("Name: ", line.split()[1])
                            print("Age: ", line.split()[2])
                            print("Salary: ", line.split()[3])
                            print("Rating: ", line.split()[4])
                            break
                break
        else:
            print("Not Found")

    with open("index.txt", "r") as f:
        for line in f:
            if delete_eid != line.split()[0]:
                index.append(line)
    with open("index.txt", "w") as f:
        for line in index:
            f.write(line)

    employee = []
    with open("employee.txt", "r") as f:
        for line in f:
            if delete_eid != line.split()[0]:
                employee.append(line)
    with open("employee.txt", "w") as f:
        for line in employee:
            f.write(line)


# Main function
if __name__ == "__main__":
    print("Employee Record Management System")
    print("==================================")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Delete Employee")
    print("4. Exit")
    print("==================================")
    choice = ""
    while choice != "4":
        choice = input("Enter your choice: ")
        if choice == "1":
            add()
        elif choice == "2":
            search()
        elif choice == "3":
            delete()
        elif choice == "4":
            print("Exit")
        else:
            print("Invalid choice")
