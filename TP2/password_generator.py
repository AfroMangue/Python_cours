import random
import string
import math

class PasswordGenerationError(Exception):
    pass

class PasswordGenerator:
    def __init__(self, num_lowercase, num_uppercase, num_digits, num_special):
        self.num_lowercase = num_lowercase
        self.num_uppercase = num_uppercase
        self.num_digits = num_digits
        self.num_special = num_special

    def generate_password(self):
        if (
            self.num_lowercase + self.num_uppercase + self.num_digits + self.num_special
        ) < 8:
            raise PasswordGenerationError("Le mot de passe doit contenir au moins 8 caractères.")

        lowercase_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(self.num_lowercase))
        uppercase_chars = ''.join(random.choice(string.ascii_uppercase) for _ in range(self.num_uppercase))
        digit_chars = ''.join(random.choice(string.digits) for _ in range(self.num_digits))
        special_chars = ''.join(random.choice(string.punctuation) for _ in range(self.num_special))
        
        password = lowercase_chars + uppercase_chars + digit_chars + special_chars
        password = ''.join(random.sample(password, len(password)))

        entropy = self.calculate_entropy(password)
        
        return password, entropy

    @staticmethod
    def calculate_entropy(password):
        lowercase = set(string.ascii_lowercase)
        uppercase = set(string.ascii_uppercase)
        digits = set(string.digits)
        special_chars = set(string.punctuation)
        
        character_set = set(password)
        character_pool = set()

        if any(char in lowercase for char in character_set):
            character_pool |= lowercase
        if any(char in uppercase for char in character_set):
            character_pool |= uppercase
        if any(char in digits for char in character_set):
            character_pool |= digits
        if any(char in special_chars for char in character_set):
            character_pool |= special_chars

        password_length = len(password)
        pool_size = len(character_pool)

        entropy = password_length * (math.log(pool_size) / math.log(2))
        return entropy
