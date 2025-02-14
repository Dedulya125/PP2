#Example 1 Booleans
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Example 2 Operators
  print(10 + 5)

#Example 3 Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Example 4 Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Example 5 Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Example 6 Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

del thisdict("brand")


#Example 7 If ... Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b")

print("A") if a > b else print("B")

if not a > b:
  print("a is NOT greater than b")

#Example 8 While Loops
i = 1
while i < 6:
  print(i)
  i += 1

#Example 9 For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break