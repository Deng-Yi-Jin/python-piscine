class calculator:
    def __init__(self, number):
        """
        take's in number
        """
        self.number = number

    def __add__(self, object) -> None:
        """
        Addition.
        """
        self.number = [i + object for i in self.number]
        print(self.number)

    def __mul__(self, object) -> None:
        """
        Multiplication.
        """
        self.number = [i * object for i in self.number]
        print(self.number)

    def __sub__(self, object) -> None:
        """
        subtraction
        """
        self.number = [i - object for i in self.number]
        print(self.number)

    def __truediv__(self, object) -> None:
        """
        Devision
        """
        try:
            assert (object != 0), "Object can't be devided by 0"
        except AssertionError as msg:
            print("Assertion Error:", msg)
            exit(0)
        else:
            self.number = [i / object for i in self.number]
            print(self.number)
