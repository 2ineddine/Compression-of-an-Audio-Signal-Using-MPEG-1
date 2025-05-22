#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:10:49 2021

@author: boutin
"""
import numpy as np
import matplotlib.pyplot as plt

def TFCT(Nwin, Nhop, Nfft, x_vect,Fe):
    Nhop=int(Nhop)
    w_vect=np.hamming(Nwin)
    L = int(np.floor(1+len(x_vect)/Nhop)) #nb de colonnes
    nl=int(np.floor(Nfft//2+1)) #nb de lignes
    x_mat=np.zeros([nl,L],dtype=complex)
    Lx2=int((L-1)*Nhop+Nwin)
    x_vect2=np.append(x_vect,np.zeros([1,Lx2-len(x_vect)]))
    freq_vect=np.linspace(0,Fe/2,nl)
    t_vect=np.arange(Nwin//2,Nwin//2+L*Nhop,Nhop)/Fe

    for l in range(0,L):
        trame=x_vect2[l*Nhop:l*Nhop+Nwin]*w_vect
        trame_fft=np.fft.fft(trame,Nfft)
        x_mat[:,l]=trame_fft[0:nl]

    return x_mat,t_vect,freq_vect


def ITFCT(x_mat,Nwin,Nhop,Fe,w_vect):
    [nl,L]=x_mat.shape
    Nfft=2*(nl-1)
    x_vect0=np.zeros([int(Nwin+Nhop*(L-1)),1])
    
    
    for i in range(0,L):
        #i=56
        trame_fft0=x_mat[:,i]
        trame_fft0comp=np.conj(np.flipud(trame_fft0[1:-1]))
        trame_fft=np.append(trame_fft0,trame_fft0comp)
        trame=np.real(np.fft.ifft(trame_fft,Nfft))
        #plt.figure(12)
        #plt.plot(trame)
        # x_vect=np.append(x_vect,np.zeros([1,Nhop]))
        x_vect0[int(i*Nhop):int(i*Nhop+Nwin),0]=x_vect0[int(i*Nhop):int(i*Nhop+Nwin),0]+trame
        #plt.figure(13)
        #plt.plot(x_vect0)
   
    plt.figure(10)
    plt.plot(x_vect0)
    
    K=np.sum(w_vect)/Nhop
    t_vect=np.arange(0,x_vect0.size/Fe,1/Fe)
    # plt.plot(x_vect)
    # plt.show()
    y_vect0=(x_vect0/K)
    #y_vect=y_vect0.astype(np.int16)
    return y_vect0, t_vect

