from unittest.mock import patch
from external_api import fetch_product

@patch("external_api.requests.get")
def test_fetch_product(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {"product_name": "Milk", "brands": "TestBrand"}
    }

    result = fetch_product("123")
    assert result["product_name"] == "Milk"