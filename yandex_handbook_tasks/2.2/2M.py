fn = int(input())
sn = int(input())
tn = int(input())
f1, f2 = int(fn) // 10, int(fn) % 10
s1, s2 = int(sn) // 10, int(sn) % 10
t1, t2 = int(tn) // 10, int(tn) % 10
if f1 == s1 and s1 == t1:
    msg = f1
elif f2 == s2 and s2 == t2:
    msg = f2
print(msg)
