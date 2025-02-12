[clean, fs] = audioread('data/clean_audio.wav');
[wind, fs_wind] = audioread('data/wind_noise.wav');

if fs ~= fs_wind
    % Alternative to resample using interp1 (included in base MATLAB)
    t_old = linspace(0, length(wind)/fs_wind, length(wind));
    t_new = linspace(0, length(wind)/fs_wind, round(length(wind)*fs/fs_wind));
    wind = interp1(t_old, wind, t_new, 'linear');
end

% Make signals the same length by taking the minimum length
min_length = min(length(clean), length(wind));
clean = clean(1:min_length);
wind = wind(1:min_length);

% Compute power of clean signal and wind noise
power_clean = mean(clean.^2);
power_wind = mean(wind.^2);
desiredSNR = -10; % Changed from 5 to -10 dB to make wind more prominent
scaleFactor = sqrt(power_clean/(10^(desiredSNR/10)*power_wind));

wind_scaled = wind * scaleFactor;

% Mix the signals
noisy_signal = clean + wind_scaled;

% Normalize to prevent clipping
max_amplitude = max(abs(noisy_signal));
if max_amplitude > 1
    noisy_signal = noisy_signal / max_amplitude;
end

% Save the mixed signal for later processing
audiowrite('data/noisy_audio.wav', noisy_signal, fs);
