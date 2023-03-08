s1 = int(input())
s2 = int(input())
s3 = int(input())
if s2 < s1 > s3:
    w1 = 'Петя'
    if s2 > s3:
        w2 = 'Вася'
        w3 = 'Толя'
    else:
        w2 = 'Толя'
        w3 = 'Вася'
elif s1 < s2 > s3:
    w1 = 'Вася'
    if s1 > s3:
        w2 = 'Петя'
        w3 = 'Толя'
    else:
        w2 = 'Толя'
        w3 = 'Петя'
else:
    w1 = 'Толя'
    if s1 > s2:
        w2 = 'Петя'
        w3 = 'Вася'
    else:
        w2 = 'Вася'
        w3 = 'Петя'
print(f'{w1:^24}')
print(f'{w2:^8}')
print(f'{w3: >22}')
print('   II      I      III')
