from .igenerator import IGenerator
from .igen_product import IGenProduct
from .usergen_product import UserGenProduct

class UserGen(IGenerator):
    def generator_method(self) -> IGenProduct:
        user_product = UserGenProduct()
        user_product.count = self.count
        return user_product