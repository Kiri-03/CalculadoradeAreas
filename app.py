from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        figura = request.form.get('figura')

        try:
            if figura == 'cuadrado':
                lado = float(request.form.get('lado', 0))
                resultado = f"Área del cuadrado: {lado ** 2:.2f}"

            elif figura == 'triangulo':
                base = float(request.form.get('base', 0))
                altura = float(request.form.get('altura', 0))
                resultado = f"Área del triángulo: {(base * altura) / 2:.2f}"

            elif figura == 'rectangulo':
                base = float(request.form.get('base', 0))
                altura = float(request.form.get('altura', 0))
                resultado = f"Área del rectángulo: {base * altura:.2f}"

            else:
                resultado = "Por favor selecciona una figura válida."

        except ValueError:
            resultado = "Por favor ingresa valores numéricos válidos."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
