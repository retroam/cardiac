from pysb import *
from pysb.integrate import odesolve
from pysb.macros import *
from pylab import linspace, plot, xlabel, ylabel, show, savefig

# Simple toy model based on Saucerman implementation

Model()

# Declare monomers
Monomer('L', ['s'])
Monomer('R', ['s'])
Monomer('E', ['s'])
Monomer('S', ['s'])
Monomer('LR', ['s'])

# Declare parameters
Parameter('k1f', 1.0)
Parameter('k1r', 1.0)
Parameter('k2f', 1.0)
Parameter('k2r', 1.0)
Parameter('kcat', 1.0)
Parameter('Km', 1.0)
Parameter('k4', 1.0)
Parameter('L0', 1.0)
Parameter('R0', 1.0)
Parameter('E0', 1.0)
Parameter('S0', 1.0)


# Declare initial conditions
Initial(L(s=None), L0)
Initial(R(s=None), R0)
Initial(S(s=None), S0)
Initial(E(s=None), E0)

# Equations
Rule('L_binds_R', L(s=None) + R(s=None) <> L(s=1) % R(s=1), k1f, k1r)
Rule('LR_binds_E', LR(s=None) + E(s=None) <> LR(s=1) % E(s=1), k2f, k2r)


# Observe complexes
Observable('LR', L(s=1) % R(s=1))

# Simulation
time = linspace(0, 40, 100)
y = odesolve(model, time)

plot(time, y['LR'])
xlabel('time (seconds)')
ylabel('Amount of LR')
savefig('img')

