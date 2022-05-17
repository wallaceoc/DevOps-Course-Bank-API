"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client: FlaskClient):
    # Use the client to make requests to the Flask app.
    # response = client.get('/example/route')
    # Or use client.post to make a POST request
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    pass
