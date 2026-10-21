
import numpy as np

a = np.array([[10, 100, 200],
              [50, 150, 250]], dtype=np.uint8)

data = [
    ("a.dtype", "uint8", a.dtype),
    ("a.shape", "(2, 3)", a.shape),
    ("a.ndim", "2", a.ndim),
    ("a.size", "6", a.size),
    ("a.nbytes", "6", a.nbytes),
    ("a[1, 2]", "250", a[1, 2]),
    ("a[0, 1]", "100", a[0, 1]),
    ("a + 10", "[[20, 110, 210], [60, 160, 4]]", a + 10),
    ("a - 20", "[[245, 80, 180], [30, 130, 230]]", a - 20), 
    # Note: 246 is due to uint8 wrap-around (10 - 20 = -10, which wraps to 246 (taking 0 into account))
    ("a * 2", "[[20, 200, 144], [100, 44, 244]]", a * 2), 
    ("a.max()", "250", a.max()),
    ("a.max(axis=0)", "[50, 150, 250]", a.max(axis=0)),
    ("a.max(axis=1)", "[200, 250]", a.max(axis=1))
]

print("Expression | My prediction | Actual result")
print("-" * 42)

for expression, prediction, result in data:
    print(f"{expression} | {prediction} | {result}")
