# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:59:33 2021

@author: Shirgaonkar
"""

import re
def checker(contact):
    pattern=r"[789]\d{9}$"
    if re.match(pattern, contact):
        return "YES"
    else:
        return "NO"
    
n=int(input())
for i in range(n):
    print(checker(input()))