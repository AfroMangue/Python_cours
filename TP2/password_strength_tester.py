# password_strength_tester.py
import math
import unittest

class PasswordStrengthTester:
    def __init__(self, password):
        self.password = password

    def test_password_strength(self):
        entropy = self.calculate_entropy()
        
        if entropy < 64:
            return "très faible"
        elif entropy < 80:
            return "faible"
        elif entropy < 100:
            return "moyen"
        else:
            return "fort"

    def calculate_entropy(self):
        char_set = set(self.password)
        alphabet_size = len(char_set)
        password_length = len(self.password)

        entropy = password_length * (math.log(alphabet_size) / math.log(2))
        return entropy

class TestPasswordStrengthTester(unittest.TestCase):
    def test_password_strength(self):
        tester = PasswordStrengthTester("WeakPassword123")
        self.assertEqual(tester.test_password_strength(), "faible")
        
        tester = PasswordStrengthTester("StrongP@ssw0rd")
        self.assertEqual(tester.test_password_strength(), "fort")
        
        tester = PasswordStrengthTester("12345678")
        self.assertEqual(tester.test_password_strength(), "très faible")

if __name__ == "__main__":
    unittest.main()
