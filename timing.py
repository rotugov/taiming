#!/usr/bin/python3 

import time
import random

d = [[random.randint(0, 150000)] * random.randint(0, 15) for _ in range(0, 150000)]

# 1 % is None
for _ in range(0, 1500):
    i = random.randint(0, 149999)
    d[i] = None


function = lambda: d[random.randint(0, 149999)]

T = 100
R = 100000

timings = []
for _ in range(T):
    t = time.time()
    for _ in range(R):
        result = function()
        if result:
            for r in result:
                tmp = r + r
    timings.append(time.time()-t)
t = sum(timings) / len(timings)
print(f'Result with IF with 1% None: {t}')


timings = []
for _ in range(T):
    t = time.time()
    for _ in range(R):
        result = function()
        try:
            for r in result:
                tmp = r + r
        except TypeError:
            pass
    timings.append(time.time()-t)
t = sum(timings) / len(timings)
print(f'Result with TRY/EXCEPT with 1% None: {t}')
