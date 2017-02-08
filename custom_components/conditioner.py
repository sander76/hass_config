"""Activates a scene depending on time and solar position"""
from datetime import datetime, time
from homeassistant.components import scene

# The domain of your component. Should be equal to the name of your component.
DOMAIN = 'conditioner'

DEPENDENCIES = ['scene', 'sun']
SCENE_1 = 'scene.7247'

def setup(hass, config):
    """Setup is called when Home Assistant is loading our component."""

    def check_time_slot(call):
        """activates a scene depending on time and solar position"""
        current_time = datetime.now().time()

        if time(hour=7) < current_time < time(hour=9):
            if current_time < time(hour=8):
                scene.activate(hass, SCENE_1)

    def activate_test(call):
        """testing to activate a scene"""
        scene.activate(hass, SCENE_1)

    hass.services.register(DOMAIN, 'activate_test', activate_test)

    # Return boolean to indicate that initialization was successfully.
    return True
