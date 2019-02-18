import sys
import logging
import pytest
import problems.lonely_integer as li

def lonely_test():
    numbers = [0, 0, 1, 2, 1, ]
    assert li.singled_out(numbers) == [2]