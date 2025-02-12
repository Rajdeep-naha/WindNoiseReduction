import noisereduce as nr
import soundfile as sf
import numpy as np

# Load both the noisy and filtered audio
filtered_signal, fs = sf.read('data/filtered_audio.wav')
noisy_signal, _ = sf.read('data/noisy_audio.wav')

# Use a longer noise sample for better noise profile estimation
noise_clip = filtered_signal[:int(fs*2)]  # Use first 2 seconds as noise sample


reduced_noise = nr.reduce_noise(
    y=filtered_signal, 
    sr=fs,
    y_noise=noise_clip,
    stationary=False,
    prop_decrease=0.95,    # Increase noise reduction (default is 0.75)
    n_std_thresh_stationary=2.5,  # Lower threshold for noise detection
    n_fft=2048,           # Larger FFT window for better frequency resolution
    win_length=2048,      # Match with n_fft
    n_jobs=1              # Disabled parallel processing
)

# Amplify the output (increase volume)
amplification_factor = 2.5  # Increased amplification factor
reduced_noise = reduced_noise * amplification_factor

# Normalize to prevent clipping
reduced_noise = reduced_noise / np.max(np.abs(reduced_noise))

# Save the result
sf.write('data/denoised_filtered_audio.wav', reduced_noise, fs)

# Calculate SNR for both signals
def calculate_snr(signal, noise):
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Assuming first 2 seconds contain mostly noise
noise_segment = noisy_signal[:int(fs*2)]
snr_noisy = calculate_snr(noisy_signal[int(fs*2):], noise_segment)
snr_denoised = calculate_snr(reduced_noise[int(fs*2):], noise_segment)

# Visualization
import librosa.display
import matplotlib.pyplot as plt

D_noisy = librosa.amplitude_to_db(np.abs(librosa.stft(noisy_signal)), ref=np.max)
D_denoised = librosa.amplitude_to_db(np.abs(librosa.stft(reduced_noise)), ref=np.max)

plt.figure(figsize=(10, 4))
plt.subplot(1,2,1)
librosa.display.specshow(D_noisy, sr=fs, x_axis='time', y_axis='log')
plt.title(f'Noisy Signal (SNR: {snr_noisy:.2f} dB)')
plt.colorbar(format='%+2.0f dB')

plt.subplot(1,2,2)
librosa.display.specshow(D_denoised, sr=fs, x_axis='time', y_axis='log')
plt.title(f'Denoised Signal (SNR: {snr_denoised:.2f} dB)')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()
