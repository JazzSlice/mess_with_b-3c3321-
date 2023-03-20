print(f'{"RAID - controller (6)":_^20}')

logical_disk = {}
data_kit_v = -1
i = 1
disk_num = 5 #int(input(Enter number of disks: ))
disk_v = 120 #int(input(Enter disk volume: ))
index = disk_num

class disk:
    def __init__(self, num, value):
        self.num = num + 1
        self.memory = value
        self.layers = []

    def add_layer(self, data_value):
        free_memory = self.memory - self.count_busy_memory()
        if free_memory < data_value:
            print(f'Overweight data_kit for disk {self.num}')
            return
        else:
            self.layers.append(data_value)
    
    def count_busy_memory(self):
        x = 0
        for i in range(len(self.layers)):
            x += self.layers[i]
        # result = self.memory - x
        return x
    
    def print_memory_usage(self):
        # index_free = self.memory - self.count_free_memory()
        # index_busy = 1 - index_free
        print(f'Disk {self.num} | {self.count_busy_memory()} / {self.memory}')# + int(10 * index_busy) * '-' + int(10 * index_free) * '_')


for i in range(disk_num):
    logical_disk[f'{i}'] = disk(i, disk_v)

while True:

    txt = input('1. Add data kit\n2. Show logic-disk status\n3. Break\n')
    match txt:
        case '1':
            data_kit_v = 80 #int(input(Enter data-kit volume: ))
            data_vpd = data_kit_v / (disk_num - 2)
            
            if int(data_vpd) != data_vpd:
                data_vpd = abs(data_vpd) + 1

            if data_vpd > disk_v:
                print('Overweight data_kit')
                break

            for j in range(disk_num):
                if j == (index - 1) or j == index:
                    logical_disk[f'{j}'].add_layer(0.01)
                else:
                    logical_disk[f'{j}'].add_layer(data_vpd)

                if j == range(disk_num):
                    if (index - 2) > 0:
                        index -= 1
                    else:
                        index = disk_num
                

            i += 1
        case '2':
            for j in range(len(logical_disk)):
                disk_pointer = logical_disk[f'{j}']
                print(disk_pointer.print_memory_usage())
        case '3':
            break
