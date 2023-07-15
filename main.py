import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog, colorchooser, Scale, HORIZONTAL
from PIL import Image, ImageTk
import numpy as np

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.img = None
        self.img_original = None
        self.text_color = "black"
        self.text_position = (0, 0)
        self.text_content = ""

        self.toolbar = tk.Frame(root, bg="#eee", width=200)
        self.toolbar.pack(side="left", fill="y")

        self.display_frame = tk.Frame(root, bg="lightgrey", bd=5, relief=tk.RIDGE)
        self.display_frame.pack(side="right", fill="both", expand=True)

        self.button_upload = tk.Button(self.toolbar, text='Upload Image', command=self.upload_image, font=('Arial', 10), background='purple', foreground='white')
        self.button_upload.pack(fill="x", padx=2, pady=2)

        self.resize_frame = tk.Frame(self.toolbar, bg="#eee")
        self.resize_frame.pack(fill="x", padx=2, pady=2)

        self.width_scale = tk.Scale(self.resize_frame, from_=10, to=200, orient=HORIZONTAL, sliderlength=15, length=150)
        self.width_scale.set(100)
        self.width_scale.pack(side="left")

        self.height_scale = tk.Scale(self.resize_frame, from_=10, to=200, orient=HORIZONTAL, sliderlength=15, length=150)
        self.height_scale.set(100)
        self.height_scale.pack(side="left")

        self.button_resize = tk.Button(self.resize_frame, text='Resize Image', command=self.resize_image, font=('Arial', 10), background='purple', foreground='white')
        self.button_resize.pack(side="left", padx=2, pady=2)

        self.button_grayscale = tk.Button(self.toolbar, text='Toggle Grayscale', command=self.grayscale_image, font=('Arial', 10), background='purple', foreground='white')
        self.button_grayscale.pack(fill="x", padx=2, pady=2)

        self.blur_frame = tk.Frame(self.toolbar, bg="#eee")
        self.blur_frame.pack(fill="x", padx=2, pady=2)

        self.blur_intensity = tk.Scale(self.blur_frame, from_=0, to=100, orient=HORIZONTAL, sliderlength=15, length=150)
        self.blur_intensity.set(0)
        self.blur_intensity.pack(side="left")

        self.button_blur = tk.Button(self.blur_frame, text='Blur Image', command=self.blur_image, font=('Arial', 10), background='purple', foreground='white')
        self.button_blur.pack(side="left")

        self.button_edge = tk.Button(self.toolbar, text='Toggle Edge Detection', command=self.edge_detection, font=('Arial', 10), background='purple', foreground='white')
        self.button_edge.pack(fill="x", padx=2, pady=2)

        self.rotate_frame = tk.Frame(self.toolbar, bg="#eee")
        self.rotate_frame.pack(fill="x", padx=2, pady=2)

        self.rotate_scale = tk.Scale(self.rotate_frame, from_=-180, to=180, orient=HORIZONTAL, sliderlength=15, length=150)
        self.rotate_scale.set(0)
        self.rotate_scale.pack(side="left")

        self.button_rotate = tk.Button(self.rotate_frame, text='Rotate Image', command=self.rotate_image, font=('Arial', 10), background='purple', foreground='white')
        self.button_rotate.pack(side="left", padx=2, pady=2)

        self.button_text = tk.Button(self.toolbar, text='Set Text', command=self.set_text, font=('Arial', 10), background='purple', foreground='white')
        self.button_text.pack(fill="x", padx=2, pady=2)

        self.button_add_text = tk.Button(self.toolbar, text='Add Text to Image', command=self.add_text, font=('Arial', 10), background='purple', foreground='white')
        self.button_add_text.pack(fill="x", padx=2, pady=2)

        self.button_save = tk.Button(self.toolbar, text='Save Image', command=self.save_image, font=('Arial', 10), background='purple', foreground='white')
        self.button_save.pack(fill="x", padx=2, pady=2)

        self.canvas = tk.Canvas(self.display_frame, width=500, height=500, bg="white")
        self.canvas.pack(padx=10, pady=10, fill="both", expand=True)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        self.img = cv2.imread(file_path)
        self.img_original = self.img.copy()
        self.display_image(self.img)

    def display_image(self, image):
        self.canvas.delete("all")  # clear canvas before displaying new image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # convert color space from BGR to RGB
        image = Image.fromarray(image)  # convert from NumPy array to PIL Image
        self.image_temp = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_temp)

    def resize_image(self):
        width_scale = self.width_scale.get() / 100
        height_scale = self.height_scale.get() / 100
        new_width = int(self.img.shape[1] * width_scale)
        new_height = int(self.img.shape[0] * height_scale)
        self.img = cv2.resize(self.img_original, (new_width, new_height))
        self.display_image(self.img)

    def grayscale_image(self):
        if len(self.img.shape) == 2:  # if image is grayscale, revert to original
            self.img = self.img_original.copy()
        else:  # else convert to grayscale
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.display_image(self.img)

    def blur_image(self):
        blur_size = self.blur_intensity.get()
        if blur_size % 2 == 0:  # blur size must be odd
            blur_size += 1
        self.img = cv2.GaussianBlur(self.img_original,(blur_size,blur_size),0)
        self.display_image(self.img)

    def edge_detection(self):
        if len(self.img.shape) == 2:  # if image is grayscale, revert to original
            self.img = self.img_original.copy()
        else:  # else apply Canny edge detection
            self.img = cv2.Canny(self.img, 100, 200)
        self.display_image(self.img)

    def rotate_image(self):
        angle = self.rotate_scale.get()
        height, width = self.img.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
        self.img = cv2.warpAffine(self.img_original, rotation_matrix, (width, height))
        self.display_image(self.img)

    def set_text(self):
        self.text_content = simpledialog.askstring("Input", "Enter text")
        self.text_position = (simpledialog.askinteger("Input", "Enter x position"), simpledialog.askinteger("Input", "Enter y position"))
        _, color = colorchooser.askcolor()
        self.text_color = (int(color[2]), int(color[1]), int(color[0]))  # OpenCV uses BGR color space

    def add_text(self):
        self.img = cv2.putText(self.img, self.text_content, self.text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, self.text_color, 2, cv2.LINE_AA)
        self.display_image(self.img)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        cv2.imwrite(file_path, self.img)

root = tk.Tk()
root.title("Image Editor")
root.configure(background='lightgrey')  # you can change the color here
editor = ImageEditor(root)
root.mainloop()
