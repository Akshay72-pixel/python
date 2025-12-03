essential_spices = {'ginger','cardamon','cinnamon'}
optional_spices = {'clover','ginger','black pepper'}

all_spices = essential_spices | optional_spices 
print(all_spices)

common_spice = essential_spices & optional_spices
print(common_spice)

only_in_essential = essential_spices - optional_spices
print(only_in_essential)

print(f"Is 'cloves' in essential spices : {'clover' in optional_spices}")