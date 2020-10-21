#import image_to_scan
from tkinter import *
from tkinter import ttk
import imutils
import cv2
from tkinter import filedialog
def scan(path):
    image-to-scan + path

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename) 

window = Tk()
window.title('File Explorer') 
   
# Set window size 
window.geometry("500x500") 
   
#Set window background color 
window.config(background = "white") 
label_file_explorer = Label(window,  
                            text = "File Explorer using Tkinter", 
                            width = 100, height = 4,  
                            fg = "blue") 
   
       
button_explore = Button(window,  
                        text = "Browse Files", 
                        command = browseFiles)  
   
button_exit = Button(window,  
                     text = "Exit", 
                     command = exit)  
   
# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns 
label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.grid(column = 1, row = 2) 
button_exit.grid(column = 1,row = 3) 
   
# Let the window wait for any events 
window.mainloop() 