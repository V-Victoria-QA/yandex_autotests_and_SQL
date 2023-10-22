# Вакурова Виктория, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import data
import configuration

# Функция на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,  # подставляем полный url
                         json=order_body,
                         headers=data.headers)  # а здесь заголовки)

# Функция, которая вызывает функцию создания заказа и возвращает track из JSON-ответа
def post_order_and_fetch_track(order_body):
    order_response = post_new_order(order_body)
    return order_response.json()['track']

# Функция на получение заказа по треку заказа
def get_order_by_track(track_number):
    url = configuration.URL_SERVICE + f"/api/v1/orders/track?t={track_number}"
    response = requests.get(url, headers=data.headers)
    return response

# Функция для позитивной проверки
def possitive_assert(order_body):
    track_number = post_order_and_fetch_track(order_body)
    track_response = get_order_by_track(track_number)

    assert track_response.status_code == 200

# # Тест. Успешное получение заказа по его номеру.
def test_possitive_assert():
    possitive_assert(data.order_body)

