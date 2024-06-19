#OOP

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

teacher1 = Teacher("Alya", 37)
teacher2 = Teacher("Devan", 45)

teacher1.display_info()
teacher2.display_info()