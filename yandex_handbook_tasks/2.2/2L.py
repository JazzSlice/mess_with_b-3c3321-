fn = int(input())
sn = int(input())
tn = int(input())
mind, maxd = min(fn, sn, tn), max(fn, sn, tn)
if fn != mind and fn != maxd:
    midd = fn
elif sn != mind and sn != maxd:
    midd = sn
else:
    midd = tn
if (mind + midd) > maxd:
    msg = 'YES'
else:
    msg = 'NO'
print(msg)
