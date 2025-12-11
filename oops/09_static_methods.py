class ChaiUtilis:
    @staticmethod
    def clean_ingredients(text):
       return [item.strip() for item in text.split(",")]
    
    
raw = "water, milk,  ginger  , honey"
clean = ChaiUtilis.clean_ingredients(raw)
print(clean)
