from re import S
import numpy as np
from sympy import Symbol

def Matrix(a,b,c,d):
    mtr=[a,b,c,d]
    return mtr

def Multuple_mat(A,B):
    a,b,c,d=0,0,0,0
    a=A[0]*B[0]+A[1]*B[2]
    b=A[0]*B[1]+A[1]*B[3]
    c=A[2]*A[0]+A[3]*B[2]
    d=A[2]*B[1]+A[3]*B[3]
    mtr=[a,b,c,d]
    return mtr

f=Symbol('f')
L1=Symbol('L1')
L2=Symbol('L2')
L3=Symbol('L3')
n1=Symbol('n1')
n2=Symbol('n2')

A=Matrix(1,5,0,1)
print(A)
B=Matrix(1,0,0,n2/n1)
print(B)
#print(Multuple_mat(A,B))
AB=Multuple_mat(A,B)
print(AB)
C=Matrix(1,L2,0,1)
ABC=Multuple_mat(AB,C)
#print(ABC)
D=Matrix(1,0,-1/f,1)
ABCD=Multuple_mat(ABC,D)
print(ABCD)
E=Matrix(1,L3,0,1)
ABCDE=Multuple_mat(ABCD,E)
#print(ABCDE)
F=E
ABCDEF=Multuple_mat(ABCDE,F)
G=D
ABCDEFG=Multuple_mat(ABCDEF,G)
H=C
ABCDEFGH=Multuple_mat(ABCDEFG,H)
I=Matrix(1,0,0,n1/n2)
ABCDEFGHI=Multuple_mat(ABCDEFGH,I)
J=Matrix(1,L1,0,1)
ABCDEFGHIJ=Multuple_mat(ABCDEFGHI,J)
X=ABCDEFGHIJ[0]
Y=ABCDEFGHIJ[3]
#print('A=',X)
#print('D=',Y)