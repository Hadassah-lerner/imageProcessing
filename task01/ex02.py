import numpy as np

# Part 1.
black = np.zeros((100, 200), dtype=np.uint8)

# Part 2.
white = np.full((100, 200), 255, dtype=np.uint8)

# Part 3.
color = np.zeros((100, 200, 3), dtype=np.uint8)
color[:, :] = [255, 192, 203]  # RGB pink

# Part 4.
for name, img in [
    ("Black", black),
    ("White", white),
    ("Color", color),
]:
    print(name)
    print("shape:", img.shape)
    print("ndim:", img.ndim)
    print("size:", img.size)
    print("nbytes:", img.nbytes)
    print()

# Part 5.
img1 = np.zeros((1080, 1920, 3), dtype=np.uint8)
img2 = np.zeros((3000, 4000, 3), dtype=np.uint8)  # 12 million pixels

print("1920 x 1080 RGB image:")
print("nbytes:", img1.nbytes)  # 1920 * 1080 * 3 = 6,220,800 bytes

print("12-megapixel RGB image:")
print("nbytes:", img2.nbytes)  # 12,000,000 * 3 = 36,000,000 bytes
print()

# Part 6.
b = np.arange(12).reshape(3, 4)

print("Array b:")
print(b)

print("Sum of all elements:")
print(b.sum())

print("Sum with axis=0:")
print(b.sum(axis=0))

print("Sum with axis=1:")
print(b.sum(axis=1))

print("b[2, 3] and b[-1, -1]:")
print(b[2, 3], b[-1, -1])
