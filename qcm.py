questions = [
    {
        "question": "Quel est le module de test le plus commun sur Python ?",
        "choices": ["unittest", "phpunit", "Junit", "Aucune des réponses"],
        "correct_choice": 0
    },
    {
        "question": "Quel est le résultat de ces instructions ?\n\na = [1, 2, 3, 4]\nb = [3, 4, 5, 6]\nc = [x for x in a if x not in b]\nprint(c)",
        "choices": ["[1, 2]", "[5, 6]", "[1, 2, 5, 6]", "[3, 4]"],
        "correct_choice": 0
    },
    {
        "question": "Quel est le résultat de ces instructions ?\n\ns1 = {1, 2, 3, 4, 5}\ns2 = {2, 4, 6}\nprint(s1 ^ s2)",
        "choices": ["{1, 2, 3, 4, 5}", "{1, 3, 5, 6}", "{2, 4}", "Aucune des réponses"],
        "correct_choice": 1
    },
    {
        "question": "Quel mot-clé est utilisé pour lever des exceptions ?",
        "choices": ["raise", "try", "goto", "except"],
        "correct_choice": 0
    },
    {
        "question": "Quel est le résultat final de ces instructions ?\n\nset1 = {1, 3, 5}\nset2 = {2, 4, 6}\nprint(len(set1 + set2))",
        "choices": ["3", "6", "0", "Erreur d'exécution"],
        "correct_choice": 3
    },
    {
        "question": "Lequel de ces blocs sera toujours exécuté quand une exception survient ou non dans le programme ?",
        "choices": ["try", "except", "finally", "Aucune des réponses"],
        "correct_choice": 2
    },
    {
        "question": "Quel est le type de données stocké dans *args, quand passé dans une fonction ?",
        "choices": ["list", "tuple", "dict", "Aucune des réponses"],
        "correct_choice": 1
    },
    {
        "question": "Quel est le résultat de ces instructions ?\n\ndef function(*argv):\n   for arg in argv:\n       break\n   print(arg)\nfunction('Sunday', 'Monday', 'Tuesday', 'Wednesday')",
        "choices": ["Sunday", "Wednesday", "Sunday Monday Tuesday Wednesday", "Aucune des réponses"],
        "correct_choice": 0
    },
    {
        "question": "Quel est le résultat de ces instructions ?\n\ns = {1, 2, 3, 3, 2, 4, 5, 5}",
        "choices": ["{1, 2, 3, 3, 2, 4, 5, 5}", "{1, 2, 3, 4, 5}", "{1, 5}", "Aucune des réponses"],
        "correct_choice": 1
    },
    {
        "question": "Comment s'appelle ce concept ?\n\nclass Mercedes(Voiture):\n    ...",
        "choices": ["Héritage", "Création de variable", "Test", "Aucune des réponses"],
        "correct_choice": 0
    },
    {
        "question": "Quel est le test le plus rapide en théorie ?",
        "choices": ["Unitaire", "Fonctionnel", "Intégration", "Aucune des réponses"],
        "correct_choice": 0
    },
    {
        "question": "De quel élément un test unitaire peut-il dépendre ?",
        "choices": ["API", "Base de données", "API et base de données", "Aucune des réponses"],
        "correct_choice": 3
    },
    {
        "question": "Quelle déclaration est correcte dans le cadre d'un test ?",
        "choices": ["def setUp(self)", "def tearDown(self)", "test_isupper(self)", "Toutes les réponses"],
        "correct_choice": 3
    },
    {
        "question": "Quel est la bonne instruction ?",
        "choices": ["echo 'Hello world'", "print('Hello world')", "printf('Hello world')", "Aucune des réponses"],
        "correct_choice": 1
    },
    {
        "question": "Quel est le résultat de cette instruction ?\n\nprint(2**3 + (5 + 6)**(1 + 1))",
        "choices": ["129", "8", "121", "Aucune des réponses"],
        "correct_choice": 0
    },
    {
        "question": "Quel sont les types de données de la variable var ci-dessous ?\n\nvar = 10\nprint(type(var))\nvar = 'Hello'\nprint(type(var))",
        "choices": ["str et int", "int et int", "int et str", "Aucune des réponses"],
        "correct_choice": 2
    },
    {
        "question": "Quel est le résultat final de ces instructions ?\n\na = [1, 2, 3]\na = tuple(a)\na[0] = 2\nprint(a)",
        "choices": ["[2, 2, 2]", "(2, 2, 2)", "Erreur d'exécution", "Aucune des réponses"],
        "correct_choice": 2
    },
    {
        "question": "Quel est le résultat final de ces instructions ?\n\nprint(type(5 / 2))\nprint(type(5 // 2))",
        "choices": ["float et float", "int et int", "float et int", "int et float"],
        "correct_choice": 2
    },
    {
        "question": "Quel est le résultat de ces instructions ?\n\na = 3\nb = 1\nprint(a, b)\na, b = b, a\nprint(a, b)",
        "choices": ["3 1    1 3", "3 1    3 1", "1 3    1 3", "1 3    3 1"],
        "correct_choice": 0
    },
    {
        "question": "Quel est le résultat de ces instructions ?\n\nexample = ['Sunday', 'Monday', 'Tuesday', 'Wednesday'];\nprint(example[-3:-1])",
        "choices": ["['Monday', 'Tuesday']", "['Sunday', 'Monday']", "['Tuesday', 'Wednesday']", "['Wednesday', 'Monday']"],
        "correct_choice": 0
    },
    {
        "question": "Quel est le résultat de ces instructions ?\n\nword = 'Python Programming'\n"
                    "n = len(word)\nword1 = word.upper()\nword2 = word.lower()\nconverted_word = ''\n"
                    "for i in range(n):\n  if i % 2 == 0:\n    converted_word += word2[i]\n  else:\n    converted_word += word1[i]\nprint(converted_word)",
        "choices": ["pYtHoN PrOgRaMmInG", "Python Programming", "python programming", "PYTHON PROGRAMMING"],
        "correct_choice": 0
    }
]

score = 0

for i, question in enumerate(questions, start=1):
    print(f"Question {i}: {question['question']}")
    for j, choice in enumerate(question['choices']):
        print(f"{j + 1}. {choice}")

    user_choice = int(input("Votre réponse (1, 2, 3 ou 4) : "))
    
    if user_choice - 1 == question['correct_choice']:
        print("Bonne réponse!\n")
        score += 1
    else:
        print(f"Mauvaise réponse. La réponse correcte est : {question['choices'][question['correct_choice']]}\n")

print(f"Votre score final est de {score}/{len(questions)}.")
