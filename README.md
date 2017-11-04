# Website Aesthethics
This python script evaluates websites based on their aesthetics.
The script measures four different metrics of an image and scores them based on each metric’s own qualities. The metrics are the number of items on the display or clutteredness e.g how many salient objects there are on a web page, the color range of the three main colors on the page and their distance to each other in CIE lab color space, how sharp or how in focus the image is and lastly how nested or how much hierarchy there is inthe UI. Clutteredness and nestedness metrics are scored between 1-33 points where the perfect score is 33 for the perfect aesthetic result. Color range is scored between 5-18 points and image sharpness in 5-15 points range. In the end, all metric scores are added together to give the image an overall rating with max points of 99.

More indepth explanation of the scripts inner workings can be found in the pdf-file.

## HOW TO USE THE SCRIPT
**********************
Make sure all the scripts are located in the same folder where you are running the mainscript from.
There should be a folder named "Inputs" which holds the 13 images used as examples in the document.
There should also be a "Outputs"-folder which holds the 5 different folders where the rated image will 
be saved according to its rating.

The script takes two arguments.
The first argument is the name of the image-file you want to get the rating of(e.g "Inputs\input1.png").
The second argument is whether you want the resulting rating and reasons to be printed on to the image.
Use 1 to get the results printed and use 0 to not print them.
The image's size should be about 1366x768 pixels or similar and the file type .png or .jpg.

You can run the script in Windows 10 by using the command line by writing:
C:\Python27\python.exe C:\Users\Erkka\Desktop\The_Aesthethic_UI_script\main.py Inputs\input1.png 1

This can prove to be quite a hassle if the dependant packages are located elsewhere.
The easiest way to run them in Windows in that case is to just put all the script files in 
the C:\Python27\ folder and run the script from there.

If the script was run properly it should generate an image of Lings Cars in the Outputs\1-Star\ with the
rating and reasoning pasted on to the image. 

Alternatively and WHAT I RECOMMEND is that you open the "main.py" in an IDE like Spyder(https://pythonhosted.org/spyder/),
uncomment the last line #main("Inputs\input1.png",0) and run the file by pressing F5. 
This is what I SERIOUSLY recommend to save great amounts of time and suffering. 
If now the IDE says that a module is not found, read the DEPENDANCIES part to download the missing package.
It can take even up to 15 seconds to run the whole script on one image.


## DEPENDANCIES
*************
To run the script, several dependant packages need to be installed on the system. 
Make sure that you are using correct versions of the packages. 
You need exactly Python version 2.7 and Open Computer Vision library version 3.1.

You also need the following Python packages installed:
numpy
scipy
colormath
salientregions
matplotlib
PIL
sys
os

To install the packages, you can run the Python installer pip.
Write 'pip install <package needed>' in the terminal to download and install the appropriate package.
eg. 'pip install matplotlib'.
Here is a paste for installing all the packages:

pip install numpy
pip install scipy
pip install colormath
pip install salientregions
pip install matplotlib
pip install PIL
pip install sys
pip install os

If Open Computer Vision library 3.1 (opencv) is not installed:
pip install opencv-python


## Thanks

Thanks to:
    
CharlesLeifer
http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/

Creators of SalientDetect:
https://github.com/NLeSC/SalientDetector-python

texasflood
http://stackoverflow.com/questions/28498831/opencv-get-centers-of-multiple-objects

Bikramjot Singh Hanzra 
http://hanzratech.in/2015/01/16/color-difference-between-2-colors-using-python.html