from console_io import IOModule

class IOController:
    def __init__(self):
        self.io_module = IOModule()

    def get_user_input(self):
        name = self.io_module.get_input("Enter your name: ")
        age = self.io_module.get_input("Enter your age: ")
        return name, age

    def display_greeting(self, name):
        greeting = f"Hello, {name}!"
        self.io_module.display_output(greeting)
