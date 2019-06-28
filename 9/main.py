from math import sqrt

"""
1. Максимальное возможное значение a - 498. b - 499. т.к. a < b < c. Если бы это правило не соблюдалось - сумма
превысила бы тысячу.

2. Генерируем список всех возможных парх чисел, в которых a <= 498, b <= 499 и соблюдается 3 условия:
   - a < b
   - корень суммы квадратов a и b - целое число
   - сумма a, b и корня из суммы квадратов a и b == 1000
   
3. Условие подсказывает, что такая пара чисел должна быть всего одна. Проверяем длину получившегося массива.  
"""

couples = [(a, b) for a in range(1, 499)
                  for b in range(1, 500)
                  if a < b and (a**2 + b**2)**0.5 % 1 == 0 and sum((sqrt(a**2 + b**2), a, b)) == 1000]

if len(couples) == 1:
    a, b = couples[0]
    c = sqrt(a**2 + b**2)
    print(int(a * b * c))


