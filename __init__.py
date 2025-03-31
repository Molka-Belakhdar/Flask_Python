from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue ! Ajoutez un nombre dans l'URL pour voir des étoiles."

@app.route('/<int:valeur>')
def exercice(valeur):
    return '*' * valeur  

if __name__ == "__main__":
    app.run(debug=True)
