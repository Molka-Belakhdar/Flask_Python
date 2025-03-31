from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(1, valeur + 1):
        etoiles += ' ' * (valeur - j) + '*' * j + '<br>'
    return etoiles
  

if __name__ == "__main__":
    app.run(debug=True)
