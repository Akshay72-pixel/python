favourate_chais = [
    'Masale chai','Lemon Tea','Black Tea','Green Tea',
    'Masale chai','Black Tea','Elaichi Chai'
]

unique_chai = {chai for chai in favourate_chais }
# print(unique_chai)

recipes = {
    "Masala Chai":['ginger','cardamom','clove'],
    "Elaichi Chai":['cardamom','milk','tulsi'],
    "Ginger Chai":['milk','tulsi','ginger']
}

unique_value = {spice for ingredients  in recipes.values() for spice in ingredients}
print(unique_value)