def isPal():
    if word == word[::-1]:
        return True
    else:
        return False


word = input()

print(isPal())