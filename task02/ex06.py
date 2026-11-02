import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale image
if len(sys.argv) != 2:
    print("Usage: python ex06.py <image file>")
    sys.exit(1)

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not read image")
    sys.exit(1)

# Part 1 - Multiply image by 1.5
result = img * 1.5

print("Result dtype:", result.dtype)
print("Result maximum:", result.max())

# Part 2 - Convert result to uint8
result_1_5 = np.clip(result, 0, 255).astype(np.uint8)

# Part 3 - Multiply image by 2
result_2 = img * 2

print("Result dtype (multiply by 2):", result_2.dtype)
print("Result maximum (multiply by 2):", result_2.max())

# Part 4 - Multiply image by 0.5
result_0_5 = (img * 0.5).astype(np.uint8)

# Display original and results
images = [
    img,
    result_1_5,
    result_2,
    result_0_5
]

titles = [
    "Original",
    "Multiply by 1.5",
    "Multiply by 2",
    "Multiply by 0.5"
]

plt.figure(figsize=(16, 5))

for i in range(4):
    plt.subplot(1, 4, i + 1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.savefig("ex06.png")
plt.show()

# Part 5 - Bonus: Change contrast around the mean
m = img.mean()

difference = img - m

print("Mean:", m)
print("Difference dtype:", difference.dtype)

k_values = [0.5, 1.5, 2.0]

plt.figure(figsize=(15, 5))

for i, k in enumerate(k_values):

    result = (difference * k) + m

    result = np.clip(result, 0, 255).astype(np.uint8)

    plt.subplot(1, 3, i + 1)
    plt.imshow(result, cmap="gray", vmin=0, vmax=255)
    plt.title(f"Contrast k={k}")
    plt.axis("off")

plt.tight_layout()
plt.show()
