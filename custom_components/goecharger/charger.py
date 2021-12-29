"""
go-eCharger API interface

References:
 - https://github.com/goecharger/go-eCharger-API-v2/
 - https://github.com/goecharger/go-eCharger-API-v1/
"""
import httpx
import logging


_LOGGER = logging.getLogger(__name__)


class ChargerApiClient:
    def __init__(self, host):
        self.host = host

    async def get_status(self):
        return await self.request("GET", "/status")

    async def request(self, method, path):
        async with httpx.AsyncClient() as client:
            url = "http://" + self.host + path
            _LOGGER.debug(url)

            response = await client.request(method, url)
            _LOGGER.debug(f"response: {response}")

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception("error while communication with charger api")
