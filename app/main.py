# Importez le module Flask et la fonction load_dotenv
from flask import Flask
from dotenv import load_dotenv
import os

# Chargez les variables d'environnement depuis le fichier .env
load_dotenv()

# Initialisez l'application Flask
app = Flask(__name__)

# Désactivez la protection CSRF
app.config['WTF_CSRF_ENABLED'] = False

# Définissez une route pour renvoyer la chaîne de caractères inversée
@app.route('/<random_string>')
def return_backwards_string(random_string):
    return random_string[::-1]  # Inverser la chaîne de caractères

# Si le script est exécuté directement, lancez l'application Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
