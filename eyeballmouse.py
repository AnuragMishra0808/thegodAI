import cv2
import mediapipe as mp
import pyautogui


camera = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks= True)
screen_w , screen_h = pyautogui.size()

def mouse():
    while True :
        _ , frame = camera.read()
        frame = cv2.flip(frame , 1)
        rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output=face_mesh.process(rgb_frame)
        points = output.multi_face_landmarks
        frame_h , frame_w , _ = frame.shape
        if points:
            landmarks = points[0].landmark
            for id , landmark in  enumerate( landmarks[474:478] ):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame , (x,y) , 3, (100,100,0))
                if id == 3:

                    screen_x = screen_w/ frame_w *x
                    screen_y = screen_h/ frame_h *y
                    pyautogui.moveTo(screen_x , screen_y)


        cv2.imshow('eye mouse', frame)

        cv2.waitKey(1)