import time
from functools import wraps

def fib_iter(number: int)-> int:
    fib ={'a':0, 'b':1}
    if number == 0:
        return 0
    elif number == 1:
        return 1
    for _ in range(1,number):
        fib['a'], fib['b'] = fib['b'], fib['a'] + fib['b']
    return fib['b']

def fib_recur(number: int)-> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib_recur(number - 1) + fib_recur(number - 2)

def fib_mem(number: int, mem ={})-> int:
    if number in mem:
        return mem[number]
    elif number <= 1:
        return number
    else:
        n_minus_1 = fib_mem(number - 1, mem)
        n_minus_2 = fib_mem(number - 2, mem)
        mem[number] = n_minus_1 + n_minus_2
    return mem[number]

def main()-> None:
    number: int = 10
    print(f"Using Iterative Fibonacci: {number}  {fib_iter(number)}")
    print(f"Using Recursive Fibonacci {number}: is {fib_recur(number)}")
    print(f"Using memorization of 100: is {fib_mem(100)}")

if __name__=="__main__":
    main()
