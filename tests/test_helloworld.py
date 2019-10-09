import unittest


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        """
        Hello World test
        """
        two = 1 + 1
        print("Hello World!")
        self.assertTrue(two == 2, "Hello World Worked!")


if __name__ == "__main__":
    unittest.main()
