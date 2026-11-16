import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():

    # Part 1 and Part 2:
    # Convert the image to a wider data type and calculate the simple mean in two ways.
    if len(sys.argv) != 2:
        print("Usage: python ex09.py <image_path>")
        return

    img = cv2.imread(sys.argv[1])

    if img is None:
        print("Could not read the image.")
        return

    # Method 1: convert to a wider integer type before adding channels.
    img_int = img.astype(np.int32)
    gray_mean_1 = img_int.mean(axis=2)

    # Method 2: use np.sum with a wider type, then divide.
    gray_mean_2 = img.astype(np.float64).sum(axis=2) / 3


    # Part 3:
    # Implement the weighted grayscale formula using broadcasting and sum.
    # BGR order in OpenCV, so the weights are B, G, R.
    weights = np.array([0.114, 0.587, 0.299])
    gray_formula = (img.astype(np.float64) * weights).sum(axis=2)
    gray_formula = np.clip(gray_formula, 0, 255).astype(np.uint8)


    # Part 4:
    # Compare the weighted formula with OpenCV's grayscale conversion.
    # Convert both arrays to signed/wider integers before subtraction.
    gray_cv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    difference = np.abs(
        gray_formula.astype(np.int16) - gray_cv.astype(np.int16)
    )
    print(f"Maximum absolute difference: {difference.max()}")


    # Part 5:
    # Display the simple mean and weighted formula side by side.
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(gray_mean_1.astype(np.uint8), cmap="gray")
    plt.title("Simple mean")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray_formula, cmap="gray")
    plt.title("Weighted formula")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()