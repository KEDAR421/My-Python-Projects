import random
from pathlib import Path

# for i in range(3):
#     print(random.random())
for i in range(3):
    print(random.randint(10,20))
#for the selection of leader
member=['kedar','sada','aju','bara','daya','raju','keshar']
captain=random.choice(member)
print(captain)

#for dice
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second

dice=Dice()
print(dice.roll())


path=Path()
for file in path.glob('*'):
    print(file)