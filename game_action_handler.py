from game_action import GameAction
from console_io import ConsoleIO
from typing import Optional
    
class GameActionHandler():

    def game_action_handler(self, user_input: str) -> Optional[GameAction]:
        user_input = user_input.lower()
        if user_input == GameAction.HELP.value:
            print(self.help_message)
            return GameAction.HELP       
        elif user_input == GameAction.RESET.value:
            return self.reset_handler()
        elif user_input == GameAction.EXIT.value:
            return self.exit_handler()

    def exit_handler(self) -> Optional[GameAction]:
        if self.is_confirmed_input("really exit the game? (y/n): "):
            return GameAction.EXIT

    def reset_handler(self) -> Optional[GameAction]:
        if self.is_confirmed_input("really reset the game? (y/n): "):
            return GameAction.RESET
            
    @staticmethod
    def is_confirmed_input(text: str) -> bool:    
        confirmation = ConsoleIO.get_input(text)
        return confirmation.lower() == "y"

    help_message = (
"""--------\n
Action commands:\n
    H: game help\n
    R: Reset the game\n
    E: Exit the game\n
Input the marking position: format 'row, column'\n
--------\n"""
    )