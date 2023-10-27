# quiz.py
import random
from question import Question

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
        random.shuffle(self.questions)
        for question in self.questions:
            self.afficher_question(question)
            reponse_utilisateur = self.obtenir_reponse_utilisateur()
            if question.est_correcte(reponse_utilisateur):
                print("Correct !\n")
                self.score += 1
            else:
                print(f"Faux. La réponse correcte est {question.reponse_correcte}.\n")

    def afficher_score(self):
        print(f"Votre score final est : {self.score}/{len(self.questions)}")
