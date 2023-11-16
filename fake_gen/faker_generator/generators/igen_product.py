from abc import ABC, abstractmethod

"""
Interface for Generator Product
"""
class IGenProduct(ABC):
    def __init__(self):
        self.count: int = 1
    """
    Generator method
    """
    @abstractmethod
    def gen(self):
        pass