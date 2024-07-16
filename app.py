from flask import Flask, request, render_template
import numpy as np

# Crear la aplicación Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/decision", methods=['POST'])
def decision():
    player1_name = request.form['Player1_name']
    player2_name = request.form['Player2_name']
    tourney_name = request.form['tourney_name']
    surface = request.form['surface']
    round = request.form['round']

    # Generar aleatoriamente la recomendación
    recomendaciones = ["Apostar a jugador 1", "Apostar a jugador 2", "No apostar"]
    decision = np.random.choice(recomendaciones)

    return render_template('index.html', decision=decision)

# Python main
if __name__ == "__main__":
    app.run(debug=True)