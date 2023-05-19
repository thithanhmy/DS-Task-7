# DS-Task-7


total = 0
count = 0

# While loop repition structure to implement program.
while True:
    user_input = input('Please enter a number (-1 to stop): ')
    if user_input == '-1':         
        break

    try:
        user_input = int(user_input)        #place int() here because of ValueError control below
        total += user_input
        count += 1
    except ValueError:      #built in python control if int() doesn't work on user_input.
        print('Please enter an integer.')       #programme request to type in integer.

if count > 0:
    average = total / count
    print(f'The average of the numbers entered is {average}.')
