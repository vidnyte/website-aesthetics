#http://stackoverflow.com/questions/28498831/opencv-get-centers-of-multiple-objects
    
import cv2
import numpy

def num_objects(thresh):
    #thresh = 500;
    img = cv2.imread("output_1.png",0)
    _, contours, _ = cv2.findContours(img.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
    #print len(contours)
    centres = []
    for i in range(len(contours)):
      if cv2.contourArea(contours[i]) < thresh:
        continue
      moments = cv2.moments(contours[i])
      centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
      cv2.circle(img, centres[-1], 3, (0, 0, 0), -1)
    
    #cv2.imshow('image', img)
    #cv2.imwrite('output_2.png',img)
    #print len(centres)
    return len(centres)
    
