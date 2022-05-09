from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw

pos = (0, 0)
text = "I'm watermark!"
fill = (93, 93, 93)

window = Tk()
window.title("Watermark")
window.config(padx=20, pady=20)
window.minsize(width=300, height=200)


def open_save_file():

    filename = filedialog.askopenfilename(title='Chose an image', filetypes=[('Image Files', '*jpeg *jpg *png')])
    if len(filename) == 0:
        pass
    else:
        img = Image.open(filename)

        w, h = img.size
        if h > 638:
            resize_val = h / 638
            h = h / resize_val
            w = w / resize_val
        if w > 1296:
            resize_val = w / 1296
            h = h / resize_val
            w = w / resize_val
        img = img.resize((round(w), round(h)))

        drawing = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 14)
        drawing.text(pos, text, fill=fill, font=font)

        img.save(f"watermarked_{filename.split('/')[-1]}")

        img = ImageTk.PhotoImage(img)
        label_img = Label(window, image=img)
        label_img.image = img
        label_img.grid(row=1, column=0, columnspan=2, pady=10)


button_add = Button(text="Select image", command=open_save_file)
button_add.grid(row=0, column=0)
window.mainloop()
