import allure
import requests
import pytest

from helpers.urls import LOGIN_COURIER_URL


@allure.epic("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться;")
    @allure.title("Для авторизации нужно передать все обязательные поля")
    @allure.title("Успешный запрос возвращает id")
    def test_login_success(self, create_and_delete_courier):
        success_data = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"]
        }


        response = requests.post(LOGIN_COURIER_URL, data=success_data)

        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert "id" in response.json()



    @allure.title("Система вернёт ошибку, если неправильно указать логин или пароль")
    def test_invalid_password(self, create_and_delete_courier):
        unsuccess_data = {
            "login": create_and_delete_courier["login"],
            "password": "asdgsdbr"
        }
        response = requests.post(LOGIN_COURIER_URL, data=unsuccess_data)

        assert response.status_code == 404, f"Ошибка: {response.text}"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Если какого-то поля нет, запрос возвращает ошибку")
    def test_non_existent_field(self, create_and_delete_courier):
        unsuccess_data = {
            "password": create_and_delete_courier["login"],
        }
        response = requests.post(LOGIN_COURIER_URL, data=unsuccess_data)

        assert response.status_code == 400, f"Ошибка: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;")
    def test_non_existent_account(self, create_and_delete_courier):
        unsuccess_data = {
            "login": "asd",
            "password": create_and_delete_courier["password"]
        }
        response = requests.post(LOGIN_COURIER_URL, data=unsuccess_data)

        assert response.status_code == 404, f"Ошибка: {response.text}"
        assert response.json()["message"] == "Учетная запись не найдена"