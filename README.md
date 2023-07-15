# ImageEditor Program

This program is a simple image editor built with Python. It provides a graphical user interface for performing various image editing operations, including uploading an image, resizing the image, converting the image to grayscale, blurring the image, performing edge detection on the image, rotating the image, adding text to the image, and saving the image.

# How to Run?
you can simply copy and paste the program and run, however, you will need to install the libraries mentioned bellow

## Libraries Used

### Tkinter
Tkinter is Python's standard GUI (Graphical User Interface) package. It provides a powerful object-oriented interface to the Tk GUI toolkit, and is the de facto standard for Python GUI development.

Functions used from Tkinter:

- `Tk`: The root window for the application.
- `Frame`: A rectangular region on the screen. It is used as a container to hold other widgets.
- `Button`: A button that can contain text and can perform an action when clicked.
- `Canvas`: A canvas widget that provides a flexible area for creating a wide variety of graphics.
- `Scale`: A scale widget that provides a slider for selecting a numerical value.
- `filedialog.askopenfilename`: Prompts the user to choose a file to open.
- `filedialog.asksaveasfilename`: Prompts the user to choose a location and filename to save a file.
- `simpledialog.askstring`: Prompts the user to input a string.
- `simpledialog.askinteger`: Prompts the user to input an integer.
- `colorchooser.askcolor`: Prompts the user to choose a color.

### OpenCV (cv2)
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It includes several hundreds of computer vision algorithms.

Functions used from OpenCV:

- `cv2.imread`: Loads an image from a file.
- `cv2.cvtColor`: Converts an image from one color space to another.
- `cv2.resize`: Resizes an image.
- `cv2.GaussianBlur`: Blurs an image using a Gaussian filter.
- `cv2.Canny`: Performs edge detection using the Canny algorithm.
- `cv2.getRotationMatrix2D`: Calculates an affine matrix of 2D rotation.
- `cv2.warpAffine`: Applies an affine transformation to an image.
- `cv2.putText`: Draws a text string on an image.
- `cv2.imwrite`: Saves an image to a specified file.

### PIL (Python Imaging Library)
The Python Imaging Library (PIL) adds image processing capabilities to your Python interpreter.

Functions used from PIL:

- `Image.fromarray`: Creates an image memory from an object exporting the array interface.
- `ImageTk.PhotoImage`: Creates a photo image from a PIL image.

### NumPy
NumPy is a Python package. It stands for 'Numerical Python'. It is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

No specific functions from NumPy are directly used in this code, but NumPy arrays are used indirectly when working with images in OpenCV. For example, images loaded with `cv2.imread` are stored as NumPy arrays.
