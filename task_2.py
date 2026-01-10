import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло
N = 100000  # Кількість випадкових точок (можна змінити для перевірки точності)

# Генеруємо випадкові точки X та Y
# X в діапазоні [a, b]
rand_x = np.random.uniform(a, b, N)
# Y в діапазоні [0, max_y], де max_y = f(b) = 4 (для монотонно зростаючої функції)
max_y = f(b)
rand_y = np.random.uniform(0, max_y, N)

# Перевіряємо, які точки потрапили під криву (y < f(x))
points_under_curve = rand_y < f(rand_x)
count_under = np.sum(points_under_curve)

# Площа прямокутника, в якому ми розкидали точки
area_rectangle = (b - a) * max_y

# Обчислення інтеграла методом Монте-Карло
monte_carlo_integral = (count_under / N) * area_rectangle

print(f"Кількість точок: {N}")
print(f"Інтеграл (Monte Carlo): {monte_carlo_integral}")

# Перевірка аналітичним методом (SciPy)
result_quad, error = spi.quad(f, a, b)
print(f"Інтеграл (SciPy quad): {result_quad}")

# Розрахунок похибки
absolute_error = abs(monte_carlo_integral - result_quad)
relative_error = (absolute_error / result_quad) * 100
print(f"Абсолютна похибка: {absolute_error}")
print(f"Відносна похибка: {relative_error:.4f}%")

# Візуалізація
# plt.figure(figsize=(8, 6))
plt.scatter(rand_x[points_under_curve], rand_y[points_under_curve], color='green', s=1, label='Під кривою')
plt.scatter(rand_x[~points_under_curve], rand_y[~points_under_curve], color='red', s=1, label='Над кривою')
x_line = np.linspace(a, b, 100)
plt.plot(x_line, f(x_line), color='black', linewidth=2, label='f(x)=x^2')
plt.title(f'Метод Монте-Карло (N={N})')
plt.legend()
plt.show()