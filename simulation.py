#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 2019

@author: kristjan
"""

import pandas as pd
import numpy as np
from scipy.integrate import odeint

from components import Signal, Velve

Us = 5 # amplitude
Cp = 1 # pumpkammerkapazität
Rs = 1 # schlauchwiderstand
Rv = 1 # ventilwiderstand
Ur = 0 # reservoirdruck
Uc0 = 0 # startdruck in der pumpkammer

T = 35*(Rs+Rv)*Cp # ladedauer | warum nicht faktor 5 !?
steps = 500 # anzahl der zeitschritte
t_space = np.linspace(0, 2*T, steps, endpoint=True)

signal = Signal(amplitude=Us, frequency=1/T)
us = signal.rect # anregungssignal der pumpe
velve = Velve(R=Rv)  
Rvelve = velve.const # ventiltyp
    
i_scale = 5 # hängt auch von der anzahl der zeitschritte ab!

##############################################################################

def du_dt(u, t):
    u = u[0]
    uv = (Ur-us(t)+u)*Rv/(Rv+Rs)-us(t)+u
    return (us(t)-u+Ur)/((Rs+Rvelve(uv))*Cp)
    
uc = odeint(du_dt, Uc0, t_space)[:,0]

data = pd.DataFrame(columns = ['t', 'us', 'uc', 'ur', 'i'])
data['uc'] =  uc
data['t'] =  t_space
data['us'] = [us(t) for t in t_space]
data['ur'] = [Ur for _ in t_space]
data['i'] = np.gradient(uc)*i_scale

axes = data.plot(x='t', y=['us', 'uc', 'ur', 'i'], grid=True)
axes.set_title('Simple Pump')
axes.set_xlabel('Time [s]')
axes.set_ylabel('Voltage [V]')

print('nettostrom:', data['i'].sum())

