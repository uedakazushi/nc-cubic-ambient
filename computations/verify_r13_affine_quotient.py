#!/usr/bin/env python3
"""Exact QQ test for the graded R(1,3) affine action and discriminant covariance.

Checks a nontrivial change of coordinates, the eight critical points, degree-8
polynomial covariance, and the 12-dimensional affine tangent orbit.
A finite witness does not replace the general theorem in the manuscript.
"""
from itertools import product
import sympy as S
x,y,z,L=S.symbols('x y z lambda')
U=S.Matrix([x,y,z])
f=x**3-3*x+y**3-12*y+z**3-48*z
A=S.Matrix([[2,1,0],[0,3,1],[0,0,5]])
b=S.Matrix([1,-2,1]); D=A.det()
assert D==30
sub=lambda p,v:S.expand(p.subs(dict(zip(U,v)),simultaneous=True))
g=S.expand((sub(f,A*U+b)-sub(f,b))/D)
assert all(S.expand(q)==0 for q in S.Matrix([S.diff(g,v) for v in U])-A.T*S.Matrix([sub(S.diff(f,v),A*U+b) for v in U])/D)
points=[S.Matrix(v) for v in product((-1,1),(-2,2),(-4,4))]
values=[sub(f,v) for v in points]; fb=sub(f,b)
moved=[A.inv()*(p-b) for p in points]
for p,v in zip(moved,values):
    assert all(sub(S.diff(g,w),p)==0 for w in U)
    assert S.simplify(sub(g,p)-(v-fb)/D)==0
delta=S.prod(L+v for v in values)
deltag=S.prod(L+sub(g,p) for p in moved)
assert S.expand(deltag-D**(-8)*delta.subs(L,D*L-fb))==0
q=S.Matrix([1,2,3]); c=S.Matrix([1,2,4])
fstar=sum(v**3+q[i]*v**2+c[i]*v for i,v in enumerate(U))
M=S.Matrix(3,3,lambda i,j:S.Symbol('m%d%d'%(i,j)))
beta=S.Matrix(S.symbols('b0 b1 b2'))
unknowns=list(M)+list(beta)
lin=S.expand((S.Matrix([S.diff(fstar,v) for v in U]).T*(M*U+beta))[0]-S.trace(M)*fstar)
P=S.Poly(lin,x,y,z)
equations=[S.expand(P.coeff_monomial(x**i*y**j*z**k)) for i in range(4) for j in range(4-i) for k in range(4-i-j) if i+j+k>0]
V=S.linear_eq_to_matrix(equations,unknowns)[0]
assert V.shape==(19,12) and V.rank()==12
print('PASS affine action, eight critical points, and discriminant covariance (QQ)')
print('PASS affine-orbit tangent rank=12 and finite stabilizer witness')
print('det(A)=',D,'f(b)=',fb,'critical values=',sorted(values))

# Generic reconstruction of the gradient from its 8-point Jacobian scheme:
# an integrable 3x3 recombination of the three quadratic gradients is scalar.
fw=3*(x**3+y**3+z**3)+5*x*y*z+x**2+2*y**2+3*z**2+x+2*y+4*z
Q=S.Matrix([S.diff(fw,v) for v in U])
N=S.Matrix(3,3,lambda i,j:S.Symbol('n%d%d'%(i,j)))
Pvec=N*Q
closed=[]
for i,j in ((0,1),(0,2),(1,2)):
    eq=S.Poly(S.expand(S.diff(Pvec[j],U[i])-S.diff(Pvec[i],U[j])),x,y,z)
    closed.extend(eq.coeff_monomial(v) for v in (1,x,y,z))
C=S.linear_eq_to_matrix(closed,list(N))[0]
assert C.shape==(12,9) and C.rank()==8
assert C.nullspace()==[S.Matrix([1,0,0,0,1,0,0,0,1])]
print('PASS gradient integrability rank=8, scalar kernel')
