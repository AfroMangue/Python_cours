from password_strength_tester import PasswordStrengthTester
from password_generator import PasswordGenerator, PasswordGenerationError
from passphrase_generator import PassphraseGenerator, WordlistNotFoundError

def main():
    while True:
        try:
            choice = input("Bienvenue sur le générateur et testeur de mot de passe : \n1 - Testeur de mot de passe \n2 - Générateur de mot de passe \n3 - Générateur de passphrase\nChoisissez une option (1,2 ou 3) :")

            if choice == "1":
                password = input("Entrez le mot de passe à tester : ")
                tester = PasswordStrengthTester(password)
                strength = tester.test_password_strength()
                print(f"Force du mot de passe : {strength}")

            elif choice == "2":
                num_lowercase = int(input("Nombre de minuscules : "))
                num_uppercase = int(input("Nombre de majuscules : "))
                num_digits = int(input("Nombre de chiffres : "))
                num_special = int(input("Nombre de caractères spéciaux : "))
                generator = PasswordGenerator(num_lowercase, num_uppercase, num_digits, num_special)
                password, entropy = generator.generate_password()
                print(f"Mot de passe généré : {password}")
                print(f"Entropie du mot de passe : {entropy:.2f}")
                tester = PasswordStrengthTester(password)
                strength = tester.test_password_strength()
                print(f"Force du mot de passe : {strength}")

            elif choice == "3":
                num_words = int(input("Nombre de mots dans la passphrase : "))
                generator = PassphraseGenerator(num_words)
                passphrase = generator.generate_passphrase()
                print(f"Passphrase générée : {passphrase}")

        except PasswordGenerationError as e:
            print(f"Erreur de génération de mot de passe : {e}")
        except WordlistNotFoundError as e:
            print(f"Erreur de fichier de liste de mots : {e}")
        except ValueError as e:
            print(f"Erreur : {e}")

        another_attempt = input("Voulez-vous essayer de nouveau ? (Oui/Non): ")
        if another_attempt.lower() != "oui":
            break

if __name__ == "__main__":
    main()
