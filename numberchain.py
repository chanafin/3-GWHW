
number = 0
playing = 'y'

"As long as playing = y, the loop will continue"
while playing == 'y':
    user_number = int(input("How many numbers? "))
    user_number += number
    
    "The for loop prints to the screen with the range between variable 'number' and 'user_number'"
    
    for i in range(number, user_number):
        print(i)
        "number increments by one so that all user inputs are non-repetitive"
        number = number + 1
    "The input asks the user to input the status of the variable 'playing'"  
    playing = input("Are you still playing? (y)es or (n)o ")
    
    "the script ends if playing == 'n' or continues if == 'y'"
    if playing == 'n':
        break
    elif playing == 'y':
        continue
    

        