function [OutSignal]=QuantiseAudio(InSignal,N,up_limit,down_limit,NSFlag,DitherFlag)

% function y = QuantiseAudio(x,N,UpLimit,DowmLimit,NSFlag,DitherFlag).
% This function quantises the input signal x using N bit resolution.
% The quantiser output range is [DownLimit UpLimit]. During the
% quantisation, controlled dither can be added and noise-shaping
% techniques can be applied, using the following options:
%
%   uplimit, downlimit = the max and min value of the input signal
%	NSFlag	= 0 No noise-shaping
%			= 2	2nd order noise-shaping
%			= 3 3rd order noise-shaping
%	DitherFlag	= 0 No dither
%			= 1	RPDF dither
%			= 2	TPDF dither
%			= 3 HighPass TPDF dither
%
%  Author: Andreas Floros
%  Digital Audio Technology Toolbox
%  Audio Group, WCL, University of Patras
%  Last Modified: 22/03/2005.

% Initialization
  OutSignal=[];
  dither=[];

% Find the number of points to be calculated
  npoints=max(size(InSignal));

% Calculate the PCM quantization step
  LSB=(up_limit-down_limit)/(2^N-1);

% Calculate dither sequence if desired
  if (DitherFlag==0)
	dither=zeros(size(InSignal));
	InSignal=InSignal+dither;
  else
	dither=CreateDither(DitherFlag,LSB,npoints);
	InSignal=InSignal+dither;
  end

% Perform quantization process without NoiseShaping
  if (NSFlag==0)
	
	OutSignal=LSB*floor((InSignal/LSB)+1/2); %*floor
	i=find(OutSignal>up_limit);
	Umatrix=ones(size(i))*up_limit;
	OutSignal(i)=Umatrix;

	i=find(OutSignal<down_limit);
	Umatrix=ones(size(i))*down_limit;
	OutSignal(i)=Umatrix;
  end

% Perform quantization process 2nd Order NoiseShaping
  if (NSFlag==2)
	f1=0;
  	f2=0;
	for i=1:1:npoints
		w=2*f1-f2;
		OutSignal(i)=LSB*floor(((InSignal(i)-w)/LSB)+1/2);

		if (OutSignal(i)>up_limit)
	        	OutSignal(i)=up_limit;
		end

		if (OutSignal(i)<down_limit)
		        OutSignal(i)=down_limit;
		end

		f=OutSignal(i)-InSignal(i)+w;

		f2=f1;
		f1=f;
	end
        OutSignal=OutSignal';

  end

% Perform quantization process 3rd Order NoiseShaping
  if (NSFlag==3)
  	f1=0;
  	f2=0;
  	f3=0;
  	for i=1:1:npoints
		w=3*f1-3*f2+f3;
		OutSignal(i)=LSB*floor(((InSignal(i)-w)/LSB)+1/2);

		if (OutSignal(i)>up_limit)
	        	OutSignal(i)=up_limit;
		end

		if (OutSignal(i)<down_limit)
		        OutSignal(i)=down_limit;
		end

		f=OutSignal(i)-InSignal(i)+w;
		f3=f2;
        	f2=f1;
		f1=f;
	end
	OutSignal=OutSignal';

  end
