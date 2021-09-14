import pytest

import api.api


@pytest.fixture
def client():
    api.api.app.config["TESTING"] = True
    with api.api.app.test_client() as client:
        yield client


def test_echo_correct_input(client):
    post_data = {"username": "xyz", "upload": "xyz"}
    correct_response = {"username": "xyz", "upload": "xyz", "echoed": True}
    value = client.post('/api/echo', json=post_data)
    assert correct_response == value.get_json()


def test_echo_correct_input_put_method(client):
    post_data = {"username": "xyz", "upload": "xyz"}
    correct_response = {"username": "xyz", "upload": "xyz", "echoed": True}
    value = client.put('/api/echo', json=post_data)
    assert correct_response == value.get_json()


def test_echo_preexisting_field_true(client):
    post_data = {"username": "xyz", "upload": "xyz", "echoed": True}
    value = client.post('/api/echo', json=post_data)
    assert value.status == '400 BAD REQUEST'


def test_echo_preexisting_field_other(client):
    post_data = {"username": "xyz", "upload": "xyz", "echoed": "xyz"}
    correct_response = {"username": "xyz", "upload": "xyz", "echoed": True}
    value = client.post('/api/echo', json=post_data)
    assert correct_response == value.get_json()


def test_echo_bad_post_data(client):
    post_data = """lalalalalala:{}{}echoed"""
    value = client.post('/api/echo', json=post_data)
    assert value.status == '400 BAD REQUEST'
