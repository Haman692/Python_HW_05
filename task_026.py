# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def deg(numberA, numberB):


    if numberB == 1:
        return numberA
    return numberA * deg(numberA, numberB - 1)

number1 = int(input('Введите число: '))
number2 = int(input('Введите степень: '))
print(deg(number1, number2))