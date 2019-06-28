#Функция определяет является ли число простым
def is_simple(num):

    if num < 2:
        return False

    simple = True
    for x in range(2, round(num**0.5)+1):
        if num % x == 0 and num != x:
            simple = False

    return simple


i = 1 #Порядковый номер простого числа
num = 2 #Само число
while i <= 1001:
    if is_simple(num):
        i += 1
    if i <= 1001: #условие, чтобы не прибавлять единицу на последнем цикле
        num += 1

print(num)
