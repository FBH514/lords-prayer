import csv
import json
import os
import random
from pprint import pprint
from typing import Any, Optional

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
        if file_name is None or data is None:
            return
        with open(file_name, "w") as file:
            if file_name.endswith(".csv"):
                csv.writer(file)
            elif file_name.endswith(".json"):
                json.dump(file, data)
            else:
                file.writelines(data)

class Bible:

    def __init__(self, prophet=None, book=None) -> None:
        """
        Initialize the object.
        :param prophet: The prophet.
        :param book: The book.
        """
        self.__prophets = self.load_prophets()
        self.__prophet = prophet
        if self.__prophet is None or not self.find_prophet(self.__prophet):
            self.__prophet = random.choice(self.__prophets)
        self.__FILE_NAME = f"Bible/{self.__prophet}.json"
        self.__bible = FileHandling.open(self.__FILE_NAME)
        self.__books = self.load_books()
        self.__book = book
        if self.__book is None:
            self.__book = random.choice(self.__books)
        if not self.is_valid_book(self.__book, self.__prophet):
            raise ValueError(f"{book} is not a valid book.")

    def __repr__(self) -> str:
        """
        Get the string representation of the object.
        :return: The string representation of the object.
        """
        if self.__prophet is None:
            return f"Praying the Bible"
        elif self.__book is None:
            return f"Praying the {self.__prophet}"
        return f"Praying {self.__book}, {self.__prophet}"

    @staticmethod
    def load_prophets() -> list:
        """
        Load all prophets.
        :return: A list of all prophets.
        """
        data = []
        for _ in os.listdir("Bible"):
            pr = _.split(".")[0]
            # if pr in data:
            #     continue
            # for _ in pr[:2]:
            #     if _ in string.digits or _ in string.whitespace:
            #         pr = pr.replace(_, "")
            data.append(pr)
        return data

    def load_books(self) -> Optional[list[int]]:
        """
        Load all books.
        :return: List of all books.
        """
        if self.__bible is None:
            return None
        return [_ + 1 for _ in range(len(self.__bible))]

    @staticmethod
    def find_prophet(prophet) -> bool:
        """
        Find the prophet.
        :param prophet: The prophet.
        :return: True if the prophet is found, False otherwise.
        """
        if prophet is None:
            return False
        for _ in os.listdir("Bible"):
            prophet = prophet.title()
            if prophet == _.split(".")[0]:
                return True
        return False

    @staticmethod
    def is_valid_prophet(prophet) -> bool:
        """
        Check if the prophet is valid.
        :param prophet: The prophet.
        :return: True if the prophet is valid, False otherwise.
        """
        if prophet is None:
            return False
        return Bible.find_prophet(prophet)

    @staticmethod
    def is_valid_book(book, prophet):
        """
        Check if the book is valid.
        :param book: The book.
        :param prophet: The prophet.
        :return: True if the book is valid, False otherwise.
        """
        if book is None or prophet is None:
            return False
        data = FileHandling.open(f"Bible/{prophet}.json")
        books = [_ + 1 for _ in range(len(data))]
        return book in books

    def get_prophet(self) -> str:
        """
        Get the prophet.
        :return: The prophet.
        """
        return self.__prophet

    def get_book(self) -> str:
        """
        Get the book.
        :return: The book.
        """
        return self.__book

    def read(self) -> None:
        """
        Read the book.
        :return: The book.
        """
        data = self.__bible[int(self.__book - 1)]
        print(f"Reading: {self.__prophet}")
        for key in data.keys():
            print(f"{key}\n{data[key]}\n")
            UserInput("—> ").get_str_input()
            print()


if __name__ == "__main__":
    pprint(Bible().read())

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
        if file_name is None:
            return
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
