def aveg(a=9,b=4):
    print("avg=",(a+b)/2)
aveg()
aveg(4,6)
aveg(9)#it gives the value of a
aveg(b=6)
def name(fname,mname='kedar',lname='aju'):
    print('hello ',fname,mname,lname)
    return (fname,mname,lname)
c=name('jj','gd','dd')
print(c)


def aveargw(*number):
    sum=0
    for i in number:
        sum=sum+1
        return sum/len(number)
c=aveargw(2,5,1,8,5)
print(c)