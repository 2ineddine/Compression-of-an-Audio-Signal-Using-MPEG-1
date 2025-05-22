"""
#############################
#   MIDTREAD_DEQUANTIZER    #
#############################
Created on Fri Apr  2 11:10:49 2021

@author: boutin
"""
import numpy as np

def Fuquant_inv(xq,R):
    if R==0:
        return 0
    else :
        yq=np.round(xq)
        sign=-2*(yq//(2**(R-1)))+1
        Q=2/(2**R-1)
        x=yq%(2**(R-1))
        return sign*Q*x