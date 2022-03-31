function plotSpectrum(sig,fs,dB,logx)

% Plot spectal magnitude in linear or dB scale
% In order to be imported in the switch-case statement, dB and logx 
% parameters have to be converted to a single string varibale using 
% the num2str function

    params = num2str([dB logx]);
    l = length(sig);    
    fvec = 0:fs/l:fs-1/l; % frequency vector
    
    spec = fft(sig); % spectrum
    magSpec = abs(spec); % spectral magnitude
    magSpec_dB = 20*log10(magSpec(1:l/2)); % spectral magnitude in dB
    
    switch params
        case '0  0'
            plot(fvec(1:l/2),magSpec(1:l/2));
        case '0  1'
            semilogx(fvec(1:l/2),magSpec(1:l/2));
        case '1  0'
            plot(fvec(1:l/2), magSpec_dB(1:l/2));
        case '1  1'
            semilogx(fvec(1:l/2), magSpec_dB(1:l/2));
    end

end