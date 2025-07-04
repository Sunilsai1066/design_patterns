from abc import ABC, abstractmethod


class CheckBox(ABC):
    @abstractmethod
    def is_checked(self):
        pass


class Button(ABC):
    @abstractmethod
    def is_clicked(self):
        pass


class WinCheckBox(CheckBox):
    def is_checked(self):
        print("Windows CheckBox Created")


class MacCheckBox(CheckBox):
    def is_checked(self):
        print("Mac CheckBox Created")


class WinButton(Button):
    def is_clicked(self):
        print("Windows Button Created")


class MacButton(Button):
    def is_clicked(self):
        print("Mac Button Created")


class GUIFactory(ABC):
    @abstractmethod
    def create_checkbox(self):
        pass

    @abstractmethod
    def create_button(self):
        pass


class WindowsGUIFactory(GUIFactory):
    def create_checkbox(self):
        return WinCheckBox()

    def create_button(self):
        return WinButton()


class MacGUIFactory(GUIFactory):
    def create_checkbox(self):
        return MacCheckBox()

    def create_button(self):
        return MacButton()


class GenerateGUIFactory:
    @staticmethod
    def create_factory(os):
        if os == "Windows":
            return WindowsGUIFactory()
        elif os == "Mac":
            return MacGUIFactory()
        else:
            raise ValueError("Unsupported OS")


if __name__ == "__main__":
    factory = GenerateGUIFactory.create_factory("Mac")

    factory_checkbox = factory.create_checkbox()
    factory_button = factory.create_button()
    factory_checkbox.is_checked()
    factory_button.is_clicked()
