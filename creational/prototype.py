from copy import deepcopy
from abc import ABC, abstractmethod


class EmailTemplate(ABC):
    def clone(self):
        return deepcopy(self)

    @abstractmethod
    def set_content(self, content):
        pass

    @abstractmethod
    def send(self):
        pass


class TUFWelcome(EmailTemplate):
    def __init__(self):
        self.subject = "Welcome to TUF"
        self.content = None

    def set_content(self, username):
        self.content = f"Welcome to TUF {username}"

    def send(self):
        print("Sending TUF Welcome Email")
        print(self.content)


class TUFPlusWelcome(EmailTemplate):
    def __init__(self):
        self.subject = "Welcome to TUF+"
        self.content = None

    def set_content(self, username):
        self.content = f"Welcome To TUF+ {username}"

    def send(self):
        print("Sending TUF Plus Welcome Email")
        print(self.content)


class PrototypeRegistry:
    def __init__(self):
        self.registry = {
            "TUF": TUFWelcome(),
            "TUF+": TUFPlusWelcome()
        }

    def find_prototype(self, name):
        prototype = self.registry.get(name, None)
        if prototype:
            return self.registry[name].clone()
        raise ValueError(f"Invalid prototype name {name}")


if __name__ == "__main__":
    registry = PrototypeRegistry()
    tuf_users = ["A1", "A2", "A3"]
    tufplus_users = ["B1", "B2"]

    for user in tuf_users:
        tuf_welcome = registry.find_prototype("TUF")
        tuf_welcome.set_content(user)
        tuf_welcome.send()

    for user in tufplus_users:
        tufplus_welcome = registry.find_prototype("TUF+")
        tufplus_welcome.set_content(user)
        tufplus_welcome.send()
