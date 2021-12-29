"""
Charger Sensors
"""
import logging

from homeassistant.helpers.entity import Entity

from .const import (
    ICON_ALLOW,
    ICON_CURRENT,
    ICON_PLUG,
    ICON_ENERGY,
    ICON_POWER,
    ICON_VOLTAGE,
)

from .coordinators import SensorDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


class ApiSensor(Entity):
    """
    Status Api Sensor
    """

    def __init__(self, coordinator: SensorDataUpdateCoordinator, charger_id: int, charger_name: str, phase=0):
        """Initialize the sensor"""
        self.coordinator = coordinator
        self.charger_id = charger_id
        self.charger_name = charger_name
        self.phase = phase

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
            return None


class StateSensor(ApiSensor):
    """
    Displays car attribute [Ready|Charging|Waiting|Finished]
    """

    _state = "Unknown"

    @property
    def name(self):
        """Sensor name"""
        return f"{self.charger_name} State"

    @property
    def unique_id(self):
        """Unique entity id"""
        return f"goecharger:{self.charger_id}:state"

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


class AllowSensor(ApiSensor):
    """
    Displays alw sensor [True|False]
    """

    _state = "Unknown"

    @property
    def name(self):
        """Sensor name"""
        return f"{self.charger_name} Allow"

    @property
    def unique_id(self):
        """Unique entity id"""
        return f"goecharger:{self.charger_id}:allow"

    @property
    def state(self):
        """Sensor state"""
        alw = self._get_status().get("alw")
        _LOGGER.debug("allow (alw): %s", alw)
        if alw:
            if alw == "1":
                self._state = True
            if alw == "0":
                self._state = False
        else:
            self._state = "Unknown"

        return self._state

    @property
    def icon(self):
        """Sensor icon"""
        return ICON_ALLOW


class TotalEnergySensor(ApiSensor):
    """
    Displays eto sensor
    """

    _state = "Unknown"

    @property
    def name(self):
        """Sensor name"""
        return f"{self.charger_name} Total Energy"

    @property
    def unique_id(self):
        """Unique entity id"""
        return f"goecharger:{self.charger_id}:total_energy"

    @property
    def state(self):
        """Sensor state"""
        eto = self._get_status().get("eto")
        _LOGGER.debug("total energy (eto): %s", eto)
        if eto:
            self._state = float(eto) / 10
        else:
            self._state = "Unknown"

        return self._state

    @property
    def icon(self):
        """Sensor icon"""
        return ICON_ENERGY

    @property
    def unit_of_measurement(self):
        """Sensor unit of measurement"""
        return "kWh"


class VoltageSensor(ApiSensor):
    """
    Displays nrg sensor (voltage)
    """

    _state = "Unknown"

    @property
    def name(self):
        """Sensor name"""
        return f"{self.charger_name} Voltage L{self.phase}"

    @property
    def unique_id(self):
        """Unique entity id"""
        return f"goecharger:{self.charger_id}:voltage_L{self.phase}"

    @property
    def state(self):
        """Sensor state"""
        nrg = self._get_status().get("nrg")
        volt = 0
        _LOGGER.debug("energy (nrg): %s", nrg)
        if nrg:
            volt = nrg[self.phase - 1]
            self._state = int(volt)
        else:
            self._state = "Unknown"

        return self._state

    @property
    def icon(self):
        """Sensor icon"""
        return ICON_VOLTAGE

    @property
    def unit_of_measurement(self):
        """Sensor unit of measurement"""
        return "V"


class CurrentSensor(ApiSensor):
    """
    Displays nrg sensor (current)
    """

    _state = "Unknown"

    @property
    def name(self):
        """Sensor name"""
        return f"{self.charger_name} Current L{self.phase}"

    @property
    def unique_id(self):
        """Unique entity id"""
        return f"goecharger:{self.charger_id}:current_L{self.phase}"

    @property
    def state(self):
        """Sensor state"""
        nrg = self._get_status().get("nrg")
        current = -1
        _LOGGER.debug("energy (nrg): %s", nrg)
        if nrg:
            current = nrg[self.phase + 3]
            self._state = float(current) / 10
        else:
            self._state = "Unknown"

        return self._state

    @property
    def icon(self):
        """Sensor icon"""
        return ICON_CURRENT

    @property
    def unit_of_measurement(self):
        """Sensor unit of measurement"""
        return "A"


class PowerSensor(ApiSensor):
    """
    Displays nrg sensor (power)
    """

    _state = "Unknown"

    @property
    def name(self):
        """Sensor name"""
        return f"{self.charger_name} Power L{self.phase}"

    @property
    def unique_id(self):
        """Unique entity id"""
        return f"goecharger:{self.charger_id}:power_L{self.phase}"

    @property
    def state(self):
        """Sensor state"""
        nrg = self._get_status().get("nrg")
        power = -1
        _LOGGER.debug("energy (nrg): %s", nrg)
        if nrg:
            power = nrg[self.phase + 6]
            self._state = float(power) / 10
        else:
            self._state = "Unknown"

        return self._state

    @property
    def icon(self):
        """Sensor icon"""
        return ICON_POWER

    @property
    def unit_of_measurement(self):
        """Sensor unit of measurement"""
        return "kW"


class TotalPowerSensor(ApiSensor):
    """
    Displays nrg sensor (total_power)
    """

    _state = "Unknown"

    @property
    def name(self):
        """Sensor name"""
        return f"{self.charger_name} Total Power"

    @property
    def unique_id(self):
        """Unique entity id"""
        return f"goecharger:{self.charger_id}:total_power"

    @property
    def state(self):
        """Sensor state"""
        nrg = self._get_status().get("nrg")
        power = -1
        _LOGGER.debug("energy (nrg): %s", nrg)
        if nrg:
            power = nrg[11]
            self._state = float(power) / 100
        else:
            self._state = "Unknown"

        return self._state

    @property
    def icon(self):
        """Sensor icon"""
        return ICON_POWER

    @property
    def unit_of_measurement(self):
        """Sensor unit of measurement"""
        return "kW"
