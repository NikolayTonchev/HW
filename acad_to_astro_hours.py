# Define class Hours
class Hours:
    # Define Set Methods and validate
    def set_Astronomical_Hours(self, Astronomical_Hours_Value):
        if isinstance(Astronomical_Hours_Value, int) and Astronomical_Hours_Value in range(0,61):
            self._Astronomical_Hours = Astronomical_Hours_Value
        else:
            print('Wrong definition of Minutes per Astronomical hour. Check your code!')
            quit()
    def set_Academical_Hours(self, Academical_Hours_Value):
        if isinstance(Academical_Hours_Value, int) and Academical_Hours_Value in range(0,61):
            self._Academical_Hours = Academical_Hours_Value
        else:
            print('Wrong definition of Minutes per Academical hour. Check your code!')
            quit()
    def set_Breaks(self, Breaks_Value):
        if isinstance(Breaks_Value, int) and Breaks_Value in range(0,61):
            self._Breaks = Breaks_Value
        else:
            print('Wrong definition of Minutes per Break. Check your code!')
            quit()

    # Define method to convert hours 
    def ConvertHours(self, Course_Hours):
        # The assumption is that after each 3 academical hours there is a following 15 minutes break.
        result = ( ( Course_Hours * self._Academical_Hours ) + ( int(Course_Hours / 3) * self._Breaks ) ) / self._Astronomical_Hours
        return result

# Try-Except block for handling of ValueError
while True:
    try:
        Academical_Hours = int(input('Enter academical hours:'))
        if Academical_Hours < 0:
            print('Please enter positive integer, try again')
            continue
        break
    except ValueError as error:
        print('Not a proper integer! Enter again')

# Create an object of class Hours
MyHours = Hours()

# Call set methods and define how many minutes has each type
MyHours.set_Astronomical_Hours(60)
MyHours.set_Academical_Hours(40)
MyHours.set_Breaks(15)

# Call ConvertHours method from class Hours()
result = MyHours.ConvertHours(Academical_Hours)

# Change the output in hours / minutes format
if result % 1 == 0:
    output = int(result)
    print(f'Astronomical Hours: {output} hours')
else:
    output_hours = int(result)
    output_minutes = round(result % 1 * 60)
    print(f'Astronomical Hours: {output_hours} hours {output_minutes} minutes')