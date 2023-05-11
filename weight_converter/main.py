# weight converter in Python

print("This program will take a weight measurement in Kilograms or Pounds")
print("It will then convert the weight into the opposite unit and display it")
print()

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {weight} {unit}")