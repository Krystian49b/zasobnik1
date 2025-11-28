operator = input('what is your operator? (+ - * /')
num1 = float(input('what is your first number? '))
num2 = float(input('what is your second number?'))
num3 = float(input('what is your third number?'))
num4 = float(input('what is your fourth number?'))
if operator == "+":
   result = num1 + num2 + num3 + num4
   print(result)
elif operator == '-':
    result =  num1 - num2
    print(result)
elif operator == '*':
   result = num1 * num2
   print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print(f'{operator} is invalid')