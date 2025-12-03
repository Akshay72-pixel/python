def chai_customer():
    print("welcome")
    order = yield
    while True:
        print(f"Hello your order {order}")
        order = yield
    

stall = chai_customer()
next(stall)

stall.send("Masale Chai")
stall.send("Ginger Chai")
