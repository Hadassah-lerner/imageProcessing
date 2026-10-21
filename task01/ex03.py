import numpy as np

# Part 1.
x = np.array([100, 200, 250], dtype=np.uint8)

print("Part 1: uint8 arithmetic")
print("x + 10:", x + 10)
print("x + 100:", x + 100)
print("x - 150:", x - 150)
print("x * 2:", x * 2)
print("x.astype(np.int16) + 100:", x.astype(np.int16) + 100)
print("x * 1.5:", x * 1.5)
print("(x * 1.5).dtype:", (x * 1.5).dtype)
print()

# Part 2.
print("Part 2: x + 300")
try:
    print(x + 300)
except OverflowError as error:
    print("OverflowError:", error)
print()

# Part 3.
def add_safe(x, b):
    result = x.astype(np.int16) + b
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

print("Part 3: add_safe")
print("add_safe(x, 100):", add_safe(x, 100))
print("add_safe(x, -150):", add_safe(x, -150))
print()

# Part 5. (Bonus)
x_int8 = np.array([100, 120, 127], dtype=np.int8)

print("Part 5 (Bonus): int8 arithmetic")
print("x_int8:", x_int8)
print("x_int8 + 10:", x_int8 + 10)
print("x_int8 + 100:", x_int8 + 100)
try:
    print("x_int8 - 150:", x_int8 - 150)
except OverflowError as error:
    print("x_int8 - 150 raises OverflowError:", error)
print("x_int8 * 2:", x_int8 * 2)
print("x_int8.astype(np.int16) + 100:", x_int8.astype(np.int16) + 100)
print("x_int8 * 1.5:", x_int8 * 1.5)
print("(x_int8 * 1.5).dtype:", (x_int8 * 1.5).dtype)

one_int8 = np.array([127], dtype=np.int8)
print("127 + 1 with int8:", one_int8 + 1)
