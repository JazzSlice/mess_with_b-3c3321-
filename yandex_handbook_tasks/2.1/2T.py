weight = int(input())
ps = int(input())
p1 = int(input())
p2 = int(input())

qr = (ps - p2) / (p1 - p2)
w1 = qr * weight 
w2 = weight - w1
print(int(w1), int(w2))