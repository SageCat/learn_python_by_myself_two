class Human(object):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def print_info(self):
        print("info is ", self.name, self.gender, self.age)


class Student(Human):
    def __init__(self, name, gender, age, height):
        super(Student, self).__init__(name, gender, age)
        self.height = height

    def print_info(self):
        print("info is ", self.name, self.gender, self.age, self.height)


s = Student(age=23, name="Sage", gender="Female", height=1.34)
s.print_info()
print(s)
