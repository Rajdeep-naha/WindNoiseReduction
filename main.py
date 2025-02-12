from sc_wind_noise_generator import WindNoiseGenerator
import numpy as np
from scipy.io import wavfile
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Create generator with specific parameters
generator = WindNoiseGenerator(
    fs=48000,          # Sampling frequency in Hz
    duration=15, 
    generate=True,      # Duration in seconds
    wind_profile=None, # Use default wind profile      
    gustiness=3,       # Gustiness factor
    start_seed=None    # Random seed

)

# Generate and play the wind noise
wn_sample, _ = generator.generate_wind_noise()  # Unpack the tuple
# Ensure the signal is in the correct shape for playback (stereo)
if isinstance(wn_sample, np.ndarray) and wn_sample.ndim == 1:
    wn_sample = wn_sample.reshape(-1, 1)  # Convert to 2D array for mono
    wn_sample = np.column_stack((wn_sample, wn_sample))  # Duplicate for stereo

# Normalize to [-1, 1] range
wn_sample = wn_sample / np.max(np.abs(wn_sample))

# Convert to 16-bit PCM
wn_sample = (wn_sample * 32767).astype(np.int16)

# Save the audio file in the data folder
output_path = os.path.join('data', 'wind_noise.wav')
wavfile.write(output_path, generator.fs, wn_sample)

# For playback, convert back to float32 in [-1, 1] range
wn_sample_float = wn_sample.astype(np.float32) / 32767.0
generator.play_signal(wn_sample_float)

