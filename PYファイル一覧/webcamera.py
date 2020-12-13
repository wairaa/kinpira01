import tkinter as tk
import threading
import cv2
from PIL import Image,ImageTk
img_counter = 0
bootKey=True
recKey=False

def CV_init():
    global cap
    global w
    global h
    global out
    global img_counter
    cap = cv2.VideoCapture(1)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(w)
    print(h)
  
    #コーデック
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    img_name = "yasu{}.mp4".format(img_counter)
    out = cv2.VideoWriter(img_name, fourcc, fps, (w, h))
    print("cv_init_fin")
    img_counter += 1
    
    

def CV_loop():
    global frame
    global im
    if bootKey:
        ret, frame = cap.read()
        #dsizeは出力するサイズをタプルで(width, height)の順で指定
        frame = cv2.resize(frame, dsize=(w, h))
        if recKey:
            out.write(frame)
        im = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        #create_image(x,y,image=省略可tkinterのPhotoImage,anchor=既定はcenter
        #canvasの0, 0の位置に画像の左上を合わせるときは、x=0, y=0, anchor='nw'
        canvas.create_image(w, h, image=im,anchor='se')
        #after() には単純な時間待ちと一定時間後に指定した command を起動するタイマー
        root.after(1,CV_loop)
    else:
        print("exit")
        CV_exit()

def CV_exit():
    cap.release()
    out.release()
    root.destroy()

def recording():
    global recKey
    if recKey:
        recKey=False
    else:
        recKey=True

def finish():
    global bootKey
    global recKey
    bootKey=False
    recKey=False

def save():
    recKey = False
    CV_init()
    

root=tk.Tk()
canvas=tk.Canvas(root,width = 800, height = 600)
canvas.pack()
btn_rec=tk.Button(root,text="rec",command=recording)
btn_rec.pack(side = 'top')
btn_fin=tk.Button(root,text="res",command=save)
btn_fin.pack(side = 'top')
btn_fin=tk.Button(root,text="fin",command=finish)
btn_fin.pack(side = 'top')



CV_init()
threading.Thread(target=CV_loop).start()
root.mainloop()
