price=1000000;
is_good_credit=True;
if is_good_credit:
    price=price-(10/100)*100
else:
    price=price-(20/100)*100
print(price)