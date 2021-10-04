
"""
Solve Task (2) Mosscow - Apartment (Logic Gates) in Google Beginners Quest 2021

"""


import random

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0


while True:
     A_B = ~(A | ~B) 
     C_D = (~C | D)
     E_F = (E | ~F)
     G_H = ~(G | H)
     H_I = (H ^ I)
     I_J = (I & J)

     up_1 = (A_B & ~(C_D | E_F))
     down_1 = ((G_H & H_I) & I_J)

     result= up_1 & down_1

     if result == 1:
          print(f"A = {A} \nB = {B} \nC = {C} \nD = {D} \nE = {E} \nF = {F} \nG = {G} \nH = {H} \nI = {I} \nJ = {J}")
          break

     tmp = random.randint(0, 10)

     if tmp == 0:
          A = not A
     elif tmp == 1:
          B = not B
     elif tmp == 2:
          C = not C
     elif tmp == 3:
          D = not D
     elif tmp == 4:
          E = not E
     elif tmp == 5:
          F = not F
     elif tmp == 6:
          G = not G
     elif tmp == 7:
          H = not H
     elif tmp == 8:
          I = not I
     elif tmp == 9:
          J = not J
     
