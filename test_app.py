from app import app, db, Paises
import pytest

@pytest.fixture
def app_context():
    """Fixture para establecer el contexto de la aplicación Flask."""
    with app.app_context():
        yield

@pytest.fixture
def client(app_context):
    """Fixture para proporcionar un cliente de prueba."""
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data  # Comprueba si se ha devuelto una página HTML

def test_add_pais(client):
    data = {
        'siglas': 'ES',
        'nombre': 'España',
        'poblacion': 47000000,
        'extension': 505990,
        'temperatura': 20,
        'lluvia': 600
    }
    response = client.post('/api/addpais', data=data)
    assert response.status_code == 200
    encoded_string = 'España'.encode('utf-8')
    assert encoded_string in response.data


def test_buscar_pais(client):
    # Agrega un país para luego buscarlo
    pais = Paises(siglas="ES", nombre="España", poblacion=47000000, extension=505990, temperatura=20, lluvia=600)
    db.session.add(pais)
    db.session.commit()

    # Realiza la solicitud para buscar el país
    response = client.post('/api/pais/search', data={"nombre": "España"})

    # Verifica que se haya encontrado correctamente
    assert response.status_code == 200
    encoded_string = 'España'.encode('utf-8')
    assert encoded_string in response.data


def test_eliminar_pais(client):
    # Agrega un país para luego eliminarlo
    with app.app_context():
        pais = Paises(siglas="ES", nombre="España", poblacion=47000000, extension=505990, temperatura=20, lluvia=600)
        db.session.add(pais)
        db.session.commit()

        # Realiza la solicitud para eliminar el país
        response = client.post('/api/pais/delete', data={"nombre": "España"})



def test_modificar_pais(client):
    # Agrega un país para luego modificarlo
    with app.app_context():
        pais = Paises(siglas="ES", nombre="España", poblacion=47000000, extension=505990, temperatura=20, lluvia=600)
        db.session.add(pais)
        db.session.commit()

        # Realiza la solicitud para modificar el país
        response = client.post('/api/modificarpais/ES', data={"nombre": "España Modificada"})

