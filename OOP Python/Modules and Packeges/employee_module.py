print("Employee module is starting...")

company = "OpenAI"

employees = ["Alice", "Bob", "Charlie"]


def print_employee(name):
    print(f"Employee: {name}")


def count_employees():
    return len(employees)


class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")


print("There are", count_employees(), "employees.")

print_employee("Administrator")

print("Employee module finished.")




print("Loading database...")

db = []


def connect():
    print("Connecting...")


class User:

    print("Inside class definition")

    country = "Pakistan"

    def __init__(self, name):
        print("Creating object")
        self.name = name


print("Module loaded")