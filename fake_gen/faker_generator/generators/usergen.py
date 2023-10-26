from .igenerator import IGenerator
from .igen_product import IGenProduct
from .usergen_product import UserGenProduct

class UserGen(IGenerator):
    def __init__(self, count:int):
        self.count:int = count

    def generator_method(self) -> IGenProduct:
        return UserGenProduct(count=self.count)