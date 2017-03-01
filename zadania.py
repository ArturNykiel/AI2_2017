def donuts(ile):
  if ile < 10:
    return 'liczba paczkow: '+ str(ile)
  else:
    return 'liczba paczkow: wiele'

def both_ends(cos):
  if len(cos) < 2:
    return ''
  p2 = cos[0:2]
  o2 = cos[-2:]
  return p2 + o2

def fix_start(cos):
  head = cos[0]
  back = cos[1:]
  fixed_back = back.replace(head, '*')
  return head + fixed_back

def mix_up(a, b):
  a1 = b[:2] + a[2:]
  b1 = a[:2] + b[2:]
  return a1 + ' ' + b1

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
  print ('donuts')
  test(donuts(4), 'liczba paczkow: 4')
  test(donuts(9), 'liczba paczkow: 9')
  test(donuts(10), 'liczba paczkow: wiele')
  test(donuts(99), 'liczba paczkow: wiele')

  print()
  print ('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print()
  print ('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print()
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__ == '__main__':
  main()
