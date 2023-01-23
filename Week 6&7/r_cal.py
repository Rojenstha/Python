def sum(a,b):
    add=a+b
    print("The sum is",add)
def sub(a,b):
    minus=a-b
    print("The substraction is",minus)
def multi(a,b):
    into=a*b
    print("The multiplication is",into)
def div(a,b):
    divide=a/b
    print("The division is",divide)
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
cal=int(input("Enter 1 for add, 2 for substract, 3 for multiply and 4 for division:"))
if (cal==1):
    sum(a,b)
if (cal==2):
    sub(a,b)
if (cal==3):
    multi(a,b)
if (cal==4):
    div(a,b)
else:
    print("Wrong syntax")
