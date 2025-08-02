number=[2,4,5,12,8,91,2,3,11]
# number.append(5)
# number.append(89)
# print(number)
new_number=[]
for num in number:
    if num not in new_number:
        new_number.append(num)
print(new_number)
#duplicate numbers removed