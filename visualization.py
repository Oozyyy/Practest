import matplotlib.pyplot as plt

requests_data = {
    'Запрос 1': 10,
    'Запрос 2': 15,
    'Запрос 3': 7,
    'Запрос 4': 18,
    'Запрос 5': 22
}

plt.figure(figsize=(7, 7))
plt.pie(requests_data.values(), labels=requests_data.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Распределение количества записей по запросам')
plt.savefig('requests_stats.png')
plt.show()
