# # 40: Create RGB image-like data:
# # Create a (4, 4, 3) array.

# # Multiply each color channel by:

# # [1.0, 0.5, 0.2]

# # using broadcasting.
# import numpy as np
# tensor= np.random.randint(0,255,size= (4,4,3))
# print(tensor)

# row_vector= np.array([1.0,0.5,0.2])
# print(row_vector)

# result= tensor * row_vector
# print(f"The result is: {result}")


# Claude Code



# 40: Create RGB image-like data:
# (4, 4, 3) → 4×4 pixels, each with R, G, B channels (0–255)
# Scale factors [1.0, 0.5, 0.2]: R unchanged, G halved, B at 20%
# Shape (3,) broadcasts over (4, 4) automatically

import numpy as np

np.random.seed(42)

image = np.random.randint(0, 256, size=(4, 4, 3))        # valid RGB range
channel_scale = np.array([1.0, 0.5, 0.2])               # shape (3,)

print("Original image:\n", image)
print(f"\nChannel scale factors: {channel_scale}")

# multiply → scale factor broadcasts across all 4×4 pixels
scaled = image * channel_scale                           # shape stays (4, 4, 3)
result = np.clip(scaled, 0, 255).astype(np.uint8)        # keep valid, cast to image type

print(f"\nScaled image (shape {result.shape}):\n", result)