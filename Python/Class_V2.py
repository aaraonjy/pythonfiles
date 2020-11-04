class Student():

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def getData(self):
        return '\n'.join(( '{} = {}' .format(item, self.__dict__[item]) for item in self.__dict__))

# Create List to store multiple Objects from User Input
students = []

# Determine Size of List
numberofstudents = int(input("Enter Number of Students: "))

for x in range(numberofstudents):

    print("\nEnter Person {} Details".format(x+1))

    name = str(input("Enter Name: "))
    age = int(input("Enter Age: "))

    # Create Student Object
    collectedstudents = Student(name, age)

    # Store Student Object into List
    students.append(collectedstudents)

# Print Student Object with formatting

for collectedstudents in students:
    print(collectedstudents.getData())
