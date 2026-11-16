import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():

    # Part 1: 
    # Read the image and print the shapes of the required expressions.
    if len(sys.argv) != 2:
        print("Usage: python ex07.py <image_path>")
        return

    img = cv2.imread(sys.argv[1])

    if img is None:
        print("Could not read the image.")
        return

    expressions = {
        "img[10, 20]": img[10, 20],
        "img[:, :, 0]": img[:, :, 0],
        "img[100:200, 50:150]": img[100:200, 50:150],
        "img[::2, ::2]": img[::2, ::2],
        "img[::-1, :]": img[::-1, :],
        "img[:, ::-1, :]": img[:, ::-1, :],
        "img[0]": img[0],
        "img[:, 0]": img[:, 0],
    }

    for expression, result in expressions.items():
        print(f"{expression}: shape: {result.shape}")


    # Display the crop, reduction, upside-down image, and mirror image.
    # Convert BGR to RGB only for correct Matplotlib display.
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    crop = rgb[100:200, 50:150]
    reduced = rgb[::2, ::2]
    upside_down = rgb[::-1, :]
    mirror = rgb[:, ::-1, :]

    fig, axes = plt.subplots(1, 4, figsize=(14, 4))
    results = [
        ("img[100:200, 50:150]", crop),
        ("img[::2, ::2]", reduced),
        ("img[::-1, :]", upside_down),
        ("img[:, ::-1, :]", mirror),
    ]

    for ax, (title, image) in zip(axes, results):
        ax.imshow(image)
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()


    # Part 4: 
    # Create a black 10-pixel frame using four slice assignments.
    framed = img.copy()
    framed[:10, :] = 0
    framed[-10:, :] = 0
    framed[:, :10] = 0
    framed[:, -10:] = 0

    framed_rgb = cv2.cvtColor(framed, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(6, 5))
    plt.imshow(framed_rgb)
    plt.title("Black frame - 10 pixels")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()