avialable_size = ['smmall','medium','large']

if (size:=input("Enter the cup sizes").lower() not in avialable_size ):
    print(f"{size} cups are aviable....")