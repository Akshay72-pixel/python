class A:
    label = "A : BASS CLASS"
    
class B(A):
    label = "B : Masala blend"
    
class C(A):
    label = "C : Herbal blend"
    
class D(B,C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)