print('This is Calculator!\n'
      ' Let\'s start')

a = int(input('Enter first number (a): '))
b = int(input('Enter second number (b): '))
action = input('Choose operation:\n'
               '    1.  a + b\n'
               '    2.  a - b\n'
               '    3.  a * b\n'
               '    4.  a / b\n'
               '    5.  a ** b\n')

if '1' in action:
    result = a + b
elif '2' in action:
    result = a - b
elif '3' in action:
    result = a * b
elif '4' in action:
    result = float(a / b)
elif '5' in action:
    result = a ** b

print('Результат равен: ', result)