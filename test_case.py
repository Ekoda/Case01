import unittest
from case import manage

class TestManage(unittest.TestCase):
    def test_lowercase(self):
        inventory = 0
        testcases = ['l', 's', 'i']
        for x in testcases:
            self.assertEqual(manage(x, inventory), 'Invalid')

    def multiple_commands(self):
        inventory = 0 
        testcases = ['LS123451', 'As323d123', 'L2SD', 'I030129as', 'L1321123124125S', 'I123124312Ö451', 'S802S']
        for x in testcases:
            self.assertEqual(manage(x, inventory), 'Invalid')

    def test_no_command(self):
        inventory = 0
        testcases = ['1235123', 123123, 25, '2356', 234234234, 5235]
        for x in testcases:
            self.assertEqual(manage(x, inventory), 'Invalid')

    def test_extreme_numbers(self):
        inventory = 0
        testcases = ['L', 'I12312104581208120812580128051208521', 'S12124124124124124124', 'I1000000000000000000', 'I000', 'S0', 'I-0', 'S-0']
        self.assertEqual(manage(testcases[0], inventory), 0)
        self.assertEqual(manage(testcases[1], inventory), 12312104581208120812580128051208521)
        self.assertEqual(manage(testcases[2], inventory), -12124124124124124124)
        self.assertEqual(manage(testcases[3], inventory), 1000000000000000000)
        self.assertEqual(manage(testcases[4], inventory), 0)
        self.assertEqual(manage(testcases[5], inventory), 0)
        self.assertEqual(manage(testcases[6], inventory), 0)
        self.assertEqual(manage(testcases[7], inventory), 0)

    def test_negatives(self):
        inventory = 0
        testcases = ['I-1235122', 'S-123512213', 'I-1351512']
        self.assertEqual(manage(testcases[0], inventory), -1235122)
        self.assertEqual(manage(testcases[1], inventory), 123512213)
        self.assertEqual(manage(testcases[2], inventory), -1351512)

    def test_inventory_values(self):
        self.assertEqual(manage('L', -100), -100)
        self.assertEqual(manage('L', 100), 100)
        self.assertEqual(manage('L', 0), 0)

    def test_unacceptable_L_values(self):
        inventory = 0
        testcases = ['L1235', 'L-123123', 'L0', 'L-0', 'LL', 'LSI', 'LI']
        for x in testcases:
            self.assertEqual(manage(x, inventory), 'Invalid')

    def test_float(self):
        inventory = 0
        testcases = ['I1.235123', 'S643.00', 'I.1', 'S.02']
        for x in testcases:
            self.assertEqual(manage(x, inventory), 'Invalid')
