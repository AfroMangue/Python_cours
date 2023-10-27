import random
import os

class WordlistNotFoundError(Exception):
    pass

class PassphraseGenerator:
    def __init__(self, num_words):
        self.num_words = num_words
        self.wordlist = self.load_wordlist()

    def load_wordlist(self):
        script_dir = os.path.dirname(__file__)
        wordlist_path = os.path.join(script_dir, 'wordlist.txt')
        
        if not os.path.exists(wordlist_path):
            raise WordlistNotFoundError("Fichier de liste de mots introuvable.")

        with open(wordlist_path, 'r') as file:
            words = [line.strip() for line in file]
        return words

    def generate_passphrase(self):
        words = [random.choice(self.wordlist) for _ in range(self.num_words)]
        passphrase = ' '.join(words)
        return passphrase
