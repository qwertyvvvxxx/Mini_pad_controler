from enum import Enum

class Screen(Enum):
    HOME = "HOME"
    MENU = "MENU"
    SYSTEM = "SYSTEM"
    APPS = "APPS"


class DeviceSimulator:
    def __init__(self):
        self.current_screen = Screen.HOME

    def go_home(self) -> str:
        self.current_screen = Screen.HOME

        return self.current_screen.value

    def switch_screen(self, target_screen):
        if target_screen == Screen.HOME:
            return self.go_home()
        elif target_screen in [Screen.MENU, Screen.SYSTEM, Screen.APPS]:
            self.current_screen = target_screen
            return self.current_screen.value
