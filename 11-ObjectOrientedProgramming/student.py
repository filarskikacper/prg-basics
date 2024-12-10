# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.number = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.number = 1
    student2.name = "Olivia"
    student2.age = 21
    student2.number = 2
    student3.name = "Pawel"
    student3.age = 20
    student3.number = 3

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.number}. {student1.name}, {student1.age} years old')
    print(f'{student2.number}. {student2.name}, {student2.age} years old')
    print(f'{student3.number}. {student3.name}, {student3.age} years old')

if __name__ == "__main__":
    main()