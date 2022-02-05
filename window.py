from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog




window = Tk()
window.title("X-ray Analyzer")
window.geometry("1000x700")
window.configure(bg = "#ffffff")

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    686.5, 201.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
def btn_clicked():
    global my_img
    #for path -------------
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    my_label =  Label(window, text=window.filename).place(x=500,y=0)
    #------------------
    my_image =  Image.open(window.filename)
    img = my_image.resize((250,250))
    my_img= ImageTk.PhotoImage(img)
    
    my_image_label = Label(window,image=my_img)
    #image placement
    my_image_label.place(x=500,y=40)
    
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 125, y = 493,
    width = 171,
    height = 55)

window.resizable(False, False)
window.mainloop()
