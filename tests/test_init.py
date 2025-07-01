"""Test component setup."""
from homeassistant.setup import async_setup_component

from custom_components.hacs_beem_cloud_solar_battery.const import DOMAIN


async def test_async_setup(hass):
    """Test the component gets setup."""
    assert await async_setup_component(hass, DOMAIN, {}) is True