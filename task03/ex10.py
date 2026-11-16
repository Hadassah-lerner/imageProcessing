import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():

    # Part 1: 
    # Convert the image to grayscale and count bright and dark pixels.
    if len(sys.argv) != 2:
        print("Usage: python ex10.py <image_path>")
        return

    img = cv2.imread(sys.argv[1])

    if img is None:
        print("Could not read the image.")
        return

    # Convert the color image to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bright_count = (gray > 200).sum()
    dark_count = (gray < 50).sum()

    print(f"Pixels brighter than 200: {bright_count}")
    print(f"Pixels darker than 50: {dark_count}")


    # Part 2: 
    # Create a black-and-white image using a boolean mask.
    binary_mask = np.zeros_like(gray)
    mask = gray > 128
    binary_mask[mask] = 255


    # Create a black-and-white image using np.where.
    binary_where = np.where(gray > 128, 255, 0).astype(np.uint8)


    # Part 3: 
    # Create a mask for bright pixels.
    bright_mask = gray > 200


    # Color bright pixels red in the original color image.
    # OpenCV stores colors as B, G, R, so red is [0, 0, 255].
    red_result = img.copy()
    red_result[bright_mask] = [0, 0, 255]


    # Display the original and modified images side by side.
    original_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    red_result_rgb = cv2.cvtColor(red_result, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(red_result_rgb)
    plt.title("Pixels brighter than 200 in red")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()