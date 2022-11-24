#!/usr/bin/python3
'''Learning how to object oriented programming in python3'''
class Person:
    def __init__(self, name, age, height, weight, color, gender, parent):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.color = color
        self.gender = gender
        self.parent = parent


    def say_hi(self):
        print("hello, my name is", self.name)
        print("hello, I'm", self.age)
        print("hello, my height is", self.height)
        print("hello, my weight is", self.weight)
        print("hello, my skin color is", self.color)
        print("hello, my gender is", self.gender)
        print("hello, my parents are", self.parent)

p = Person("Sunday", "21 years old", "5.8h", "80kg", "dark", "Male", "Mr & Mrs Obasi")
p.say_hi()
#The previous 2 line can also be written as this
# You can also do it like the Person("Sunday", "21 years old", "5.8h", "80kg", "dark", "Male", "Mr & Mrs Obasi").say_hi()

class Robot:
    """Represent a robot, with a name."""
    # A class variable, counting the number of robots 
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # Add to the population

        Robot.population += 1

    def die(self):
        """I am dying"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots workings.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot yeah, they can do that"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """prints the current population."""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi
Robot.how_many

print("\nRobots can do some work here\n")

print("Robot have finished their work. So let's destroy them.")

droid1.die()
droid2.die()

Robot.how_many()

class SchoolMember:
    """Represents any school member"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    
    def tell(self):
        """tell my detail"""
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mr. Aaron', 40, 30000)
s = Student('Sunday', 25, 75)
# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()


# How to an write class square that defines a square

