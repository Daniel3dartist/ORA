from abc import ABC, abstractmethod

"""
Factory Creator Interface for Validations
"""
class IValidator(ABC):
    """
    Factory method
    """    
    @abstractmethod
    def validator_method(self):
        pass

    """
    Validation result/product
    """
    def validator(self):
        product = self.validator_method()
        result = product.is_valid()
        return result
