import cv

filename = "adi.jpg"

im = cv.LoadImageM("./ad_images/"+filename, 
                    cv.CV_LOAD_IMAGE_GRAYSCALE)
dest = cv.CreateMat(im.height, im.width, cv.CV_16S)
cv.Sobel(im, dest, 1, 1)
#cv.Canny(im, dest, 2.2, 1.5, aperture_size = 3)
cv.SaveImage("./ad_images/edge-"+filename, dest)


