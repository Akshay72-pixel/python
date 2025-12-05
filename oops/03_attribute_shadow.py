class Chai:
    temperature = "Hot"
    strength = "Strong"
    
    
cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "Small"
print(cutting.temperature)
print(Chai.temperature)
# del cutting.cup
del cutting.temperature
print(cutting.temperature)
print(cutting.cup)