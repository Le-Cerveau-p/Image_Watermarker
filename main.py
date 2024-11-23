import sys
from tkinter import *
from tkinter import colorchooser, ttk, font, filedialog
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os
from matplotlib import font_manager
from random import randint


# pick_img_frame = None
canvas = None
img_picked_frame = None
title = None
img = None
size = None
result = None
card = None
img_file = None
#function to load fonts

font_picked = ''




# Image Processing
class Image_Dec():
    def __init__(self, url):
        self.url = url
        self.img = Image.open(url)
        self.length = self.img.size[0]
        self.breadth = self.img.size[1]
        print(self.img.format, self.img.size, self.img.mode)

    def write_text(self, text, x_pos, y_pos, text_color, font_size, font_family):
        font_ = font_manager.FontProperties(family=font_family, style='italic')
        file = font_manager.findfont(font_)
        # font = ImageFont.truetype(f"C:/Windows/Fonts/{font_family}.ttf", font_size)
        font_ = ImageFont.truetype(file, font_size)
        d = ImageDraw.Draw(self.img)
        d.text(position(x_pos, y_pos, self.length, self.breadth), text, fill=text_color, anchor="la", font=font_)

    def show(self):
        self.img.show()

    def save(self):
        self.img.save(f"{self.url}{randint(100000,9999999)}.jpg")


def write_image(text, font, color, position):
    im1 = Image_Dec(img_file)
    im1.write_text(
        text=text,
        x_pos=position[0],
        y_pos=position[1],
        text_color=color,
        font_size=(20*im1.img.size[0]/500),
        font_family=font
    )
    im1.show()
    im1.save()






# Function to pick font
def font_pick():
    def on_mousewheel(event):
        my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def getText(event):
        global font_picked
        f = event.widget
        font_picked = f.cget("text")
        outer_frame.destroy()
        canvas.itemconfig(title, text=result['text'], font=(font_picked, 20, "italic"), fill=result['color'])

    outer_frame = Toplevel(root)
    outer_frame.title("Pick your font")
    my_canvas = Canvas(outer_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = Scrollbar(outer_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    btn1 = Button(outer_frame,
                  text="Browse...",
                  compound="left",
                  fg="blue", width=22,
                  font=("bold", 10),
                  height=1,
                  )

    btn1.place(x=300, y=300)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind(
        '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    )
    my_canvas.bind_all("<MouseWheel>", on_mousewheel)

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    font_families = font.families()
    for item in font_families:
        font_name = Label(second_frame, text=item, font=(item, 20, "italic"))
        font_name.grid(column=0, row=font_families.index(item))
        font_name.bind("<Button-1>", getText)

    # return font_picked


#function for watermark customization
def water_mark_entry():
    global result
    result = {
            'color': '',
            'text': '',
            'font': ''
        }
    color = ''
    def save():
        global result
        color = colorchooser.askcolor(title="Choose color")
        result = {
            'color': color[1],
            'text': water_mk.get(),
            # 'font': combobox.get(),
        }
        font_pick()
        window.destroy()



    window = Toplevel(root)
    window.title("Watermark")
    window.config(pady=20, padx=20)
    water_mk = Entry(window, width=30)
    water_mk.insert(END, string="Enter watermark.")
    water_mk.grid(row=0, column=0)



    _btn = Button(window, text='save', highlightthickness=0, command=save)
    _btn.grid(row=2, column=0)






# Resize Image for viewing on  Tkinter
def resize(size, length):
    breath = int(size[1] * length/size[0])
    return length, breath


# Resize position for stamping watermark on original image
def position(pos_x, pos_y, x_, y_):
    y_cor = int(y_ * pos_y/size[1])
    x_cor = int(x_ * pos_x/size[0])
    return (x_cor, y_cor)


# Load Image picking frame
def pick_img_fr_():
    global img_picked_frame, pick_img_frame
    img_picked_frame.destroy()
    pick_img_frame = pick_img_fr()
    pick_img_frame.pack(fill="both", expand=True)


# Image picking frame
def pick_img_fr():
    global img
    frame = Frame(root)
    canvas = Canvas(frame, width=800, height=526, bg='#7a7a52', highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=1)

    _btn = Button(frame, text='pick image', highlightthickness=0, command=img_picked_fr_)
    _btn.grid(row=1, column=0)
    return frame


# Load frame to show image picked
def img_picked_fr_():
    global size, img_size
    image_filetypes = [
    ('PNG Files', '*.png'),
    ('JPEG Files', '*.jpg;*.jpeg'),
    ('GIF Files', '*.gif'),
    ('BMP Files', '*.bmp'),
    ('TIFF Files', '*.tiff;*.tif'),
    ('All Image Files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.tif'),
    ('All Files', '*.*')
    ]

    global pick_img_frame, img_picked_frame, card, img_file
    pick_img_frame.destroy()
    img_file = filedialog.askopenfilename(title='select image files', filetypes=[('All Image Files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.tif')])
    img = Image.open(img_file)
    size = resize(img.size, 750)
    img_ = img.resize(size)
    card = ImageTk.PhotoImage(img_)

    img_picked_frame = img_picked_fr()
    img_picked_frame.pack()
    img_picked_frame.place(anchor='center', relx=0.5, rely=0.5)


# Load Refresh frame to avoid font stain
def refresh_fr_():
    global pick_img_frame, img_picked_frame, card
    pick_img_frame.destroy()

    img_picked_frame = refresh_fr()
    img_picked_frame.pack()
    img_picked_frame.place(anchor='center', relx=0.5, rely=0.5)



# Frame to show Image picked and watermark
def img_picked_fr():
    global title, canvas
    frame = Frame(root)
    canvas = Canvas(frame, width=size[0], height=size[1], bg='#7a7a52', highlightthickness=0)
    canvas_img = canvas.create_image((size[0]/2), (size[1]/2), image=card)
    title = canvas.create_text(400, 150, text='', anchor=NW)

    canvas.grid(row=0, column=0, columnspan=2)

    _btn = Button(frame, text='add watermark', highlightthickness=0, command=water_mark_entry)
    _btn.grid(row=1, column=0)
    _btn = Button(frame, text='save', highlightthickness=0, command=stamp)
    _btn.grid(row=1, column=1)

    canvas.tag_bind(title, "<Button-1>", drag_start)
    canvas.tag_bind(title, '<B1-Motion>', mov)
    return frame


# Refresh frame to avoid font stain
def refresh_fr():
    global title, canvas
    position = canvas.coords(title)
    canvas = Canvas(img_picked_frame, width=size[0], height=size[1], bg='#7a7a52', highlightthickness=0)
    canvas_img = canvas.create_image((size[0]/2), (size[1]/2), image=card)
    title = canvas.create_text(int(position[0]), int(position[1]), text=result['text'], font=(font_picked, 20, "italic"), fill=result['color'], anchor=NW)

    canvas.grid(row=0, column=0, columnspan=2)

    canvas.tag_bind(title, "<Button-1>", drag_start)
    canvas.tag_bind(title, '<B1-Motion>', mov)


# stamp watermark and save watermarked image
def stamp():
    position = canvas.coords(title)
    write_image(text=result['text'], font=font_picked, color=result['color'], position=position)
    print('saved')


root = Tk()
root.wm_title('Watermarker')
root.config(pady=20, padx=20)


# Key bindings
def upKey(event):
    canvas.move(title, 0, -1)
    refresh_fr()

def downKey(event):
    canvas.move(title, 0, 1)
    refresh_fr()

def leftKey(event):
    canvas.move(title, -1, 0)
    refresh_fr()

def rightKey(event):
    canvas.move(title, 1, 0)
    refresh_fr()


def drag_start(event):
    widget = event.widget
    x, y = widget.coords(title)
    # save the offset of the click position from the obj's top-left corner
    widget.dx, widget.dy = event.x-x, event.y-y

def mov(event):
    widget = event.widget
    # Calculate the new position by adjusting the coordinates with the mouse drag offset
    new_x, new_y = event.x - widget.dx, event.y - widget.dy
    # Move the text (title) to the new position without redrawing
    widget.coords(title, new_x, new_y)
    refresh_fr()



# UI declarations and defaults
pick_img_frame = pick_img_fr()
pick_img_frame.pack(fill="both", expand=True)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
root.focus_set()
root.mainloop()