n=int(input("Enter the number:"))

for i in range(1,n):
  if((n==2 ) or (n%i!=0)):
    print("Prime")
  else:
    print("Not Prime")