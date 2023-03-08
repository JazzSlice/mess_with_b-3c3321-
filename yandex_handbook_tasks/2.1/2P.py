storage = int(input())
shop = int(input())
speed = int(input())
time = (shop - storage) / speed
print('{:.2f}'.format(time))
