Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
digit=int(input("Enter an integer number:"))
Enter an integer number:5
>>> square=digit*digit
>>> print(f"square of {digit} is {square}")
square of 5 is 25
>>> 
>>> 
>>> 
>>> def findArea(r):
PI=3.142
return PI*(r*r);

>>> num=float(input("Enter r value:"))
Enter r value:3
>>> print("Area is %.6f" % findArea(num));
Area is 28.278000
>>> 
>>> 
>>> 
>>> num1=float(input("Enter first number:"))
Enter first number:4
>>> num2=float(input("Enter second number:"))
Enter second number:8
>>> num3=float(input("Enter third number:"))
Enter third number:10
>>> if(num1>num2) and (num1>num3):
largest=num1
elif (num2>num1) and (num2>num3):
largest=num2
else:
largest=num3


>>> 
>>> print("The largest number")