# Wind Noise Reduction System

A Python and MATLAB-based system for wind noise reduction in audio signals. This project implements a multi-stage approach combining spectral modeling for wind noise generation and advanced noise reduction techniques.

## Overview

The system addresses wind noise in audio recordings through three main stages:
1. Wind noise simulation using spectral modeling
2. Audio mixing with controlled Signal-to-Noise Ratio (SNR)
3. Noise reduction using spectral subtraction techniques

## Features

- **Wind Noise Generation**: Realistic wind noise synthesis using spectral modeling
- **Controlled Mixing**: Precise SNR control for mixing clean audio with wind noise
- **Noise Reduction**: Advanced spectral noise reduction with SNR optimization
- **Analysis Tools**: 
  - SNR calculation
  - Spectrogram visualization
  - Before/after comparison tools

## Requirements

### Python Dependencies
python
numpy>=1.20.0
scipy>=1.7.0
soundfile>=0.10.0
noisereduce>=2.0.0
librosa>=0.8.1
matplotlib>=3.4.0
sounddevice>=0.4.4

### Required Data Files
- clean_speech.wav # Reference clean speech recordings
- wind_samples.wav # Sample wind recordings for modeling
- test_audio.wav # Test audio files
- validation_set.wav # Validation audio samples
- calibration_tone.wav # Calibration reference signal

### MATLAB Requirements
- MATLAB R2019b or newer
- Basic MATLAB (no additional toolboxes required)

## Project Structure

WindNoiseReduction/
├── data/ # Audio files directory
│ ├── clean_audio.wav # Original clean audio
│ ├── wind_noise.wav # Generated wind noise
│ ├── noisy_audio.wav # Mixed audio
│ ├── filtered_audio.wav # Filtered audio output
│ ├── denoised_audio.wav # Processed output
│ └── denoised_filtered_audio.wav # Filtered and denoised output
├── main.py # Wind noise generator
├── sc_wind_noise_generator.py # Spectral modeling wind noise generator
├── mixerFunction.m # MATLAB mixing script
└── noiseReduction.py # Noise reduction implementation  

Processes the noisy audio and generates denoised output.

## Results

The system provides:
- Denoised audio file
- Spectrograms comparing original and processed audio
- SNR measurements showing noise reduction effectiveness

### Sample Results
- Initial SNR: -10 dB (noisy audio)
- Final SNR: Improved by approximately 15-20 dB
- Preserved speech intelligibility while reducing wind noise

## Implementation Details

### Wind Noise Generation
- Uses spectral modeling synthesis
- Controllable parameters:
  - Wind speed
  - Gustiness
  - Spectral characteristics

### Noise Reduction
- Spectral subtraction technique
- Adaptive threshold determination
- SNR-based optimization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Rajdeep Naha](https://github.com/Rajdeep-naha)

## Acknowledgments

- noisereduce library for spectral noise reduction
- librosa for audio processing and visualization
- MATLAB for signal processing capabilities
- SC-Wind-Noise-Generator for wind noise generation

## Contact

For any queries or suggestions, please open an issue in the GitHub repository.