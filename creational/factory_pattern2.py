from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class WindowsButton(Button):
    def click(self):
        print("Click From Windows Button")


class LinuxButton(Button):
    def click(self):
        print("Click From Linux Button")


class ButtonFactory:
    @staticmethod
    def create_button(button_type):
        if button_type == "Windows":
            return WindowsButton()
        elif button_type == "Linux":
            return LinuxButton()
        else:
            raise Exception("Invalid button type")


class Dialog:
    def __init__(self, button):
        if not isinstance(button, Button):
            raise Exception("Invalid Button Object")
        self._button = button

    def onclick(self):
        print("Clicking Button From Dialog")
        self._button.click()


if __name__ == "__main__":
    windows_button = ButtonFactory.create_button("Windows")
    linux_button = ButtonFactory.create_button("Linux")
    dialog = Dialog(windows_button)
    dialog.onclick()
