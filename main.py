# Importation des classes Quiz et Question à partir des modules externes.
from quiz_module import Quiz
from question import Question

# Définition de la fonction principale du programme.
def main():
    # Messages de bienvenue pour les utilisateurs.
    print("Bienvenue au Quiz IoT !")
    print("Testez vos connaissances en IoT avec ce quiz.")
    print("Vous avez 10 questions à répondre. Bonne chance!\n")

    # Création d'une instance de la classe Quiz pour gérer le quiz.
    quiz = Quiz()

    # Définition des données des questions sous forme de liste de tuples.
    questions_data = [
        ("Qu'est-ce que l'acronyme IoT signifie?", ["Internet of Things", "Internet of Time", "Internet of Technology"], "a"),
        ("Quelle technologie sans fil est couramment utilisée pour la communication IoT?", ["LoRaWAN", "Zigbee", "Bluetooth"], "a"),
        ("Qu'est-ce qu'un capteur IoT?", ["Un dispositif pour mesurer une quantité physique", "Un micro-ordinateur", "Une application mobile"], "a"),
        ("Quel langage de programmation est souvent utilisé pour développer des applications IoT?", ["Python", "Java", "C#"], "a"),
        ("Quel protocole de communication est utilisé pour la communication entre les appareils IoT et le cloud?", ["HTTP", "MQTT", "FTP"], "b"),
        ("Quelle est la principale caractéristique de la technologie LoRaWAN?", ["Haute vitesse de transmission", "Longue portée de transmission", "Faible consommation d'énergie"], "b"),
        ("Qu'est-ce qu'un microcontrôleur dans le contexte de l'IoT?", ["Un petit ordinateur portable", "Un dispositif pour mesurer la température", "Un ordinateur intégré pour le contrôle"], "c"),
        ("Quelle est la principale préoccupation en matière de sécurité dans l'IoT?", ["La sécurité des données", "La taille des appareils", "La couleur des appareils"], "a"),
        ("Que signifie MQTT dans le contexte de l'IoT?", ["Message Queue Telemetry Transport", "My Quick Test Tool", "Maximum Quality Technology Transfer"], "a"),
        ("Quelle entreprise a popularisé le terme 'IoT'?", ["Apple", "Cisco", "Kevin Ashton"], "c"),
    ]

    # Boucle pour créer des objets Question à partir des données et les ajouter au quiz.
    for data in questions_data:
        question = Question(data[0], data[1], data[2])
        quiz.ajouter_question(question)

    # Début du quiz en appelant la méthode commencer_quiz() et affichage du score à la fin.
    quiz.commencer_quiz()
    quiz.afficher_score()

# Vérification si le script est exécuté en tant que programme autonome.
if __name__ == "__main__":
    main()  # Appel de la fonction main() pour lancer le quiz.
