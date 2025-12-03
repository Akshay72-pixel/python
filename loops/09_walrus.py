# value = 13
# remainder = value % 5

# if remainder:
#     print(f"It's not divisible {remainder}")

value = 13

if(remainder := value % 5):
    print(f"It's not divisible {remainder}")

available_sizes = ['small','medium','large']

# if(requested_Size:=input("Enter size of cup = ").lower()) in available_sizes:
#     print(f"Requested is available {requested_Size}")

flavours = ["masale chai","ginger chai","lemon chai"]

while(flavour:= input("Enter the flavour of chai you want = ").lower()) not in flavours:
    print(f"Sorrry we didn't have these {flavour}....")

print(f"Here is your {flavour}")