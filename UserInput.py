class UserInput:

    def __init__(self):
        self.__input: str = ""

    def set_input(self, prompt="") -> None:
        self.__input = input(prompt)

    def get_input(self) -> str:
        return self.__input
