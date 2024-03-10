from dataclasses import dataclass

@dataclass
class Player:
    name : str
    country : str
    position : str
    lineup : str
    stars : float
    points : float


