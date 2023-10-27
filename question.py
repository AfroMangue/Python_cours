# Définition de la classe Question pour représenter une question dans un quiz.

class Question:
    def __init__(self, texte, options, reponse_correcte):
        # Initialisation de la classe Question avec le texte de la question, les options de réponse et la réponse correcte.
        self.texte = texte  # Le texte de la question.
        self.options = options  # Les options de réponse (une liste de chaînes de caractères).
        self.reponse_correcte = reponse_correcte  # La lettre représentant la réponse correcte.

    def est_correcte(self, reponse_utilisateur):
        # Méthode pour vérifier si la réponse de l'utilisateur est correcte.

        # Comparer la réponse de l'utilisateur avec la réponse correcte.
        return reponse_utilisateur == self.reponse_correcte
