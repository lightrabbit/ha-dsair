from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_SCAN_INTERVAL
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN, CONF_GW, DEFAULT_GW, DEFAULT_PORT, GW_LIST

_LOGGER = logging.getLogger(__name__)


def _log(s: str):
    s = str(s)
    for i in s.split("\n"):
        _LOGGER.debug(i)


class DsAirFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        self.host = None
        self.port = None
        self.gw = None

    async def async_step_user(
            self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:

        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        errors = {}
        if user_input is not None:
            _log(user_input[CONF_HOST])
            _log(user_input[CONF_PORT])
            _log(user_input[CONF_GW])
            return self.async_create_entry(
                title="金制空气", data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_HOST): str,
                vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
                vol.Optional(CONF_GW, default=DEFAULT_GW): vol.In(GW_LIST),
                vol.Optional(CONF_SCAN_INTERVAL, default=5): vol.In([5])
            }), errors=errors
        )
