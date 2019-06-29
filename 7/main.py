from eulerlib import check_simple
from datetime import datetime
start = datetime.now()

i = 1 #Порядковый номер простого числа
count = 10001
num = 2 #Само число



while i <= count:
    if check_simple(num):
        i += 1
    if i <= count: #условие, чтобы не прибавлять единицу на последнем цикле
        num += 1

end = datetime.now()
print('Ответ: ', num)
print('Время выполнения: ', end - start)

