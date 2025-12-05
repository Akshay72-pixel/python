class Chai:
    origin = "India"
    
print(Chai.origin)

Chai.is_hot = True

print(Chai.is_hot)

masale = Chai()
masale.is_hot = False
print(masale.is_hot) 
print(Chai.is_hot)

masale.flavour = 'garlic'
print(masale.flavour)