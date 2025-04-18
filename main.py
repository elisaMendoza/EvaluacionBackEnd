from flask import request, Flask, render_template, url_for, redirect, flash, session
from markupsafe import escape
import os

app = Flask(__name__)

# ruta de prueba
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/mostrardatos', methods=['POST', 'GET'])
def mostrardatos():
    if request.method == 'POST':
        anno = request.form['anno']
        marca = request.form['marca']
        color = request.form['color']
        combustible = request.form['combustible']
        numpuertas = request.form['numpuertas']
        traccion = request.form['traccion']
        if(not os.path.exists('data.csv')):
            with open('data.csv', 'w') as file:
                file.write(f"{anno};{marca};{color};{combustible};{numpuertas};{traccion}")
        else:
            with open('data.csv', 'a') as file:
                file.write(f"\n")
                file.write(f"{anno};{marca};{color};{combustible};{numpuertas};{traccion}")
        return render_template('mostrardatos.html', anno=anno, marca=marca, color=color, combustible=combustible, numpuertas=numpuertas, traccion=traccion)

    @app.route('/mostrardatos', methods=['GET', 'POST'])
    def mostrardatos():
        if request.method == 'POST':
            anno = request.form['anno']
            marca = request.form['marca']
            color = request.form['color']
            combustible = request.form['combustible']
            numpuertas = request.form['numpuertas']
            traccion = request.form['traccion']
            if not os.path.exists('data.csv'):
                with open('data.csv', 'w') as file:
                    file.write(f"{anno};{marca};{color};{combustible};{numpuertas};{traccion}")
            else:
                with open('data.csv', 'a') as file:
                    file.write(f"\n{anno};{marca};{color};{combustible};{numpuertas};{traccion}")
            return render_template('mostrardatos.html', anno=anno, marca=marca, color=color, combustible=combustible, numpuertas=numpuertas, traccion=traccion)
        elif request.method == 'GET':
            if os.path.exists('data.csv'):
                with open('data.csv', 'r') as file:
                    data = file.readlines()
                return render_template('mostrardatos.html', data=data)
            else:
                flash("No data available.")
                return redirect(url_for('registro'))

if __name__ == '__main__':
    app.run(debug=True)