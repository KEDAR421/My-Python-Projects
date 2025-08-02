try:
    age=int(input("age= "))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print('age van not be zero')
except ValueError:
    print('invalid')