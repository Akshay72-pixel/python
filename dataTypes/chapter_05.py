ingredients = ["Water","milk","black tea"]
ingredients.append("Ginger")
print(ingredients)
ingredients.remove("Water")
print(ingredients)

spice_options = ['ginger','cardomoom']
chai_ingredient = ['milk','tea powder']

spice_options.extend(chai_ingredient)
spice_options.insert(2,'water')
print(spice_options)

smI = spice_options.pop(0)
print(smI)

spice_options.reverse()
print(spice_options)

spice_options.sort()
print(spice_options)

max_sugar = [1,2,3,4,5]
print(f"{max(max_sugar)}")
print(f"{min(max_sugar)}")

