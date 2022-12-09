import csv


class OurFather:

    def __init__(self):
        self.FILE_NAME = "ourfather.csv"
        self.our_father = self.load_our_father()

    def __repr__(self):
        pass

    def load_our_father(self):
        with open(self.FILE_NAME, "r") as f:
            reader = csv.reader(f)
            return list(reader)

    def get_our_father(self):
        return self.our_father

    @staticmethod
    def get_input(prompt="") -> str:
        return input(prompt)

    def run(self):
        for row in self.our_father:
            print("Enter the verse above then press enter.")
            print("".join(row))
            self.get_input()
            print()
        print("Amen.")
        print()
