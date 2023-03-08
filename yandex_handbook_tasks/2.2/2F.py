year = int(input())
if (year % 100) == 0 and (year % 400) > 0:
    msg = 'NO'
elif (year % 4) == 0:
    msg = 'YES'
else:
    msg = 'NO'
print(msg)
