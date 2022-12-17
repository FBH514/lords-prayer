import csv
from user_input import UserInput


class Pray(UserInput):

    def __init__(self, file_name) -> None:
        """
        Initialize the class.
        :param file_name: The name of the file to open.
        """
        super().__init__()
        self.__FILE_NAME: str = file_name
        self.__prayer = None
        self.set_prayer(self.__FILE_NAME)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        :return: A string representation of the object.
        """
        return f"Praying {self.__FILE_NAME.split('.')[0]}."

    def set_prayer(self, file_name) -> None:
        """
        Set the prayer.
        :param file_name: The name of the file to open.
        :return: None
        """
        with open(file_name, "r") as f:
            self.__prayer = list(csv.reader(f))

    def get_prayer(self) -> list:
        """
        Get the prayer.
        :return: The prayer as a list.
        """
        return self.__prayer

    def run(self) -> None:
        """
        Run the program.
        :return: None
        """
        print("Enter the verse above then press enter.\n")
        for row in self.__prayer:
            print("".join(row))
            UserInput("—> ").get_str_input()
            print()
        print("Amen.")
        print()
