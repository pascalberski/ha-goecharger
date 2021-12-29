"""
Sensor platform for Charger
"""
import logging

from homeassistant.core import Config, HomeAssistant

from .charger_sensors import (
    CurrentSensor,
    PowerSensor,
    StateSensor,
    AllowSensor,
    TotalEnergySensor,
    TotalPowerSensor,
    VoltageSensor,
)

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
    sensor_coordinators = data.get("sensor_coordinators")
    for sensor_coordinator in sensor_coordinators:
        charger_sensors = create_charger_sensors(sensor_coordinator)
        async_add_entities(charger_sensors, True)


def create_charger_sensors(coordinator):
    charger_sensors = [
        StateSensor(coordinator, coordinator.charger_id, coordinator.charger_name),
        AllowSensor(coordinator, coordinator.charger_id, coordinator.charger_name),
        TotalEnergySensor(
            coordinator, coordinator.charger_id, coordinator.charger_name
        ),
        TotalPowerSensor(coordinator, coordinator.charger_id, coordinator.charger_name),
    ]

    for i in range(1, 4):
        charger_sensors.append(
            VoltageSensor(
                coordinator, coordinator.charger_id, coordinator.charger_name, i
            )
        )
        charger_sensors.append(
            CurrentSensor(
                coordinator, coordinator.charger_id, coordinator.charger_name, i
            )
        )
        charger_sensors.append(
            PowerSensor(
                coordinator, coordinator.charger_id, coordinator.charger_name, i
            )
        )

    return charger_sensors
