# AI2_2017


```


String1



donuts
 OK  got: 'Number of donuts: 4' expected: 'Number of donuts: 4'
 OK  got: 'Number of donuts: 9' expected: 'Number of donuts: 9'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
both_ends
 OK  got: 'spng' expected: 'spng'
 OK  got: 'Helo' expected: 'Helo'
 OK  got: '' expected: ''
 OK  got: 'xyyz' expected: 'xyyz'
fix_start
 OK  got: 'ba**le' expected: 'ba**le'
 OK  got: 'a*rdv*rk' expected: 'a*rdv*rk'
 OK  got: 'goo*le' expected: 'goo*le'
 OK  got: 'donut' expected: 'donut'
mix_up
 OK  got: 'pox mid' expected: 'pox mid'
 OK  got: 'dig donner' expected: 'dig donner'
 OK  got: 'spash gnort' expected: 'spash gnort'
 OK  got: 'fizzy perm' expected: 'fizzy perm'
 
 
 
 string2
 
 
 
 verbing
 OK  got: 'hailing' expected: 'hailing'
 OK  got: 'swimingly' expected: 'swimingly'
 OK  got: 'do' expected: 'do'
not_bad
 OK  got: 'This movie is good' expected: 'This movie is good'
 OK  got: 'This dinner is good!' expected: 'This dinner is good!'
 OK  got: 'This tea is not hot' expected: 'This tea is not hot'
 OK  got: "It's bad yet not" expected: "It's bad yet not"
front_back
 OK  got: 'abxcdy' expected: 'abxcdy'
 OK  got: 'abcxydez' expected: 'abcxydez'
 OK  got: 'KitDontenut' expected: 'KitDontenut'
 
 
 
 list1
 
 
 
 match_ends
 OK  got: 3 expected: 3
 OK  got: 2 expected: 2
 OK  got: 1 expected: 1
front_x
 OK  got: ['xaa', 'xzz', 'axx', 'bbb', 'ccc'] expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
 OK  got: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'] expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
 OK  got: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
sort_last
 OK  got: [(2, 1), (3, 2), (1, 3)] expected: [(2, 1), (3, 2), (1, 3)]
 OK  got: [(3, 1), (1, 2), (2, 3)] expected: [(3, 1), (1, 2), (2, 3)]
 OK  got: [(2, 2), (1, 3), (3, 4, 5), (1, 7)] expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
 
 
 
 
 list2
 
 
 remove_adjacent
 OK  got: [1, 2, 3] expected: [1, 2, 3]
 OK  got: [2, 3] expected: [2, 3]
 OK  got: [] expected: []
linear_merge
  X  got: ['zz', 'xx', 'aa', 'bb', 'cc'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
  X  got: ['xx', 'aa', 'bb', 'cc', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
  X  got: ['bb', 'bb', 'aa', 'aa', 'aa'] expected: ['aa', 'aa', 'aa', 'bb', 'bb']


///////////////////////////////////////////////////////////////////////////////////////////////lab2

Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/student.INFORMATYKA/Desktop/lab2.py ===========
>>> hellow()
Hello, World!
>>> ox()
  |  |  
--------
  |  |  
--------
  |  |  

>>> XLxo()
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
========+========+========
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
========+========+========
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
>>> buzz(41)
408
>>> collatz(13)
10
>>> 
>>> convert(212)
100.0
>>> ob_ref()
[1, 0, 0]
['a', '', '']
[[1], [1], [1]]
>>> gcd(10, 25)
5
>>> flip_dict({"CA" : "US", "NY": "US", "ON": "CA"})
{'US': ['CA', 'NY'], 'CA': ['ON']}
>>> comprehension_read()
[1, 2, 3, 4]
[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
[0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9]
['python']
[None, None, None]
[[3, 2, 1, 12], ['a', 'b', 'c', 'aaaa'], [('do',), ['re'], 'mi', ('do', 'do', 'do', 'do')]]
['Y', 'O', 'N']
{8, 2, 3, 5}
>>> comprehension_write()
[1, 3, 5, 7]
[True, False, True, False]
['sam', 'guido']
['A', 'O', 'P']
['apple', 'pear']
[('apple', 5), ('orange', 6), ('pear', 4)]
{'pear': 4, 'orange': 6, 'apple': 5}
>>>


////////////////////////////////////////////////////////////////////////////////////////////////////Lab3.py

>>> print_two(1,2)
Arguments: 1 and 2

>>> print_two_test()
Arguments: 4 and 1
Arguments: 4 and 1
Arguments: 4 and 1
>>> 

>>> keyword_args(a=4)
a: 4
b: 1
c: X
d: None
>>> 

>>> print_keyword_args()
a: 5
b: 1
c: X
d: None
a: 5
b: 1
c: X
d: None
a: 5
b: 8
c: X
d: None
a: 5
b: 2
c: 4
d: None
a: 5
b: 0
c: 1
d: None
a: 5
b: 2
c: 4
d: 8
a: 1
b: 1
c: 7
d: None
a: 5
b: 2
c: []
d: 5
a: 1
b: 1
c: 7
d: None

>>> variadic()
Positional: ()
Keyword: {}

>>> print_variadic()
Positional: (2, 3, 5, 7)
Keyword: {}
Positional: (1, 1)
Keyword: {'n': 1}
Positional: ()
Keyword: {}
Positional: ()
Keyword: {'cs': 'Computer Science', 'pd': 'Product Design'}
Positional: (5, 8)
Keyword: {'k': 1, 'swap': 2}
Positional: (8, 3, 4, 5)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
Positional: (8, 3, 4, 5)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
Positional: (3, 4, 5, 8, 4, 1)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}
Positional: ({'a': 5, 'b': 'x'}, 'a', 'b')
Keyword: {'a': 5, 'b': 'x'}

>>> all_together(x=1,y=2)
x: 1
y: 2
z: 1
nums: ()
indent: True
spaces: 4
options: {}

>>> print_all_together()
x: 2
y: 5
z: 7
nums: (8,)
indent: False
spaces: 4
options: {}
x: 2
y: 5
z: 7
nums: (6,)
indent: None
spaces: 4
options: {}
x: {'x': 0, 'y': 1}
y: 0
z: 1
nums: (2, 3, 4, 5, 6, 7, 8, 9)
indent: True
spaces: 4
options: {}
x: [1, 2]
y: {3: 4}
z: 1
nums: ()
indent: True
spaces: 4
options: {}
x: 8
y: 9
z: 10
nums: (2, 4, 6)
indent: True
spaces: 0
options: {'a': [4, 5], 'b': 'x'}
x: 8
y: 9
z: 2
nums: (4, 6, 'z')
indent: True
spaces: 0
options: {'a': [4, 5], 'b': 'x'}

>>> speak_excitedly("test")
'test!'

>>> average(1,2,3,4,5)
3.0

>>> test_make_table()
=========================
| first_name  |     Sam |
| last_name   | Redmond |
| shirt_color |    pink |
=========================
==================================
|            song |    Style     |
| artist_fullname | Taylor $wift |
|           album |     1989     |
==================================

///////////////////////////////////////////////////LAB4.py

>>> alpha_score("ABC")
6

>>> two_best(["slowo","wyraz","wyrazenie"])
['slowo', 'wyraz']

>>> test_two_best()
['PyThOn', 'wOrLD']

>>> float_Control(1)
'Winner'
>>> float_Control(-1)
'Loser'
>>> float_Control(5)
'Tied'

>>> iterator_Consumption()
True
68
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    iterator_Consumption()
  File "C:/Python zadania/lab4.py", line 88, in iterator_Consumption
    (next(it))  # => StopIteration
StopIteration


```
