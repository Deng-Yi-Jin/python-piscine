import sys


def check_argv(str):
    for i in str:
        if i.isdigit() or i.isalpha() or i.isspace():
            continue
        else:
            return False
    return True


def sos(str):
    '''
    Convert a string to morse code
    '''
    print_mourse = ""
    NESTED_MOURSE = {
        ' ': '/ ', 'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ',
        'e': '. ', 'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ',
        'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ',
        'o': '--- ', 'p': '.--. ', 'q': '--.- ', 'r': '.-. ', 's': '... ',
        't': '- ', 'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ',
        'y': '-.-- ', 'z': '--.. ', '1': '.---- ', '2': '..--- ',
        '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ',
        '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- '}
    for i in str:
        print_mourse += NESTED_MOURSE[i.lower()]
    print(print_mourse)


def main():
    try:
        assert len(sys.argv) == 2, "Bad number of argumenst"
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(0)
    try:
        assert check_argv(sys.argv[1]), "Not digits or string"
        exit(0)
    except AssertionError as msg:
        print("AssertionError:", msg)
    else:
        sos(sys.argv[1])


if __name__ == '__main__':
    main()
