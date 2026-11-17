#!/usr/bin/env python3
"""Exact QQ witness for the eight nodal members of a cubic pencil (SymPy)."""
from itertools import product
from sympy import Matrix, Poly, symbols, diff, prod, eye, zeros

x,y,z,lam=symbols('x y z lambda')
f=x**3-3*x+y**3-12*y+z**3-48*z
variables=(x,y,z)
crit=list(product((-1,1),(-2,2),(-4,4)))
H=Matrix([[diff(f,a,b) for b in variables] for a in variables])
values=[]
for p in crit:
    d=dict(zip(variables,p))
    assert all(diff(f,v).subs(d)==0 for v in variables)
    assert H.det().subs(d)!=0
    values.append(f.subs(d))
assert len(set(values))==8
basis=list(product((0,1),repeat=3))
M=zeros(8)
for j,exps in enumerate(basis):
    for i,coef,square in ((0,-2,1),(1,-8,4),(2,-32,16)):
        new=list(exps)
        if new[i]==0:
            new[i]=1; mult=1
        else:
            new[i]=0; mult=square
        M[basis.index(tuple(new)),j]+=coef*mult
D=Poly((lam*eye(8)+M).det(),lam)
assert D==Poly(prod(lam+v for v in values),lam)
assert D.degree()==8
print("PASS: 8 Morse critical points and distinct values")
print("critical values:",sorted(values))
print("Delta_f(lambda) =",D.as_expr().factor())
