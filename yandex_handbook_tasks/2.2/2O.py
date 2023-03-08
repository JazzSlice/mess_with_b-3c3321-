fn = int(input())
sn = int(input())

fnfd, fnsd = fn // 10, fn % 10
snfd, snsd = sn // 10, sn % 10

fnum = max(fnfd, fnsd, snfd, snsd)
tnum = min(fnfd, fnsd, snfd, snsd)

if fnum == fnfd:
    if tnum == fnsd:
        snum = (snfd + snsd) % 10
    elif tnum == snfd:
        snum = (fnsd + snsd) % 10
    else:
        snum = (fnsd + snfd) % 10
elif fnum == fnsd:
    if tnum == fnfd:
        snum = (snfd + snsd) % 10
    elif tnum == snfd:
        snum = (fnfd + snsd) % 10
    else:
        snum = (fnfd + snfd) % 10
elif fnum == snfd:
    if tnum == fnfd:
        snum = (fnsd + snsd) % 10
    elif tnum == fnsd:
        snum = (fnfd + snsd) % 10
    else:
        snum = (fnfd + fnsd) % 10
else:
    if tnum == fnfd:
        snum = (fnsd + snfd) % 10
    elif tnum == fnsd:
        snum = (fnfd + snfd) % 10
    else:
        snum = (fnfd + fnsd) % 10
print(f'{fnum}{snum}{tnum}')
