# A programme that solves a quadratic expression

print(f'This programme solves this quqdratic expression: x\u2076 + 9 / 3y');
x = int(input('Input the value of x?'));
y = int(input('What is the value of y?'));

print(f'You gave \'{x}\' as the value of x, and \'{y}\' as the value of y. \nSo: {x}\u2076 + 9 / 3y is = {(x**6) + (9 / (3*y))}');