import cv2
import numpy as np
import csv
import os
from datetime import datetime
import face_recognition

 
video_capture = cv2.VideoCapture(0)
 
Abhinav_image = face_recognition.load_image_file("Abhinav.jpg")
Abhinav_encoding = face_recognition.face_encodings(Abhinav_image)[0]
 
Khushi_image = face_recognition.load_image_file("Khushi.jpeg")
Khushi_encoding = face_recognition.face_encodings(Khushi_image)[0]

Yashika_image = face_recognition.load_image_file("Yashika.jpeg")
Yashika_encoding = face_recognition.face_encodings(Yashika_image)[0]

Jyotiraditya_image = face_recognition.load_image_file("Jyotiraditya.jpeg")
Jyotiraditya_encoding = face_recognition.face_encodings(Jyotiraditya_image)[0]


Alok_image = face_recognition.load_image_file("Alok.jpeg")
Alok_encoding = face_recognition.face_encodings(Alok_image)[0]


Shrey_image = face_recognition.load_image_file("Shrey.jpeg")
Shrey_encoding = face_recognition.face_encodings(Shrey_image)[0]






known_face_encoding = [
Abhinav_encoding,
Khushi_encoding,
Yashika_encoding,
Jyotiraditya_encoding,
Alok_encoding,
Shrey_encoding
]
 
known_faces_names = [
"Abhinav Maheshwari",
"Khushi Arora",
"Yashika",
"Jyotiraditya",
"Alok Raj",
"Shrey"

]
 
students = known_faces_names.copy()
 
face_locations = []
face_encodings = []
face_names = []
s=True
 
 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
 
 
 
f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)
p=0


def run(video_capture, s, known_face_encoding, known_faces_names, students,message2):
    now = datetime.now()
    namee=''
    with open(current_date+'.csv', mode ='a')as file:
        lnwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        while True:
            _,frame = video_capture.read()
            small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
            rgb_small_frame = small_frame[:,:,::-1]
            if s:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(small_frame,face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                    name=""
                    face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                    best_match_index = np.argmin(face_distance)
                    if matches[best_match_index]:
                        name = known_faces_names[best_match_index]
     
                    face_names.append(name)
                    if name in known_faces_names:
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        bottomLeftCornerOfText = (10,100)
                        fontScale              = 1.5
                        fontColor              = (255,0,0)
                        thickness              = 3
                        lineType               = 2
                        
                        

                        cv2.putText(frame,name+' Present', 
                            bottomLeftCornerOfText, 
                            font, 
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)
                        


                        
     
                        if name in students:
                            students.remove(name)
                            
                            current_time = now.strftime("%H-%M-%S")
                            namee=namee+(name+' Present')+'\n\n'
                            lnwriter.writerow([name])
            
            cv2.imshow("attendence system",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                
                message2.config(text=namee, bg="#f0f4f9", fg="black")

                break

 
video_capture.release()
cv2.destroyAllWindows()
f.close()