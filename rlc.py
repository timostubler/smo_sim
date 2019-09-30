# -*- coding: utf-8 -*-
# α, β, Γ, γ, Δ, δ, ϵ, ζ
# η, Θ, ϑ, ι, κ, Λ, λ, μ
# ν, Ξ, ξ, Π, π, ρ, Σ, σ
# τ, Φ, ϕ, χ, Ψ, ψ, Ω, ω
"""
Created on Tue May 14 14:02:31 2019
@author: timo.stubler / kristjan.axelsson
"""

import pandas as pd
from numpy import linspace as ls
from scipy.integrate import odeint
from math import sin,sqrt

R0 = 1*10**-1 # Ω
L = 1*10**-3 # H
C = 1*10**-2 # F
ue = 5 # V
uc0 = 0 # V
i0 = 0 # A
f = 50 # Hz
T = R0*C*100 # s
steps = 1200
p = T*2 # s
ts = ls(0, T*12, steps)
x0  = [uc0, i0]

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

# Lösung für veränderlichen Widerstandswert (Klappen)
# Widerstand bei unterschiedlichen Druckdifferenzen variabel! uc = x[0]
# Multiplizieren oder Dividieren bei R ??
def dx_dt(x, dt):
    if (signal(dt)-x[0]) < 0:
        R = R0/sqrt(abs(signal(dt)-x[0]))
    else:
        R = 100*R0
    return [x[1]/C, -x[0]/L-x[1]*R/L + signal(dt)/L]
  
res = odeint(dx_dt, x0, ts)

result = pd.DataFrame()
result['uc'] = res[:,0]
result['i'] = res[:,1]
result['t'] = ts
result['ue'] = [signal(dt) for dt in ts]
ax = result.plot(x='t', y=['ue', 'i', 'uc'], grid=True)
ax.set_title('RLC Schwingkreis')
ax.set_xlabel('t [s]')
