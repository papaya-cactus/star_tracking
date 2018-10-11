"""
#### Star Tracking Algorithm for telescope guiding system ####

This algorithm allows one to track the movement of multiple stars across the sky. The difference in tracking can be used to evaluate how well 
a camera is performing at tracking. Further applications may include using such an algorithm on multiple cameras, eg: a wide field one and a narrow field one. 
The difference between both ccds can be obtained and be utilzied as a framework for guiding the telescope.  

This .py file contains the main functions to track star movement and plot the results. Helper functions are located in the files get_coordinates.py 
and plot_results.py 

"""


import numpy
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import scipy.signal
import os,sys
from get_coordinates import stardistancex, stardistancey, getTime
from plot_results import plot_coordinates, plot_histogram

# First function takes the directory which contains the fit files as input
# Outputs a txt file containing x,y (coordinates) and t 
# You will need to provide a guess on where the star is to increase efficiency. These are input as minx, maxx, miny maxy
# The function then searches for the star within this range

def track_movement(file_location,minx,maxx,miny,maxy,output_name):
    os.chdir(file_location)
    X1Array = []
    Y1Array = []
    Time = []

    for i in range (0,len(os.listdir(file_location))): 
        filename = os.listdir(file_location)[i]
    
        if filename.find(".fit") != -1:
            X1Array.append(stardistancex(filename,minx,maxx))
            Y1Array.append(stardistancey(filename,miny,maxy))
            Time.append(getTime(filename));
            
    numpy.savetxt(output_name, numpy.c_[X1Array,Y1Array,Time])     

# To plot the movement of stars, we input the txt file containing coordinates of stars.
# In this example we have info for two stars, so the txt file has the form x1,x2,y1,y2 t whereby 1 and 2 refer to the different stars

# We also plot a histogram showing the tracking error between two stars

def plot_movement(input_coordinates):
    plot_coordinates(input_coordinates)
    plot_histogram(input_coordinates)
  