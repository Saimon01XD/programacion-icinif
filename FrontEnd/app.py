from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__) #FLASK name ME INICIa EL PROYECTO; PIDO QUE ME LO GUARDE EN app
app._static_folder = 'templates/static'     #FUNCIONO CONCHATUMAREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/MRuta.db"   # ... = "sql..." se establece que trabajare con sqlite, luego digo donde estara mi base de datos
db = SQLAlchemy(app) #AQUI INICIALIZO SQLALCHEMY




 
@app.route("/")
def index() :
    return render_template("index.html")     #AQUI CADA VEZ QUE SE CAMBIE CODIGO; EL SERVIDOR SE REINICIARA

if __name__ == "__main__" :
    app.run(debug = True)


#Para ejecutar "  python app.py  " ; Hasta aqui, si se inicializa el servidor saldra error, no asustarse
