#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 2019

@author: kristjan
"""

import numpy as np

class Signal:
    
    def __init__(self, amplitude, frequency):
        self.amplitude = amplitude
        self.period = 1/frequency
    
    def rect(self, t):
        if (t % self.period) <= self.period/2:
            return self.amplitude
        else:
            return -self.amplitude
        
    def sin(self, t):
        return self.amplitude*(np.sin(2*np.pi*t/self.period))
    
    
class Velve:
    
    def __init__(self, R):
        self.R = R
    
    def const(self, u):
        return self.R*np.sqrt(abs(u))
        
    def backward(self, u):
        if u > 0: # druckhub
            return self.R*10**9 # kein leckstrom
        else: # saughub
            return self.R
        
    def forward(self, u):
        if u > 0: # druckhub
            return self.R
        else: # saughub
            return self.R*10**2 # leckstrom 
    

if __name__ == '__main__':
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    
    signal = Signal(amplitude=5, frequency=1)
    curves = pd.DataFrame(columns=['t', 'sin', 'rect'])
    curves['t'] = np.linspace(0, 3, 251)
    curves['sin']  = [signal.sin(t)  for t in curves['t']]
    curves['rect'] = [signal.rect(t) for t in curves['t']]
    curves.plot(x='t', y=['sin', 'rect'], ax=ax1, grid=True)
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Voltage [V]')
    
    velve = Velve(R=1)
    curves = pd.DataFrame(columns=['u', 'v_fw', 'v_bw'])
    curves['u'] = np.linspace(-1, 1, 251)
    curves['v_fw'] = [velve.forward(u) for u in curves['u']]
    curves['v_bw'] = [velve.backward(u) for u in curves['u']]
    curves.plot(x='u', y=['v_fw', 'v_bw'], ax=ax2, grid=True)
    ax2.set_yscale('log')
    ax2.set_xlabel('Voltage [V]')
    ax2.set_ylabel('Resistance [Ohm]')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    