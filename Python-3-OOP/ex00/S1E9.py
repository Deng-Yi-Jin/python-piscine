from abc import ABC, abstractmethod


class Character(ABC):
    '''
    Character Class
    '''
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        The Character is Alive
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        The Character was slain
        """
        self.is_alive = False


class Stark(Character):
    '''
    Stark Class
    '''
    def __init__(self, first_name, is_alive=True):
        """
        The Character is Alive
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        The Character is dead
        """
        super().die()
