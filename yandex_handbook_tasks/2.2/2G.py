poly = int(input())
fi = poly // 1000
se = poly % 1000 // 100
th = poly // 10 % 10
fo = poly % 10
if fi == fo and se == th:
    msg = "YES"
else:
    msg = 'NO'
print(msg)
