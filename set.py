#Create empty set

s = set()

#add element

s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)

#add 3 (value that already exist)

s.add(3)
print(s)

#remove one value
s.remove(2)
print(s)

#show length

print(f"The set has {len(s)} elements")
