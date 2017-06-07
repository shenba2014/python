class Student:
    __name = ""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


if __name__ == "__main__":
    student = Student("leo")
    print(student.getName())
