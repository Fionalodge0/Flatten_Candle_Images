import numpy as np
import cv2
from timeit import default_timer as timer
from scipy import fftpack

img1 = np.float64(cv2.imread("Crop1.jpg")) #Candle rot1
img2 = np.float64(cv2.imread("Crop2.jpg")) #candle rot2
img3 = np.float64(cv2.imread("Crop3.jpg")) #candle rot3
img4 = np.float64(cv2.imread("Crop4.jpg")) #candle rot4

img5 = np.float64(cv2.imread("Crop5.jpg")) #valspar label

def flatten_by_min_floor(image):
    #Dimensions needed
    height, width = np.shape(image)[:2]
    radius = width/2.0
    #Initiate new_width and its linspace
    new_width = int(np.floor(np.pi*radius))
    new_width_linspace = np.linspace(0, new_width, new_width, dtype = np.int32)
    #Make a linspace for points along the arclength
    arc_points = np.int32(radius-radius*np.cos(new_width_linspace/radius))
    #Make an array full of width-2
    A = np.empty(new_width)
    A.fill(width-2)
    #Determine floor of arc length and width-2
    arc_points_floor = np.int32(np.minimum(arc_points, A))
    diff = arc_points_floor-arc_points
    #Initialize Empty
    empty = np.zeros((height, new_width, 3), dtype = np.float64)
    #Distribute Intensities
    for i in range(np.size(new_width_linspace)):
        k = arc_points_floor[i]
        empty[:,i,:] = image[:,k,:] + (image[:, k+1,:] - image[:, k,:])*diff[i]
    #Normalize
    empty[empty <= 0] = 0
    empty[empty >= 255] = 255
    return empty

def flatten_by_min_floor_gray(image):
    #Dimensions needed
    height, width = np.shape(image)[:2]
    radius = width/2.0
    #Initiate new_width and its linspace
    new_width = int(np.floor(np.pi*radius))
    new_width_linspace = np.linspace(0, new_width, new_width, dtype = np.int32)
    #Make a linspace for points along the arclength
    arc_points = np.int32(radius-radius*np.cos(new_width_linspace/radius))
    #Make an array full of width-2
    A = np.empty(new_width)
    A.fill(width-2)
    #Determine floor of arc length and width-2
    arc_points_floor = np.int32(np.minimum(arc_points, A))
    diff = arc_points_floor-arc_points
    #Initialize Empty
    empty = np.zeros((height, new_width), dtype = np.float64)
    #Distribute Intensities
    for i in range(np.size(new_width_linspace)):
        k = arc_points_floor[i]
        empty[:,i] = 1.0*image[:,k] + 1.0*(image[:, k+1] - image[:, k])*diff[i]
    #Normalize
    empty[empty <= 0] = 0
    empty[empty >= 255] = 255
    return empty


#New flats color and grayscale
flat1 = flatten_by_min_floor(img1)
flat2 = flatten_by_min_floor(img2)
flat3 = flatten_by_min_floor(img3)
flat4 = flatten_by_min_floor(img4)

flat5 = flatten_by_min_floor(img5)


#Had to resize images for stitching programs to be same w,h (I cropped them otherwise there was too much black)
flat1_RE = flat1[4:404, 3:500, :]
flat2_RE = flat2
flat3_RE = flat3[2:402, 3:500, :]
flat4_RE = flat4[7:407, 6:503, :]

#cv2.imwrite("flat1Resize.png", flat1_RE)
#cv2.imwrite("flat2Resize.png", flat2_RE)
#cv2.imwrite("flat3Resize.png", flat3_RE)
#cv2.imwrite("flat4Resize.png", flat4_RE)

cv2.imwrite("flat5.jpg", flat5)
cv2.imshow("huh", np.uint8(flatten_by_min_floor(img5)))
cv2.waitKey(0)
cv2.destroyAllWindows()
