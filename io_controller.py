from console_io import ConsoleIO
import re
from typing import Optional

class Parser:
    @staticmethod
    def parse_input(input_str: str) -> Optional[str]:
        try:
            input_str = input_str.replace(" ", "")
            return input_str
        except ValueError:
            raise ValueError("Invalid input. Try again")

    @staticmethod
    def validate_position_format(input: str) -> bool:
        pattern = r"\d+,\d+"
        return re.match(pattern, input)

    @staticmethod
    def validate_action_format(input: str) -> bool:
        pattern = r"[h]"
        return re.match(pattern, input, re.I)

class IOController:
    @staticmethod
    def get_input(prompt: str) -> str:
        return ConsoleIO.get_input(prompt)

    @staticmethod
    def get_integer_input(prompt: str) -> int:
        while True:
            try:
                user_input = input(prompt)
                value = int(user_input)
                return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    @staticmethod
    def handle_input(prompt) -> dict:
        while True:
            try:
                user_input = ConsoleIO.get_input(prompt)
                parsed_input = Parser.parse_input(user_input)
                if Parser.validate_position_format(parsed_input):
                    row, column = map(int, parsed_input.split(","))
                    if 1 <= row <= 3 and 1 <= column <= 3:
                        return row, column
                    else:
                        raise ValueError("Invalid input. Enter in the range of '1 to 3'.")
                else:
                    raise ValueError("Invalid input. Try again.")
            except ValueError as e:
                print(str(e))
