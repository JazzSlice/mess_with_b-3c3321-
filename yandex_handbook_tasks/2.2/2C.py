s1 = int(input())
s2 = int(input())
s3 = int(input())
if s3 < s1 > s2:
    winner = 'Петя'
elif s3 < s2 > s1:
    winner = 'Вася'
else:
    winner = 'Толя'
print(winner)