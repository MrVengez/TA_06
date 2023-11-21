from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = 0.0
    asistencia = 75
    resultado = ''
    aprob = 40.0

    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        numero3 = float(request.form['numero3'])
        asis = float(request.form['numero4'])
        promedio = (numero1 + numero2 + numero3) / 3

        if promedio >= aprob and asis >= asistencia:
            resultado = 'Felicitaciones !!! con tu Promedio de ' + str(promedio) + ' y Asistencia del ' + str(asis) + '% has aprobado la materia :D'

        elif promedio < aprob and asis >= asistencia:
            resultado = 'lastima !!! tu promedio fue ' + str(promedio) + ' con esta nota no alcanzas para aprobar y tu Asistencia fue ' + str(
                asis) + '% has reprobado esta vez :C'
        elif promedio >= aprob and asis < asistencia:
            resultado = 'lastima !!! tu promedio fue ' + str(promedio) + ' pero tu baja asistencia de ' + str(
                asis) + '% no alcanza para aprobar, has reprobado esta vez :C'
        else:
            resultado = 'Tu promedio ' + str(promedio) + ' o asistencia del ' + str(asis) + '% no alcanza para ser aprobado. Mejor suerte la próxima vez :C'

    return render_template('ejercicio1.html', resultado=resultado)




@app.route('/ejercicio2', methods=['GET', 'POST'])
def nombre_largo():
    resultado = ''

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        nombre_mas_largo = max(nombres, key=len)
        longitud_nombre_mas_largo = len(nombre_mas_largo)

        resultado = f'El nombre con más caracteres es "{nombre_mas_largo}" con {longitud_nombre_mas_largo} caracteres.'

    return render_template('ejercicio2.html', resultado=resultado)


if __name__ == '__main__':
    app.run()
