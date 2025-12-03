def serve_chai():
    yield "First Order"
    yield "Second Order"
    yield "Third Order"

stall = serve_chai()

print(next(stall))  
print(next(stall))  
print(next(stall))  
