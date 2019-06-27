from math import sqrt
n = 600851475143

# Функция определяет является ли число x простым, перебирая все значения от 2
# до корня из x, т.к.
def is_simple(x):
    result = True
    for i in range(2, round(sqrt(x))):
        if x % i == 0:
            result = False
            break
    return result

#Выводит на печать максимальное значение из списка всех простых делителей n
print(max([x for x in range(2, round(sqrt(n))) if n % x == 0 and is_simple(x)]))
