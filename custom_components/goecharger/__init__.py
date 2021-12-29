"""
Integrates your go-eCharger with Home Assistant

For more details about this integration, please refer to
https://github.com/pascalberski/ha-goecharger
"""
import logging
from homeassistant.const import CONF_ID

from homeassistant.core import Config, HomeAssistant
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv
from homeassistant.exceptions import PlatformNotReady

from .const import CONF_HOST, CONF_NAME, CONF_CHARGERS

from .const import (
    DOMAIN,
    STARTUP_MESSAGE,
)
from .charger import ChargerApiClient
from .coordinators import (
    SensorDataUpdateCoordinator,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration"""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
        _LOGGER.debug(STARTUP_MESSAGE)

    charger_config = config[DOMAIN]
    # Configuration
    #host = charger_config.get(CONF_HOST)

    chargers = charger_config.get(CONF_CHARGERS)
    sensor_coordinators = []

    for charger in chargers:
        host = charger.get(CONF_HOST)
        charger_name = charger.get(CONF_NAME)
        charger_id = charger.get(CONF_ID)

        client = ChargerApiClient(host)

        _LOGGER.debug(f"initialising sensor coordinator - {charger_id} - {charger_name} - {host}")
        sensor_coordinator = SensorDataUpdateCoordinator(hass, client, charger_id, charger_name)
        await sensor_coordinator.async_refresh()

        if not sensor_coordinator.last_update_success:
            _LOGGER.error("Unable to get data from charger")
            raise PlatformNotReady

        sensor_coordinators.append(sensor_coordinator)

    hass.data[DOMAIN]["sensor_coordinators"] = sensor_coordinators

    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)

    return True
