from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-text', methods=['GET', 'POST'])
def vars():
    cities = request.form['test']
    print(cities)
    return render_template('index.html', cities=cities)


if __name__ == '__main__':
    app.run()