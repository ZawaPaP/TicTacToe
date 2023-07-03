from game_command import GameCommand
from console_io import ConsoleIO
from typing import Optional
    
class GameCommandHandler():

    def game_command_handler(self, user_input: str) -> Optional[GameCommand]:
        user_input = user_input.lower()
        if user_input == GameCommand.HELP.value:
            print(self.help_message)     
        elif user_input == GameCommand.RESET.value:
            return self.reset_handler()

    def reset_handler(self) -> Optional[GameCommand]:
        if self.is_confirmed_input("really reset the game? (y/n): "):
            return GameCommand.RESET
            
    @staticmethod
    def is_confirmed_input(text: str) -> bool:    
        confirmation = ConsoleIO.get_input(text)
        return confirmation.lower() == "y"

    help_message = (
"""
--------
Command commands:
    H: game help
    R: Reset the game
    Ctrl + c: Exit the game
Input the marking position: format 'row, column'
--------
"""
    )