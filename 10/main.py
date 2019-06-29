from math import sqrt, ceil
from datetime import datetime
from eulerlib import check_simple, has_zero_mod

start = datetime.now()

'''До какого числа нужно посчитать сумму простых чисел'''
limit = 2000000

'''Предел диапазона в котором должны лежать все простые делители limit - это корень из limit, округленный в бОльшую
сторону.'''
max_simple_divider = ceil(sqrt(limit))


'''Находим все простые числа до max_simple_divider обычным перебором делителей до квадратного  корня с помощью
функции is_simple'''
dividers = [x for x in range(max_simple_divider) if check_simple(x)]
s = sum(dividers)

'''Любое число больше max_simple_divider будет составным, если делится без остатка хотя бы на одно простое число из
списка simples. В ином случае оно простое.'''
for i in range(max_simple_divider, limit + 1):
    if not has_zero_mod(i, dividers):
        s += i

end = datetime.now()
print('Ответ: ', s)
print('Время выполнения: ', end - start)



