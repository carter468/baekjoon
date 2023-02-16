# 잠수함 식별
# Gold 5, regex

import re

print('SUBMARINE' if re.compile('(100+1+|01)+').fullmatch(input()) else 'NOISE')