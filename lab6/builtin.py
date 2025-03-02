# task 1
nums = [1, 2, 3, 4, 5]
x = '*'.join(str(i) for i in nums)
print(eval(x))

# task 2
string = input()
cntup = 0
cntlow = 0
for i in string:
    if i.isupper():
        cntup += 1
    elif i.islower():
        cntlow += 1
print("Uppercase letters: ",cntup)
print("Lowercase letters: ",cntlow)

# task 3
string = input()
if string == string[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")

# task 4
import time 
num = int(input())
milisec = int(input())
sec = milisec/1000
time.sleep(sec)
sqrt = num ** 0.5
txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(fnum = num, fsec = milisec, fsqrt = sqrt)
print(txt)

# task 5
mytuple = (True, True, False)
mytuple2 = (True, True, True)
print(all(mytuple))
print(all(mytuple2))