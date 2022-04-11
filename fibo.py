# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 13:29:53 2022

@author: 81906
"""

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    #printをwhileにそろえると結果が改行なしで出力される
 


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
    #returnをwhileの方に揃えないと0
    
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))