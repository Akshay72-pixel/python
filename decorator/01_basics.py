import functools
def decorators_my(func):
    @functools.wraps(func)
    def wrapper():
        print("Before Function Runs")
        func()
        print("After Function Runs")
    return wrapper

@decorators_my
def greet():
    print("Good morning")
    
greet()
print(greet.__name__)