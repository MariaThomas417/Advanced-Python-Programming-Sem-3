print("Decorators")
def my_decorator(func):
        def wrapper():
              print("Something is happening before the function is called. ")
              func()
              print("Something is happening after the function is called. ")
        return wrapper

@my_decorator
def say_hello():
       print("Hello!")
say_hello()

print("Iterators")
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print("Generators")

def countdown(n):
       while n>0:
              yield n
              n -=1

for num in countdown(5):
       print(num)

print("Closures")
def outer_func(x):
        def inner_func(y):
            return x + y
        return inner_func

add_five = outer_func(5)
print(add_five(3))

          