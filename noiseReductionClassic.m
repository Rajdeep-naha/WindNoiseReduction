% Load the noisy signal
[noisy_signal, fs] = audioread('data/noisy_audio.wav');

% Time domain plot
t = (0:length(noisy_signal)-1)/fs;
figure;
subplot(2,1,1); plot(t, noisy_signal); title('Noisy Signal - Time Domain'); xlabel('Time (s)');

% Frequency domain plot
N = length(noisy_signal);
Y = fft(noisy_signal);
f = (0:N-1)*(fs/N);
subplot(2,1,2); plot(f, abs(Y)); title('Magnitude Spectrum'); xlabel('Frequency (Hz)');
xlim([0, fs/2]);

% Simple FIR high-pass filter
filter_length = 101;  % Filter length (odd number)
cutoff_freq = 300;    % Cutoff frequency in Hz
nyquist = fs/2;       % Nyquist frequency
normalized_cutoff = cutoff_freq/nyquist;

% Create simple high-pass filter coefficients
n = -(filter_length-1)/2:(filter_length-1)/2;
h = -sin(2*pi*normalized_cutoff*n)./(pi*n);
h((filter_length+1)/2) = 1 - 2*normalized_cutoff;  % Handle division by zero at n=0

% Apply Hamming window to reduce ringing
w = 0.54 - 0.46*cos(2*pi*(0:filter_length-1)/(filter_length-1));
h = h.*w;

% Filter the signal using convolution
filtered_signal = conv(noisy_signal, h, 'same');

% Plot the results
figure;
subplot(2,1,1);
plot(t, noisy_signal);
title('Original Noisy Signal');
xlabel('Time (s)');

subplot(2,1,2);
plot(t, filtered_signal);
title('Filtered Signal');
xlabel('Time (s)');

% Save the filtered signal
audiowrite('data/filtered_audio.wav', filtered_signal, fs);
