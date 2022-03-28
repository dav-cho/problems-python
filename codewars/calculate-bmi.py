##
#### Calculate BMI (8 kyu)
##############################


def bmi(weight, height):
    bmi = weight / height**2
    responses = ["Underweight", "Normal", "Overweight", "Obese"]

    return responses[(bmi > 18.5) + (bmi > 25) + (bmi > 30)]


print(bmi(50, 1.80))  # "Underweight"
print(bmi(80, 1.80))  # "Normal"
print(bmi(90, 1.80))  # "Overweight"
print(bmi(110, 1.80))  # "Obese"
print(bmi(50, 1.50))  # "Normal"
