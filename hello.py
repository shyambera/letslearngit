a = int(input("enter number a:"))
b = int(input("enter number b:"))
c = int(input("enter number c:"))
if a<=b:
    if a<=c:
        print("minimum is a:")
    else:
        print("minimum is c:")
elif b<=c:
        print("minimum is b:")
else:
        print("minimum is c:")
