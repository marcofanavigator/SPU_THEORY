import sympy as sp
y, Nf, Lambda = sp.symbols('y Nf Lambda', positive=True)
phi = sp.symbols('phi', positive=True)
a, b = sp.symbols('a b')
mf = y*phi
Vt = a*phi**2 + b*phi**4
VCW = - Nf * mf**4 / (64*sp.pi**2) * sp.log(mf**2 / Lambda**2)
V = Vt + VCW
Vp = sp.diff(V, phi)
Vpp = sp.diff(Vp, phi)
# lambdify for numeric eval
f_V = sp.lambdify((phi,a,b,y,Nf,Lambda), V, 'numpy')
f_Vpp = sp.lambdify((phi,a,b,y,Nf,Lambda), Vpp, 'numpy')
# example numeric
print("V''(phi0) sympy:", f_Vpp(6.051296464823242, -1.0, 0.01, 0.16, 1.0, 1e5))
