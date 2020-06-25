B = imread('pup.jpg');

subplot(1,2,1);
imshow(B);
title('Original Image : 100% Fourier Modes')
Bfft = fft2(B);

Bsort = sort(abs(Bfft(:))); %flattened
g = 0.05; %5 percent
id = (1-g)*length(Bsort);
idf = floor(id);
thresh = Bsort(idf); %greatest coef value in sorted list

indx = abs(Bfft)>(thresh);
Bnew = Bfft.*indx;
Bim = ifft2(Bnew);

subplot(1,2,2);
imshow(uint8(Bim));
title('Compressed Image : 5% of the Fourier Modes')







