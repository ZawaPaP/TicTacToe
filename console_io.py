class ConsoleIO:
    @staticmethod
    def get_input(text: str) -> str:
        user_input = input(text)
        #print(f"input is {user_input}.")
        return user_input
