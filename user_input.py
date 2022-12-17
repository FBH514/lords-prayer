class UserInput:

    def __init__(self, prompt: str = "") -> None:
        """
        Initialize the class.
        :param prompt: The prompt to display to the user.
        """
        self.__input = None
        self.__prompt = prompt

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        :return: A string representation of the object.
        """
        return f"{self.__prompt} prompted" \
               f" The user input was {self.__input}."

    def get_str_input(self) -> str:
        """
        Get the user's input as a string.
        :return: The user's input as a string.
        """
        while True:
            try:
                self.__input = str(input(self.__prompt))
                return self.__input
            except ValueError:
                print("Your input must be a string.")

    def get_num_input(self) -> float:
        """
        Get the user's input as a number.
        :return: The user's input as a number.
        """
        while True:
            try:
                self.__input = float(input(self.__prompt))
                return self.__input
            except ValueError:
                print("Your input must be a number.")
