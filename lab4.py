import random      
import functools   
import operator    
import itertools    
import collections  
import inspect      

def test_lambda():
    (lambda val: val ** 2)(5)  # => 25
    (lambda x, y: x * y)(3, 8)  # => 24
    (lambda s: s.strip().lower()[:2])('  PyTHon')

def test_map():
    print(list(map(int, ['12', '-2', '0'])))
    print(list(map(len, ['hello', 'world'])))
    print(list(map(lambda s: s[::-1], ['hello', 'world'])))
    print(list(map(lambda n: (n, n ** 2, n ** 3), range(2, 6))))
    print(list(map(lambda l, r: l * r, zip(range(2, 5), range(3, 9, 2)))))

def test_filter():
    print(list(filter(lambda x: int(x) >= 0, ['12', '-2', '0'])))
    print(list(filter(lambda x: x == 'world', ['hello', 'world'])))
    print(list(filter(lambda x: x[0] == 'S', ['Stanford', 'Cal', 'UCLA'])))
    print(list(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(20))))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    return functools.reduce(lambda x, y: x * y / gcd(x, y), args)

def fact(n):
    return functools.reduce(operator.mul, range(n))

def testfact():
    print(fact(3))
    print(fact(7))
