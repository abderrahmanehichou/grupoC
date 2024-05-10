import pytest
from app import app
from Models import db, Paises


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Insertar datos de prueba en la base de datos
            # Esto es opcional dependiendo de tus necesidades de prueba
            p1 = Paises(siglas="US", nombre="Estados Unidos", poblacion=328200000, extension=9834000, temperatura=15, lluvia=1000)
            p2 = Paises(siglas="CN", nombre="China", poblacion=1439323776, extension=9597000, temperatura=18, lluvia=641)
            db.session.add_all([p1, p2])
            db.session.commit()
        yield client
        # Limpiar la base de datos después de las pruebas
        db.drop_all()

def test_get_paises(client):
    response = client.get("/api/paises")
    assert response.status_code == 200
    assert len(response.json) == 2  # Verificar que se devuelvan todos los países

def test_get_pais_by_name(client):
    response = client.get("/api/pais/Estados Unidos")
    assert response.status_code == 200
    assert response.json["siglas"] == "US"

def test_add_pais(client):
    data = {
        "siglas": "CA",
        "nombre": "Canadá",
        "poblacion": 38008005,
        "extension": 9976140,
        "temperatura": -5,
        "lluvia": 544
    }
    response = client.post("/api/pais", json=data)
    assert response.status_code == 201
    assert response.json["msg"] == "País agregado correctamente"

