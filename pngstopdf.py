""""
It needs PIL package ->Pillow
""""

from PIL import Image

image1 = Image.open(r'path where the image is stored\file name.png')
image2 = Image.open(r'path where the image is stored\file name.png')
image3 = Image.open(r'path where the image is stored\file name.png')
image4 = Image.open(r'path where the image is stored\file name.png')

im1 = image1.convert('RGB')
im2 = image2.convert('RGB')
im3 = image3.convert('RGB')
im4 = image4.convert('RGB')

""""
excluding the first image
""""
imagelist = [im2,im3,im4]

im1.save(r'path where the pdf will be stored\new file name.pdf',save_all=True, append_images=imagelist)

"""
If you need to convert jpg format pictures to pdf, please replace all png in the template with jpg.
"""
