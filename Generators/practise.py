def infinite_chai():
    count = 1
    while True:
        yield f"Order {count}"
        count += 1
        
chai = infinite_chai()
for _ in range(3):
    print(next(chai))
    


