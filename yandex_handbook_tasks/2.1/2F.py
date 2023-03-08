product = input()
price = int(input())
weight = int(input())
money = int(input())

cost = weight * price
back_pay = money - cost
print(f'Чек\n{product} - {weight}кг - {price}руб/кг\nИтого: {cost}руб')
print(f'Внесено: {money}руб\nСдача: {back_pay}руб')
