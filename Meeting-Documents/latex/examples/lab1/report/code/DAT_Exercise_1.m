%% load packages 

pkg load signal;
pkg load communications;

%%  signal generation

% global variables
fs = 44100;
t = 0:1/fs:3-1/fs;

% -------------- PART A1 ----------------
% sine signal 
f = 500;
S1 = sin(2*pi*f*t);
[S1]=QuantiseAudio(S1,16,1, -1,0,3);
figure
plot(t(1:1000),S1(1:1000));
title('S1 = sin(2 \cdot \pi \cdot f \cdot t)');
%figure
saveas(1, "plots/s1.png");
plotSpectrum(S1,fs,1,1);
% figure
saveas(1, "plots/s1_spectrum.png");
specgram(S1, 256, fs);
saveas(1, "plots/s1_spectrogram.png");

%% 

% chirp signal
S2 = chirp(t,440,3,1320);
[S2]=QuantiseAudio(S2,16,1, -1,0,3);
%figure
plot(t,S2);
title('S2 = chirp(t), f_s=440Hz f_e=1320Hz');
saveas(1, "plots/s2.png");
audiowrite("sounds/s2.wav", S2, fs);
% figure
plotSpectrum(S2,fs,1,1);
saveas(1, "plots/s2_spectrum.png");
% figure
specgram(S2, 256, fs);
saveas(1, "plots/s2_spectrogram.png");

% click track signal
%%Use Audacity for better results 
N=length(S1);
tempo = 120;
bps = tempo/60;
S3=zeros(1,N);
S3(1:fs/bps:N)=1;
[S3]=QuantiseAudio(S3,16,1, -1,0,3);
% figure
plot(t,S3);
title('S3 = click(t), tempo=120');
saveas(1, "plots/s3.png");
% figure
plotSpectrum(S3,fs,0,1);
% figure
saveas(1, "plots/s3_spectrum.png");
specgram(S3, 256, fs);
saveas(1, "plots/s3_spectrogram.png");
%%
%% 

% white gaussian noise signal
S4=wgn(1, length(t), 1);
% figure
[S4]=QuantiseAudio(S4,16,1, -1,0,3);
plot(t,S4);
title('S4 = wgn(t)');
saveas(1, "plots/s4.png");
% figure
plotSpectrum(S4,fs,1,1);
saveas(1, "plots/s4_spectrum.png");
% figure
specgram(S4, 256, fs);
saveas(1, "plots/s4_spectrogram.png");

% -------------- PART A2 ----------------
% load LP,HP and BP filters

LP_coeffs = fir1(100, 500/fs, 'low');
HP_coeffs = fir1(100, 1000/fs, 'high');
BP_coeffs = fir1(100, [500/fs, 1000/fs], 'bandpass');

% Filtered S1

SF1 = filter(LP_coeffs, 1, S1);
plot(t(1:1000),SF1(1:1000));
saveas(1, "plots/sf1_lp.png");
plotSpectrum(SF1,fs,0,1);
saveas(1, "plots/sf1_lp_spectrum.png");
specgram(SF1, 256, fs);
saveas(1, "plots/sf1_lp_spectrogram.png");

SF1 = filter(HP_coeffs, 1, S1);
plot(t(1:1000),SF1(1:1000));
saveas(1, "plots/sf1_hp.png");
plotSpectrum(SF1,fs,0,1);
saveas(1, "plots/sf1_hp_spectrum.png");
specgram(SF1, 256, fs);
saveas(1, "plots/sf1_hp_spectrogram.png");

SF1 = filter(BP_coeffs, 1, S1);
plot(t(1:1000),SF1(1:1000));
saveas(1, "plots/sf1_bp.png");
plotSpectrum(SF1,fs,0,1);
saveas(1, "plots/sf1_bp_spectrum.png");
specgram(SF1, 256, fs);
saveas(1, "plots/sf1_bp_spectrogram.png");


% Filtered S2

SF2 = filter(LP_coeffs, 1, S2);
plot(t(1:1000),SF2(1:1000));
saveas(1, "plots/sf2_lp.png");
plotSpectrum(SF2,fs,0,1);
saveas(1, "plots/sf2_lp_spectrum.png");
specgram(SF2, 256, fs);
saveas(1, "plots/sf2_lp_spectrogram.png");

SF2 = filter(HP_coeffs, 1, S2);
plot(t(1:1000),SF2(1:1000));
saveas(1, "plots/sf2_hp.png");
plotSpectrum(SF2,fs,0,1);
saveas(1, "plots/sf2_hp_spectrum.png");
specgram(SF2, 256, fs);
saveas(1, "plots/sf2_hp_spectrogram.png");

SF2 = filter(BP_coeffs, 1, S2);
plot(t(1:1000),SF2(1:1000));
saveas(1, "plots/sf2_bp.png");
plotSpectrum(SF2,fs,0,1);
saveas(1, "plots/sf2_bp_spectrum.png");
specgram(SF2, 256, fs);
saveas(1, "plots/sf2_bp_spectrogram.png");
% Filtered S3

SF3 = filter(LP_coeffs, 1, S3);
plot(t(1:1000),SF3(1:1000));
saveas(1, "plots/sf3_lp.png");
plotSpectrum(SF3,fs,0,1);
saveas(1, "plots/sf3_lp_spectrum.png");
specgram(SF3, 256, fs);
saveas(1, "plots/sf3_lp_spectrogram.png");

SF3 = filter(HP_coeffs, 1, S3);
plot(t(1:1000),SF3(1:1000));
saveas(1, "plots/sf3_hp.png");
plotSpectrum(SF3,fs,0,1);
saveas(1, "plots/sf3_hp_spectrum.png");
specgram(SF3, 256, fs);
saveas(1, "plots/sf3_hp_spectrogram.png");

SF3 = filter(BP_coeffs, 1, S3);
plot(t(1:1000),SF3(1:1000));
saveas(1, "plots/sf3_bp.png");
plotSpectrum(SF3,fs,0,1);
saveas(1, "plots/sf3_bp_spectrum.png");
specgram(SF3, 256, fs);
saveas(1, "plots/sf3_bp_spectrogram.png");

% Filtered S4

SF4 = filter(LP_coeffs, 1, S4);
plot(t(1:1000),SF4(1:1000));
saveas(1, "plots/sf4_lp.png");
plotSpectrum(SF4,fs,0,1);
saveas(1, "plots/sf4_lp_spectrum.png");
specgram(SF4, 256, fs);
saveas(1, "plots/sf4_lp_spectrogram.png");

SF4 = filter(HP_coeffs, 1, S4);
plot(t(1:1000),SF4(1:1000));
saveas(1, "plots/sf4_hp.png");
plotSpectrum(SF4,fs,0,1);
saveas(1, "plots/sf4_hp_spectrum.png");
specgram(SF4, 256, fs);
saveas(1, "plots/sf4_hp_spectrogram.png");

SF4 = filter(BP_coeffs, 1, S4);
plot(t(1:1000),SF4(1:1000));
saveas(1, "plots/sf4_bp.png");
plotSpectrum(SF4,fs,0,1);
saveas(1, "plots/sf4_bp_spectrum.png");
specgram(SF4, 256, fs);
saveas(1, "plots/sf4_bp_spectrogram.png");
