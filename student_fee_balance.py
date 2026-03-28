# Student fee balance

user_total_fee = float(input('Enter the total fee: '));
user_paid_fee = float(input('Enter the paid fee: '));

user_balance_fee = user_total_fee - user_paid_fee;
print(f'Your balance is: {user_balance_fee}.')