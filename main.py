from pray import Pray

def main():
    count = 0
    while True:
        choice = menu()
        Pray(choice).run()
        count += 1
        print(f"Prayed {count} times.")


def menu():
    print("1. Pray the Our Father")
    print("2. Pray the Hail Mary")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("You chose to pray the Our Father.")
                return "our_father.csv"
            elif choice == 2:
                print("You chose to pray the Hail Mary.")
                return "hail_mary.csv"
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
