

import tkinter as tk
import atten
import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime


# Create the root window
root = tk.Tk()

root.overrideredirect(True)


# Set the window size and position
width = 700
height = root.winfo_screenheight()-100 # Get the screen height
# Calculate the x- and y-coordinates to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))

root.geometry(f"{width}x{height}+{x}+{y}")

x_cord = 75;
y_cord = 20;
checker=0;

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

def mark_attendance():
    
    atten.run(video_capture, s, known_face_encoding, known_faces_names, students,message2)
    # Open the CSV file in read mode
    

# Set the background color to white
root.configure(bg="white")

# Add logo to the top left corner
logo_img = tk.PhotoImage(file="logo.png")
logo_img = logo_img.subsample(1)

# def run_jjcopy():
#     root.destroy()
#     os.system('python jjcopy.py')

# Create a label widget for the logo and pack it in the top left corner
logo_label = tk.Label(root, image=logo_img, bd=0)
logo_label.pack(side="left", anchor="nw", padx=10, pady=10)



# Add text to the right of the logo
text_label= tk.Label(root, text="ATTENDANCE RECOGNITION SYSTEM" ,bg="white"  ,fg="blue"  ,width=35  ,height=1,font=('Sitka Text Semibold', 18, 'bold underline')) 

text_label.pack(pady=30, anchor="n")

line_canvas = tk.Canvas(root, height=1, width = 700,bg="black", highlightthickness=0)
line_canvas.create_line(0, 0, width, 0, fill="black")
line_canvas.place(x=75-x_cord,y=130-y_cord)










button = tk.Button(root, text="MARK ATTENDANCE", command=mark_attendance, width=40 ,height=1  ,fg="white"  ,bg="black" ,font=('Sitka Text Semibold', 18, ' bold ') )
button.place(x=120-x_cord, y=150-y_cord)



lbl = tk.Label(root, text="Attendance list:", width=12  ,height=1  ,fg="green"  ,bg="white" ,font=('Sitka Text Semibold', 18, ' bold ') ) 
lbl.place(x=120-x_cord, y=250-y_cord)


# # Add a line below the "Attendance list:" line
# line2_canvas = tk.Canvas(root, height=1, bg="black", highlightthickness=0)
# line2_canvas.create_line(0, 0, width, 0, fill="black")
# line2_canvas.place(x=120-x_cord, y=150-y_cord)
# message2 = tk.Label(root, height=screen_height*0.025, width=67, bg="#f0f4f9", fg="black", font=("Helvetica", 12), wrap="word", state="disabled")
# message2.place(x=120-x_cord, y=290-y_cord)

message2 = tk.Label(root, height=20, width=67,  font=("Helvetica", 12))
message2.place(x=120-x_cord, y=290-y_cord)

# Add an exit button in the bottom left corner
exit_button = tk.Button(root, text="EXIT", width=10, height=1, bg="black", fg="white", font=('Sitka Text Semibold', 15, 'bold'), command=root.destroy)
exit_button.place(x=20, y=height-70)



root.mainloop()






