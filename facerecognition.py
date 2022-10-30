import cv2
from simple_facerec import SimpleFacerec

sfr = SimpleFacerec()

sfr.load_encoding_images("img/")

cam = cv2.VideoCapture(0)

def facerecog():

        while True:

            ret , frame = cam.read()


            face_locations, face_names  =  sfr.detect_known_faces(frame)

            for face_loc, name in zip(face_locations, face_names):
                y1 , x2 , y2 , x1 = face_loc[0] , face_loc[1] , face_loc[2] , face_loc[3]

                cv2.putText(frame ,name , (x1 , y1 -10) , cv2.FONT_HERSHEY_DUPLEX , 1 , (255, 0, 0) , 2)

                cv2.rectangle(frame , (x1, y1) ,(x2 , y2) , (100 , 100 ,0) , 4 )

                if 'unknown' in name:
                    a = 'False'
                else :
                    a = 'True'

                print(a)

            cv2.imshow("frame" , frame)
            key = cv2.waitKey(9)
            if key == 27:
                break

            cam.release()
            cv2.destroyAllWindows
