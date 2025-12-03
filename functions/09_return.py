def make_chai():
    return "Here is your masal chaiii"

return_value = make_chai()
print(return_value)

def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry chai over early"
    return "chai is ready"

print(chai_status(1))

def chai_left():
    return 20,100

remain , sold = chai_left()
print(remain,sold)