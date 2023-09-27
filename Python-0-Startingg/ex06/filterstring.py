import sys
from ft_filter import ft_filter


def check_len(word_len):
    return lambda str: len(str) > word_len


def main():
    try:
        assert len(sys.argv) == 3, "arguments are bad"
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(0)
    try:
        assert sys.argv[2].isdigit(), "second argument is not an integer"
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(0)
    word_length = int(sys.argv[2])
    splited_word = sys.argv[1].split()
    min_len = check_len(word_length)
    result = ft_filter(min_len, splited_word)
    new = [x for x in result]
    print(new)


if __name__ == "__main__":
    main()
