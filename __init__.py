
from flask import Flask

app = Flask(__name__)

def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]
    max_val = liste_nombres[0]
    for n in liste_nombres[1:]:
        if n > max_val:
            max_val = n
    return str(max_val)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
