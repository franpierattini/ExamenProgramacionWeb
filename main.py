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



usuarios = {
    "juan": "admin",
    "pepe": "user"
}



@app.route('/ejercicio2', methods=['POST', 'GET'])
def ejercicio2():
    error = None
    mensaje = None
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contrasena = request.form['contrasena']

        # Verificar si el usuario y la contraseña son correctos
        if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
            if nombre_usuario == 'juan':
                mensaje = f"Bienvenido administrador {nombre_usuario}"
            else:
                mensaje = f"Bienvenido usuario {nombre_usuario}"
        else:
            error = "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."

    return render_template("ejercicio2.html", error=error, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

