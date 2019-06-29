from math import sqrt, ceil

'''Проверяет является ли число простым методом перебора всех чисел от 2 до квадратного корня из num и нахождения
остатка от деления'''
def check_simple(num):
    if num == 2:
        return True

    if num < 2 or num % 2 == 0:
        return False

    result = True
    for x in range(2, ceil(sqrt(num)) + 1):
        if num % x == 0:
            result = False
    return result


'''Проверяет делится ли число num без остатка хотя бы на одно число из списка dividers.'''
def has_zero_mod(n, dividers):
    for div in dividers:
        if n % div == 0:
            return True
    return False