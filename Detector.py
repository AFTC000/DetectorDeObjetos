import torch
import cv2
import numpy as np
import pandas    

model = torch.hub.load('ultralytics/yolov5', 'custom', 
                       path = 'C:/Users/ADMIN/Desktop/Video/best.pt')

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    detect = model(frame)
    resolucion = frame.shape

    Ymax = 480
    Xmax = 650 

    Ycen = Ymax/2
    Xcen = Xmax/2
    
    centro = Ycen, Xcen

    info = detect.pandas().xyxy[0]
    objeto_0 = info.iloc[0]


    if(objeto_0["confidence"] > 0.65):
        print(objeto_0["xmax"])

    YminOBJ = "ymin"
    XminOBJ = "xmin"

    YmaxOBJ = "ymax"
    XmaxOBJ = "xmax"

    YcenOBJ = ((YmaxOBJ-YminOBJ)/2+YminOBJ)
    XcenOBJ = ((XmaxOBJ-XminOBJ)/2+XminOBJ)

    centroOBJ = YcenOBJ, XcenOBJ

    CentroTotal = 

    cv2.imshow('Detector de Legos', np.squeeze(detect.render()))

    q = cv2.waitKey(5)
    if q ==27:
        break

cap.release()
cv2.destroyAllWindows()
 