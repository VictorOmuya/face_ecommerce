import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import ImageGrab



def capture(path):
    
    known_image = face_recognition.load_image_file(path)

    known_encoding = face_recognition.face_encodings(known_image)[0]
      
    encodeListKnown = known_encoding
     
    cap = cv2.VideoCapture(0)
     
    while True:
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
     
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
     
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces([encodeListKnown],encodeFace)
            faceDis = face_recognition.face_distance([encodeListKnown],encodeFace)
            
            matchIndex = np.argmin(faceDis)
        
         
            if matches[matchIndex]:
                name = 'recognized'  
                for i in faceDis:
                    #print(faceDis)
                    if i >= 0.5:
                        #print(faceDis)
                        name = 'not recognized'
                        y1,x2,y2,x1 = faceLoc
                        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    
                    else:
                        #print(faceDis)
                        name = 'recognized'      
                        y1,x2,y2,x1 = faceLoc
                        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            else:
                name = 'not recognized'
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
         
     
        cv2.imshow('Webcam',img)
        cv2.waitKey(1)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            
                break
    cap.release()    
    cv2.destroyAllWindows()
    
    
        
    return name, matchIndex
#classn, imgs = classname()
#findEncodings(imgs)


def detectface():     
    #try:

    name, matchIndex = capture()
            
    if name == 'recognized':
        
        res = 'authentication successful'      
        print('authentication successful')
            
    elif name == 'not recognized':
        res = 'authentication failed'
        print('authentication failed...')
                
    else:
        res = 'authentication failed'
        print('authentication failed...')
    return name, res
    #except:
        #print('Fatal Error!')