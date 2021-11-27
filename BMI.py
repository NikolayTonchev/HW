# Define method for calculation of BMI
def BMI_Calc(Weight, Height):
    return Weight / ( Height * Height )

# Try-Except block for handling of ValueError & negative input of Weight
while True:
    try:
        Weight = float(input('Enter weight in kilogram:'))
        if Weight < 0:
            print('Please enter positive number, try again')
            continue
        break
    except ValueError as error:
        print('Not a proper number! Enter again')

# Try-Except block for handling of ValueError & negative input of Height
while True:
    try:
        Height = float(input('Enter height in meters:'))
        if Height < 0:
            print('Please enter positive number, try again')
            continue
        if Height > 3:
            print('You have entered too big number! Please make sure your input is in meters')
            continue
        break
    except ValueError as error:
        print('Not a proper number! Enter again')

# Call BMI_Calc method
result = BMI_Calc(Weight, Height)

# Print results
print(f'The body mass index (BMI) is: {round(result,2)}')