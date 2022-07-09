from ast import Break
from operator import index
from tkinter import E
from cv2 import circle
import matplotlib.pylab as plt
from skimage.io import imread
from skimage.io import rgb2gray
from skimage.io import filters
import numpy as np
import cv2
import pandas as pd
import math

#Date:2022-07-08 : 9:18pm
#Date:2022-07-09 : 3:00pm 
# I cant post on github cause wifi shit
#Hours spent: 3

im = cv2.imread("image here")
red_px = []
red_py = []
green_py = []
green_px = []
green_coords = {}
red_coords= {}

def image_green(im,green_py,green_px):
    image = cv2.resize(im, (100, 100)) #resized to 100,100 to make it easier to data anaylitics later
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([36,25,25])#lower_green = np.array([50,100,100])
    higher_green = np.array([70,225,225])
    mask_green = cv2.inRange(HSV,lower_green,higher_green) # this has the green version of the image

    green_pixels = np.argwhere(cv2.inRange(mask_green,(lower_green),(higher_green)))
    for px,py in green_pixels:
        green_px.append(px)
        green_py.append(py)

def image_red(im,red_py,red_px):
    image = cv2.resize(im, (100, 100)) #resized to 100,100 to make it easier to data anaylitics later
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,100,20])
    higher_red = np.array([10,225,225])
    mask_red = cv2.inRange(HSV,lower_red,higher_red) # this has the green version of the image

    red_pixels = np.argwhere(cv2.inRange(mask_red,(lower_red),(higher_red)))
    for px,py in red_pixels:
        red_px.append(px)
        red_py.append(py)

def green_sort(green_px, green_py, green_coords):
    green_coords = list(zip([green_px],[green_py]))
    sorted(green_coords, key = lambda p: math.atan2(p[1], p[0])) #atan2(y,x)
    red_coords = red_coords[::-1]
    return green_coords

def red_sort(red_px, red_py, red_coords):
    red_coords = list(zip(red_px, red_py))
    sorted(red_coords, key = lambda p: math.atan2(p[1], p[0])) #atan2(y,x)
    red_coords = red_coords[::-1]
    return red_coords

def green_seperate(green_coords, green_py, green_px):
    green_px = []
    green_py = []

    green_py, green_px = zip(*green_coords)
    return green_py, green_px

def red_seperate(red_coords):
    red_px = []
    red_py = []

    red_py, red_px = zip(*red_coords)
    return red_py, red_px

def data_red(red_px, red_py):
    data = {
        "px_red": red_px,
        "py_red": red_py
    }

    df_red = pd.DataFrame(data)
    return df_red

def data_green(green_px, green_py):
    data = {
        "px_green": green_px,
        "py_green": green_py
    }
    df_green = pd.DataFrame(data)
    return df_green

def green_plot(df_green):
    fig, ax = plt.subplots(figsize = (18,10))
    ax.scatter(df_green['px_green'],df_green["py_green"])
    ax.set_xlabel("X cords")
    ax.set_ylabel("Y cords")
    plt.show()

def red_plot(df_red):    
    fig, ax = plt.subplots(figsize = (18,10))
    ax.scatter(df_red['px_green'],df_red["py_green"])
    ax.set_xlabel("X cords")
    ax.set_ylabel("Y cords")
    plt.show()
    
""" Have yet to determine if needed cause wifi shit
def green_outliers(green_py, green_px):
    diffs = []
    try:
        for num in range(len(green_py)):
            if num+1 < len(green_py):
                diffs.append(abs(green_py[num])-green_py[num+1])
        offender = max(diffs)
        bye = diffs.index(offender+1)
        green_py.remove(green_py[bye])
    except Exception as e:
        pass
    try:
        for num in range(len(green_px)):
            if num+1 < len(green_px):
                diffs.append(abs(green_px[num])-green_px[num+1])
        offender = max(diffs)
        bye = diffs.index(offender+1)
        green_px.remove(green_px[bye])
    except Exception as e:
        pass
def red_outliers(red_py, red_px):
    diffs = []
    try:
        for num in range(len(red_py)):
            if num+1 < len(red_py):
                diffs.append(abs(red_py[num])-red_py[num+1])
        offender = max(diffs)
        bye = diffs.index(offender+1)
        red_py.remove(red_py[bye])
    except Exception as e:
        pass
    try:
        for num in range(len(red_px)):
            if num+1 < len(red_px):
                diffs.append(abs(red_px[num])-red_px[num+1])
        offender = max(diffs)
        bye = diffs.index(offender+1)
        red_px.remove(red_px[bye])
    except Exception as e:
        pass
"""
