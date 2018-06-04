#!/bin/python

import math
import os
import random
import re
import sys

n = int(raw_input().strip())

for i in range(1, 11):
    print "{} x {} = {}".format(n, i, i * n)



if __name__ == '__main__':
    n = int(raw_input().strip())