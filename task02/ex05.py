import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Part 1 - Safe addition and brighten function
def add_safe(img, b):
    result = img.astype(np.int16) + b
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

def brighten(img, b, method):

    if method == "np":
        return img + b

    elif method == "cv2":
        if b >= 0:
            return cv2.add(img, b)
        else:
            return cv2.subtract(img, -b)

    elif method == "clip":
        return add_safe(img, b)

# Read grayscale image
if len(sys.argv) != 2:
    print("Usage: python ex05.py <image file>")
    sys.exit(1)

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not read image")
    sys.exit(1)

# Part 2 - Brighten image using three methods
b = 100

img_np = brighten(img, b, "np")
img_cv2 = brighten(img, b, "cv2")
img_clip = brighten(img, b, "clip")

images = [img, img_np, img_cv2, img_clip]

titles = [
    "Original",
    "NumPy",
    "OpenCV",
    "Clip"
]

plt.figure(figsize=(16, 5))

for i in range(4):
    plt.subplot(1, 4, i + 1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.savefig("ex05.png")
plt.show()

# Part 3 - Print maximum values
print("Original max:", img.max())
print("NumPy max:", img_np.max())
print("OpenCV max:", img_cv2.max())
print("Clip max:", img_clip.max())

# Part 4 - Darken image using b=-100
b = -100

img_cv2_dark = brighten(img, b, "cv2")
img_clip_dark = brighten(img, b, "clip")

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(img_cv2_dark, cmap="gray", vmin=0, vmax=255)
plt.title("OpenCV -100")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(img_clip_dark, cmap="gray", vmin=0, vmax=255)
plt.title("Clip -100")
plt.axis("off")

plt.tight_layout()
plt.show()

# Part 5 - Display without vmin and vmax
plt.figure(figsize=(16, 5))

for i in range(4):
    plt.subplot(1, 4, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.savefig("ex05_no_vmin.png")
plt.show()
