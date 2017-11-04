# -*- coding: utf-8 -*-
"""
Color1
#CharlesLeifer.com
#Bikramjot Singh Hanzra 
#http://hanzratech.in/2015/01/16/color-difference-between-2-colors-using-python.html
"""

from matplotlib.colors import hex2color, rgb2hex
from colormath.color_objects import sRGBColor, LabColor 
from colormath.color_conversions import convert_color 
from colormath.color_diff import delta_e_cie2000 

from collections import namedtuple
from math import sqrt
import random
try:
    import Image
except ImportError:
    from PIL import Image
    
def rate(arg1):
    Point = namedtuple('Point', ('coords', 'n', 'ct'))
    Cluster = namedtuple('Cluster', ('points', 'center', 'n'))
    
    def get_points(img):
        points = []
        w, h = img.size
        for count, color in img.getcolors(w * h):
            points.append(Point(color, 3, count))
        return points
    
    rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))
    
    def colorz(filename, n=3):
        img = Image.open(filename)
        img.thumbnail((200, 200))
        w, h = img.size
    
        points = get_points(img)
        clusters = kmeans(points, n, 1)
        rgbs = [map(int, c.center.coords) for c in clusters]
        return map(rtoh, rgbs)
    
    def euclidean(p1, p2):
        return sqrt(sum([
            (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
        ]))
    
    def calculate_center(points, n):
        vals = [0.0 for i in range(n)]
        plen = 0
        for p in points:
            plen += p.ct
            for i in range(n):
                vals[i] += (p.coords[i] * p.ct)
        return Point([(v / plen) for v in vals], n, 1)
    
    def kmeans(points, k, min_diff):
        clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]
    
        while 1:
            plists = [[] for i in range(k)]
    
            for p in points:
                smallest_distance = float('Inf')
                for i in range(k):
                    distance = euclidean(p, clusters[i].center)
                    if distance < smallest_distance:
                        smallest_distance = distance
                        idx = i
                plists[idx].append(p)
    
            diff = 0
            for i in range(k):
                old = clusters[i]
                center = calculate_center(plists[i], old.n)
                new = Cluster(plists[i], center, old.n)
                clusters[i] = new
                diff = max(diff, euclidean(old.center, new.center))
    
            if diff < min_diff:
                break
    
        return clusters
        
    
    print colorz(arg1)
    colors0 = colorz(arg1)
    color1 =  colors0[2]
    color2 =  colors0[1]
    color3 = colors0[0]
    
    
    #############################
    def color_difference(coll1,coll2):
        # First color
        col1 = hex2color(coll1);
        color1_rgb = sRGBColor(col1[0],col1[1],col1[2]);
        # Second color
        col2 = hex2color(coll2);
        color2_rgb = sRGBColor(col2[0],col2[1],col2[2]);
        # Convert from RGB to Lab Color Space 
        color1_lab = convert_color(color1_rgb, LabColor); 
        # Convert from RGB to Lab Color Space 
        color2_lab = convert_color(color2_rgb, LabColor); 
         # Find the color difference 
        delta_e = delta_e_cie2000(color1_lab, color2_lab); 
        #print "The difference between the 2 color = ", delta_e
        return delta_e
    
    
    rat1 = color_difference(color1,color2)    
    rat2 = color_difference(color2,color3)  
    #print "Colors added together", rat1+rat2  
    #print "Color Ratio:", rat1/rat2
    return rat1+rat2



