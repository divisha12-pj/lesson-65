def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print("After swapping first number is ",a)
    print("after swapping second number is",b)

num1=int(input("enter first number"))
num2=int(input("enter second number"))
print("before swapping first number is ",num1)
print("before swapping second number is",num2)



swap(num1,num2)

def swap1(a,b):
       
       a=a+b
       b=a-b
       a=a-b
       print("After swapping first number is ",a)
       print("after swapping second number is",b)

swap1(20,30)