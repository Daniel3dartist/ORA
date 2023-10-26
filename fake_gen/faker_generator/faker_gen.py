from typing import Type
from .generators.igenerator import IGenerator

"""
Fake Generator
"""
class FakerGen:
        def generate(generator: Type[IGenerator]):
                return generator.generator()
    
"""   
        def itemgen(self):
        fake_itens = ItemGen.gen()
        return fake_itens
"""