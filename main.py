from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ejercicio1', methods=['POST', 'GET'])
def ejercicio1():
    if request.method == "POST":
        nombre = (request.form['nombre'])
        edad = int(request.form[ 'edad' ])
        cantidad = int(request.form[ 'cantidad' ])
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario
        descuento = 0
        if edad >= 18 and edad <= 30:
            descuento = 15
        elif edad > 30:
            descuento = 25
        
        total_descuento = total_sin_descuento * descuento / 100
        total = total_sin_descuento - total_descuento
        
        return render_template("ejercicio1.html", nombre=nombre, total_sin_descuento=total_sin_descuento, total_descuento=total_descuento, total=total)

    return render_template("ejercicio1.html")


@app.route('/ejercicio2', methods=['POST', 'GET'])
def ejercicio2():
    if request.method == "POST":
        nom1 = request.form[ 'nom1']
        nom2 = request.form[ 'nom2' ]
        nom3 = request.form[ 'nom3' ]
        mayor = max(nom1, nom2, nom3, key=len)
        cantidad = len(mayor)
        return render_template("ejercicio2.html", mayor=mayor, cantidad=cantidad)
    
    return render_template("ejercicio2.html")
       