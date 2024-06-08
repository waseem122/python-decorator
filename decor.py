def strn_decor(func):
    def wrapper(**kwargs):
        result = func(kwargs)
        return result

    return wrapper



def hello_world(func):
    print('Hi!')
    def wrapper(*args):
        result = func(*args)
        print(result)
        return 'Decorator is complete!'
    
    return wrapper
@strn_decor
def greetings(greetin):
    print(type(greetin))
    for a, b in greetin.items():
        result = b
    return result


@hello_world
def hello(a, b):
    return a+b

print(hello(2,3))
print(greetings(greets = 'Hello Everyone! How are you doing?'))