#!/usr/bin/env python
# -*- coding:utf8 -*-

import re
p = re.compile(r'(\w+) (\w+)')
s = 'hello 123, hello 456'

print p.sub(r'hello world', s)
print p.sub(r'\2 \1', s)


def func(m):
    return 'hi' + ' ' + m.group(2)


print p.sub(func, s)
print p.sub(func, s, 1)
