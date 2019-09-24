# α, β, Γ, γ, Δ, δ, ϵ, ζ
# η, Θ, ϑ, ι, κ, Λ, λ, μ
# ν, Ξ, ξ, Π, π, ρ, Σ, σ
# τ, Φ, ϕ, χ, Ψ, ψ, Ω, ω

"""
Created on Sun Sep 8 20:48:25 2019
@author: kristjan.axelsson
"""

import pandas as pd
import numpy as np
from numpy import linspace as ls
from scipy.integrate import odeint
from math import sin, log

R = 1*10**-1 # Ω
C = 1*10**-2 # F
ue = 5 # V
uc0 = 0 # V
i0 = 0 # A
f = 10 # Hz
T = 5*R*C # s
p = T*2 # s
steps = 200
ts = ls(0, T*5, steps+1)
u0  = uc0

def const(dt):
    return ue

def rect(dt):
    if (dt % p) > p/2:
        return -ue
    else:
        return ue
    
def sinus(dt):
    return ue*(sin(f*dt/T))

signal = rect

def diode_thing(du):
    du = float(du[0])
    if du > 0:
        return R#*log(1+du)
    else:
        return 10*R

def du_dt(u, dt):
    ur = signal(dt)-u
    R = diode_thing(ur)
    return ur/(R*C)

res = odeint(du_dt, u0, ts)

result = pd.DataFrame()
result['uc'] = res[:,0]
result['t'] = ts
result['ue'] = [signal(dt) for dt in ts]
ax = result.plot(x='t', y=['ue', 'uc'], grid=True)
ax.set_title('RC Glied')
ax.set_xlabel('t [s]')
print('T:', T)
