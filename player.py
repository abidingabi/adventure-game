import os
from inventory import *

class Player:
    filePath = ''
    #A class for a player
    def __init__(self, tempFilePath):
        global filePath
        self.inventory = ['']*10
        filePath = tempFilePath
        
        try:
            if (os.path.getsize(filePath) != 0): #If inventory.txt is not empty
                self.inventory = readInv(filePath)
            else: #If inventory.txt is empty
                writeInvStructure(filePath)
        except WindowsError: #If inventory.txt does not exist
            with open(filePath,'a+') as file:
                writeInvStructure(file) #Creates inventory file and creates inventory structure