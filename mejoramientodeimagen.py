import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("fotos/lena.jpg"), cv2.COLOR_BGR2RGB)

blur = cv2.medianBlur(img, 9)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Filtro de Mediana')
plt.xticks([]), plt.yticks([])
plt.show()