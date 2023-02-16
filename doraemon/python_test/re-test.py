import re

str_ = 'data'

r = re.match(
        r'^\s*([alarm|data])\s*$',
        str_)

if r is not None:
    print(r.groups(0))
    print(r.groups(1))


