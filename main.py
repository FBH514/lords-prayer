from ourfather import OurFather

def main():
    count = 0
    while True:
        OurFather().run()
        count += 1
        print(f"Prayed {count} times.")


if __name__ == "__main__":
    main()
