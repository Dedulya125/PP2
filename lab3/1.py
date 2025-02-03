grams = int(input())

def _convert(a):
    ounces = 28.3495231 * grams
    print(f"{grams} grams is equal to {ounces} ounces")

_convert(grams)