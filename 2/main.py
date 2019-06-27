numbers = [1, 2]

#Дополняем список всеми числами Фибоначчи до 4 000 000
while numbers[-1] + numbers[-2] < 4000000:
    numbers.append(numbers[-1] + numbers[-2])

#Печатаем сумму четных чисел из этого списка
print(sum([x for x in numbers if x % 2 == 0]))
