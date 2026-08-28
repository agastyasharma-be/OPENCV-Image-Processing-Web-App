import cv2
path="Resources/dog.png"
def read_img(path):
    img=cv2.imread(path)
    return img  
def crop_img(img,height,width):
    imgcropped=img[0:height,0:width]
    return imgcropped
def resize_img(img,width,height):
    width,height=1000,1000
    imgresize=cv2.resize(img,(width,height))
    return imgresize
def grayscale_img(img):
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return imggray
def blur_img(img):
    imgblur=cv2.GaussianBlur(img,(17,17),0)
    return imgblur
def edge_img(img):
    imgcanny=cv2.Canny(img,150,150)
    return imgcanny
