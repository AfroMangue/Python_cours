# quiz.py

# Importation des modules requis.
import random
from question import Question

# Définition de la classe Quiz pour gérer un quiz.

class Quiz:
    def __init__(self):
        # Initialisation de la classe Quiz avec une liste de questions et un score initial de 0.
        self.questions = []  # Une liste vide pour stocker les questions.
        self.score = 0  # Le score du joueur, initialisé à zéro.

    def ajouter_question(self, question):
        # Méthode pour ajouter une question à la liste des questions.
        self.questions.append(question)

    def afficher_question(self, question):
        # Méthode pour afficher une question et ses options de réponse.
        print(question.texte)  # Affichage du texte de la question.
        for i, option in enumerate(question.options, start=1):
            print(f"{chr(96 + i)}. {option}")  # Affichage des options de réponse sous forme de lettres (a, b, c).

    def obtenir_reponse_utilisateur(self):
        # Méthode pour obtenir la réponse de l'utilisateur et s'assurer qu'elle est valide.
        reponse_utilisateur = input("Votre réponse (a, b ou c) : ").lower()  # Lecture de la réponse de l'utilisateur en minuscules.
        while reponse_utilisateur not in ['a', 'b', 'c']:
            # Boucle pour vérifier que la réponse de l'utilisateur est a, b ou c.
            print("Réponse non valide. Veuillez entrer a, b ou c.")
            reponse_utilisateur = input("Votre réponse (a, b ou c) : ").lower()
        return reponse_utilisateur  # Renvoie la réponse de l'utilisateur.

    def commencer_quiz(self):
        # Méthode pour démarrer le quiz.
        random.shuffle(self.questions)  # Mélange aléatoire des questions pour un ordre aléatoire.
        for question in self.questions:
            self.afficher_question(question)  # Affichage de la question et de ses options.
            reponse_utilisateur = self.obtenir_reponse_utilisateur()  # Obtention de la réponse de l'utilisateur.
            if question.est_correcte(reponse_utilisateur):
                print("Correct !\n")  # Message en cas de réponse correcte.
                self.score += 1  # Augmentation du score en cas de réponse correcte.
            else:
                print(f"Faux. La réponse correcte est {question.reponse_correcte}.\n")  # Message en cas de réponse incorrecte.

    def afficher_score(self):
        # Méthode pour afficher le score final du joueur.
        print(f"Votre score final est : {self.score}/{len(self.questions)}")