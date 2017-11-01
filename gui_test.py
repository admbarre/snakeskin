import os
import snakeskin as skin
from tkinter.filedialog import askopenfilenames
from tkinter import *

def add_files():
    new_files = askopenfilenames(initialdir = '/',
            title = 'Select the images you wish to scale.')
    for f in new_files:
        g_files.append(f)
        image_list.insert(END, os.path.basename(f))
    resize.config(state=NORMAL)

def donothing():
    pass

def pipeline():
    images, names = skin.load_images(g_files)
    resized = skin.resize(images)
    success = skin.save(resized,names)
    if success:
        print('Yatta!')

g_files = []
root = Tk()
image_list = Listbox(root)
image_list.config(listvariable=g_files)
image_list.pack()
resize = Button(root,state=DISABLED,text='Resize',command=pipeline)
resize.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Add files', command = add_files)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

root.config(menu=menubar)
root.mainloop()

