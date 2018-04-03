import numpy as np
import cv2
from scipy import fftpack

img4 = cv2.imread("Last4.jpg")
img1 = cv2.imread("Last1.jpg")
img2 = cv2.imread("Last2.jpg")
img3 = cv2.imread("Last3.jpg")
img5 = cv2.imread("Valspar.jpg")
h,w = np.shape(img4)[0], np.shape(img4)[1] #All images are same height and width

#Resize Images
c = 1000 # I had to vary this for the stitching program
resize1 = cv2.resize(img1, (c,c))
resize2 = cv2.resize(img2, (c,c))
resize3 = cv2.resize(img3, (c,c))
resize4 = cv2.resize(img4, (c,c))
resize5 = cv2.resize(img5, (c,c))

#Available Structuring Elements
def circle_n(radius):
    img = np.zeros((2*radius+1, 2*radius+1), dtype=np.uint8)
    cv2.circle(img, (radius, radius), radius, 1, -1)
    return img
kernel9 = np.ones((9,9), dtype=np.float64)/81 #square structuring element
kernel7 = np.ones((7, 7), dtype=np.float64) / 49 #square structuring element
kernel5 = np.ones((5,5), dtype=np.float64)/25 #square structuring element
kernel3 = np.ones((3, 3), dtype=np.float64) / 9
#---------------------------------Crop Steps------------------------------------------------------------------#
#1.) Erode by a structing element to make the background darker
#2.) Turn the image into grayscale and binary
#3.) find the edges by Canny Edge detection
#4.) Use np.argmax, np.where to find the pixel values of the edges
#5.) Crop and save image
#--------------------------------Crop of Candle 1--------------------------------------------------------
erode1 = cv2.erode(resize1, kernel5)
erode1[erode1 >= 150] = 255
erode1[erode1 < 150] = 0
gray1 = cv2.cvtColor(erode1, cv2.COLOR_BGR2GRAY)
ret1, thresh1 = cv2.threshold(gray1,0,200,cv2.THRESH_BINARY)
edges1 = cv2.Canny(thresh1,100,200)
crop_w_left1 = np.where(np.argmax(edges1, axis = 0))[0][0]
crop_h_left1 = np.where(np.argmax(edges1, axis = 1))[0][0]
crop_w_right1 = np.where(np.argmax(edges1, axis = 0))[-1][-1]
crop_h_right1 = np.where(np.argmax(edges1, axis = 1))[-1][-1]
crop1 = resize1[crop_h_left1:crop_h_right1, crop_w_left1:crop_w_right1]
#---------------------------------Crop of Image 2----------------------------------------------------------
erode2 = cv2.erode(resize2, kernel7)
erode2[erode2 >= 150] = 255
erode2[erode2 < 150] = 0
gray2 = cv2.cvtColor(erode2, cv2.COLOR_BGR2GRAY)
ret2, thresh2 = cv2.threshold(gray2,0,255,cv2.THRESH_BINARY)
edges2 = cv2.Canny(thresh2,100,200)
crop_w_left2 = np.where(np.argmax(edges2, axis = 0))[0][0]
crop_h_left2 = np.where(np.argmax(edges2, axis = 1))[0][0]
crop_w_right2 = np.where(np.argmax(edges2, axis = 0))[-1][-1]
crop_h_right2 = np.where(np.argmax(edges2, axis = 1))[-1][-1]
crop2 = resize2[crop_h_left2:crop_h_right2, crop_w_left2:crop_w_right2]
#-------------------------Crop of Candle 3---------------------------------------
erode3 = cv2.erode(resize3, kernel3)
erode3[erode3 >= 150] = 255
erode3[erode3 < 150] = 0
gray3 = cv2.cvtColor(erode3, cv2.COLOR_BGR2GRAY)
ret3, thresh3 = cv2.threshold(gray3,0,200,cv2.THRESH_BINARY)
edges3 = cv2.Canny(thresh3,100,200)
crop_w_left3 = np.where(np.argmax(edges3, axis = 0))[0][0]
crop_h_left3 = np.where(np.argmax(edges3, axis = 1))[0][0]
crop_w_right3 = np.where(np.argmax(edges3, axis = 0))[-1][-1]
crop_h_right3 = np.where(np.argmax(edges3, axis = 1))[-1][-1]
crop3 = resize3[crop_h_left3:crop_h_right3, crop_w_left3:crop_w_right3]
#--------------------------------Crop of Candle 4--------------------------------
erode4 = cv2.erode(resize4, kernel3)
erode4[erode4 >= 100] = 255
erode4[erode4 < 100] = 0
gray4 = cv2.cvtColor(erode4, cv2.COLOR_BGR2GRAY)
ret4, thresh4 = cv2.threshold(gray4,0,200,cv2.THRESH_BINARY)
edges4 = cv2.Canny(thresh4,100,200)
crop_w_left4 = np.where(np.argmax(edges4, axis = 0))[0][0]
crop_h_left4 = np.where(np.argmax(edges4, axis = 1))[0][0]
crop_w_right4 = np.where(np.argmax(edges4, axis = 0))[-1][-1]
crop_h_right4 = np.where(np.argmax(edges4, axis = 1))[-1][-1]
crop4 = resize4[crop_h_left4:crop_h_right4, crop_w_left4:crop_w_right4]

#----------Crop of Valspar----------------------#
erode5 = cv2.erode(resize5, kernel3)
erode5[erode5 >= 170] = 255
erode5[erode5 < 170] = 0
gray5 = cv2.cvtColor(erode5, cv2.COLOR_BGR2GRAY)
ret5, thresh5 = cv2.threshold(gray5,100,170,cv2.THRESH_BINARY)
edges5 = cv2.Canny(thresh5,100,200)
crop_w_left5 = np.where(np.argmax(edges5, axis = 0))[0][0]
crop_h_left5 = np.where(np.argmax(edges5, axis = 1))[0][0]
crop_w_right5 = np.where(np.argmax(edges5, axis = 0))[-1][-1]
crop_h_right5 = np.where(np.argmax(edges5, axis = 1))[-1][-1]
crop5 = resize5[crop_h_left5:crop_h_right5, crop_w_left5:crop_w_right5]


#Save Images
cv2.imwrite("Crop1.jpg", crop1)
cv2.imwrite("Crop2.jpg", crop2)
cv2.imwrite("Crop3.jpg", crop3)
cv2.imwrite("Crop4.jpg", crop4)
cv2.imwrite("Crop5.jpg", crop5)

cv2.imshow("Grayscale", np.uint8(crop5))
cv2.waitKey(0)
cv2.destroyAllWindows()
