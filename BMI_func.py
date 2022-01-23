def get_user_data():
    while True:
        try:
            user_name = input('Enter user name:')
            if len(user_name) < 2:
                print('User name must be at least 2 characters long!')
                continue
            break
        except ValueError as error:
            print('Not a proper string! Enter again')
    
    while True:
        try:
            height = float(input('Enter height in meters:'))
            if height < 50 or height > 250:
                print('Number not in range [50-250]. Enter number in range!')
                continue
            break
        except ValueError as error:
            print('Not a proper number! Enter again')
    
    while True:
        try:
            weight = float(input('Enter weight in kilogram:'))
            if weight < 5 or weight > 300:
                print('Number not in range [5-300]. Enter number in range!')
                continue
            break
        except ValueError as error:
            print('Not a proper number! Enter again')
    
    result = dict()
    result['name'] = user_name
    result['height'] = height
    result['weight'] = weight

    return result

def cm_to_meters(cm):
 return cm / 100

def calc_BMI(w,h):
  return w / (h * h)

def calc_BMI_category(bmi):
    if(bmi < 16):
        return 'Severe Thinness'
    elif (bmi < 17):
        return 'Moderate Thinness'
    elif (bmi < 18.5):
        return 'Mild Thinness'
    elif (bmi < 25):
        return 'Normal'
    elif (bmi < 30):
        return 'Overweight'
    elif (bmi < 35):
        return 'Obese Class I'
    elif (bmi < 40):
        return 'Obese Class II'
    elif (bmi >= 40):
        return 'Obese Class III'


def print_results(bmi_category):
  print(f'The body mass index (BMI) of is: {bmi_category}')


user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],cm_to_meters(user_data["height"]) )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)
