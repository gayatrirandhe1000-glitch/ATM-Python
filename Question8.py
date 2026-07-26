# Calculate the BMI of a person given their weight in kilograms and height in meters.
w = float(input("Enter your weight in kilograms: "))
h = float(input("Enter your height in meters: "))
bmi = w / (h * h)
print(f"Your BMI is {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")
else:
    print("Invalid BMI value.")