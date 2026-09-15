# Ковалев Александр, 47-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def test_create_order():
    response = sender_stand_request.create_order(data.order_body)
    assert response.status_code == 201
    assert "track" in response.json()


def test_get_order_by_track():
    create_response = sender_stand_request.create_order(data.order_body)
    track = create_response.json()["track"]

    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200
