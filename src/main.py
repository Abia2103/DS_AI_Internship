#Task 1: The Area & Perimeter Tool (Functions & Return Values)

def calc_rectangle(length, width):
    area = length*width
    peri = 2*(length+width)
    return(area,peri)

len = int(input("Enter the length of the rectangle: "))
wid = int(input("Enter the width of the rectangle: "))

ans = calc_rectangle(len, wid)
print(f"Area: {ans[0]} Perimeter: {ans[1]}")

#Task 2: The Logic Library (Custom Modules)
import math_operations

print(math_operations.power(3, 2))
print(math_operations.average([10, 20, 30, 40]))