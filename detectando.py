import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

objeto = cv2.CascadeClassifier('cascade.xml')

cv2.namedWindow('Imagen')
cv2.createTrackbar('scaleFactor',"Imagen",5,500,nothing)
cv2.createTrackbar('minNeighbors',"Imagen",1,500,nothing)
cv2.createTrackbar('minSize1',"Imagen",1,500,nothing)
cv2.createTrackbar('minSize2',"Imagen",1,500,nothing)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    scaleFactor = cv2.getTrackbarPos('scaleFactor',"Imagen")
    minNeighbors = cv2.getTrackbarPos('minNeighbors',"Imagen")
    minSize1 = cv2.getTrackbarPos('minSize1',"Imagen")
    minSize2 = cv2.getTrackbarPos('minSize2',"Imagen")

    toy = objeto.detectMultiScale(gray,
    scaleFactor = scaleFactor,
    minNeighbors = minNeighbors,
    minSize=(minSize1,minSize2))

    for (x,y,w,h) in toy:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'objeto',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()