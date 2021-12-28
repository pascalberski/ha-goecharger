"""
Charger Sensors
"""
import logging

from homeassistant.helpers.entity import Entity

from .const import ICON_PLUG

from .coordinators import SensorDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

class ApiSensor(Entity):
    """
    Status Api Sensor
    """

    def __init__(
        self,
        coordinator: SensorDataUpdateCoordinator,
    ):
        """Initialize the sensor"""
        self.coordinator = coordinator

    @property
    def name(self):
        """Sensor name"""
        return "Charger"

    @property
    def should_poll(self):
        """No need to poll, Coordinator notifies entity of updates"""
        return False

    @property
    def available(self):
        """Whether sensor is available"""
        return self.coordinator.last_update_success

    @property
    def icon(self):
        """Sensor icon"""
        return ICON_PLUG

    @property
    def unit_of_measurement(self):
        """Sensor unit of measurement"""
        return None

    async def async_added_to_hass(self):
        """Connect to dispatcher listening for entity data notifications"""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def async_update(self):
        """Update entity"""
        await self.coordinator.async_request_refresh()

    def _get_status(self):
        try:
            return self.coordinator.data
        except Exception as exc:
            _LOGGER.error("Unable to get api data\n%s", exc)


class StateSensor(ApiSensor):
    """
    Displays car attribute [Ready|Charging|Waiting|Finished]
    """
    _state = "Unknown"

    @property
    def name(self):
        """Sensor name"""
        return "Charger State"

    @property
    def unique_id(self):
        """Unique entity id"""
        return "goecharger:state"

    @property
    def state(self):
        """Sensor state"""
        car = self._get_status().get("car")
        _LOGGER.debug("status (car): %s", car)
        if car:
            if car == "1":
                self._state = "Ready"
            if car == "2":
                self._state = "Charging"
            if car == "3":
                self._state = "Waiting"
            if car == "4":
                self._state = "Finished"
        else:
            self._state = "Unknown"

        return self._state

    @property
    def icon(self):
        """Sensor icon"""
        return ICON_PLUG
