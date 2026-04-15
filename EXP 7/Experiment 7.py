class University:
    def show_result(self):
        name = input("Name: ")
        marks = input("Marks: ")
        print(f"{name} scored {marks} in Python exam")

u = University()
u.show_result()

class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

for pet in [Animal(), Dog(), Cat()]:
    pet.speak()

class Creature:
    def speak(self):
        print("Creature sound")

class Puppy(Creature):
    def speak(self):
        super().speak()
        print("Puppy: Woof Woof!")

p = Puppy()
p.speak()