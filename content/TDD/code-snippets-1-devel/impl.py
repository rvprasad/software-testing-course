def type_of_triangle(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        raise RuntimeError()

    if x + y <= z or x + z <= y or y + z <= x:
        return "Not a triangle"
        
    if x == y == z:
        return "equilateral"
        
    if x == y or x == z or y == z:
        return "isoceles"
    
    return "scalene"

