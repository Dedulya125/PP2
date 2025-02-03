def _primeNumber(num):
    deliteli = 0
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            deliteli +=1
    if deliteli >= 1:
        return False
    else:
        return True

def _findprime(nums):
    primeNums = []
    for i in range(len(nums)):
        if _primeNumber(int(nums[i])):
            primeNums.append(nums[i])
    print(primeNums)

a = list(input().split())
_findprime(a)