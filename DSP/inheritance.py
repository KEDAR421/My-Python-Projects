class Mamals():
    def walk(self):
        print('walk')
        print('bark')
class Dog(Mamals):
    pass
class Cat(Mamals):
    pass
dog1=Dog()
dog1.walk()