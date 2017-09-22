
import unittest
from main import *
from inventory import *

testInventoryPath = '.\\testinventory.txt'

class GameTest(unittest.TestCase):
    def test_inv_creation(self):
        resetInventory(testInventoryPath)

        with open(inventoryPath, 'r') as file:
            currentTestInventory = file.read()
        self.assertEqual(invStructure, currentTestInventory, 'Inventory Structure Writing')

    def test_inv_writing_reading(self):
        resetInventory(testInventoryPath)

        slot = 0
        for slot in xrange(10):
            writeInv(slot, 'item', testInventoryPath)
        print readInv(testInventoryPath)
        self.assertEqual(['item']*10, readInv(testInventoryPath), 'Inventory Read and Writing')

resetInventory(testInventoryPath)

if __name__ == '__main__':
    unittest.main()
