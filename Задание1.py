print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
print('Сумма этих чисел:', a + b)
print('Разность этих чисел:', a - b)
print('Произведение этих чисел:', a * b)
print('Среднее арифметическое этих чисел:', ((a + b)/2))
print('Частное этих чисел', (round((a / b), 2)))

if b < 0:
    b = b * (-1)
if a < 0:
    a = a * (-1)

if b > a:
    print('Разность максимального и минимального по модулю:', b - a)
elif a > b:
    print('Разность максимального и минимального по модулю:', a - b)
elif a == b:
    print('Разность максимального и минимального по модулю:', 0)

