def update_order():
    chai_type = "Lemon Tea"
    def kitchen():
        nonlocal chai_type 
        chai_type = "Ginger Chai"
        print(chai_type)
    kitchen()
    print(chai_type)    
update_order()