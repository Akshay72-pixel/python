# chai_order = dict(type="Masale chai",size="Large",sugar=2)
# print(chai_order)

chai_recipe = {}
chai_recipe["base"] = "Green Tea"
chai_recipe["liquid"] = "milk"
print(f"chai recipe : {chai_recipe}")       
print(f"Recipe base : {chai_recipe['base']}")
del chai_recipe["liquid"]
print(f"chai recipe : {chai_recipe}")   

chai_order  = {'type':'Ginger chai','size' : 'Medium','sugar':'1'} 
# print(f"All keys : {chai_order.keys()}")
# print(f"All Values : {chai_order.values()}")
# print(f"All Items : {chai_order.items()}")

last_Item = chai_order.popitem()
print(last_Item)

chai_order.update(last_Item)
print(chai_order)