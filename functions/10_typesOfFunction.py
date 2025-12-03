def pure_cups(cups):
    return cups*10

total_chai = 0

def impure_chai(cups):
    global total_chai  
    total_chai += cups
    
def pourchai(n):
    if n==5:
        return;
    print(n)
    return pourchai(n+1)
    
pourchai(1)

chai_types = ['light','kadak','ginger','lemon']

strong_chai = list(filter(lambda chai:chai!='kadak',chai_types))
print(strong_chai)