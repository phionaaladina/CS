# The volume of a sphere with radius r is (4/3)* pie * r**3. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places

import math

# Function to calculate the volume of a sphere
def calculate_volume():
    # # Get radius input from the user
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4/3) * math.pi * radius**3
    # Display the volume rounded to 2 decimal places
    print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")
calculate_volume()



