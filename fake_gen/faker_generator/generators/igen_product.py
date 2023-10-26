from abc import ABC, abstractmethod

"""
Interface for Generator Product
"""
class IGenProduct(ABC):
    """
    Generator method
    """
    @abstractmethod
    def gen(self):
        pass