class Person:
    def walk(self):
        print(f"Person is walking!")
    
    def talk(self):
        print(f"Person is talking!")

class Teacher(Person):
    def teach(self):
        print(f"Teacher is teaching!")

class Student(Person):
    def study(self):
        print(f"Students are studying!")

teachers = Teacher()
teachers.walk()
teachers.talk()
teachers.teach()

students = Student()
students.walk()
students.talk()
students.study()