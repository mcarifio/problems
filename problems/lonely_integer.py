#!/usr/bin/env python3
# The [Lonely Integer](https://www.hackerrank.com/challenges/lonely-integer/problem) Problem

from collections import Counter
from collections import defaultdict
from typing import List
from functools import reduce

def singled_out(a:List[int]) -> List[int]:
    return [ k for (k, v) in Counter(a).items() if v == 1 ]

def singled_out_brute_force(a:List[int]) -> List[int]:
    result = defaultdict(int)
    for i in a: result[i] += 1
    return [ k for (k, v) in result.items() if v == 1 ]

if __name__ == '__main__':
    numbers = [0, 0, 1, 2, 1, ]
    print(singled_out(numbers))
    print(singled_out_brute_force(numbers))