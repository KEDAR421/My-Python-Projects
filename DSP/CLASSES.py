# class Point:
#     def move(self):
#         print('move')
#     def draw(self):
#         print('draw')
#
# point1=Point()
# point1.x=10
# point1.y=20
# print(point1.x)
# point1.draw()
class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi, i am {self.name}")

john=Person('kedarnath')
print(john.name)
john.talk()

bob=Person('jaanii')
bob.talk()