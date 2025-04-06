import pytest
from unittest.mock import patch, Mock
from crypto import get_crypto_price, get_historical_data 

# Test para get_crypto_price
def test_get_crypto_price():
    price = get_crypto_price("bitcoin")
    assert isinstance(price, (int, float))
    assert price > 0

# Test para errores de API
@patch('requests.get')
def test_api_failure(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response
    
    price = get_crypto_price("bitcoin")
    assert price is None

# Test para datos históricos
@patch('requests.get')
def test_historical_data(mock_get):
    # Configuramos el mock para datos históricos
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "prices": [
            [1672531200000, 16500.0],  # [timestamp, precio]
            [1672617600000, 16800.0]
        ]
    }
    mock_get.return_value = mock_response
    
    dates, prices = get_historical_data("bitcoin", days=2)
    
    assert len(dates) == 2
    assert len(prices) == 2
    assert all(isinstance(x, float) for x in prices)
    assert prices[0] == 16500.0