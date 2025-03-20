import math

def square(side):
    area = side * side
    if not (isinstance(side, int) 
            or (isinstance(side, float) and side.is_integer())):
        return math.ceil(area)
    return area
print(square(5))
print(square(5.0))
print(square(5.3))
print(square(5.5))
print(square(3))
print(square(3.9))