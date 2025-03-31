from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(valeur):
        for i in range(valeur-j):
            etoiles += '*'
        etoiles += '<br>'
    return etoiles
  

if __name__ == "__main__":
    app.run(debug=True)
