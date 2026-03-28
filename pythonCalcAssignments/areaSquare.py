# A programme that finds the area of a square

user_input = int(input('How do you wish to find the area of your square? \n1: with its length? \n2: with the diagonal?'));

if user_input == 1: 
 length = int(input('What is the length?'))
 print(f'You inputted {length}. Area = {length**2}')  
elif user_input == 2: 
 length_two = int(input('What is the diagonal?')) 
 print(f'You inputted {length_two}. Area = {(length_two**2) /2}');
else:
    print('Invalid input. \nRe-run the code!');