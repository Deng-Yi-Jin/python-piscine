import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random ID for a student."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """self init"""
        self.login = self.name[0] + self.surname
        self.id = generate_id()
