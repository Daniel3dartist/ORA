from generators.usergen import UserGen
from generators.itemgen import ItemGen


class FakerGen:
    def __init__(self, usercount:int = 0, itemcount:int = 0):
        self.usercount = usercount
        self.itemcount = itemcount
    
    def usergen(self):
        fake_users = UserGen.gen(self.usercount)
        return fake_users
    
    def itemgen(self):
        fake_itens = ItemGen.gen()
        return fake_itens