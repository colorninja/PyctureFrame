try:
  #For Python3
  from configparser import ConfigParser
except ImportError:
  #For Python2
  from ConfigParser import ConfigParser

import glob, os
from random import randint
import threading

class PyFImageFiles:

  def refreshFiles(self):
    formats = ["jpg", "jpeg", "png", "gif", "bmp", "eps", "tiff"]
    refreshRate = 60.0 * 10.0
    #print("Refreshing files")
    for format in formats:
      self.images.extend(glob.glob("*." + format))
    self.refreshTimer = threading.Timer(refreshRate, self.refreshFiles)
    self.refreshTimer.start()


  def destroy(self):
    self.refreshTimer.cancel()

  def __init__(self):
    #Read from the settings ini
    config = ConfigParser()
    config.read("PyctureSettings.ini")
    #Set our image path from settings
    images_path = config.get("DEFAULT", "images_path")
    os.chdir(images_path)
    self.images = []
    self.refreshFiles()

  def getRandomImage(self):
    return self.images[randint(0, len(self.images) - 1)]
