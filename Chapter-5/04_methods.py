s={1,5,32,54,5,5,5,"Harry"}
print(s)
s.add(5666)
print(s)

'''
Sets are unordered
Does not allow Duplicates
Cannot access the index
'''
print(len(s))
s.remove(5)

print(s)

s.pop()
print(s)

s.clear()
print(s)

myset={1,2,3}
new_set=myset.copy()
new_set.add(4)
print(new_set)
print(myset)
new_set.discard(4)
print(new_set)

my_set = {1, 2}
my_set.update([3, 4], {5, 6})
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
