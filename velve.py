# α, β, Γ, γ, Δ, δ, ϵ, ζ
# η, Θ, ϑ, ι, κ, Λ, λ, μ
# ν, Ξ, ξ, Π, π, ρ, Σ, σ
# τ, Φ, ϕ, χ, Ψ, ψ, Ω, ω

"""
Created on Sun Sep 8 12:15:01 2019
@author: kristjan.axelsson
"""

import pandas as pd
from numpy import linspace, sqrt

C = 1 # Formafaktor aus analytischem Model
b = 1 # m
l = 1 # #
h = 1 # m
η = 1 # viskosität
μ = 1 # faktor aus blendenströmung
ρ = 1 # kg/m^3
p0 = 0 # Ps
pmax = 500 # Pa
steps = 100
p_range = linspace(p0, pmax, steps)

# berechnung der volumenströme Q
Q_spalt = lambda dp: b*h**3*dp/(12*η*l)
Q_blende = lambda dp: μ*b*h*sqrt(2*dp/ρ)
Q_equal = η*l*(2/ρ)**(2/5)/(2*C**2)

data = pd.DataFrame()
data['Pressure'] = p_range
data['Spalt'] = Q_spalt(p_range)
data['Blende'] = Q_blende(p_range)

ax = data.plot(x='Pressure', y=['Spalt', 'Blende'], grid=True)
ax.set_title('Ventilströmungen')
ax.set_xlabel('Pressure [Pa]')
ax.set_ylabel('Volumenstrom [kg/m^3]')
print('Qspalt equal Qblende:', Q_equal, '[Pa]')



