import unittest


class Test(unittest.TestCase):
    def test_0_stock_input(self):
        x = str(input('Type "VOO": ')).upper()
        y = "VOO"
        self.assertEqual(x, y)


if __name__ == "__main__":
    unittest.main()