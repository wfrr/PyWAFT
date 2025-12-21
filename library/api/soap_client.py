from requests import Session
from zeep import Client, Transport


class SoapClient:
    def __init__(self, wsdl_url: str) -> None:
        self._wsdl_url = wsdl_url
        # self._service_url = service_url
        _session = Session()
        _transport = Transport(session=_session)
        self._client = Client(wsdl=wsdl_url, transport=_transport)
        self._service = self._client.service

    def __getattr__(self, name):
        return getattr(self._service, name)
