"""
Given n as input. Print following pattern using For loop.
n=2
1 
12 
2
"""

n = 2
pt = ""
pt2 = ""
for i in range(1, n+1):
  pt = pt + str(i)
  print(pt)
for i in range(1, n+1):
  pt2 = pt2 + str(n)
  n = n - 1
  print(pt2)
  