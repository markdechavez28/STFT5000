import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm  

input_folder = "clips"
output_folder = "stft"

os.makedirs(output_folder, exist_ok=True)

audio_files = [f for f in os.listdir(input_folder) if f.endswith((".wav", ".mp3", ".flac", ".ogg"))]  # Supports multiple formats
n = len(audio_files)

for i, file in enumerate(tqdm(audio_files, desc="Processing Audio Files", unit="file")):
    file_path = os.path.join(input_folder, file)
    
    try:
        y, sr = librosa.load(file_path, sr=None, mono=True, res_type='kaiser_best')
        
        stft_result = librosa.stft(y)
        stft_db = librosa.amplitude_to_db(np.abs(stft_result), ref=np.max)  # Convert to decibels

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(stft_db, sr=sr, x_axis="time", y_axis="log")
        plt.colorbar(format="%+2.0f dB")
        plt.title(f"Spectrogram: {file}")
        plt.tight_layout()

        output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.png")
        plt.savefig(output_file, dpi=300)
        plt.close()

    except Exception as e:
        print(f"Error processing {file}: {e}")

print("Processing complete!")
