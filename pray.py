import csv
from UserInput import UserInput


class Pray(UserInput):

    def __init__(self, file_name) -> None:
        super().__init__()
        self.__FILE_NAME: str = file_name
        self.__prayer = self.set_prayer()

    def __repr__(self) -> str:
        pass

    def set_prayer(self) -> list:
        with open(self.__FILE_NAME, "r") as f:
            reader = csv.reader(f)
            return list(reader)

    def get_prayer(self) -> list:
        return self.__prayer

    def run(self) -> None:
        print("Enter the verse above then press enter.")
        for row in self.__prayer:
            print("".join(row))
            UserInput().set_input()
            print()
        print("Amen.")
        print()
