import pytest
from app import create_app

# Los tests buscaran las fixtures en el mismo file. Al no encontrarlas buscaran en conftest.py

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app  # taking it out of the scope


@pytest.fixture()
def client(app):
    return app.test_client()  # instancia de app flask para testing


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()