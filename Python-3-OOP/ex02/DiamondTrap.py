from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King of the Seven Seas
    """
    def __init__(self, first_name, is_alive=True):
        """
        King's Info
        """
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """
        Return King's eye color
        """
        return (self.eyes)

    def get_hairs(self):
        """
        Return King's hair color
        """
        return (self.hair)

    def set_eyes(self, eyes):
        """
        Set King's eye color
        """
        self.eyes = eyes

    def set_hairs(self, hair):
        """
        Set King's hair color
        """
        self.hair = hair
