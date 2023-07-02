from console_io import ConsoleIO
import re
from typing import Optional

class Parser:
    @staticmethod
    def parse_input(input_str: str) -> Optional[str]:
        try:
            input_str = input_str.replace(" ", "")
            return input_str
        except Exception as e:
            print(f"{str(e)}, invalid command. Please input h for help")
            raise

    @staticmethod
    def validate_position_format(input: str) -> bool:
        pattern = r"\d+,\d+"
        return re.match(pattern, input)

    @staticmethod
    def validate_action_format(input: str) -> bool:
        pattern = r"[hre]"
        return re.match(pattern, input, re.I)

class IOController:
    def handle_input(self, text) -> dict:
        while True:
            try:
                user_input = ConsoleIO.get_input(text)
                parsed_input = Parser.parse_input(user_input)
                if Parser.validate_position_format(parsed_input):
                    row, col = map(int, parsed_input.split(","))
                    if 1 <= row <= 3 and 1 <= col <= 3:
                        return {'position': (row, col)}
                    else:
                        print("Invalid input. Please enter the position in the range of '1 to 3'.")
                elif Parser.validate_action_format(parsed_input):
                    return {'command': parsed_input}
                else:
                    print("Invalid input. Please input h for help.")
            except Exception:
                continue
