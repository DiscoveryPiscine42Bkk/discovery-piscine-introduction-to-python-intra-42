import sys


def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        text = " ".join(sys.argv[1:])
        print(text.upper())


if __name__ == "__main__":
    main()