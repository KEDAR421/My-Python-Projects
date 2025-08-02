# def leap_year(year):
#     if(year%4==0 and year % 100 !=0) or (year %400==0):
#         return True;
#     else:
#         return False
# print(leap_year(2016))
##sum of two numbers
# def table(a):
#     tab=[]
#     for i in range(10):
#         tab.append((i+1)*a)
#     return tab
# print(table(2))
#keep taking numbers till enter x

while(True):
   num=int(input("enter number= "))
   if(num=='x'):
       break
   else:
       print(num)
