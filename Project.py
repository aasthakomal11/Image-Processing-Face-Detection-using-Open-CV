# Importing the libraries
import cv2
from tkinter import * 

root=Tk()

root.eval('tk::PlaceWindow . center')
root.geometry("500x500")
filename = PhotoImage(file= 'C://Users//KIIT//Desktop//ABD.png')
canvas1 = Canvas(root, width = 600, height = 600)
canvas1.pack(fill = "both" , expand = True)
canvas1.create_image(0,0,image = filename , anchor ="nw")


blind_var=StringVar()
video_capture=0
def start():
    player=blind_var.get()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
            
    def detect(gray, frame):
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
                smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
        return frame
    global video_capture
    video_capture = cv2.VideoCapture(0)
    while True:
        _, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = detect(gray, frame)
        cv2.imshow('Video', canvas)
        c = cv2.waitKey(1)
        if c == 27:
            stop()
            break

            #break
def stop():
    video_capture.release()
    cv2.destroyAllWindows()
    root.destroy()
 
#Cblind_label = Label(root, text = 'FACE DETECTION', font=('calibre',10, 'bold'))
#C_entry = Entry(root,textvariable = blind_var, font=('calibre',10,'normal'))
canvas1.create_text(250, 50, text= "FACE DETECTION SYSTEM",fill="red",font=('Helvetica 15 bold'))
#canvas1.create_text(250,50,text = "FACE DETECTION SYSTEM" , font = ('calibre',20,'bold'))
Button1=Button(root,text = 'Start',width = 10 , height = 2 , bd = '10', command = start)
Button2=Button(root,text = 'Stop', width = 10 , height = 2 , bd = '10',command = stop)

#Cblind_label.grid(row=200,column=250)
Button1_canvas = canvas1.create_window(230 , 300 ,anchor = "nw" , window = Button1 )
Button2_canvas = canvas1.create_window(230 , 360,anchor = "nw" , window = Button2 )

#C_entry.grid(row=0,column=1)
#sub_btn.grid(row=1,column=1)
#sub_btn1.grid(row=1,column=2)

root.mainloop()



