# -*- coding: utf-8 -*-
"""
Program PI value calculate

Created on Tue Apr 19 22:46:00 2023

@author: LN Starmark
@e-mail: ln.starmark@ekatra.io
@e-mail: ln.starmark@gmail.com
@tel:    +380 66 9805661
"""
import str_common as strc
import time

def approximate_pi(n):
    step = 1.0 / n
    res = 0.0

    for i in range(n):
        x = (i + 0.5) * step
        res += 4.0 / (1.0 + x * x)
    return step * res

def main():
    strc.titleprogram("Test time evaluation calculate value PI",
                      "Test with other N approximation values",
                      "ln.starmark@gmail.com\tln.starmark@ekatra.io")

    lst = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
    
    for i in lst:

        start = time.time()
        res = approximate_pi(i)
        end = time.time() - start

        print(f"N approximation = {i}")
        print(f"Pi = {res}")
        print(f"Time = {end}")
        print()

if __name__ == '__main__':
    main()