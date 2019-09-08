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
from math import sin

R = 1*10**-1 # Ω
L = 1*10**-3 # H
C = 1*10**-2 # F
ue = 5 # V
uc0 = 0 # V
i0 = 0 # A
f = 50 # Hz
T = 0.2 # s
steps = 100

ts = ls(0, T, steps)
x0  = [uc0, i0]

def dx_dt_1(x, dt):
    return [x[1]/C, -x[0]/L-x[1]*R/L + ue/L]
    
def dx_dt_2(x, dt):
    return [x[1]/C, -x[0]/L-x[1]*R/L + ue*(sin(f*dt/T))/L]
  
res = odeint(dx_dt_1, x0, ts)

result = pd.DataFrame()
result['uc'] = res[:,0]
result['i'] = res[:,1]
result['t'] = ts
ax = result.plot(x='t', y=['uc', 'i'], grid=True)
ax.set_title('LRC Schwingkreis')
ax.set_xlabel('t [s]')





