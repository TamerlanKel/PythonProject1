# Работа с библиотекой pandas
import pandas as pd

file = 'data.csv'
data = pd.read_csv(file)
print(data.head())

# Рассчитываем средний возраст 3 человек
data['AGE'] = [28, 32, 22]
average_age = sum(data['AGE']) / 3
print(f'Средний возраст: {average_age}')

# Работа с библиотекой NumPy
import numpy as np

array = np.arange(10)
print(array)
array = np.arange(10) + 5
print(array)
array = np.arange(10) ** 8
print(array)

# Работа с билбиотекой matplotlib
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt


x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]


plt.plot(x, y, marker='o', color='blue')
plt.title('Простая линейная зависимость')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()