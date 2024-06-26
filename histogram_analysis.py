import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':
    img=cv2.imread('./images/cat.png',cv2.IMREAD_GRAYSCALE)
    img_plt=img.ravel()
    print(img.shape)
    assert img is not None,"file could not be read"
    plt.subplot(1,2,1)
    plt.hist(img.ravel(),256,[0,256])
    plt.subplot(1,2,2)
    plt.imshow(img_plt.reshape(*img.shape))
    plt.show()



