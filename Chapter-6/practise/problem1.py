num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
num4=int(input("Enter number 4:"))

greatest_number=0

if(num1>num2 and num1>num3 and num1>num4):
  greatest_number=num1

elif(num2>num1 and num2>num3 and num2>num4):
  greatest_number=num2

elif(num3>num1 and num3>num2 and num3>num4):
  greatest_number=num3

else:
  greatest_number=num4

print("The greatest Number is ",greatest_number)