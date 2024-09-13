spam=['make a lot of money','buy now','click this','subscribe this']

message=input("enter your comment:").lower()


if (message in spam):
  print("Found Spam")
  
else:
  print(message)