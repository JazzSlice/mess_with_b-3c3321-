num = int(input())
fi = num % 1000 // 100
se = num // 1000
th = num % 10
fo = num % 100 // 10
num = f'{fi}{se}{th}{fo}'
print(num)
