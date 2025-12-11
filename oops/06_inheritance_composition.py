class BaseChai:
    def __init__(self, type_):
        self.type = type_
    
    def prepare_chai(self):
        print("Preparing ",self.type)

class MasaleChai(BaseChai):
    def add_spice(self):
        print("Adding Ginger, Cradamom, Cloves")
        
class ChaiShop:
    chai_cls = BaseChai
    
    def __init__(self):
        self.chai = self.chai_cls("regular")
        
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")

class FancyChaiShop(ChaiShop):
    chai_cls = MasaleChai
    
shop = ChaiShop()
Fancy = FancyChaiShop()
shop.serve()
Fancy.serve()
Fancy.chai.add_spice()