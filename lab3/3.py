a, b = 35, 94
def _pairs(numhead, numlegs):
    rabbits = (numlegs / 2) - numhead
    chickens = numhead - rabbits
    print(f"There is {rabbits} rabbits and {chickens} chickens")

_pairs(a,b)