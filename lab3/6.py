text = input()
def wordRev(word):
    a = word.split()
    a = list(a)
    a.reverse()
    x = ' '.join(a)
    print(x)

wordRev(text)