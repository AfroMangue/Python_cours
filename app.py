import random

# Définition de la classe Question pour représenter une question du quiz
class Question:
    def __init__(self, texte, options, reponse_correcte):
        self.texte = texte
        self.options = options
        self.reponse_correcte = reponse_correcte
        self.shuffle_options()  # Appel à la méthode pour mélanger les options lors de l'initialisation

    def shuffle_options(self):
        random.shuffle(self.options)  # Mélange aléatoirement l'ordre des options

    def est_correcte(self, reponse_utilisateur):
        # Mapping des réponses valides ("a", "b", "c") aux indices (0, 1, 2)
        reponses_valides = ["a", "b", "c"]
        reponse_utilisateur = reponse_utilisateur.lower()
        if reponse_utilisateur in reponses_valides:
            index_reponse = reponses_valides.index(reponse_utilisateur)
            return index_reponse == int(self.reponse_correcte) - 1
        return False

# Définition de la classe Quiz pour gérer le quiz
class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def ajouter_question(self, question):
        self.questions.append(question)

    def afficher_question(self, question):
        print(question.texte)
        for i, option in enumerate(question.options, start=1):
            print(f"{chr(96 + i)}. {option}")

    def obtenir_reponse_utilisateur(self):
        reponse_utilisateur = input("Votre réponse (a, b ou c) : ").lower()
        while reponse_utilisateur not in ['a', 'b', 'c']:
            print("Réponse non valide. Veuillez entrer a, b ou c.")
            reponse_utilisateur = input("Votre réponse (a, b ou c) : ").lower()
        return reponse_utilisateur

    def commencer_quiz(self):
        random.shuffle(self.questions)  # Mélange les questions dans un ordre aléatoire
        for question in self.questions:
            self.afficher_question(question)  # Affiche la question
            reponse_utilisateur = self.obtenir_reponse_utilisateur()  # Demande la réponse de l'utilisateur
            if question.est_correcte(reponse_utilisateur):
                print("Correct !\n")  # Affiche un message si la réponse est correcte
                self.score += 1
            else:
                print(f"Faux. La réponse correcte est {chr(96 + int(question.reponse_correcte))}.\n")  # Affiche la réponse correcte

    def afficher_score(self):
        # Affiche le score final du quiz
        print(f"Votre score final est : {self.score}/{len(self.questions)}")

def main():
    print("Bienvenue au Quiz IoT !")
    print("Testez vos connaissances en IoT avec ce quiz.")
    print("Vous avez 10 questions à répondre. Bonne chance!\n")

    quiz = Quiz()

    questions_data = [
        ("Qu'est-ce que l'acronyme IoT signifie?", ["Internet of Things", "Internet of Time", "Internet of Technology"], "1"),
        ("Quelle technologie sans fil est couramment utilisée pour la communication IoT?", ["LoRaWAN", "Zigbee", "Bluetooth"], "1"),
        ("Qu'est-ce qu'un capteur IoT?", ["Un dispositif pour mesurer une quantité physique", "Un micro-ordinateur", "Une application mobile"], "1"),
        ("Quel langage de programmation est souvent utilisé pour développer des applications IoT?", ["Python", "Java", "C#"], "1"),
        ("Quel protocole de communication est utilisé pour la communication entre les appareils IoT et le cloud?", ["HTTP", "MQTT", "FTP"], "2"),
        ("Quelle est la principale caractéristique de la technologie LoRaWAN?", ["Haute vitesse de transmission", "Longue portée de transmission", "Faible consommation d'énergie"], "2"),
        ("Qu'est-ce qu'un microcontrôleur dans le contexte de l'IoT?", ["Un petit ordinateur portable", "Un dispositif pour mesurer la température", "Un ordinateur intégré pour le contrôle"], "3"),
        ("Quelle est la principale préoccupation en matière de sécurité dans l'IoT?", ["La taille des appareils", "La sécurité des données", "La couleur des appareils"], "2"),
        ("Que signifie MQTT dans le contexte de l'IoT?", ["Message Queue Telemetry Transport", "My Quick Test Tool", "Maximum Quality Technology Transfer"], "1"),
        ("Quelle entreprise a popularisé le terme 'IoT'?", ["Apple", "Cisco", "Kevin Ashton"], "3"),
    ]

    for data in questions_data:
        question = Question(data[0], data[1], data[2])
        quiz.ajouter_question(question)

    quiz.commencer_quiz()  # Démarre le quiz
    quiz.afficher_score()  # Affiche le score final

if __name__ == "__main__":
    main()
