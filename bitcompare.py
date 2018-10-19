#!/usr/bin/env python
#Created By: J.Medlock
#Created On: 2017.08.25

X = str(input('Please enter a bit number: '))
Y = str(input('Please enter a bit number to compare: '))

#combined[X, Y]

def findBit(X, Y):
    one = "1"
    new_x = X
    new_y = Y
    list_x = []
    list_y = []
    together = []
    differentLength = abs(len(X)) - len(Y)
    final = ""

    if len(X) > len(Y):
        for i in X:
          together.append("0")
        new_x = ("0" * differentLength) + Y
    elif len(Y) > len(X):
        for i in Y:
          together.append("0")
        new_y = ("0" * differentLength) + X

    for i in new_x:
      list_x.append(i)
      list_y.append(i)
      
    for i, c in enumerate(new_x):
      if c != list_y[i]:
        together[i] = "1"
        
    for i, c in enumerate(new_y):
      if c != list_x[i]:
        together[i] = "1"
       
    final = "0b" + final.join(together)
    return final

print findBit(X, Y)
