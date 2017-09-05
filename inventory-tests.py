
import unittest
from main import *

testInventoryPath = '.\\testinventory.txt'

class GameTest(unittest.TestCase):
    def test_inv_writing(self):
        os.remove(testInventoryPath)

        with open(inventoryPath,'a+') as file:
            writeInvStructure(file) #Creates inventory file and creates inventory structure

        with open(inventoryPath, 'r') as file:
            currentTestInventory = file.read()

        self.assertEqual(invStructure, currentTestInventory, 'Inventory Structure Writing Functional')

if __name__ == '__main__':
    unittest.main()
