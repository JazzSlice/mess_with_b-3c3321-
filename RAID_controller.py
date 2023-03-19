print(f'{"RAID - controller (6)":_^20}')

layers = {}
data_kit_v = -1
i = 1
while True:

    txt = input('1. Add data kit\n2. Show logic-disk status\n3. Break\n')
    match txt:
        case '1':
            if data_kit_v < 0:
                disk_num = 5 #int(input(Enter number of disks: ))
                disk_v = 120 #int(input(Enter disk volume: ))

            data_kit_v = 80 #int(input(Enter data-kit volume: ))
            data_vpd = data_kit_v / (disk_num - 2)
            if int(data_vpd) != data_vpd:
                data_vpd = int(data_vpd) + 1

            if data_vpd > disk_v:
                print('Overweight data_kit')
                break

            logical_disk = []
            for j in range(disk_num):
                if j % 2 != 0:
                    logical_disk.append(0.01)
                else:
                    logical_disk.append(data_vpd)

            layers[f'{i}'] = logical_disk
            i += 1
        case '2':
            
            for i in range(len(logical_disk)):
                print(logical_disk[i])
            print(layers)
        case '3':
            break
