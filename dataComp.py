import numpy as np
#random bar codes 

def getrand():
    n = 20
    GG = np.random.random([n,n])
    x = np.arange(n)
    X,Y = np.meshgrid(x,x)
    #print(GG)
    GG[GG>0.5] = 1
    GG[GG<=0.5] = 0
    return GG

import matplotlib.pyplot as plt

GG = getrand()
plt.figure(figsize = (8,5))
plt.subplot(1,3,1)
plt.imshow(GG, cmap = 'binary')
plt.title('Random Image 1', fontSize = 15)

GG = getrand()
plt.subplot(1,3,2)
plt.imshow(GG, cmap = 'binary')
plt.title('Random Image 2', fontSize = 15)

GG = getrand()
plt.subplot(1,3,3)
plt.imshow(GG, cmap = 'binary')
plt.title('Random Image 3', fontSize = 15)


plt.show()

#-----------------------------------------------------------
# Interpolate

import matplotlib.image as mim
G = mim.imread('pipp.png')

#make it square
a,b = (len(G), len(G[0]))
dim = min(a,b)
G_sq = G[int(a/2-dim/2) : int(a/2 + dim/2)+1, int(b/2 - dim/2): int(b/2 + dim/2)+1,:]


def mush(img):
    '''
    returns the average
    '''
    return np.mean(np.mean(img, axis = 0), axis = 0)

#interpolate
def sqs(img, img_):
    '''
    img = og image
    img_ = new smaller img
    '''
    big = len(img)
    sml  = len(img_)
    
    cut = int(big/sml)
    
    for i in range(sml):
        for j in range(sml):
            
            #mush temp
            m_tmp = img[cut*i:cut*(i+1), cut*j:cut*(j+1),:]
            img_[i,j,:] = mush(m_tmp)
             
    return img_ 

plt.figure(figsize = (10,10))

G_sm = sqs(G_sq, np.zeros([20,20,3]))
plt.subplot(2,2,1)
plt.imshow(G_sm, cmap = 'binary')
plt.title('20 X 20 Pixel Space', fontSize = 15)

G_sm = sqs(G_sq, np.zeros([40,40, 3]))
plt.subplot(2,2,2)
plt.imshow(G_sm, cmap = 'binary')
plt.title('40 X 40 Pixel Space', fontSize = 15)

G_sm = sqs(G_sq, np.zeros([100,100, 3]))
plt.subplot(2,2,3)
plt.imshow(G_sm, cmap = 'binary')
plt.title('100 X 100 Pixel Space', fontSize = 15)

plt.subplot(2,2,4)
plt.imshow(G_sq, cmap = 'binary')
plt.title('Original - 216 X 216 Pixel Space', fontSize = 15)
plt.show()




