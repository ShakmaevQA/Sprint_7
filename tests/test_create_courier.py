import allure
import requests
import pytest

from helpers.data import Data
from helpers.urls import CREATE_COURIER_URL


@allure.epic("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    @allure.title("Чтобы создать курьера, нужно передать в ручку все обязательные поля")
    @allure.title("Запрос возвращает правильный код ответа")
    @allure.title("Успешный запрос возвращает {'ok':true}")
    def test_create_valid_courier(self):

        courier_data = Data.create_valid_courier()

        with allure.step(f"Отправка POST-запроса на создание курьера с данными: {courier_data}"):
            response = requests.post(CREATE_COURIER_URL, data=courier_data)

        assert response.status_code == 201, f"Ошибка: {response.text}"
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_no_duplicate_courier(self, create_and_delete_courier):

        with allure.step(f"Отправка POST-запроса на создание дублирующего курьера с данными: {create_and_delete_courier}"):
            response = requests.post(CREATE_COURIER_URL, data=create_and_delete_courier)

        assert response.status_code == 409, f"Ошибка: {response.text}"
        assert response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title("Eсли одного из полей нет, запрос возвращает ошибку")
    def test_create_invalid_courier(self):
        courier_data = Data.create_invalid_courier()
        with allure.step(f"Отправка POST-запроса с неполными данными: {courier_data}"):
            response = requests.post(CREATE_COURIER_URL, data=courier_data)

        assert response.status_code == 400, f"Ошибка: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"


    @allure.title("Проверка обязательности всех полей для создания курьера")
    @pytest.mark.parametrize("missing_field", [
        "login",
        "password",
        "firstname"
    ])
    def test_missing_required_fields(self, missing_field):
        full_data = Data.create_valid_courier()

        incomplete_data = full_data.copy()
        incomplete_data.pop(missing_field)
        with allure.step(f"Отправка POST-запроса без поля '{missing_field}': {incomplete_data}"):
            response = requests.post(CREATE_COURIER_URL, data=incomplete_data)

        assert response.status_code == 400, f"Ошибка: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
