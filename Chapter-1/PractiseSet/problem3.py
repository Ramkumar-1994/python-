import os

directory_path='/'

content=os.listdir(directory_path)
print(content)

for item in content:
  print(item)