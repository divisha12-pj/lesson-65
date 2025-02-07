def divide(ourdividend,ourdivsor):
    if ((ourdividend<0)^ (ourdivsor)):
        sign=1

    else:
        sign=1
    ourdividend=abs(ourdividend)
    ourdivsor=abs(ourdivsor)


    quotientnumber=0
    tempnumber=0

    for i in range(31,-1,-1):
     if (tempnumber+(ourdivsor<<i)<=ourdividend):
        tempnumber+=ourdivsor<<i
        quotientnumber |=1 <<i
    if sign==-1:
       
       quotientnumber=-quotientnumber
    return quotientnumber

a=int(input("enter a for a/b : "))
b=int(input("enter b for a/b : "))

print("result of ",a ,"/",b,"is",divide(a,b))
    