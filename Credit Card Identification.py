from tkinter import *
from PIL import ImageTk, Image
root=Tk()
import random
root.configure(background = "grey")
root.title("Credit Card Identification")
root.geometry("700x600")

img=ImageTk.PhotoImage(Image.open("card.jpg"))
label = Label(root, image=img)

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

def indentification():
  try:
      input_value = int(input_box.get())
      message.box.showinfo("Message", "Credit Card accepted")
      
  except (ValueError):
      message.box.showinfo("Alert", "Credit Card accepted")
     
btn = Button(root, text = "Check Credit Card", command = indentification)
btn.place(relx = 0.5, rely = 0.4 , anchor = CENTER)
label = place(relx = 0.5, rely =0.7, anchor = CENTER)
root.mainloop()

