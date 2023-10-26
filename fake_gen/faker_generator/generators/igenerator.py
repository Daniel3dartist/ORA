from typing import Type
from abc import ABC, abstractmethod
from .igen_product import IGenProduct


"""
Factory Creator Interface for Generator
"""
class IGenerator(ABC):
    """
    Factory method
    """    
    @abstractmethod
    def generator_method(self):
        pass

    """
    Generator result/product
    """
    def generator(self):
        product: Type[IGenProduct] = self.generator_method()
        result = product.gen()
        return result