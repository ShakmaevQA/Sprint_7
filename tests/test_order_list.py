import allure
import requests
import pytest

from helpers.urls import GET_ORDERS_URL


@allure.epic("Просмотр заказов")
class TestOrderList:

    @allure.title("Просмотр списка заказов")
    def test_order_list(self):
        with allure.step("Отправка GET-запроса для получения списка заказов"):
            response = requests.get(GET_ORDERS_URL)

        assert response.status_code == 200, f"Ошибка: {response.text}"

        response_json = response.json()
        with allure.step("Проверка наличия ключей в теле ответа"):
            assert "orders" in response_json, "В ответе отсутствует ключ 'orders'"
            assert "pageInfo" in response_json, "В ответе отсутствует ключ 'pageInfo'"
            assert "availableStations" in response_json, "В ответе отсутствует ключ 'availableStations'"

        with allure.step("Проверка структуры 'pageInfo'"):
            page_info = response_json["pageInfo"]
            assert "page" in page_info, "В 'pageInfo' отсутствует ключ 'page'"
            assert "total" in page_info, "В 'pageInfo' отсутствует ключ 'total'"
            assert "limit" in page_info, "В 'pageInfo' отсутствует ключ 'limit'"
