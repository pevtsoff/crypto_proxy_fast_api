import json
from unittest.mock import MagicMock, patch

from fastapi import HTTPException
from fastapi.testclient import TestClient

from ..app import app

client = TestClient(app)


def load_mock_data(filename):
    with open(f"./mock_data/{filename}", "r") as file:
        data = file.read()

    return data


def test_get_block_by_number_no_cache():
    request_mock = MagicMock()
    memcached_mock = MagicMock()
    response = MagicMock()
    mock_data = load_mock_data("cloud_flare_response.txt")

    response.text = mock_data
    request_mock.post.return_value = response
    response.raise_for_status.return_value = None
    expected = json.loads(mock_data)

    with patch("crypto_proxy.services.cloud_flare.mc_client.get", return_value=None):
        with patch("crypto_proxy.services.cloud_flare.requests", request_mock):
            with patch("crypto_proxy.services.cloud_flare.mc_client.set", memcached_mock):

                response = client.get("/cf_proxy/block/0x200100")
                assert response.json() == expected


def test_get_block_by_number_cache():
    memcached_mock = MagicMock()
    mock_data = load_mock_data("cloud_flare_response.txt")
    memcached_mock.return_value = mock_data
    expected = json.loads(mock_data)

    with patch("crypto_proxy.services.cloud_flare.mc_client.get", memcached_mock):
        response = client.get("/cf_proxy/block/0x200100")
        assert response.json() == expected


def test_get_404_error_for_non_existing_block():
    with patch("crypto_proxy.services.cloud_flare.mc_client.get", return_value=None):
        with patch(
            "crypto_proxy.services.cloud_flare.BlockService._get_cf_block_data",
            side_effect=HTTPException(status_code=404, detail="Block #xxx  not found"),
        ):

            response = client.get("/cf_proxy/block/0x200100")
            assert response.json() == {"detail": "Block #xxx  not found"}


def test_get_transaction_by_hash():
    pass


def test_get_transaction_by_index():
    pass


def test_get_404_for_non_exisiting_transaction():
    pass
