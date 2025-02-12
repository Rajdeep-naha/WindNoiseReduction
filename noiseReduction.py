import noisereduce as nr
import soundfile as sf
import numpy as np
import librosa.display
import matplotlib.pyplot as plt

def calculate_snr(signal, noise):
    """Calculate Signal-to-Noise Ratio in dB"""
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    return 10 * np.log10(signal_power / noise_power)

# Load audio files
filtered_signal, fs = sf.read('data/filtered_audio.wav')
noisy_signal, _ = sf.read('data/noisy_audio.wav')

# Get noise profile from the beginning of the recording
# Usually wind noise is most prominent in the first few seconds
noise_sample = filtered_signal[:int(fs*2)]  # 2 sec noise sample

# Try to clean up the audio
cleaned = nr.reduce_noise(
    y=filtered_signal, 
    sr=fs,
    y_noise=noise_sample,
    stationary=False,
    prop_decrease=0.95,    
    n_std_thresh_stationary=2.5,
    n_fft=2048,
    win_length=2048,
    n_jobs=1  
)

# The output is usually too quiet, let's fix that
cleaned = cleaned * 2.5  # Boost volume a bit

# Make 
cleaned = cleaned / np.max(np.abs(cleaned))

# Save the cleaned audio
sf.write('data/denoised_filtered_audio.wav', cleaned, fs)

# Let's see how much we improved the SNR
noise_chunk = noisy_signal[:int(fs*2)]  # Use first 2 seconds as noise reference
before_snr = calculate_snr(noisy_signal[int(fs*2):], noise_chunk)
after_snr = calculate_snr(cleaned[int(fs*2):], noise_chunk)

# Plot spectrograms to compare
plt.figure(figsize=(12, 5))

# Before cleaning
plt.subplot(1, 2, 1)
D_noisy = librosa.amplitude_to_db(np.abs(librosa.stft(noisy_signal)), ref=np.max)
librosa.display.specshow(D_noisy, sr=fs, x_axis='time', y_axis='log')
plt.title(f'Before (SNR: {before_snr:.1f} dB)')
plt.colorbar(format='%+2.0f dB')

# After cleaning
plt.subplot(1, 2, 2)
D_clean = librosa.amplitude_to_db(np.abs(librosa.stft(cleaned)), ref=np.max)
librosa.display.specshow(D_clean, sr=fs, x_axis='time', y_axis='log')
plt.title(f'After (SNR: {after_snr:.1f} dB)')
plt.colorbar(format='%+2.0f dB')

plt.tight_layout()
plt.show()
