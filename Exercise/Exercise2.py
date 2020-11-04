import math

def area(rad):

    result = math.pi*(rad * rad)
    print("The area of circle is: {:.2f}" .format(result))


radius = int(input("Please provide your radius to calculate area of circle:"))

area(radius)
