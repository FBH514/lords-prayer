from user_input import UserInput
from pray import Pray, Bible


def main() -> None:
    """
    Run the program.
    :return: None
    """
    count = 0
    num = num_of_times()
    while num > count:
        choice = menu()
        if isinstance(choice, tuple):
            pray = Bible(choice[0], choice[1])
            pray.read()
        else:
            Pray(choice).run()
        count += 1
        print(f"Prayed {count} times.")
        print()


def menu():
    """
    Get the choice of prayer.
    :return: The choice of prayer.
    """
    print("1. Pray the Our Father")
    print("2. Pray the Hail Mary")
    print("3. Pray the Bible")
    while True:
        choice = UserInput("—> ").get_num_input()
        if choice == 1:
            print("You chose to pray the Our Father.")
            return "our_father.csv"
        elif choice == 2:
            print("You chose to pray the Hail Mary.")
            return "hail_mary.csv"
        elif choice == 3:
            print("You chose to pray the Bible.")
            prophet = select_prophet()
            book = select_book(prophet)
            return prophet, book
        else:
            print("Invalid choice.")

def num_of_times() -> float:
    """
    Get the number of times to pray.
    :return: The number of times to pray.
    """
    while True:
        num = UserInput("How many times do you want to pray? —> ")\
            .get_num_input()
        if num > 0:
            return num
        print("Invalid number.")

def select_prophet():
    while True:
        pr = UserInput("Which prophet do you want to pray? —> ")\
            .get_str_input()
        if Bible.is_valid_prophet(pr):
            return pr
        print("Invalid prophet.")

def select_book(prophet):
    if prophet is None:
        return
    while True:
        bk = UserInput("Which book do you want to pray? —> ")\
            .get_num_input()
        if Bible.is_valid_book(bk, prophet):
            return bk
        print("Invalid book.")


if __name__ == "__main__":
    main()
