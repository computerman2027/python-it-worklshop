p=float(input("enter principal : "))
r=float(input("enter interest : "))
t=float(input("enter years : "))

i=(p*r*t)/100
amt=p+i

print("Interest = ",round(i,2))
print("Total amount = ",round(amt,2));
