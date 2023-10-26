from abc import ABC, abstractmethod

"""
Interface for Validator Product
"""
class IValidatorProduct(ABC):
    """
    Validator method
    """
    @abstractmethod
    def is_valid(self):
        pass