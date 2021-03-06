# α, β, Γ, γ, Δ, δ, ϵ, ζ
# η, Θ, ϑ, ι, κ, Λ, λ, μ
# ν, Ξ, ξ, Π, π, ρ, Σ, σ
# τ, Φ, ϕ, χ, Ψ, ψ, Ω, ω

"""
Created on Sun Sep 8 20:48:25 2019
@author: kristjan.axelsson
"""

import pandas as pd
from numpy import linspace as ls
from scipy.integrate import odeint
from math import sin

R = 1*10**-1 # Ω
C = 1*10**-2 # F
ue = 5 # V
uc0 = 0 # V
i0 = 0 # A
f = 10 # Hz
T = 5*R*C # s
p = T*2 # s
steps = 200
ts = ls(0, T*2, steps+1)
u0  = uc0

def const(dt):
    return ue

def rect(dt):
    if (dt % p) > p/2:
        return 0
    else:
        return ue
    
def sinus(dt):
    return ue*(sin(f*dt/T))

signal = rect

def du_dt(u, dt):
    return (signal(dt)-u)/(R*C)

res = odeint(du_dt, u0, ts)

result = pd.DataFrame()
result['uc'] = res[:,0]
result['t'] = ts
result['ue'] = [signal(dt) for dt in ts]
ax = result.plot(x='t', y=['ue', 'uc'], grid=True)
ax.set_title('RC Glied')
ax.set_xlabel('t [s]')
print('T:', T)





