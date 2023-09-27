import sys


def building(str):
    upper, lower, punct, spaces, digits = 0, 0, 0, 0, 0
    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digits += 1
        elif i.isspace():
            spaces += 1
        elif not i.isalnum() and not i.isspace():
            punct += 1
    print(f"The string contains {len(str)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")
    pass


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as msg:
        print("AssertionError:", msg)
    else:
        if (len(sys.argv) == 2):
            str = sys.argv[1]
        elif (len(sys.argv) == 1):
            print("What is the text to count?")
        str = sys.stdin.readline()
        building(str)


if __name__ == "__main__":
    main()
