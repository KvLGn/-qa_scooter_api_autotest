# Ковалев Александр, 47-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def test_create_order_and_get_by_track():
    # Шаг 1: создать заказ
    create_response = sender_stand_request.create_order(data.order_body)
    assert create_response.status_code == 201

    # Шаг 2: сохранить номер трека
    track = create_response.json()["track"]

    # Шаг 3: получить заказ по треку
    get_response = sender_stand_request.get_order_by_track(track)

    # Шаг 4: проверить, что код ответа равен 200
    assert get_response.status_code == 200
