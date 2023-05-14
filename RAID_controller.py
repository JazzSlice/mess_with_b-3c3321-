print(f'{"RAID - controller (6)":_^20}')

logical_disk = {}
data_kit_v = -1
i = 1
disk_num = 5 #int(input(Enter number of disks: ))
disk_v = 120 #int(input(Enter disk volume: ))
index = disk_num
rebase_flag = 0

class disk:
    def __init__(self, num, value):
        self.num = num + 1
        self.memory = value
        self.layers = []

    def add_layer(self, data_value):
        if self.memory < sum(self.layers) + data_value:
            print(f'Overweight data_kit for disk {self.num}')
            return 1
        else:
            self.layers.append(round(data_value, 2))
    
    def count_busy_memory(self):
        x = 0
        for i in range(len(self.layers)):
            x += self.layers[i]
        # result = self.memory - x
        return x
    
    def removeLayer(self, x):
        x = x - 1
        del self.layers[x]

    def print_memory_usage(self):
        # index_free = self.memory - self.count_free_memory()
        # index_busy = 1 - index_free
        print(f'Disk {self.num} | {round(self.count_busy_memory(),2)} / {round(self.memory, 2)}')# + int(10 * index_busy) * '-' + int(10 * index_free) * '_')


for i in range(disk_num):
    logical_disk[f'{i}'] = disk(i, disk_v)

while True:

    txt = input('1. Add data kit\n2. Show logic-disk status\n3. Remove layer\n4. Break\n')
    match txt:
        case '1':
            data_kit_v = 80 #int(input(Enter data-kit volume: ))
            data_vpd = data_kit_v / (disk_num - 2)
            
            if int(data_vpd) != data_vpd:
                data_vpd = round(data_vpd) + 1

            if data_vpd > disk_v:
                print('Overweight data_kit')
                break
            
            if index -1 == 0:
                op1 = index -1
                op2 = disk_num -1
                rebase_flag = 1
            else:
                op1 = index - 1
                op2 = index - 2

            for j in range(disk_num):
                if j == op1 or j == op2:
                    logical_disk[f'{j}'].add_layer(0.01)
                else:
                    logical_disk[f'{j}'].add_layer(data_vpd)

            index -= 1

            if rebase_flag:
                index = disk_num
                rebase_flag = 0
                
            i += 1
        case '2':
            check_len = []
            line = '\n| Layer |'
            for j in range(disk_num):
                line += f'      Disk {j+1}      |'
            line += f'\n{"":-^104}\n|       |'
            for j in range(disk_num):
                line += f'   Data  | Secret |'
                check_len.append(len(logical_disk[f'{j}'].layers))
            line += f'\n{"":-^104}\n'
            for j in range(min(check_len)):
                line += f'|{j+1:^7}| '
                for g in range(len(logical_disk)):
                    mem = logical_disk[f'{g}'].layers[j]
                    line += f'{mem // 1: >7.2f} | {mem % 1: >6.2f} | '
                line += '\n'
            util = 0
            line += f'{"":-^104}\n|       |'
            for i in range(len(logical_disk)):
                util += logical_disk[f'{i}'].count_busy_memory()
                line += f" {logical_disk[f'{i}'].count_busy_memory(): >7.2f} / {logical_disk[f'{i}'].memory :.2f} |"

            line += f'\nUtilisation: {round((disk_v * disk_num - util) / (disk_v * disk_num), 2)}\n'
            print(line)
        case '3':
            layer = int(input('Which layer do you want delete?\n'))
            for j in range(len(logical_disk)):
                disk_pointer = logical_disk[f'{j}']
                disk_pointer.removeLayer(layer)
        case '4':
            break
