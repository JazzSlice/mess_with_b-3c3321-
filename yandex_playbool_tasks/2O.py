hours = int(input())
minutes = int(input())
time = int(input())
deliver_hrs = ((minutes + time) // 60 + hours) % 24
deliver_mins = (minutes + time) % 60
deliver_time = f'{deliver_hrs // 10}{deliver_hrs % 10}:{deliver_mins // 10}{deliver_mins % 10}'

print(deliver_time)
