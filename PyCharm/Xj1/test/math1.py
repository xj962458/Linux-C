import sympy
a=sympy.Abs(sympy.sqrt(3)-sympy.sqrt(6))-sympy.Abs(3-sympy.sqrt(6))
print(a)

b=(sympy.I**2+sympy.I**3+sympy.I**(-1))/(1-sympy.I)
b=sympy.simplify(b)
print(b)

x=sympy.Symbol("x")
c=sympy.solveset((x+2)**3-125,domain=sympy.Reals)
print(c)

z=sympy.Symbol("z")
d=sympy.solveset((z-sympy.I)*sympy.I-(2+sympy.I),domain=sympy.Complexes)
print(d)
e=sympy.simplify(d)
print(e)
f=sympy.simplify(-sympy.I*(2+sympy.I)+sympy.I)
print(f)

