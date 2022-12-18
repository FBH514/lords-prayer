import csv
import json
from typing import Any

from user_input import UserInput

class FileHandling:

    def __init__(self, file_name) -> None:
        """
        Initialize the object.
        :param file_name: The name of the file.
        """
        self.__FILE_NAME = file_name

    def __repr__(self) -> str:
        """
        Get the string representation of the object.
        :return: The string representation of the object.
        """
        return f"Handling {self.__FILE_NAME}"

    @staticmethod
    def file_type(file_name) -> str:
        return file_name.split(".")[-1]

    @staticmethod
    def open(file_name) -> Any:
        """
        Open the file.
        :param file_name: The name of the file.
        :return: The file.
        """
        with open(file_name, "r") as file:
            if file_name.endswith(".csv"):
                return list(csv.reader(file))
            elif file_name.endswith(".json"):
                return json.load(file)
            return file.readlines()

    @staticmethod
    def save(file_name, data) -> None:
        """
        Save the file.
        :param file_name: The name of the file.
        :param data: The data to save.
        :return: None
        """
        with open(file_name, "w") as file:
            if file_name.endswith(".csv"):
                csv.writer(file)
            elif file_name.endswith(".json"):
                json.dump(file, data)
            else:
                file.writelines(data)

class Pray(UserInput, FileHandling):

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
        self.__prayer = self.open(file_name)

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
