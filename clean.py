import os
import cv2
import numpy as np
from PIL import Image

input_folder = "stft"
output_folder = "stft_cleaned"
os.makedirs(output_folder, exist_ok=True)

CROP_LEFT_OFFSET = 264
CROP_TOP_OFFSET = 111
CROP_RIGHT_OFFSET = 581
CROP_BOTTOM_OFFSET = 173

def normalize_image(img_gray):
    """
    1) Convert pixel range from [0,255] -> [0,1].
    2) Z-score normalization: (x - mean) / std
    3) Rescale back to [0,255] for saving as PNG.
    """
    img_float = img_gray.astype(np.float32) / 255.0
    zscored = (img_float - img_float.mean()) / (img_float.std() + 1e-6)

    zscored_norm = ((zscored - zscored.min()) / (zscored.max() - zscored.min()) * 255.0)
    return zscored_norm.astype(np.uint8)

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(".png"):
        file_path = os.path.join(input_folder, file_name)

        with Image.open(file_path) as im:
            width, height = im.size

            left   = CROP_LEFT_OFFSET
            top    = CROP_TOP_OFFSET
            right  = width - CROP_RIGHT_OFFSET
            bottom = height - CROP_BOTTOM_OFFSET

            cropped_im = im.crop((left, top, right, bottom))

        cropped_np = np.array(cropped_im.convert("L"))

        norm_np = normalize_image(cropped_np)

        output_path = os.path.join(output_folder, file_name)
        cv2.imwrite(output_path, norm_np)

        print(f"Processed & saved: {output_path}")

print("\n✅ All spectrograms cropped & normalized in 'output_cleaned' folder!")
