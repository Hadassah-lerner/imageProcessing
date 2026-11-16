import sys
import time
import cv2
import numpy as np


# Part 1: 
# Measure the execution time of loop and NumPy implementations.
def brighten_loop(img, value=50):
    result = img.copy()
    h, w, c = result.shape

    for y in range(h):
        for x in range(w):
            for channel in range(c):
                result[y, x, channel] = min(
                    int(result[y, x, channel]) + value, 255
                )

    return result


# NumPy implementation used for comparison.
def brighten_numpy(img, value=50):
    return np.clip(img.astype(np.int16) + value, 0, 255).astype(np.uint8)


# Repeat each measurement and calculate the median time.
def measure(function, img, repeats=5):
    times = []

    for _ in range(repeats):
        start = time.perf_counter()
        function(img)
        elapsed = (time.perf_counter() - start) * 1000
        times.append(elapsed)

    # Ignore the first run because it can be slower.
    measured = times[1:]
    return np.median(measured)


# Part 1 and Part 2: 
# Run the measurements on different image sizes.
def main():
    if len(sys.argv) != 2:
        print("Usage: python ex08.py <image_path>")
        return

    img = cv2.imread(sys.argv[1])

    if img is None:
        print("Could not read the image.")
        return

    images = [
        ("original", img),
        ("half", img[::2, ::2]),
        ("quarter", img[::4, ::4]),
    ]

    print("| img.size | loop (ms) | numpy (ms) | speedup |")
    print("|----------|-----------|------------|---------|")

    for name, current in images:
        loop_time = measure(brighten_loop, current)
        numpy_time = measure(brighten_numpy, current)
        speedup = loop_time / numpy_time

        print(
            f"| {current.size} | {loop_time:.3f} | "
            f"{numpy_time:.3f} | {speedup:.2f}x |"
        )


if __name__ == "__main__":
    main()