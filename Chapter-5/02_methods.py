marks={
  "harry":100,
  "Rohan":56,
  "Shubham":23
}

print(marks.items())    #values of keysand values in form of tuple
print(marks.values())   #values of dictionary
print(marks.keys()) # shows the keys of dictionary

marks.update({"Renuka":98,"Harry":50})

print(marks)

print(marks.get("renuka"))  #returns None
# print(marks["renuka"])  #returns error

print(marks)
# marks.clear()
marks.pop("harry")

print(marks)