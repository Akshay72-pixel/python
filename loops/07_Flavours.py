flavours = ["Ginger","Out Of Stock","Lemon","Disconnetinued",'Pudina']

for flavour in flavours:
    if flavour=="Out Of Stock":
        continue
    elif flavour=="Disconnetinued":
        break
    print(f"Flavour are {flavour}")
print("All Over")