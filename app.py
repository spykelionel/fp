from functools import reduce

# Pure function - no side effects 
def add(x, y):
    return x + y

# Higher-order function taking/returning functions
def apply(f, x, y):
    return f(x, y)

# Map function applying a function over a sequence
def map(f, seq):
    return [f(x) for x in seq]

# Filter function removing elements using predicate
def filter(pred, seq): 
    return [x for x in seq if pred(x)]

# Reduce function folding list to single value
def reduce(f, seq, init):
    acc = init
    for x in seq:
        acc = f(acc, x)
    return acc

# Function composition
def compose(f, g):
    return lambda x: f(g(x))

# Usage:
nums = [1, 2, 3]

add_2 = apply(add, 2, 3) # Higher-order 
print(add_2) # Prints 5

doubled = map(lambda x: 2*x, nums) 
print(doubled) # [2, 4, 6] 

evens = filter(lambda x: x%2 == 0, doubled)
print(evens) # [4, 6]

sum = reduce(add, nums, 0)  
print(sum) # 6

# Composition
times2 = lambda x: x*2  
inc = lambda x: x+1
times2theninc = compose(inc, times2)
print(times2theninc(5)) # Prints 11