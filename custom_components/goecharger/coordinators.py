"""
go-eCharger sensor data update coordinator
"""
from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import (
    DOMAIN,
)
from .charger import ChargerApiClient

REFRESH_INTERVAL_STATUS = timedelta(minutes=1)

_LOGGER = logging.getLogger(__name__)


class SensorDataUpdateCoordinator(DataUpdateCoordinator):
    """Manages fetching Status Data from charger api"""

    def __init__(self, hass: HomeAssistant, client: ChargerApiClient):
        """Initialize"""
        self.name = f"{DOMAIN}_sensor_coordinator"
        self._client = client

        super().__init__(
            hass, _LOGGER, name=self.name, update_interval=REFRESH_INTERVAL_STATUS
        )

    async def _async_update_data(self):
        """Update charger sensors"""
        try:
            return await self._client.get_status()
        except Exception as exc:
            raise UpdateFailed from exc
