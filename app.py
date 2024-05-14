from flask import Flask, jsonify, request, render_template, Response
from Models import db, Paises
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/paises.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False
app.config["JSON_AS_ASCII"] = False  # Configurar para que los JSON utilicen UTF-8
db.init_app(app)


#Aquí empiezan las rutas
@app.route("/")
def home():
    return render_template("index.html")

""" @app.route("/searchpais", methods=["GET"])
def searchpais():
    return render_template("searchpais.html") """


""" @app.route("/api/paises", methods=["GET"])
def getPaises():
    try:
        
        paises = Paises.query.all()
        toReturn = [pais.serialize() for pais in paises]
        return jsonify(toReturn), 200

    except Exception:
        
        exception("[SERVER]: Error ->")
        return render_template("error.html"), 500 """

""" @app.route("/api/pais/<string:nombre>", methods=["GET"])
def getPaisByName(nombre):
    try:
        pais = Paises.query.filter_by(nombre=nombre).first()
        if not pais:
            return render_template("dont_exist.html"), 200
        else:
            return jsonify(pais.serialize()), 200
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500 """

    
""" @app.route("/api/pais/siglas/<string:siglas>", methods=["GET"])
def getPaisBySiglas(siglas):
    try:
        pais = Paises.query.filter_by(siglas=siglas).first()
        if not pais:
            return render_template("dont_exist.html"), 200
        else:
            return jsonify(pais.serialize()), 200
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500 """


""" @app.route("/api/pais/poblacion/<int:poblacion>", methods=["GET"])
def getPaisesByPoblacion(poblacion):
    try:
        paises = Paises.query.filter_by(poblacion=poblacion).all()
        if not paises:
            return jsonify({"msg": f"No hay paises con la población de: '{poblacion}'"}), 404
        else:
            return jsonify([pais.serialize() for pais in paises]), 200
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return jsonify({"msg": "Ha ocurrido un error"}), 500 """



""" @app.route("/api/pais", methods=["POST"])
def addPais():
    try:
        data = request.json
        nuevo_pais = Paises(**data)
        db.session.add(nuevo_pais)
        db.session.commit()
        return jsonify({"msg": "País agregado correctamente"}), 201
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500 """
    



""" @app.route("/api/pais/<string:siglas>", methods=["PUT"])
def updatePais(siglas):
    try:
        pais = Paises.query.get(siglas)
        if not pais:
            return render_template("dont_exist.html"), 404
        data = request.json
        for key, value in data.items():
            setattr(pais, key, value)
        db.session.commit()
        return jsonify({"msg": "País actualizado correctamente"}), 200
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500 """
    



""" @app.route("/api/pais/<string:siglas>", methods=["DELETE"])
def deletePais(siglas):
    try:
        pais = Paises.query.get(siglas)
        if not pais:
            return render_template("dont_exist.html"), 404
        db.session.delete(pais)
        db.session.commit()
        return jsonify({"msg": "País eliminado correctamente"}), 200
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500 """

#Aquí empiezan las rutas de front


@app.route("/api/addpais", methods=["POST"])
def addpais():
    try:
        siglas = request.form["siglas"]
        nombre = request.form["nombre"]
        poblacion = request.form["poblacion"]
        extension = request.form["extension"]
        temperatura = request.form["temperatura"]
        lluvia = request.form["lluvia"]

        pais = Paises(siglas, nombre, int(poblacion), int(extension), int(temperatura), int(lluvia) )
        db.session.add(pais)
        db.session.commit()

        return render_template("add_pais.html", pais=pais.serialize())
    
    except Exception:
        exception("\n[SERVER]: Error in route /api/addpais. Log: \n")
        return render_template("error.html"), 500


# Buscar mediante formulario
""" @app.route("/api/searchpais", methods=["POST"])
def searchPaisForm():
    try:
        namePais = request.form["nombre"]

        pais = Paises.query.filter(Paises.nombre.like(f"%{namePais}%")).first()
        if not pais:
            return render_template("result.html", pais=pais), 200
        else:
            return render_template("result.html", pais=pais.serialize())
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500 """



@app.route("/api/pais/delete", methods=["POST", "DELETE"])
def deletePaisForm():
    try:
        nombre = request.form.get("nombre")
        pais = Paises.query.filter_by(nombre=nombre).first()
        if not pais:
            return render_template("dont_exist.html"), 404
        db.session.delete(pais)
        db.session.commit()
        return render_template("delete_success.html"), 200  # Renderiza el template HTML
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500
        

@app.route("/api/pais/search", methods=["POST"])
def searchPaisFormu():
    try:
        namePais = request.form["nombre"]

        pais = Paises.query.filter(Paises.nombre.like(f"%{namePais}%")).first()
        if not pais:
            return render_template("result.html", pais=pais), 200
        else:
            return render_template("result.html", pais=pais.serialize())
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500
    
@app.route("/paises")
def listPaises():
    try:
        paises = Paises.query.all()
        return render_template("list_paises.html", paises=paises)
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500
    


@app.route("/api/modificarpais", methods=["POST"])
def modificarpais():
    try:
        nombre_pais = request.form.get("nombre")
        pais = Paises.query.filter_by(nombre=nombre_pais).first()
        if not pais:
            return render_template("dont_exist.html"), 404
        return render_template("modify_pais.html", pais=pais.serialize()), 200
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500 

@app.route("/api/modificarpais/<string:siglas>", methods=["POST"])
def modificarPais(siglas):
    try:
        pais = Paises.query.filter_by(siglas=siglas).first()

        if not pais:
            return render_template("dont_exist.html"), 404
        
        # Actualizar los campos del país según los datos enviados en el formulario
        data = request.form
        for key, value in data.items():
            setattr(pais, key, value)
        
        db.session.commit()
        return render_template("modify_ok.html", pais=pais.serialize())
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return render_template("error.html"), 500



if __name__ =="__main__":
    app.run(debug=True, port=5000)

