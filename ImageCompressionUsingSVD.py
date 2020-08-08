import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#Getting Image Path
path = 'image.jpg'
#Opening Image
img = Image.open(path) 
#Return the size, in bytes, of path. Raise os.error if the file does not exist
s = float(os.path.getsize(path))/1000 
#Printing Dimensions
print("Size(dimension): ",img.size)
#Title of image as size as a float to 2 decimal places
plt.title("Original Image (%0.2f Kb):" %s)
#Showing Image
plt.imshow(img)

#Converting image to greyscale
imggray = img.convert('L')
#Returns the contents of this image as a sequence object containing pixel values
imgmat = np.array( list(imggray.getdata(band = 0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])
#Image Matrix
imgmat = np.matrix(imgmat)
plt.figure()
plt.imshow(imgmat, cmap = 'gray')
plt.title("Image after converting it into the Grayscale pattern")
plt.show()

print("After compression: ")
#single value decomposition
U, S, Vt = np.linalg.svd(imgmat) 
for i in range(1, 91, 20): # i values of 5, 25 and 45
    compressed = np.matrix(U[:, :i]) * np.diag(S[:i]) * np.matrix(Vt[:i,:])
    plt.imshow(compressed, cmap = 'gray')
    title = "Image after =  %s" %i
    plt.title(title)
    plt.show()
    result = Image.fromarray((compressed).astype(np.uint8))
    result.save('compressed.jpg')
    path = 'compressed.jpg'
    im = Image.open(path)
    c = float(os.path.getsize(path))/1000
    print("Compressed Image (%0.2f Kb):" %c)