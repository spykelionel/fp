def countdown(n):
    while n > 0:
        yield n
        n -= 1

counter = countdown(5)
for num in counter:
    print(num)


import sys
# List comprehension
squared_list = [x ** 2 for x in range(1, 1000000)]
sys.getsizeof(squared_list)
# 8448728

# Generator expression
squared_generator = (x ** 2 for x in range(1, 1000000))
sys.getsizeof(squared_generator)
# 112


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_sequence = fibonacci_generator()
for _ in range(10):
    print(next(fib_sequence))