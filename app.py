from flask import Flask, render_template

app = Flask(__name__)

etudiants = [
    {"nom": "Aminata Dione", "note": 18},
    {"nom": "Mamadou Fall", "note": 17},
    {"nom": "Fatou Ndiaye", "note": 16},
    {"nom": "Ousmane Diop", "note": 14},
    {"nom": "Awa Sarr", "note": 12}
]

etudiants.sort(key=lambda x: x["note"], reverse=True)

@app.route('/')
def accueil():
    return render_template('index.html', etudiants=etudiants)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
