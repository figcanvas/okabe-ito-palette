function c = okabe_ito(n)
%OKABE_ITO Okabe-Ito (Wong) colorblind-safe palette as an n-by-3 RGB matrix.
%   colororder(okabe_ito(4))   % first four colors in the recommended order
if nargin < 1, n = 8; end
c = [230 159   0;   % orange
       0 114 178;   % blue
       0 158 115;   % bluish green
     213  94   0;   % vermillion
      86 180 233;   % sky blue
     204 121 167;   % reddish purple
       0   0   0;   % black
     240 228  66];  % yellow, last: 1.32:1 on white
c = c(1:n, :) / 255;
end
