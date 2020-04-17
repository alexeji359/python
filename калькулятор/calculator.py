import colorama
from colorama import Back


a = int(input('Выберите первое число '))
dei = str(input('Что делать : *, /, -, +, найти остаток от деления, возвести в степень или найти факториал? '))


    

if dei == '*' or dei == '/' or dei == '-' or dei == '+' or dei == 'найти остаток от деления' or dei == 'возвести в степень':
    b = int(input('Выберите второе число '))

if dei == '*':
    print(int(a * b))

if dei == '/':
     c = a / b

if dei == '-':
    c =  a - b

if dei == '+':
    c = a + b

if dei == 'найти остаток от деления':
    c = a % b

if dei == 'возвести в степень':
    c  =  a ** b
    
if dei == 'найти факториал':
    res = 1
    for i in range(1, a + 1):
        res *= i
    c = res
print(c) 
    
        
        

    
    
