ADD = ['+', 'plus',]
SUBTRACT = ['-', 'minus',]
MULTIPLY = ['*', 'multiply', 'x']
DIVIDE = ['/', 'divide',]


expression = text


expression = expression.lower().split()

expression_left = expression[0]
expression_middle = expression[1]
expression_right = expression[2]

answer = None

if expression_middle in ADD:
    answer = int(expression_left) + int(expression_right)
if expression_middle in SUBTRACT:
    answer = int(expression_left) - int(expression_right)
if expression_middle in MULTIPLY:
    answer = int(expression_left) * int(expression_right)
if expression_middle in DIVIDE:
    answer = int(expression_left) / float(expression_right)

result = str(answer)
return f'Result of, {text} is {result}'