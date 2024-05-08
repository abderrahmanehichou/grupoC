from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class Paises(db.Model):

    rowid = db.Column(db.Integer, primary_key=True)
    siglas = db.Column(db.String(5), unique=True, nullable=False)
    nombre = db.Column(db.String(200), unique=True, nullable=False)
    poblacion = db.Column(db.Integer, unique=False, nullable=False)
    extension = db.Column(db.Integer, unique=False, nullable=False)
    temperatura = db.Column(db.Integer, unique=False, nullable=False)
    lluvia = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, siglas, nombre, poblacion, extension, temperatura, lluvia):
        super().__init__()
        self.siglas = siglas
        self.nombre = nombre
        self.poblacion = poblacion
        self.extension = extension
        self.temperatura = temperatura
        self.lluvia = lluvia


    def __str__(self):
        return "\Siglas: {}. Nombre: {}. Poblacion: {}. Extension: {}. Temperatura: {}. LLuvia: {}. \n".format(
            self.siglas,
            self.nombre,
            self.poblacion,
            self.extension,
            self.temperatura,
            self.lluvia,

        )

    def serialize(self):
        return{
            "rowid": self.rowid,
            "siglas": self.siglas,
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "extension": self.extension,
            "temperatura": self.temperatura,
            "lluvia" : self.lluvia,
            
        }