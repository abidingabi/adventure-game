inventoryPath = '.\\inventory.txt'
import os
invStructure = 'Slot0:\nSlot1:\nSlot2:\nSlot3:\nSlot4:\nSlot5:\nSlot6:\nSlot7:\nSlot8:\nSlot9:'
inventoryPath = '.\\inventory.txt'

def resetInventory(f):
    try:
        os.remove(f)
    except WindowsError:
        pass

    with open(f,'a+') as file:
        writeInvStructure(file) #Creates inventory file and creates inventory structure

def readInv(file): #reads what is contained in inventory
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in range(len(lines)):
            if line == 9:
                lines[line] = lines[line][6:]
            else:
                lines[line] = lines[line][6:-1]
    return lines

def writeInv(slot, item, file):
    with open(file, 'r') as f:
        content = f.readlines()
    if slot == 9:
        content += ['Slot' + str(slot) + ':' + item]
    else:
        content += ['Slot' + str(slot) + ':' + item + '\n']

    with open(file, 'w') as f:
        f.writelines(content)

def writeInvStructure(file):
    with open(inventoryPath, 'w') as text_file:
        text_file.write(invStructure)

