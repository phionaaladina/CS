import math
#using a function, create a function that calculates the volume of a cylinder.

# V = πr2h

radius = float(input('cylinder radius: '))

height = float(input('cylinder height: '))

cylynder_volume =  math.pi*radius**height

print(f'The volume of the cylinder with radius {radius} cm and height {height}cm  is {cylynder_volume} cm')