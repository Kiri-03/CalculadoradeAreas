from flask import Flask, render_template, request

app = Flask(__name__)

def area_cuadrado(lado):
    return lado * lado

def area_triangulo(base, altura):
    return (base * altura) / 2

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        figura = request.form['figura']
        if figura == 'cuadrado':
            lado = float(request.form['lado'])
            resultado = f"Área del cuadrado: {area_cuadrado(lado)}"
        elif figura == 'triangulo':
            base = float(request.form['base'])
            altura = float(request.form['altura'])
            resultado = f"Área del triángulo: {area_triangulo(base, altura)}"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)