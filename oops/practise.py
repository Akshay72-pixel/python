class BaseClass:
    def __init__(self,type_):
        self.type = type_
    def prepare_chai(self):
        print(f"Preparing ",{self.type})
        
class Masalechai(BaseClass):
    def add_spices(self):
        print(f"For preparing {self.type} chai  we have to bring masale")
class fancyChai:
    chai_cls = BaseClass
    