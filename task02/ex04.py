import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as plt_patches

# Part 1 - Read and display an image
if len(sys.argv) != 2:
    print("Usage: python ex04.py <image file>")
    sys.exit(1)

print(f"Image path: {sys.argv[1]}")

img = cv2.imread(sys.argv[1])

if img is None:
    print(f"Error: Could not read image from {sys.argv[1]}")
    sys.exit(1)

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(f"Image type: {type(img)}")
print(f"Image dtype: {img.dtype}")
print(f"Image shape: {img.shape}")

print(f"Top-left pixel (R, G, B): {rgb_img[0, 0]}")

# Part 2 - Check an invalid filename
invalid_img = cv2.imread("invalid_image.jpg")
print(f"Invalid image result: {invalid_img}")

# Part 3 - Display BGR and RGB
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("BGR Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rgb_img)
plt.title("RGB Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Part 4 - Display the three color channels
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]

plt.figure(figsize=(16, 5))

plt.subplot(1, 4, 1)
plt.imshow(rgb_img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(blue_channel, cmap="gray")
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(green_channel, cmap="gray")
plt.title("Green Channel")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(red_channel, cmap="gray")
plt.title("Red Channel")
plt.axis("off")

plt.tight_layout()
plt.savefig("ex04.png")
plt.show()

# Part 5 - Read image in grayscale
gray_img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

print(f"Grayscale image shape: {gray_img.shape}")
