from functools import wraps

def log_acticity(func):
     @wraps(func)
     def wrapper(*args,**kewords):
         print(f"    Calling: {func.__name__}")
         result = func(*args,**kewords)
         print(f"😊 Finished: {func.__name__}")
         return result
     return wrapper
 
@log_acticity
def bre_chai(type,milk="No"):
    print(f"Brewing {type} chai... status {milk}")
    
bre_chai("Lemon") 
 
 
 