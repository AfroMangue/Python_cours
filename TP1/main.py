# main.py
from quiz_module import Quiz
from question import Question

def main():
    print("Bienvenue au Quiz IoT !")
    print("Testez vos connaissances en IoT avec ce quiz.")
    print("Vous avez 10 questions à répondre. Bonne chance!\n")

    quiz = Quiz()

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

    for data in questions_data:
        question = Question(data[0], data[1], data[2])
        quiz.ajouter_question(question)

    quiz.commencer_quiz()
    quiz.afficher_score()

if __name__ == "__main__":
    main()
