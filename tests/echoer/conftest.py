import pytest

from library.api.api_client import ApiClient
from library.api.soap_client import SoapClient
from library.core.app_data import AppData
from library.echo import routes


@pytest.fixture
def api_client(stand: AppData) -> ApiClient:
    """API-клиент echoer."""
    return ApiClient(base_url=stand.echoer["url"])


@pytest.fixture
def soap_client(stand: AppData) -> SoapClient:
    """Soap-клиент echoer."""
    wsdl_url = stand.echoer["url"] + routes.ECHOER_SOAP_WSDL
    return SoapClient(wsdl_url=wsdl_url)
