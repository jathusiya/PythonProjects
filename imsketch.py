import numpy as np
import imageio.v2
import scipy.ndimage
import cv2

img = "OIP.jpg"

def rgb2gray(rgb):
    if len(rgb.shape) == 3 and rgb.shape[2] == 3:
        return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
    else:
        return rgb

ss = imageio.v2.imread(img)
gray = rgb2gray(ss)

i = 255 - gray

# To convert to a blurred image
blur = scipy.ndimage.gaussian_filter(i, sigma=15)

def dodge(front, back):
    # Add a small epsilon value to avoid division by zero
    epsilon = 1e-5
    final_sketch = front * 255 / (255 - back + epsilon)
    # Clip the resulting values to the valid range (0 to 255)
    final_sketch = np.clip(final_sketch, 0, 255)
    return final_sketch.astype('uint8')

r = dodge(blur, gray)

cv2.imwrite('OIP.jpg', r)
