"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_account_creation(client: FlaskClient):
    # Use the client to make requests to the Flask app.
    # response = client.get('/example/route')
    # Or use client.post to make a POST request
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    pass
