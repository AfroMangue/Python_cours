# question.py
class Question:
    def __init__(self, texte, options, reponse_correcte):
        self.texte = texte
        self.options = options
        self.reponse_correcte = reponse_correcte

    def est_correcte(self, reponse_utilisateur):
        # Comparer la réponse de l'utilisateur avec la réponse correcte
        return reponse_utilisateur == self.reponse_correcte
