# beecrowd | 1012 
import math

pi = 3.14159 
A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

s = (A + B + C)/2 
triangulo = math.sqrt(s * (s - A) * (s - B) * (s - C))
print(triangulo)