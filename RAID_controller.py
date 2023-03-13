print(f'{"RAID - controller (6)":_^20}')
disk_num = int(input())
disk_v = int(input())
data_kit_v = int(input())

data_vpd = data_kit_v / (disk_num - 2)
if int(data_vpd) != data_vpd:
    data_vpd = int(data_vpd) + 1
elif data_vpd > disk_v:
    print('Overweight data_kit')

logical_disk = []
for i in range(len(logical_disk)):
    if i % 2 == 0:
        logical_disk[i - 1] = 0.01
    else:
        logical_disk[i - 1] = data_vpd

print(logical_disk)
    
