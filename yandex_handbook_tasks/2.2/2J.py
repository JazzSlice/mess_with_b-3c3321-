pas = int(input())
fn = pas // 100
sn = pas // 10 % 10
tn = pas % 10
fp, sp = max(fn + sn, sn + tn), min(fn + sn, sn + tn)
print(f'{fp}{sp}')
