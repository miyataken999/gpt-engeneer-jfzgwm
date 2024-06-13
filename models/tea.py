from dataclasses import dataclass

@dataclass
class Tea:
    """Represents a tea variety"""
    id: int
    name: str
    origin: str
    description: str