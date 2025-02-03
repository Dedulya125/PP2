fahrenheit = int(input())

def _celsius(f):
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"{fahrenheit} fahrenheit is equal to {celsius} celsius")

_celsius(fahrenheit)