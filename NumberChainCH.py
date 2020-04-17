# Initial variable to track game play

    
number = 0

playing = 'y'

while playing == 'y':
    user_number = int(input("How many numbers? "))
    
    user_number += number
    
    for i in range(number, user_number):
        print(i)
        number = number + 1
        
    playing = input("Are you still playing? (y)es or (n)o ")
    
    if playing == 'n':
        break
    elif playing == 'y':
        continue
    else: 
        continue

        