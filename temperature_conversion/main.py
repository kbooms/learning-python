
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

degrees = chr(176)

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature is Fahrenheit is: {temp}{degrees}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius: {temp}{degrees}C")
else:
    print(f"{unit} is invalid unit of measurement")