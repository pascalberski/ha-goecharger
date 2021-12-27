"""
Integrates your go-eCharger with Home Assistant

For more details about this integration, please refer to
https://github.com/pascalberski/ha-goecharger
"""
import logging

from homeassistant.const import CONF_HOST
from homeassistant.core import Config, HomeAssistant
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv
from homeassistant.exceptions import PlatformNotReady

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
    host = charger_config.get(CONF_HOST)

    client = ChargerApiClient(host)

    hass.data[DOMAIN]["host"] = host
    hass.data[DOMAIN]["client"] = client

    
    _LOGGER.debug("initialising sensor coordinator")
    sensor_coordinator = SensorDataUpdateCoordinator(hass, client)
    await sensor_coordinator.async_refresh()

    if not sensor_coordinator.last_update_success:
        _LOGGER.error("Unable to get data from charger")
        raise PlatformNotReady

    hass.data[DOMAIN]["sensor_coordinator"] = sensor_coordinator

    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)

    return True
