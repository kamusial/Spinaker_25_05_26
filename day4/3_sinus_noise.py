import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import random

x = np.arange(-8 * np.pi, 8 * np.pi, 0.4)
y = np.array([np.sin(number) * np.exp(-0.05 * number) * random.uniform(0.5, 1.5) for number in x])

model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(20, activation='linear'))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='linear'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

x_reshape = x.reshape(-1, 1)
y_reshape = y.reshape(-1, 1)

model.fit(x_reshape, y_reshape, epochs=3000, verbose=2)

y_pred = model.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, c='r')


plt.title('Wykres funkcji sinus')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xticks(
    ticks=[-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    labels=['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
)
plt.show()




