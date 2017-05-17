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
    print(list(map(lambda l, r: l * r, range(2, 5), range(3, 9, 2))))

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
    return functools.reduce(operator.mul, range(1,n+1))

def testfact():
    print(fact(3))
    print(fact(7))

def testcomparisons():
    words = ['pear', 'cabbage', 'apple', 'bananas']
    min(words) 
    words.sort(key=lambda s: s[-1])  
    words  
    max(words, key=len)  
    x= min(words, key=lambda s: s[1::2]) 
    print(x)

def highest_alphanumeric_score():
    def alpha_score(upper_letters):
        return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))


    def two_best(words):
        words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
        return words[:2]

    print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))