fnum = int(input())
snum = int(input())

fnumf, fnums, fnumt = fnum // 100, fnum % 100 // 10, fnum % 10
snumf, snums, snumt = snum // 100, snum % 100 // 10, snum % 10
sum = f'{(fnumf + snumf) % 10}{(fnums + snums) % 10}{(fnumt + snumt) % 10}'
print(sum)

