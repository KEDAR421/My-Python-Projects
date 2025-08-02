#1 is neither prime nor a composite number.
print('prime number:-')
n=int(input("enter a number upto which you want to print the prime numbers="))
i=2
while(i<=n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
    i=i+1

#by function
print("prime number by function:-")
def prime(n):
    i=2
    while(i<n):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
        i=i+1
print(prime(n))