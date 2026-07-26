# Write a program to know if the triaangle is isosceles, equilateral or scalene
s1 = int(input("Enter frist side of triangle:"))
s2 = int( input("Enter second side of triangle:"))
s3 = int(input("Enter third side of triangle:"))
if s1 ==s2 and s2 ==s3:
    print("The triangle is equilateral")
elif s1 ==s2 or s2 == s3 or s3 == s1:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")
peri= s1+s2+s3
print(f"The perimeter of triangle of sides {s1}, {s2}, {s3} is {peri}")
