from cities import Howto
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    ciudad1 = request.form['ciudad1']
    pais1 = request.form['pais1']
    ciudad2 = request.form['ciudad2']
    pais2 = request.form['pais2']
    opcion = request.form['opciones']
    distancia=Howto(ciudad1,pais1,ciudad2,pais2,opcion)
    return render_template('distance.html',opcion=opcion,distancia=distancia)

"""@app.route('/get-text', methods=['GET', 'POST'])
def vars():
    cities = request.form['test']
    print(cities)
    return render_template('index.html', cities=cities)
"""

if __name__ == '__main__':
    app.run(debug=True)
