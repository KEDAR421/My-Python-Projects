#  #and or operator
# has_reach=False
# has_high_income=False
# if has_reach or has_high_income:
#      print("pay tax")
# else:
#     print("can not pay")
# name=input("enter your name:- ")
# print(name)
# num=int(len(name))
# if (num<3):
#     print('name must be at least 3 character')
# elif(num>50):
#     print('name is too maximum')
# else:
#     print("name looks good")
#kg to lb or lb to kg
weight=input("enter your weight=")
type=input("(L) bs (K) g:")
if (type=='K' or 'k'):
    print('weight in lb is=',2.204*int(weight))
elif(type=='L' or 'l'):
    print('lb in kg =',0.4535*int(weight))

