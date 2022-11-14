import cv2
import numpy as np
import imutils
import os

Datos = 'p'
if not os.path.exists(Datos):
    print('Carpeta creada: ',Datos)
    os.makedirs(Datos)

Datos = 'n'
if not os.path.exists(Datos):
    print('Carpeta creada: ',Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def nothing(x):
    pass

cv2.namedWindow('Imagen')
cv2.createTrackbar('Y2',"Imagen",4,480,nothing)
cv2.createTrackbar('X2',"Imagen",3,640,nothing)
cv2.createTrackbar('X1',"Imagen",1,639,nothing)
cv2.createTrackbar('Y1',"Imagen",2,479,nothing)
cv2.createTrackbar('P o N',"Imagen",0,1,nothing)

countP = 1
countN = 1
while True:

    ret, frame = cap.read()
    if ret == False: break
    imAux = frame.copy()

    x2 = cv2.getTrackbarPos('X2',"Imagen")
    y2 = cv2.getTrackbarPos('Y2',"Imagen")
    x1 = cv2.getTrackbarPos('X1',"Imagen")
    y1 = cv2.getTrackbarPos('Y1',"Imagen")
    
    cv2.rectangle(frame,(x1,y1),(x2,y2),(200,0,200),2)

    objeto = imAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto,width=38)
    #print(objeto.shape)

    k = cv2.waitKey(1)
    if k == ord('s') or k == ord('S'):
        PoN = cv2.getTrackbarPos('P o N',"Imagen")
        if PoN == 0:
            Datos = 'p'
            cv2.imwrite(Datos+'/objeto_{}_P.jpg'.format(countP),objeto)
            print('Imagen guardada:'+'/objeto_{}_P.jpg'.format(countP))
            countP += 1
        else:
            Datos = 'n'
            cv2.imwrite(Datos+'/objeto_{}_N.jpg'.format(countN),objeto)
            print('Imagen guardada:'+'/objeto_{}_N.jpg'.format(countN))
            countN += 1

    if k == 27:
        break

    cv2.imshow('frame',frame)
    cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()