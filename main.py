 # -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:06:40 2016
Collected and modified from all over the internet by Erkka Virtanen

Thanks to:
    
CharlesLeifer
http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/

Creators of SalientDetect:
https://github.com/NLeSC/SalientDetector-python

texasflood
http://stackoverflow.com/questions/28498831/opencv-get-centers-of-multiple-objects

Bikramjot Singh Hanzra 
http://hanzratech.in/2015/01/16/color-difference-between-2-colors-using-python.html

    
HOW TO USE:
The script takes one picture-file as the argument and outputs a score of x/99
of how perfect the website is aesthetically, 99 being perfect and 0 being unusable.
The script also outputs the reasons for the score.
Use 1 as the second argument to print the rating and reasoning on to the image.
Otherwise use 0.
    
"""

#IMPORT ALL SCRIPTS
import cv2
import salient_regions
import find_objects
import color_rating
import aescript2
import sharpness

def cutit(s,n):    
   return s[n:]

def printer(img,text,xx,yy,col1,col2,col3,write):
    font = cv2.FONT_HERSHEY_SIMPLEX
    print text
    if write == 1:
        cv2.putText(img,text,(xx,yy), font, 1, (col1,col2,col3), 2, cv2.LINE_AA)

def printer2(img,text,xx,yy,col1,col2,col3,write):
    font = cv2.FONT_HERSHEY_SIMPLEX
    print text
    if write == 1:
        cv2.putText(img,text,(xx,yy), font, 5, (col1,col2,col3), 5, cv2.LINE_AA)

def main(arg1,arg2):    
    #filename
    #arg1 = "Inputs\input19.png"
    path_to_image = arg1
    img = cv2.imread(path_to_image)
    name = cutit(arg1,7)
    #print name
    stars = 0
    #minimum threshold for salient regions
    arg_t = 500
    #nestedness lower threshold
    arg3 = 0.5
    #nestedness upper threshold
    arg4 = 0.8
    #Font used, background
    font = cv2.FONT_HERSHEY_SIMPLEX
    if arg2 == 1:
        cv2.rectangle(img,(0,0),(700,500),(51,0,0),-1)
    
    #Run all scripts
    salient_regions.find_salient(arg1)
    objects = find_objects.num_objects(arg_t)
    color_distance = color_rating.rate(arg1)
    sharp_factor = sharpness.sharpness_factor(arg1)
    nestedness= aescript2.main(arg1,arg3,arg4)
    
    #Give a rating to based on the results of the scripts
    #Number of objects
    points1 = 0
    #print objects
    if 14 <= objects <= 19:
        points1 = 33
        printer(img,"-Perfect amount of items on the page!",10,30,200,255,255,arg2)
    elif 8 <= objects < 14:
        points1 = 30
        printer(img,"-Good amount of items on the page",10,30,200,255,255,arg2)
    elif 4 <= objects < 8:
        points1 = 25
        printer(img,"-Not enough points of interest on page.",10,30,200,255,255,arg2)
    elif objects <= 4:
        points1 = 10
        printer(img,"-Page has too many large connected areas.",10,30,200,255,255,arg2)
    elif 20 <= objects < 26:
        points1 = 30
        printer(img,"-Good amount of items on the page.",10,30,200,255,255,arg2)
    elif 26 <= objects <= 40:
        points1 = 22
        printer(img,"-Slightly too many items on the page.",10,30,200,255,255,arg2)
    elif 40 < objects < 60:
        points1 = 13
        printer(img,"-Too many items on the page.",10,30,200,255,255,arg2)
    elif objects >= 60:
        points1 = 1
        printer(img,"-WAY too many items on the page.",10,30,200,255,255,arg2)
    
    #Color distance
    points2 = 0
    #print color_distance
    if 68 <= color_distance <= 85:
        points2 = 18
        printer(img,"-Colors are chosen perfectly!",10,60,200,255,255,arg2)
    elif 55 <= color_distance < 68:
        points2 = 15
        printer(img,"-Color range is good.",10,60,200,255,255,arg2)
    elif 45 <= color_distance < 68:
        points2 = 10
        printer(img,"-Colors are spread little too far apart.",10,60,200,255,255,arg2)
    elif color_distance < 45:
        points2 = 5
        printer(img,"-Color range is too shallow.",10,60,200,255,255,arg2)
    elif 85 <= color_distance < 95:
        points2 = 15
        printer(img,"-Colors range is good.",10,60,200,255,255,arg2)
    elif 95 < color_distance <= 120:
        points2 = 10
        printer(img,"-Colors are spread little too far apart.",10,60,200,255,255,arg2)
    elif color_distance > 120:
        points2 = 5
        printer(img,"-Color range is too large.",10,60,200,255,255,arg2)
    
    #Sharpness Factor
    points_s = 0
    if 11 <= sharp_factor <= 19:
        points_s = 15
        printer(img,"-Page looks perfectly sharp and in focus!",10,90,200,255,255,arg2)
    elif 6 <= sharp_factor < 11:
        points_s = 10
        printer(img,"-Page looks slightly soft.",10,90,200,255,255,arg2)
    elif sharp_factor < 6:
        points_s = 5
        printer(img,"-Page looks WAY too unfocused.",10,90,200,255,255,arg2)
    elif 19 < sharp_factor < 26:
        points_s = 10
        printer(img,"-Page looks a bit too sharp.",10,90,200,255,255,arg2)
    elif sharp_factor >= 26:
        points_s = 5
        printer(img,"-Page looks WAY too sharp!" ,10,90,200,255,255,arg2)
        
        
    #Nestedness level
    points3 = 0
    #print nestedness
    if 8000 <= nestedness <= 12000:
        points3 = 33
        printer(img,"-Perfect amount of order on the page!\n" ,10,120,200,255,255,arg2)
    elif 6000 <= nestedness < 8000:
        points3 = 30
        printer(img,"-Well structured page.\n" ,10,120,200,255,255,arg2)
    elif 2000 <= nestedness < 6000:
        points3 = 25
        printer(img,"-Page could be a bit more structured.\n" ,10,120,200,255,255,arg2)
    elif nestedness < 2000:
        points3 = 10
        printer(img,"-Page doesn't have enough structure.\n" ,10,120,200,255,255,arg2)
    elif 12000 <= nestedness < 14000:
        points3 = 30
        printer(img,"-Page structure is good.\n" ,10,120,200,255,255,arg2)
    elif 14000 < nestedness <= 20000:
        points3 = 23
        printer(img,"-Page is a little too rigid-looking.\n",10,120,200,255,255,arg2)
    elif nestedness > 20000:
        points3 = 5
        printer(img,"-Page has too much hierarchy.\n",10,120,200,255,255,arg2)
    
    #Calculate final score
    tikst = "*Points for Clutteredness: "+str(points1)+"/ 33"
    printer(img,tikst,10,180,192,192,192,arg2)
    tikst = "*Points for Color Range: "+ str(points2) +"/ 18"
    printer(img,tikst,10,210,192,192,192,arg2)
    tikst =  "*Points for Sharpness: "+ str(points_s) + "/ 15"
    printer(img,tikst,10,240,192,192,192,arg2)
    tikst =  "*Points for Hierarchy: "+ str(points3) +"/ 33 \n"
    printer(img,tikst,10,270,192,192,192,arg2)
    overall = points1+points2+points_s+points3
    tikst = "Overal Score: "+ str(overall)+ " / 99 points"
    printer(img,tikst,10,300,192,192,192,arg2)
    if overall >= 89:
        printer(img,"A Very Good Looking Website! :)",10,430,0,255,0,arg2)
        printer2(img,"*****",10,400,0,255,255,arg2)
        fil = "Outputs\\5-Star\\"
        dest = fil + name
        cv2.imwrite(dest,img)
        stars = 5
    elif 79 <= overall < 89:
        printer(img,"A Good Looking Website!",10,430,128,255,255,arg2)
        printer2(img,"****",10,400,0,255,255,arg2)
        fil = "Outputs\\4-Star\\"
        dest = fil + name
        cv2.imwrite(dest,img)
        stars = 4
    elif 69 <= overall < 79:
        printer(img,"An Average Looking Website!",10,430,255,153,51,arg2)
        printer2(img,"***",10,400,0,255,255,arg2)
        fil = "Outputs\\3-Star\\"
        dest = fil + name
        cv2.imwrite(dest,img)
        stars = 3
    elif 59 <= overall < 69:
        printer(img,"A Below Average Looking Website!",10,430,0,128,255,arg2)
        printer2(img,"**",10,400,0,255,255,arg2)
        fil = "Outputs\\2-Star\\"
        dest = fil + name
        cv2.imwrite(dest,img)
        stars = 2
    elif overall < 59:
        printer(img,"A Poor Looking Website! :(",10,430,0,0,255,arg2)
        printer2(img,"*",10,400,0,255,255,arg2)
        fil = "Outputs\\1-Star\\"
        dest = fil + name
        cv2.imwrite(dest,img)
        stars = 1
    return stars
'''
def runner(nimi):  
    result = ""
    score2 = main(nimi)
    for d in range(0,score2):
        result += "*"
    print "SCORE:", result
'''

'''
    
def ultra_runner(number_of_files):
    #number_of_files = 2
    numba = 0
    beginning = "Inputs\\input"
    end = ".png"
    filu = beginning + str(numba) + end
    for i in range(0,number_of_files):
        numba = numba+1
        filu = beginning + str(numba) + end
        runner(filu)
                         
'''                 
#ultra_runner(13)
#main("Inputs\input1.png",1)
