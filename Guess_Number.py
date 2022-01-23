from random import randint

max_n = 5
start  = 1
end = 10

rand_number = randint(start, end)
guessed = False
n = 1

while n <= max_n:
    while True:
        user_number = int(input('Enter a number: '))
        if ( start <= user_number <= end):
            break
        else:
            print("Enter a number in [{}, {}]".format(start, end))

    if user_number == rand_number:
        guessed = True
        break
    elif user_number < rand_number:
        print("Your number is less than mine.")
    else:
        print("your number is greater than mine.")
    n += 1

if guessed:
    print('You guessed')
else:
    print('You do not guessed')
