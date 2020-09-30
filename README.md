These are some entry-level Python exercises that explore key concepts that can be expanded upon.

Fiber Search - this exercise combines the practices of reading in an external CSV file, looping and using an f-string, all of which are extremely useful for exploring large datasets in a uniform and automated way. The first step is to identify, open and read the CSV the user wishes to explore. The next step calls  for the creation of a for loop which runs through the entire csv.reader variable (in this case, cereal_reader). Variables within the loop are created which represent specific columns and extrable data (index 0 (name of the cereal) and index 7 (fiber count)). An if statement is constucted that prints the name of the cereal and its corresponding fiber count if the condition of having a fiber value larger than or equal to five is met.

Number Chain - this represents the introduction of two new, very important Python concepts: a While Loop and User Input. The variable number is instatiated as zero and the variable 'playing' is instatiated as equal to 'y'. While 'playing' is equal to 'y', the variable 'user number'  will push the input prompt "How many numbers?" User number will then be added to the variable number, which starts at zero, but will both increase as the loop continues and persist within the loop. A for loop is then created which iterrates through the range between the variable number and the variable user number. The iterrator is printed to the screen. The variable number is then increased by one so that if the while loop continues, there will be no repetitive integers and creates an uninterrupted 'chain' of numbers. The variable playing will push another input prompt "Are you still playing (y)es or (n)o." If the variable playing is equal to 'n', the script breaks and ends. If playing is equal to 'y', the script loops again and the current value of 'number' persists.

Vote Machine - This the first involved Python exercise I have completed. The exercise combines the above concepts and includes the concept of appending to an empty list and then measuring the length and subsequently determining the maximum value of each list's length, using the len and max functions. 

The first step involves creating five empty lists. Each candidate has an empty list where votes for that respective candidate will be appended, along with an empty list for all votes. 

The next step is to join, open and read the CSV file that will be used, in this case, election result data. 

A for loop is constructed that will iterrate through the entire CSV and the candidate and vote id columns are identified. Each

Even though I now understand more elegant solutions, I will leave as-is.






