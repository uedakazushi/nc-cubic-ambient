#!/usr/bin/env python3
"""Exact QQ example: a quantum central cubic has nonclassical point values.

Finite computation in the free algebra, modulo all relation multiples of
word length <=4. This certifies the example, not a generic theorem.
Requires SymPy.
"""
from itertools import product, permutations
from sympy import Matrix, zeros

a={'x':-3,'y':-12,'z':-48}
R=[{'yz':1,'zy':-1,'xx':-3,'':-a['x']},
   {'zx':1,'xz':-1,'yy':-3,'':-a['y']},
   {'xy':1,'yx':-1,'zz':-3,'':-a['z']}]
words=['']+[''.join(t) for n in range(1,5) for t in product('xyz',repeat=n)]
index={w:i for i,w in enumerate(words)}
rows=[]
for m in range(3):
    for n in range(m+1):
        for u in product('xyz',repeat=n):
            for v in product('xyz',repeat=m-n):
                u,v=''.join(u),''.join(v)
                for r in R:
                    row={}
                    for w,c in r.items():
                        key=u+w+v
                        row[key]=row.get(key,0)+c
                    rows.append(row)
M=zeros(len(rows),len(words))
for i,row in enumerate(rows):
    for w,c in row.items():M[i,index[w]]=c
E,piv=M.rref(simplify=False)
assert M.shape==(102,121) and len(piv)==86
C={'xxx':1,'yyy':1,'zzz':1,'x':-3,'y':-12,'z':-48}
for perm in set(permutations('xyz')):
    w=''.join(perm)
    C[w]=C.get(w,0)-3
for gen in 'xyz':
    row={}
    for w,c in C.items():
        row[w+gen]=row.get(w+gen,0)+c
        row[gen+w]=row.get(gen+w,0)-c
    v=zeros(1,len(words))
    for w,c in row.items():v[0,index[w]]=c
    residual=v.copy()
    for i,j in enumerate(piv):
        residual-=v[0,j]*E[i,:]
    assert all(q==0 for q in residual)
pairs=[]
for x,y,z in product((-1,1),(-2,2),(-4,4)):
    f=x**3+y**3+z**3-3*x-12*y-48*z
    omega=f-18*x*y*z
    pairs.append((f,omega))
assert len(set(x for x,y in pairs))==len(set(y for x,y in pairs))==8
assert Matrix([[omega,1,f] for f,omega in pairs]).rank()==3
print("PASS: centrality and non-affine quantum values (QQ)")
print("classical values:",sorted(x for x,y in pairs))
print("quantum central values:",sorted(y for x,y in pairs))
