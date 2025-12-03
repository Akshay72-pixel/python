chai = "Ginger Chai"

def prepare_chai(order):
    print("preparing ",order)

prepare_chai(chai)

def specail_chai(*ingredients,**extras):
    print(ingredients)
    print(extras)
    
specail_chai("tulse",'lavang',liquid="water",foam="yes")

def chai(order=[]):
    order.append("Masale Chai")
    print(order)
    
chai()


def chai(order=None):
    if order is None:
        order = []
    print(order)
    
chai()