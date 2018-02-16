# System Class
class System(object):
    # Declaring an global variable student id which gets incremented whenever a new student is added to system
    sid = 1

    # Declaring init constructor with name, age, section
    def __init__(self, name, age, section):
        System.sid += 1
        self.name = name
        self.age = age
        self.section = section

    # sdetails is method that prints details of newly created student with some assigned student id
    def sdetails(self):
        print("Student details from Student class: " + self.name + " details," + " age is " + str(
            self.age) + " and joined as " + self.section + " and assigned an id: " + str(System.sid))
    # Student class that Inherits System class


class Student(System):
    def __init__(self, name, age, section):
        # super calls parent class constructor i.e System class and assign values of name, age, section in student class
        super(Student, self).__init__(name, age, section)

    def sdetails(self):
        print("sdetails method in student class called")

    # smisc method that tells where the control is in
    def smisc(self):
        print("In student class")

    # getsport method tell which sport the student is playing
    def getsport(self):
        print("Student is playing: " + self.sportname)

    # Private data member that can only accessed by student class object
    def __idnum(self):
        print("This is a private data member")


# Grades class which inherits student class
class Grades(Student):
    # Declaring init constructor which take math, chemistry, physics as input from the student object
    def __init__(self, math, chemistry, physics):
        self.math = math
        self.chemistry = chemistry
        self.physics = physics

    # Marks method prints grade received by student in each of the subject
    def marks(self):
        print(
            "Student got " + self.math + " grade in mathematics, " + self.chemistry + " grade in chemistry and " + self.physics + " grade in physics ")

    # sdetails method tell which methos is called when calling from subclass method
    def sdetails(self):
        print("Method in Grades class is called")

    # finalgrade method tell the final grade
    def finalgrade(self):
        print("Student graduated with good grade")


# Enroll class that uses multiple inheritance student and system and checking which method in student or system gets called is they have same method name
class Enroll(Student, System):
    # Declaring init constructor that takes name, age, section and creates a student object
    def __init__(self, name, age, section):
        # Super keyword that call parent constructor
        super(Enroll, self).__init__(name, age, section)


# Sports class that inherits student clask
class Sports(Student):
    # Declaring init constructor which takes sportname
    def __init__(self, sportname):
        self.sportname = sportname


# grad class that multiple inherits student, system
class grad(Student, System):
    # Declaring init constructor which takes name, degree
    def __init__(self, name, degree):
        self.degree = degree
        self.name = name

    # pdetails method that prints degree and student name
    def pdetails(self):
        print("Student with name " + self.name + " graduated with " + self.degree)


# Creating Student object
name = input("Enter name: ")
age = int(input("Enter age: "))
section = input("Enter section: ")

# Creating System object from system class
sys1 = System(name, age, section)
# Calling sdetails() method using system object
sys1.sdetails()
# Creating student object using student class
s1 = Student(name, age, section)
# Calling sdetails() method using Student object
s1.sdetails()
s2 = Student(name, age, section)
s3 = Student(name, age, section)
# Creating grades object
g1 = Grades('A', 'A+', 'A')
# Calling marks() method using Grades object
g1.marks()
# Creating Enroll class object
e1 = Enroll('tim', 20, 'freshmen')
# Calling sdetails() method using Enroll object
e1.sdetails()
# Creating Sports class object
sp1 = Sports('cricket')
# Calling getsport() method using Sports object
sp1.getsport()
s1._Student__idnum()
# Creating grad class object
gd1 = grad('tim', 'masters')
# Calling pdetails() method using grad object
gd1.pdetails()