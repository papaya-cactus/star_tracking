import numpy as np
import numpy
import matplotlib.pyplot as plt
from pylab import *
from scipy.optimize import curve_fit
from scipy.stats import norm
          
def plot_coordinates(filename):
    dataMatrix1 = np.genfromtxt(filename)

    x1 = dataMatrix1[:,0]
    x2 = dataMatrix1[:,1]
    y1 = dataMatrix1[:,2]
    y2 = dataMatrix1[:,3]
    t = dataMatrix1[:,4]
    
    
    plt.subplot(2,1,1)
    plt.plot(t,x1 - dataMatrix1[:,0][0],label = 'Star 1',linewidth = 0.8, color = 'r')
    plt.plot(t,x2- dataMatrix1[:,1][0], label = 'Star 2',linewidth = 0.8, color = 'b')
    plt.ylabel(' x-position / pixels')
    plt.title("x-position vs time for wide field camera")
    plt.legend()
    
    plt.subplot(2,1,2)
    plt.plot(t,1*(y1 - dataMatrix1[:,2][0]),label = 'Star 1',linewidth = 0.8, color = 'r')
    plt.plot(t,y2- dataMatrix1[:,3][0], label = 'Star 2', linewidth = 0.8, color = 'b')
    plt.xlabel("Time (Julian Date) / days")
    plt.ylabel(' y-position / pixels')
    plt.title("y-position vs time for wide field camera")
    plt.legend()
    font = {'size' :20}
    matplotlib.rc('font', **font)
    
    plt.show()
    
def plot_histogram(filename):
    
    dataMatrix1 = np.genfromtxt(filename)
    x1 = (dataMatrix1[:,0] - dataMatrix1[:,0][0])
    x2 = (dataMatrix1[:,1] - dataMatrix1[:,1][0])
    y1 = dataMatrix1[:,2] - dataMatrix1[:,2][0]
    y2 = dataMatrix1[:,3] - dataMatrix1[:,3][0]
    
    figure(2)
    arr1 = x1-x2
    (mu, sigma) = norm.fit(arr1)
    plt.subplot(2,1,1)
    plt.hist(arr1, 50,normed=True)

    mu, std = norm.fit(arr1)
    FWHM = 2*std*math.sqrt((2*np.log(2)))        
    x = np.linspace(-0.18, 0.18, 500)
    p = norm.pdf(x, mu, std)
    plt.subplot(2,1,1)
    plt.plot(x, p, 'r--', linewidth=2)
    
    plt.suptitle(r' Plot of Normalized Frequency vs $x_1 - x_2$ and $y_1 - y_2$ (Wide Field Camera)')
    plt.text(0.11, 12,  "FWHM = 0.0985" "\n" r"$\mu$ = -0.0168" "\n" r"$\sigma$ = 0.0418",fontsize = 16,
        bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})
    plt.xlabel(r'$x_1 - x_2$ / pixels' )
    plt.ylabel("Normalized Frequency")
    plt.xlim(-0.17,0.18)
    font = {'size' :20}
    matplotlib.rc('font', **font)
    
    plt.show()
    

    arr2 = y1-y2
    (mu, sigma) = norm.fit(arr2)
    plt.subplot(2,1,2)
    plt.hist(arr2, 50,normed=True)

    mu, std = norm.fit(arr2)
    FWHM = 2*std*math.sqrt((2*np.log(2)))
   
    x = np.linspace(-0.8, 0.8, 500)
    p = norm.pdf(x, mu, std)
    plt.subplot(2,1,2)
    plt.plot(x, p, 'r--', linewidth=2)
    plt.xlim(-0.8,0.5)
    plt.xlabel(r'$y_1 - y_2$ / pixels')
    plt.ylabel("Normalized Frequency")
  
    plt.text(0.24, 4,  "FWHM = 0.3711" "\n" r"$\mu$ = -0.2426" "\n" r"$\sigma$ = 0.1576",fontsize = 16,
        bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    font = {'size' : 20}
    matplotlib.rc('font', **font)
    
    plt.show()
    

