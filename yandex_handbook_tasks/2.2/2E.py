petya = 7
vasya = 6
give1 = int(input())
give2 = int(input())
petya = petya - 3 + 2 + give1
vasya = vasya + 5 - 2 + 3 + give2
if petya > vasya:
    msg = 'Петя'
else:
    msg = 'Вася'
print(msg)
