# lib/person.py

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hello World!")

    def walk(self):
        print(f"{self.name} is walking.")
