def serve_chai():
    yield "Cup 1 : masale chai"
    yield "Cup 2 : Lemon Tea " 
    yield "Cup 3 : Ginger Chai " 
    

stall = serve_chai()

print(next(stall))
print(next(stall))
print(next(stall))