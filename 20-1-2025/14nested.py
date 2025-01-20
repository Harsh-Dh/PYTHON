#nested if else
num=int(input("Enter any Number "))
if(num<0):
    print("Number is Neagtive")
elif(num>0):
    if(num<=10):
        print("Number is between 1 to 10")
    elif(num>10 and num<=20):
        print("Number is between 11 to 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")