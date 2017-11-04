import numpy as np
import cv2
import sys
import os
import scipy.io as sio
import salientregions as sr
#import matplotlib as mpl
from PIL import Image
sys.path.insert(0, os.path.abspath('..'))
    
def find_salient(arg1):
    #Load the image
    path_to_image = arg1
    img = cv2.imread(path_to_image)
    sr.show_image(img)
    
    #Convert to grey scale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #sr.show_image(grayscale)
    #equ = cv2.equalizeHist(grayscale)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(grayscale)
    
    img = cl1
    #cv2.imwrite('clahe_2.jpg',cl1)
    sr.show_image(img)
    lam_factor = 3
    area_factor_large = 0.001
    area_factor_verylarge = 0.1
    area_factor = 0.01
    lam = 50
    connectivity = 4
    weights=(0.33,0.33,0.33)
    
    binarizer = sr.DatadrivenBinarizer(area_factor_large=area_factor_large, area_factor_verylarge=area_factor_verylarge, 
                                               lam=lam, weights=weights, connectivity=connectivity)
    binarized = binarizer.binarize(img)
    
    
    detector = sr.BinaryDetector(binarized, lam, area_factor, connectivity)
    
    regions = detector.detect(binarized,True,True,False,False,False)
    
    sr.show_image(detector.get_holes())
    
    im = Image.fromarray(detector.get_holes())
    #mpl.image.imsave('out_put_salient2', im)
    #Show the holes
    #print(sr.show_image(detector.get_holes()))
    
    im.save("output_1.png","PNG")
    return
    
#find_salient("Inputs\input3.png")
