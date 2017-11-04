#http://stackoverflow.com/questions/11782147/python-opencv-contour-tree-hierarchy
####
import cv2
import numpy as np

def main(arg1,arg2,arg3):
    # Load the image
    img = cv2.imread(arg1)
    
    # Split out each channel
    blue, green, red = cv2.split(img)
    
    
    def medianCanny(img, thresh1, thresh2):
        median = np.median(img)
        img = cv2.Canny(img, int(thresh1 * median), int(thresh2 * median))
        return img
    
    # Run canny edge detection on each channel
    blue_edges = medianCanny(blue, arg2, arg3)
    green_edges = medianCanny(green, arg2, arg3)
    red_edges = medianCanny(red, arg2, arg3)
    
    # Join edges back into image
    edges = blue_edges | green_edges | red_edges
    
    
    # Find the contours
    _, contours,hierarchy = cv2.findContours(edges, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    hierarchy = hierarchy[0] # get the actual inner list of hierarchy descriptions
    
    # For each contour, find the bounding rectangle and draw it
    for component in zip(contours, hierarchy):
        currentContour = component[0]
        currentHierarchy = component[1]
        x,y,w,h = cv2.boundingRect(currentContour)
        if currentHierarchy[2] < 0:
            # these are the innermost child components
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        elif currentHierarchy[3] < 0:
            # these are the outermost parent components
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

    return len(hierarchy)
    