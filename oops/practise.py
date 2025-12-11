class chaiOrder:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size
    def order(self):
        return  f"{self.type} chai and cup size {self.size}"
    
chai = chaiOrder('Masale','large')
print(chai.order())