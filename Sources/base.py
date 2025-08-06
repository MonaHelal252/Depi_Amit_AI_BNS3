"""  
 
 
 
 
"""
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
 
 
 
class DEPI_AI_TOOL:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("House Price Prediction")
        self.root.configure(bg="Light Yellow")
 
 
        # Title Label
        title = Label(self.root, text="DEPI_ Data science mona", compound=CENTER,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
 
        image_frame = LabelFrame(self.root, text="Some pictures of houses", font=("times new roman", 16, "bold"), bg="Yellow", fg="black")
        image_frame.place(x=875, y=120, width=400, height=550)
 
 
 
       
 
if __name__ == "__main__":
    root = Tk()
    obj = DEPI_AI_TOOL(root)
    root.mainloop()
 
 