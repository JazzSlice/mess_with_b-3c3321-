num = int(input())
fd = num // 100
sd = num // 10 % 10
td = num % 10
nmin, nmax = min(fd, sd, td), max(fd, sd, td)
if nmin == fd and nmin == sd or nmin == fd and nmin == td:
    nmid = fd
elif nmin == sd and nmin == td:
    nmid = sd
elif nmax == fd and nmax == sd or nmax == fd and nmax == td:
    nmid = fd
elif nmax == sd and nmax == td:
    nmid = sd
elif nmax != fd and nmin != fd:
    nmid = fd
elif nmax != sd and nmin != sd:
    nmid = sd
else:
    nmid = td

if nmin != 0:
    fir = f'{nmin}{nmid}'
elif nmid != 0:
    fir = f'{nmid}{nmin}'
else:
    fir = f'{nmax}{nmid}'


sec = f'{nmax}{nmid}'
print(fir, sec)

