from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ejercicio1', methods=['POST', 'GET'])
def ejercicio1():
    if request.method == "POST":
        n1 = float (request.form['n1'])
        n2 = float(request.form[ 'n2' ])
        n3 = float(request.form[ 'n3' ])
        promedio = float(( n1 + n2 + n3) / 3)
        
        asistencia = float(request.form[ 'asistencia' ])
        aprobado = promedio >= 40 and asistencia >= 75
        resultado =  "Aprobado" if aprobado  else "Reprobado"
        return render_template("ejercicio1.html", promedio=promedio, resultado=resultado)
    
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
       