from flask import Flask, render_template, request

app = Flask(__name__)

def area_cuadrado(lado):
    return lado * lado

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        lado = float(request.form['lado'])
        resultado = f"Área del cuadrado: {area_cuadrado(lado)}"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)