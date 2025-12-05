class Chaicup:
    size = 150
    
    def describe(self):
        return f" A {self.size}ml cup"
    
chai = Chaicup()
print(chai.describe())
print(Chaicup.describe(chai))

