import pytest
import requests
from helpers.urls import CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL
from helpers.data import Data


@pytest.fixture
def create_and_delete_courier():
    courier = Data.create_valid_courier()
    create_response = requests.post(CREATE_COURIER_URL, data=courier)
    login_response = requests.post(LOGIN_COURIER_URL, data={
        "login": courier["login"],
        "password": courier["password"]
    })
    courier_id = login_response.json().get("id")
    yield courier
    delete_response = requests.delete(f"{DELETE_COURIER_URL}/{courier_id}")