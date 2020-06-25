B = imread('jakob-kac-Ty_e0ANh_eo-unsplash.png');

subplot(1,3,1);
imshow(B);
title('100% Fourier Modes')
Bfft = fft2(B);
ctr = 1; 

for g = [0.01, 0.001]
Bsort = sort(abs(Bfft(:))); %flattened
id = (1-g)*length(Bsort);
idf = floor(id);
thresh = Bsort(idf); %greatest coef value in sorted list

indx = abs(Bfft)>(thresh);
Bnew = Bfft.*indx;
Bim = ifft2(Bnew);

ctr = ctr +1 ;
subplot(1,3,ctr);
imshow(uint8(Bim));
title(string(g*100)+ '% of Fourier Modes')

end

%Bim = rgb2gray(uint8(Bim));
%figure();
%surf(Bim(50:50:end, 50:50:end));
%title('Pixel Intensities'); 
