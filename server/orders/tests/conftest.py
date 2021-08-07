import pytest


@pytest.fixture
def invalid_limit_price_message():
    return {"limit_price": ["Limit price must be greater than zero."]}


@pytest.fixture
def invalid_valid_until_message():
    return {"valid_until": ["Dates in the past are invalid"]}


@pytest.fixture
def invalid_quantity_message():
    return {"quantity": ["Quantity must be greater than zero."]}
