num = int(input("Enter your salary in INR"))
num1 = num + (10/100)*num
num2 = num + (20/100)*num
num3 = num + (40/100)*num
if(num<=10000):
    print("your salary is",num1)
elif(num >10000 and num <=20000):
    print("you salary is",num2)
elif(num>20000):
    print("your salary is ",num3)
else:
    print("you are fired")