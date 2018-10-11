"""
Helper functions needed for main.py are presented and described here.
If one is interested in the individual plots for each image, you can uncomment the plot lines in the functions stardistancex or stardistancey.
"""

import numpy
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import scipy.signal
import os,sys

# Defining our gaussian function which will be used later to fit pixel intensity

def gauss(x, *p):
    A = p[0]
    mu = p[1]
    sigma = p[2]
    rho = p[3]
    return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))+rho

# This function searches for the star within a specified range. This is for the x-dimension    
            
def stardistancex(filename,minx,maxx) :
    
    # star, horizontal
    g=pyfits.open(filename)
    image_data=g[0].data
    
    y=image_data.sum(0)[minx:maxx]
    x=numpy.arange(minx,maxx,1)
    xl=numpy.linspace(minx,maxx,500)
    
    a1 = image_data.sum(0)[minx:maxx].max()
    a2 = x[y.max() == y][0]
    a3 = 1
    a4 = image_data.sum(0).min() 
    coeff1, var_matrix = curve_fit(gauss,x,y,p0=[a1,a2,a3,a4])
    
    yfit=gauss(xl,coeff1[0],coeff1[1],coeff1[2],coeff1[3]);
    #plt.plot(x,y,"+") # Note these are commented as we do not want multiple plots when main.py is run
    #plt.plot(xl,yfit)
    #plt.show()
    
    return coeff1[1]

# Similar function to the above function, but this is for the y-dimension   
# Note that both these functions can be easily combined into one function if computational power becomes an issue.
# For clarity purposes we leave it as 2 different functions here     

def stardistancey(filename,miny,maxy) : 
    g=pyfits.open(filename)
    imag_data=g[0].data
    # star, vertical
    
    yV=imag_data.sum(1)[300:400]
    yV= scipy.signal.medfilt(yV,3)
    xV=numpy.arange(300,400,1)
    xlV=numpy.linspace(300,400,500)
    
    a1V = yV.max()- yV[0]
    a2V = xV[yV.max() == yV][0]
    a3V = 2
    a4V = yV[0]
    
    coeff1V, var_matrix = curve_fit(gauss,xV,yV,p0=[a1V,a2V,a3V,a4V])
    
    yfitV=gauss(xlV,coeff1V[0],coeff1V[1],coeff1V[2],coeff1V[3])
    #plt.plot(xV,yV,"+")
    #plt.plot(xlV,yfitV)
    #plt.show()
    
    return coeff1V[1]

# Function to extract time from our input fit file
                
def getTime(filename) :
    hdulist = pyfits.open(filename)  
    prihdr = hdulist[0].header          
    return prihdr['JD']  

