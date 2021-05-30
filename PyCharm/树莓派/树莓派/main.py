import cv2
import threading
import os

from tkinter import *
from PIL import Image, ImageTk
from compare_core import *
from upload import *


def resizeImage(image, width=None, height=None, inter=cv2.INTER_AREA):
    newsize = (width, height)
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        n = height / float(h)
        newsize = (int(n * w), height)
    else:
        n = width / float(w)
        newsize = (width, int(h * n))
    newimage = cv2.resize(image, newsize, interpolation=inter)
    return newimage


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def compare_face_baidu():
    access_token = get_access_token('7EHtQb4CfhOQqsZd3iYVqBVm', '3yDihiuszBIH6oDoDpTvtPHseemCcvKG')
    print(access_token)
    score = face_compare(access_token, "1.jpg", "2.jpg")
    if score >= 80:
        Label3.config(text="对比通过 相似度 %.2f" % score + "%")
    else:
        Label3.config(text="对比不通过 相似度 %.2f" % score + "%")
    upload("1.jpg", "2.jpg", score)
    os.remove("1.jpg")
    os.remove("2.jpg")


def compare_face_dlib():
    score = compare_face_recognition("1.jpg", "2.jpg")
    print(score)
    if score == 2:
        Label3.config(text="未采集到证件人脸")
    elif score == 3:
        Label3.config(text="未采集到人像人脸")
    elif score >= 0.60:
        Label3.config(text="对比通过")
    else:
        Label3.config(text="对比不通过 相似度 %.2f" % score + "%")
    upload("1.jpg", "2.jpg", score)
    os.remove("./1.jpg")
    os.remove("./2.jpg")


def show_frame():
    ret, frame = cap.read()
    # print(cap)
    if not ret:
        print("cap error")
        return 0
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cv2image = rotate(cv2image, 180)
    w = cv2image.shape[1]
    h = cv2image.shape[2]
    image_origin = resizeImage(cv2image, int(w / 3.5), int(h / 3.5), cv2.INTER_LINEAR)
    img = Image.fromarray(image_origin)
    imgtk = ImageTk.PhotoImage(image=img)
    if not os.path.exists('1.jpg'):
        Label1.imgtk = imgtk
        Label1.configure(image=imgtk)
    if not os.path.exists('2.jpg'):
        Label2.imgtk = imgtk
        Label2.configure(image=imgtk)
    window.after(10, show_frame)


def event_button0():
    Thread0.start()


def event_button1():
    ret, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    saveimage = rotate(frame, 180)
    cv2.imwrite("1.upload.jpg", saveimage)
    cv2.imwrite("1.jpg", cv2image)


def event_button2():
    ret, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    saveimage = rotate(frame, 180)
    cv2.imwrite("2.upload.jpg", saveimage)
    cv2.imwrite("2.jpg", cv2image)


def event_button3():
    if os.path.exists('1.jpg'):
        os.remove("1.jpg")


def event_button4():
    if os.path.exists('2.jpg'):
        os.remove("2.jpg")


def event_button5():
    Label3.config(text="对比中......")
    # Thread1 = threading.Thread(target=compare_face_baidu, name='compare_face_baidu')
    Thread1 = threading.Thread(
        target=compare_face_dlib, name='compare_face_dlib')
    Thread1.start()


if __name__ == "__main__":

    # Set up GUI
    window = Tk()
    window.wm_title("面向监考业务的人证核实移动终端与系统")
    window.geometry('680x350')

    # Graphics window
    main_Frame = Frame(window)
    main_Frame.pack()
    Frame_left = Frame(main_Frame)
    Frame_right = Frame(main_Frame)
    Frame_left.pack(side='left')
    Frame_right.pack(side='right')

    # Capture video frames
    Label1 = Label(Frame_left)
    Label1.pack()
    Label2 = Label(Frame_right)
    Label2.pack()

    Button1 = Button(Frame_left, text="拍照", command=event_button1)
    Button1.pack(ipadx=50)
    Button2 = Button(Frame_right, text="拍照", command=event_button2)
    Button2.pack(ipadx=50)
    Button3 = Button(Frame_left, text="重拍", command=event_button3)
    Button3.pack(ipadx=50)
    Button4 = Button(Frame_right, text="重拍", command=event_button4)
    Button4.pack(ipadx=50)
    Label3 = Label(window, text='等待拍照....', justify=LEFT)
    Label3.pack()

    Button0 = Button(Frame_left, text="开启摄像头", command=event_button0)
    Button0.pack(ipadx=50)
    Button5 = Button(Frame_right, text="对         比", command=event_button5)
    Button5.pack(ipadx=50)

    cap = cv2.VideoCapture(0)
    # cap1 = cv2.VideoCapture(1)
    # print(cap)
    if os.path.exists('1.jpg'):
        os.remove("1.jpg")
    if os.path.exists('2.jpg'):
        os.remove("2.jpg")
    Thread0 = threading.Thread(target=show_frame, name='show_frame')

    # show_frame()
    window.mainloop()  # Starts GUI
