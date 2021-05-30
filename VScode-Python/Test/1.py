class ButtonFunction():
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
        Thread1 = threading.Thread(target=compare_face_baidu, name='compare_face_baidu')
        Thread1.start()
    
    