function [dith]=CreateDither(dithtype,LSB,npoints);

% function [dither]=CreateDither(DitherType,DithSeed,npoints)
%
% This function generates dither noise of length npoints.
% The type of dither generated is controlled by the
% DitherType parameter as follwoing:
%
% Dithretype   = 1, RPDF in the range [-LSB/2 LSB/2]
%	       = 2, ÔPDF in the range [-LSB LSB]
%	       = 3, HighPass RPDF in the range [-LSB LSB]
%
% where LSB is the amplitude value that corresponds
% to the Least Significant Bit of the quantizer

%  Author: Andreas Floros
%  Digital Audio Technology Toolbox
%  Audio Group, WCL, University of Patras
%  Last Modified: 22/03/2005.


% Intitialization
a1=3453;
a2=2945;
m=65536;
c1=1;
c2=1;
dithran1=1531;
dithran2=18531;
dithtemp1=0;
dithtemp2=0;
dithtemp=0;
dith=[];


% ==================== RPDF Dither Generator =====================
%    		             
%      			  *     *     *
%		     
%  		       -LSB/2   0    LSB/2   
if (dithtype==1)
 for i=1:npoints,
    dithran1=mod((dithran1*a1+c1),m);
    dithtemp1=LSB*(dithran1-32767)/65536;
    dith=[dith dithtemp1];
 end
end
% ================================================================ 



% ==================== TPDF Dither Generator =====================
%    		                   *     
%      			    *             *
%		     *                            *
%  		   -LSB   -LSB/2   0    LSB/2    LSB
if (dithtype==2)
 for i=1:npoints,
    dithran1=mod((dithran1*a1+c1),m);
    dithran2=mod((dithran2*a2+c2),m);
    dithtemp1=LSB*(dithran1-32767)/65536;
    dithtemp2=LSB*(dithran2-32767)/65536;
    dithtemp=(dithtemp1+dithtemp2)/2;
    dith=[dith dithtemp];
 end
end
% ================================================================ 


% ============ High Pass TPDF Dither Generator ===================
%    		                   *     
%      			    *             *
%		     *                            *
%  		   -LSB   -LSB/2   0    LSB/2    LSB
if (dithtype==3)
 for i=1:npoints,
    dithran1=mod((dithran1*a1+c1),m);
    dithtemp1=LSB*(dithran1-32767)/65536;
    dithtemp=(dithtemp1-dithtemp2)/2;
    dithtemp2=dithtemp;
    dith=[dith dithtemp];
 end
end
% ================================================================ 
