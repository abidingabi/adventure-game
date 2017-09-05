import os

inventoryPath = '.\inventory.txt'

def readInv(file): #reads what is contained in inventory
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in range(0, len(lines)):
            lines[line] = lines[line][5:]
    return lines

def writeInv(slot, item, file):
    with open(file, 'r') as f:
        content = f.readlines()
    content[slot] = item + '\n'

    with open(file, 'w') as f:
        f.writelines(content)
def writeInvStructure(file):
    for i in range(0,9):
        writeInv(i, '', inventoryPath)

try:
    if (os.path.getsize(inventoryPath) != 0): #If inventory.txt is not empty
        currentInventory = readInv(inventoryPath)
    else: #If inventory.txt is empty
        writeInvStructure(inventoryPath)
except IOError: #If inventory.txt does not exist
    with open(inventoryPath,"a+") as file:
        writeInvStructure(file) #Create inventory file and create inventory structure
