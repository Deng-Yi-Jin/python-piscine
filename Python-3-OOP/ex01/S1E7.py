from S1E9 import Character


class Baratheon(Character):
    "The Baratheon Family"
    def __init__(self, first_name, is_alive=True, eyes="brown", hair="dark"):
        """
        Baratheon's character
        """
        super().__init__(first_name, is_alive)
        self.family_name = __class__.__name__
        self.eyes = eyes
        self.hair = hair

    def __str__(self):
        """
        Baratheon's line
        """
        return (f"{__class__.__name__}, has {self.eyes} and {self.hair}")

    def __repr__(self):
        """
        Baratheon's Vector
        """
        tup = (__class__.__name__, self.eyes, self.hair)
        return (f"Vector: {tup}")

    def die(self):
        """
        Baratheon's family die
        """
        super().die()


class Lannister(Character):
    """
    The Lanister Family
    """
    def __init__(self, first_name, is_alive=True, eyes="blue", hair="light"):
        """
        Lannister's true character
        """
        super().__init__(first_name, is_alive)
        self.family_name = __class__.__name__
        self.eyes = eyes
        self.hair = hair

    def __str__(self):
        """
        Lannister's line
        """
        return (f"{__class__.__name__}, has {self.eyes} and {self.hair}")

    def __repr__(self):
        """
        Lannister
        """
        tup = (__class__.__name__, self.eyes, self.hair)
        return (f"Vector: {tup}")

    def die(self):
        """
        Lannister's family die
        """
        super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True,
                         eyes="blue", hair="light"):
        """
        Lannister
        """
        return (cls(first_name, is_alive, eyes, hair))
