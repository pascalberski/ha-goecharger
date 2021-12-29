"""
Sensor platform for Charger
"""
import logging

from homeassistant.core import Config, HomeAssistant

from .charger_sensors import StateSensor, AllowSensor, TotalEnergySensor, VoltageSensor

from .const import (
    DOMAIN,
)


_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
    hass: HomeAssistant, config: Config, async_add_entities, discovery_info=None
):
    """Setup charger sensor platform"""
    _LOGGER.debug("Creating new charger sensor components")

    data = hass.data[DOMAIN]
    # Configuration
    # host = data.get("host")
    # client = data.get("client")

    # charger sensors
    sensor_coordinator = data.get("sensor_coordinator")
    charger_sensors = create_charger_sensors(sensor_coordinator)
    async_add_entities(charger_sensors, True)


def create_charger_sensors(coordinator):
    charger_sensors = [
        StateSensor(coordinator),
        AllowSensor(coordinator),
        TotalEnergySensor(coordinator),
    ]

    for i in range(1, 4):
        charger_sensors.append(VoltageSensor(coordinator, i))

    return charger_sensors
