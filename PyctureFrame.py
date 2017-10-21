try:
  #For Python3
  import tkinter as tk
  from configparses import ConfigParser
except ImportError:
  #For Python2
  import Tkinter as tk
  from ConfigParser import ConfigParser

from PIL import ImageTk, Image
from PyFWallpaper import PyFWallpaper
from PyFImageFiles import PyFImageFiles
import threading

#Read from the settings ini
config = ConfigParser()
config.read("PyctureSettings.ini")
#Set our timer time from settings
showTime = config.getint("DEFAULT", "change_time") #time for image to stay before changed in sec

#Init needed stuff
root = tk.Tk()
fileManager = PyFImageFiles()
#Get screen dimensions
displayWidth = root.winfo_screenwidth()
displayHeight = root.winfo_screenheight()
#Setup tkinter environment
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (displayWidth, displayHeight))
root.config(cursor="none")
#Escape key bind
root.focus_set()

#Get random image and resize it to screen dimensions, then add it to a tkinter label
img = PyFWallpaper(fileManager.getRandomImage())
img.changeDimensions(displayWidth, displayHeight)
imageObject = ImageTk.PhotoImage(img.image)
imageLabel = tk.Label(root, image = imageObject)
imageLabel.pack(side = "bottom", fill = "both", expand = "yes")



#Prepare timer for auto image change
def startChangeImageTimer():
  global changeImageTimer
  changeImageTimer = threading.Timer(showTime, changeImageWithTimer)
  changeImageTimer.start()

#changes the label to a new random image
def changeImage():
  global changeImageTimer, imageLabel, showTime
  img = PyFWallpaper(fileManager.getRandomImage())
  img.changeDimensions(displayWidth, displayHeight)
  imageObject = ImageTk.PhotoImage(img.image)
  imageLabel.configure(image=imageObject)
  imageLabel.image = imageObject

#Timer helper
def changeImageWithTimer():
  changeImage()
  startChangeImageTimer()
startChangeImageTimer()

#Terminates the script
def closeWindow():
  global root, fileManager, changeImageTimer
  changeImageTimer.cancel()
  fileManager.destroy()
  root.quit()

########
#Events#
########

#Left-click event
def leftClick(event):
  closeWindow()
root.bind("<Button-1>", leftClick)
#Middle-click event
def middleClick(event):
  changeImageTimer.cancel()
  changeImageWithTimer()
root.bind("<Button-2>", middleClick)
#Right-click event
def rightClick(event):
  changeImageTimer.cancel()
  changeImage()
root.bind("<Button-3>", rightClick)
root.mainloop()
