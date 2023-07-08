from game_command import GameCommand
    
class GameCommandHandler():
    def game_command_handler(self, user_input: str) -> None:
        user_input = user_input.lower()
        if user_input == GameCommand.HELP.value:
            print(self.help_message)     
        else:
            raise ValueError("Invalid command. Try again")

    '''
    def reset_handler(self) -> Optional[GameCommand]:
        if self.is_confirmed_input("really reset the game? (y/n): "):
            return GameCommand.RESET
            
    @staticmethod
    def is_confirmed_input(text: str) -> bool:    
        confirmation = ConsoleIO.get_input(text)
        return confirmation.lower() == "y"
    '''
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