import allure
import requests
import pytest

from helpers.data import Data
from helpers.urls import GET_ORDERS_URL


@allure.epic("Просмотр заказов")
class TestOrderList:

    @allure.title("Просмотр списка заказов")
    def test_order_list(self):
        response = requests.get(GET_ORDERS_URL)

        assert response.status_code == 200, f"Ошибка: {response.text}"