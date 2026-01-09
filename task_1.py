import pulp

# 1. Ініціалізація моделі
# Ми хочемо максимізувати загальну кількість продуктів
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# 2. Визначення змінних
# lowBound=0 гарантує, що ми не можемо виробити від'ємну кількість
# cat='Integer' вказує, що кількість пляшок має бути цілою (не можна виробити 1.5 пляшки)
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# 3. Додавання цільової функції (Total Products)
model += lemonade + fruit_juice, "Total_Production_Amount"

# 4. Додавання обмежень (Constraints)
# Обмеження на Воду
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
# Обмеження на Цукор
model += 1 * lemonade <= 50, "Sugar_Constraint"
# Обмеження на Лимонний сік
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
# Обмеження на Фруктове пюре
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# 5. Розв'язання моделі
model.solve()

# 6. Виведення результатів
print(f"Статус розв'язання: {pulp.LpStatus[model.status]}")
print(f"Кількість Лимонаду: {lemonade.varValue}")
print(f"Кількість Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість продуктів: {lemonade.varValue + fruit_juice.varValue}")