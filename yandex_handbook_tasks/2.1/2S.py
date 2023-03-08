prod = input()
price = int(input())
weight = int(input())
money = int(input())
hw, hp = weight // 100, price // 100
dw, dp = weight // 10 % 10, price // 10 % 10
index = (hw / (hw + 0.1) ) + (hp / (hp + 0.1)) + (dw / (dw + 0.1)) + (dp / (dp + 0.1))

print(f'{"=" * 16}Чек{"=" * 16}')
print(f'Товар:{prod: >29}')
print(f'Цена:{weight: >{18 - int(index)}}кг * {price:}руб/кг')
print(f'Итого:{weight * price: >26}руб\nВнесено:{money: >24}руб\nСдача:{money - (weight * price): >26}руб')
print(f'{"=" * 35}')