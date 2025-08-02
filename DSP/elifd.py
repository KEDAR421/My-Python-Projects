age=int(input('enter your age= '))
print(age)
if(age<12):
    print('you are child')
    if(age<5):
        print('you abe baby')
elif(age>=12 & age<19):
    print('teen ager')
    if(age<16):
        print('high school student')
    else:
        print('college student')
elif(age>=19 & age<60):
    print('adult')
else:
    print('old')