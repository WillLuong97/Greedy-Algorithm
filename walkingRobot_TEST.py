#Program to test the walkingrobot algorithm
import unittest
import walkingRobot
class TestingWalkingRobot(unittest.TestCase):
    def test_9_3(self):
        test_val_1 = 9
        test_exchange_1 = 3
        desired_val = 13
        result = walkingRobot.numWaterBottles(test_val_1, test_exchange_1)

        #assertion test:
        self.assertEqual(desired_val, result) 

    def test_15_4(self):
        test_val_1 = 15
        test_exchange_1 = 4
        desired_val = 19
        result = walkingRobot.numWaterBottles(test_val_1, test_exchange_1)

        #assertion test:
        self.assertEqual(desired_val, result) 

    def test_5_5(self):
        test_val_1 = 5
        test_exchange_1 = 5
        desired_val = 6
        result = walkingRobot.numWaterBottles(test_val_1, test_exchange_1)

        #assertion test:
        self.assertEqual(desired_val, result) 

    def test_2_3(self):
        test_val_1 = 2
        test_exchange_1 = 3
        desired_val = 2
        result = walkingRobot.numWaterBottles(test_val_1, test_exchange_1)

        #assertion test:
        self.assertEqual(desired_val, result) 


if __name__ == '__main__':
    unittest.main()