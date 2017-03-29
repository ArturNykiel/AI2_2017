def hellow():
    print("Hello, World!")
    
def ox():

    x = "  |  |  "
    y = "--------"
    print(x)
    print(y)
    print(x)
    print(y)
    print(x)

def XLxo():
    s = """  |  |  H  |  |  H  |  |  
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
  |  |  H  |  |  H  |  |  """
    print(s)

def buzz(n):
    pom = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            pom = pom +  i
    return pom


def collatz(n):
    licznik = 1
    while n > 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        licznik += 1  
    return licznik


def convert(n):
    far = n
    cels = (far - 32)/1.8000
    return cels


def ob_ref():
    s = [0] * 3
    s[0] += 1
    print(s) 

    s = [''] * 3
    s[0] += 'a'
    print(s)  

    s = [[]] * 3
    s[0] += [1]
    print(s)


def gcd(a, b):
    pass
    while b:
        a, b = b, a % b
    return a

    
def flip_dict(d):
    out = {}
    for key, value in d.items():
        if value not in out:
            out[value] = []
        out[value].append(key)
    return out

def comprehension_read():
    print([x for x in [1, 2, 3, 4]])

    print([n - 2 for n in range(10)])

    print([k % 10 for k in range(41) if k % 3 == 0])

    print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

    arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
    print([el.append(el[0] * 4) for el in arr])
    print(arr)
   
    print([letter for letter in "pYthON" if letter.isupper()])

    print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})




def comprehension_write():
    arr = [0, 1, 2, 3]
    print([2 * elem + 1 for elem in arr])

    arr = [3, 5, 9, 8]
    print([elem % 3 == 0 for elem in arr])  

    arr = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
    print([elem[3:] for elem in arr if elem.startswith('TA_')])
    
    arr = ['apple', 'orange', 'pear']
    print([fruit[:1].upper() for fruit in arr])

    print([fruit for fruit in arr if len(fruit)<6])

    print([(fruit,len(fruit)) for fruit in arr])

    print({fruit:len(fruit) for fruit in arr})
