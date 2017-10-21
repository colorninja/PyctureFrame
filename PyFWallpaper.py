try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk
from PIL import ImageTk, Image


class PyFWallpaper:
  def __init__(self, filename):
    self.filename = filename
    self.image = Image.open(filename)
    self.imageTk = ImageTk.PhotoImage(self.image)

  #Blindly resizes the image
  def __resize__(self, desiredWidth, desiredHeight):
    size = int(desiredWidth), int(desiredHeight)
    self.image = self.image.resize(size,Image.ANTIALIAS)

  #Intelligently crops a photo so it fills the width/height
  def __crop__(self, desiredWidth, desiredHeight):
    #Get the current image sizes
    imageWidth, imageHeight = self.image.size
    imageWidth = float(imageWidth)
    imageHeight = float(imageHeight)
    #Calculate margins to center the image
    sideMargin = (imageWidth - desiredWidth) / 2
    topMargin = (imageHeight - desiredHeight) / 2

    #Center horizontally
    left = sideMargin
    right = imageWidth - sideMargin
    #Center vertically
    top = topMargin
    bottom = imageHeight - topMargin

    #Collect sizes in tuple
    cropSize = (int(left), int(top), int(right), int(bottom))
    self.image = self.image.crop(cropSize)

  def changeDimensions(self, desiredWidth, desiredHeight):
    imageWidth, imageHeight = self.image.size
    widthRatio = float(desiredWidth) / float(imageWidth)
    heightRatio = float(desiredHeight) / float(imageHeight)
    #===DEBUG====
    '''
    print "Desired dimensions: %dx%d" % (desiredWidth, desiredHeight)
    print "Current image dimensions: %dx%d" % (imageWidth, imageHeight)
    print "Width ratio: %.15f" % (widthRatio)
    print "Height ratio: %.15f" % (heightRatio)
    '''
    #============
    if((imageHeight * widthRatio) >= desiredHeight):
      #Resize to width (change height)
      self.__resize__(desiredWidth, imageHeight * widthRatio)
      #print "Resized to %dx%d" % self.image.size
      self.__crop__(desiredWidth, desiredHeight)
      #print "Cropped to: %dx%d" % self.image.size
    elif((imageWidth * heightRatio) >= desiredWidth):
      #Resize to height (change width)
      self.__resize__(imageWidth * heightRatio, desiredHeight)
      #print "Resized to: %dx%d" % self.image.size
      self.__crop__(desiredWidth, desiredHeight)
      #print "Cropped to %dx%d" % self.image.size
