# A programme that calculates the total number of books bought by a user

user_input = int(input('How many books did you buy?'));

total_price = 0
for i in range(user_input):
    price = int(input(f'What is the price of book {i +1}?'))
    total_price += price #This is like saying total_price = total_price + price
print(f'The total price for your {user_input}books is: {total_price}');        
