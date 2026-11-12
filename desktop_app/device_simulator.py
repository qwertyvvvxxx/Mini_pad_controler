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

        return f"Current screen: {self.current_screen.value}"

    def switch_screen(self, target_screen):
        match target_screen:
            case Screen.HOME:
                return self.go_home()
            case Screen.MENU:
                self.current_screen = Screen.MENU
                return f"Current screen: {self.current_screen.value}"
            case Screen.SYSTEM:
                self.current_screen = Screen.SYSTEM
                return f"Current screen: {self.current_screen.value}"
            case Screen.APPS:
                self.current_screen = Screen.APPS
                return f"Current screen: {self.current_screen.value}"
            case _:
                self.current_screen = Screen.HOME
                return f"Current screen: {self.current_screen.value}"
