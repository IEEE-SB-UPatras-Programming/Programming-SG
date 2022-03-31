%% load packages
pkg load signal
pkg load communications

%%  signal generation

% global variables
fs = 44100;
t = 0:10/fs:3-1/fs;

% -------------- PART A1 ----------------
% sine signal 
f = 500;
S1 = sin(2*pi*f*t);
[OutSignal]=QuantiseAudio(S1,16,1, -1,0,3);
figure
plot(t,OutSignal);
print "plots/s1.png"
figure
plotSpectrum(OutSignal,fs,1,1);
print "plots/s1_spectrum.png"
figure
specgram(S1, 256, fs);
print "plots/s1_spectrogram.png"

% x = chirp([0:0.001:2],0,2,500);  # freq. sweep from 0-500 over 2 sec.
% Fs=1000;                  # sampled every 0.001 sec so rate is 1 kHz
% step=ceil(20*Fs/1000);    # one spectral slice every 20 ms
% window=ceil(100*Fs/1000); # 100 ms data window
% specgram(x, 2^nextpow2(window), Fs, window, window-step);
% print "plots/test.png"

% chirp signal
S2 = chirp(t,440,2,1320);
figure
plot(t,S2);
print "plots/chirp.png"
figure
plotSpectrum(S2,fs,1,1);
print "plots/chirp_spectrum.png"
figure
specgram(S2, 256, fs / 10);
print "plots/chirp_spectrogram.png"

% click track signal
%%Use Audacity for better results 
N=length(S1);
tempo = 120;
bps = tempo/60;
S3=zeros(1,N);
S3(1:fs/bps:N)=1;
figure
plot(t,S3);
print "plots/click.png"
figure
plotSpectrum(S3,fs,0,1);
print "plots/click_spectrum.png"
figure
specgram(S3, 256, fs / 10);
print "plots/click_spectrogram.png"
%%
%% 

% white gaussian noise signal
l = length(t);
S4=wgn(1,l,50);
figure
plot(t,S4);
print "plots/wgn.png"
figure
plotSpectrum(S4,fs,1,1);
print "plots/wgn_spectrum.png"
figure
specgram(S4);
print "plots/wgn_spectrogram.png"



% -------------- PART A2 ----------------
% load LP,HP and BP filters

load('filters.mat');

% sine signal 
S1LP = filter('LP',S1); % apply LP filter on sine signal
%...........
%...........
