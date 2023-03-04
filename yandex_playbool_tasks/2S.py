prod = input()
price = int(input())
weight = int(input())
money = int(input())

print(f'{"=" * 16}Чек{"=" * 16}')
print('Товар:{: >29}\nЦена:{: >16}кг * {:}руб/кг'.format(prod, weight, price))
print('Итого:{: >26}руб\nВнесено:{: >24}руб\nСдача:{: >26}руб'.format(weight * price, money, money - (weight * price)))
print(f'{"=" * 35}')
