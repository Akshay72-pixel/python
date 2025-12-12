class ChaiOrder:
    def __init__(self, tea_type , size, sweetness):
        self.tea_type = tea_type
        self.size = size 
        self.sweetness = sweetness
        
    @classmethod
    def from_dist(cls,order_data):
        return cls(
             order_data["tea_type"],
             order_data["size"],
             order_data["sweetness"],
        )
    @classmethod
    def from_string(cls,order_data):
        tea_type, sweetness, size = order_data.split("-")
        return cls(tea_type, size, sweetness )
    
class chaiiUtil:
    @staticmethod
    def is_valid_size(size):
        return size in ['Small','Medium','Large']    


print(chaiiUtil.is_valid_size("Medium"))

order1 = ChaiOrder.from_dist({"tea_type":"masale","size":"large","sweetness":"normal"})
print(order1.__dict__)
order2 = ChaiOrder.from_string('Ginger-Medium-Normal')
print(order2.__dict__)