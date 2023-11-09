# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

bmi = weight/(height**2)

if (bmi < 18.5):
    print(f'Your BMI is {bmi}, you are underweight.')
if (bmi >18.5 and bmi<25):
    print(f'Your BMI is {bmi}, you have a normal weight.') 
if (bmi >25 and bmi <30):
    print(f'Your BMI is {bmi}, you are slightly overweight.')
if (bmi >30 and bmi <35):
    print(f'Your BMI is {bmi}, you are obese.')
if (bmi > 35):
    print(f'Your BMI is {bmi}, you are clinically obese.')
              


# he testing code will check for print output that is formatted like one of the lines below:

# "Your BMI is 18.28678, you are underweight."
# "Your BMI is 22.0, you have a normal weight."
# "Your BMI is 28.50752, you are slightly overweight."
# "Your BMI is 32.56189, you are obese."
# "Your BMI is 37.50000, you are clinically obese."
# Example Input 2