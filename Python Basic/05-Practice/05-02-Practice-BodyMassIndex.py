weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

bmi = weight_kg / (height_m ** 2)

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 24.9:
    bmi_category = "Normal weight"
elif bmi < 29.9:
    bmi_category = "Overweight"
else:
    bmi_category = "Obesity"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {bmi_category}")
