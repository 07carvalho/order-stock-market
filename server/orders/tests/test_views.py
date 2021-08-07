import pytest
from django.urls import reverse
from freezegun import freeze_time


@freeze_time("2020-01-01")
@pytest.mark.django_db
@pytest.mark.parametrize(
    "payload,expected_status_code",
    [
        (
            {
                "isin": "DE0005545503",
                "limit_price": 999.99,
                "side": "sell",
                "valid_until": 1659894673,
                "quantity": 99,
            },
            201,
        ),
        (
            {
                "isin": "DE0005545503",
                "limit_price": 999.99,
                "side": "buy",
                "valid_until": 1659894673,
                "quantity": 99,
            },
            201,
        ),
        (
            {
                "isin": "DE0005545503",
                "limit_price": 999.99,
                "side": "borrow",
                "valid_until": 1659894673,
                "quantity": 99,
            },
            400,
        ),
    ],
)
def test_create_with_full_order_payload(client, payload, expected_status_code):
    url = reverse("orders-list")
    response = client.post(url, data=payload, format="json")
    assert response.status_code == expected_status_code


@pytest.mark.django_db
def test_limit_price_validation(client, invalid_limit_price_message):
    url = reverse("orders-list")
    payload = {
        "isin": "DE0005545503",
        "limit_price": 0,
        "side": "sell",
        "valid_until": 1659894673,
        "quantity": 99,
    }
    response = client.post(url, data=payload, format="json")
    assert response.status_code == 400
    assert response.json() == invalid_limit_price_message


@pytest.mark.django_db
def test_valid_until_validation(client, invalid_valid_until_message):
    url = reverse("orders-list")
    payload = {"isin": "DE0005545503", "side": "sell", "valid_until": 123, "quantity": 99}
    response = client.post(url, data=payload, format="json")
    assert response.status_code == 400
    assert response.json() == invalid_valid_until_message


@pytest.mark.django_db
def test_quantity_validation(client, invalid_quantity_message):
    url = reverse("orders-list")
    payload = {
        "isin": "DE0005545503",
        "side": "sell",
        "valid_until": 1659894673,
        "quantity": 0,
    }
    response = client.post(url, data=payload, format="json")
    assert response.status_code == 400
    assert response.json() == invalid_quantity_message


@pytest.mark.django_db
def test_use_get_method(client):
    url = reverse("orders-list")
    response = client.get(url)
    assert response.status_code == 405
