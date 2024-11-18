print("Select the operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
n=int(input("choose operation:"))
if n==1:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    add=a+b
    print("sum= ",add)
elif n==2:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    sub=a-b
    print("Difference=",sub)
elif n==3:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    multi=a*b
    print("Product=",multi)
elif n==4:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    div=a/b
    print("Quotient=",div)
else:
   print("Invalid operation")



