def hello_world(func):
    print('Hi!')
    def wrapper(*args):
        result = func(*args)
        print(result)
        return 'Decorator is complete!'
    
    return wrapper


@hello_world
def hello(a, b):
    return a+b

print(hello(2,3))