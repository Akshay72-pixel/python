def chai_customer():
    print("Welcome")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield
stall = chai_customer()
next(stall)

stall.send("Masasle chai")
stall.send("Ginger chai")