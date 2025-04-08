import allure
import requests
import pytest

from helpers.data import Data
from helpers.urls import CREATE_ORDER_URL

@allure.epic("Создание заказа")
class TestCreateOrder:

    @allure.title("Можно создать заказ с разными вариантами цвета")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_colors(self, color):

        color_order = Data.create_order(color)

        with allure.step(f"Отправка POST-запроса на создание заказа с цветом: {color}"):
            response = requests.post(CREATE_ORDER_URL, json=color_order)

        assert response.status_code == 201, f"Ошибка: {response.text}"
        assert "track" in response.json(), "Ответ не содержит track"