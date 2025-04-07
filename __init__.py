from flask import Flask

app = Flask(name)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]
    max_valeur = liste_nombres[0]
    for n in liste_nombres:
        if n > max_valeur:
            max_valeur = n

    return str(max_valeur)

if name == 'main':
    app.run(host='0.0.0.0')
