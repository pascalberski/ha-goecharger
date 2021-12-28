"""
Constants for go-echarger
"""
# Base component constants
NAME = "go-eCharger Integration"
DOMAIN = "goecharger"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.2"
DEFAULT_NAME = "goecharger"

ISSUE_URL = "https://github.com/pascalberski/ha-goecharger/issues"

# Icons
ICON_BATTERY = "mdi:battery-50"
ICON_PLUG = "mdi:ev-plug-type2"
ICON_ALLOW = "mdi:check-bold"
ICON_ENERGY = "mdi:lightning-bolt-circle"
ICON_CURRENT = "mdi:lightning-bolt-outline"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Configuration and options
CONF_HOST = "host"

# Startup
STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME} by Pascal Berski (@pascalberski)
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
