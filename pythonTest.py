from __future__ import print_function
from builtins import input
import cv2 as cv
import numpy as np
import argparse


from tkinter import *


parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
args = parser.parse_args()


image = cv.imread(cv.samples.findFile(args.input))
if image is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

new_image = np.zeros(image.shape, image.dtype)


def runOnOK ():
    
    alpha = float(slider1.get())//10
    beta = slider2.get()
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0 , 255)
    cv.imshow('New Image', new_image)
    lookUpTable(new_image)
    
   

def saveIMG():
    cv.imwrite('NewIMG.jpg', new_image)

def lookUpTable(new_image):
    f= open("output.txt","w+")
    identity = np.arange(256, dtype = np.dtype('uint8'))
    zeros = np.zeros(256, np.dtype('uint8'))
    lut = np.dstack((identity, identity, zeros))
    dstImage = cv.LUT(new_image, lut)
    print(dstImage)

root = Tk()
root.title("Modificare IMG")
root.geometry("500x200")

l1 = Label(root, text='Contrast')
l1.pack()
slider1 = Scale(root, from_=10, to=30, orient = HORIZONTAL)
slider1.pack()
l2 = Label(root, text='Brightness')
l2.pack()
slider2 = Scale(root, from_=-255, to=255, orient = HORIZONTAL)
slider2.pack()

Button1 = Button(root, text="OK", bg='gray', fg='green', command=runOnOK)
Button1.pack(side = 'right')

Button2 = Button(root, text="Cancel", bg='gray', fg='red', command=root.destroy)
Button2.pack(side = 'left')

Button3 = Button(root, text="Save Image", bg='gray', fg='purple', command=saveIMG)
Button3.pack(side = 'bottom')

cv.waitKey()
cv.imshow('Original Image', image)
root.mainloop()

