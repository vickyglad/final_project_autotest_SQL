import configuration
import sender_stand_request
import data

# Виктория Гладырева, 12-я когорта — Финальный проект. Инженер по тестированию плюс

def get_order(track):
    track = post_new_order(data.headers).json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH + track)

def positive_assert(order):
    order_response = get_order(track)
    assert order_response.status_code == 200

def test_order():
    positive_assert




