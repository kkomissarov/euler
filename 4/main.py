from datetime import datetime
start = datetime.now()

result = max(i * j for i in range(100, 1000)
                   for j in range(100, 1000)
                   if str(i * j) == str(i * j)[::-1])

end = datetime.now()
print('Ответ:', result)
print('Время выполнения:', end - start)
