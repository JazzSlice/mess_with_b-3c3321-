name = input()
closet = int(input())
group = closet // 100
bed = closet // 10 % 10
num = closet % 10
card = f'Группа №{group}.\n{num}. {name}.\nШкафчик: {closet}.\nКроватка: {bed}.'

print(card)
