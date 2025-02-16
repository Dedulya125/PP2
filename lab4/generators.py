#Ex 1
def square_generator(num):
    for i in range(1, num + 1):
        yield i ** 2

num = int(input())
squares = square_generator(num)
for square in squares:
    print(square)

#Ex 2
def evens(num):
    
    for x in range(1, num + 1):
        if(x % 2 == 0):
            yield x
      
num = int(input())

evens = evens(num)

for even in evens:
    print(even)

#Ex 3
def div(num):
    
    for x in range(1, num + 1):
        if(x % 3 == 0 and x % 4 == 0):
            yield x
    
num = int(input())

nums = div(num)

for x in nums:
    print(x)

#Ex 4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)

#Ex 5
def countdown(num):
    while num >= 0:
        yield num
        num -= 1

num = int(input())

for i in countdown(num):
    print(num)