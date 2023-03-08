pas = int(input())
fn = pas // 100
sn = pas // 10 % 10
tn = pas % 10
mind, maxd = min(fn, sn, tn), max(fn, sn, tn)
if fn != mind and fn != maxd:
    midd = fn
elif sn != mind and sn != maxd:
    midd = sn
else:
    midd = tn
if (mind + maxd) == (midd * 2):
    msg = 'YES'
else:
    msg = 'NO'
print(msg)
