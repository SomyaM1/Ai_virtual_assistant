from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import action
import speech_to_text
root = tk.Tk()
root.title("AI Assistant")
root.geometry("500x675")
root.resizable(False, False) #by using this we aren't able to resize the window.
root.config(bg="#6F8FAF")

#ask fun:
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'USER--->' + user_val+"\n")
    if bot_val != None:
        text.insert(END, 'BOT<---' + str(bot_val)+"\n" )
    if bot_val == "Okay":
        root.destroy()

#send fun:
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'USER--->' + send+"\n")
    if bot != None:
        text.insert(END, 'BOT<---' + str(bot)+"\n" )
    if bot == "Okay":
        root.destroy()

#delete sun:
def del_text():
    text.delete("1.0", "end")

#Frame:
frame=LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.grid(row=0, column=1, padx=55, pady=10)

#Text Label:
text_label = Label(frame, text="AI Assistant", font=("comic Sans ms", 14, "bold"), width=10, height=1)
frame.config(bg="#6F8FAF")  #remove later.
text_label.grid(row=0, column=1, padx=10, pady=10)

#Image:
image_path = r"c:\Users\b\Desktop\AI Assistant\AI Assistant.png"  # Correct path
image = Image.open(image_path)

# Resize the image
resized_image = image.resize((200, 200))  # Resize to 200x200 pixels

# Convert the resized image to PhotoImage
photo = ImageTk.PhotoImage(resized_image)
image_label=Label(frame, image=photo)

# Create a Label widget with the image
image_label = tk.Label(root, image=photo)
image_label.grid(row=2, column=1, padx=10, pady=10)

# Keep a reference to the image to avoid garbage collection
image_label.image = photo

#Adding a text widget:
text=Text(root, font=('courier 10 bold'), bg="#356696")
text.grid(row=2, column=1)
text.place(x=50, y=345, width=375, height=100)

#Entry widget:
entry=Entry(root, justify=CENTER)
entry.place(x=65, y=475, width=345, height=30)

#Buttons:
Button1=Button(root, text="ASK", bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=40, y=545)
Button2=Button(root, text="SEND", bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=345, y=545)
Button3= Button(root, text="DELETE", bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=185, y=545)








root.mainloop()
