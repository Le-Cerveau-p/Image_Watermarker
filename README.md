---

# **Image Watermarker**

A Python program that allows users to add custom text watermarks to their images and adjust the watermark's position before saving the result. The tool provides an intuitive graphical interface for watermark customization.

---

## **Features**

- Allows users to select images of various formats (JPEG, PNG, BMP, TIFF, etc.).
- Customizable text watermark:
  - Choose text, font family, font size, and color.
  - Drag the watermark to the desired position on the image.
- Real-time preview of the watermark on the image.
- Saves the watermarked image with a unique name to avoid overwriting the original.

---

## **Installation**

### **Prerequisites**
- Python 3.x installed on your system.
- Required Python packages: 
  - `Pillow`
  - `matplotlib` (for font management)
  - `tkinter` (pre-installed with Python).

### **Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/image-watermarker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd image-watermarker
   ```
3. Install dependencies:
   ```bash
   pip install pillow matplotlib
   ```
4. Run the application:
   ```bash
   python main.py
   ```

---

## **Usage**

1. Launch the application.
2. Use the **Pick Image** button to select an image file.
3. Add a watermark:
   - Enter the desired text.
   - Choose the font and color.
   - Drag the watermark to your preferred position.
4. Save the watermarked image using the **Save** button.

---

## **Supported Image Formats**

- PNG
- JPEG/JPG
- BMP
- TIFF

---

## **Technologies Used**

- **Python**: Core programming language.
- **Tkinter**: For building the graphical interface.
- **Pillow**: For image manipulation.
- **Matplotlib**: For font handling.

---

## **Acknowledgments**

- Inspired by the need for easy and customizable watermarking solutions.
- Thanks to the Python community for libraries like Pillow and Tkinter.

---
