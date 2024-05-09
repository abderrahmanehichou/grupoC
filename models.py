from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
class paises(db.model):
    rowid = db.column(db.Integer,primary_key=True)
    siglas  = db.column(db.string(200),unique=True,nullable=False)
    name = db.column(db.string(200),unique=True,nullable=False)
    nombre = db.column(db.integer)
    poblacion = db.column(db.integer)
    extension =db.column(db.integer)
    lluvia = db.column(db.integer)
        