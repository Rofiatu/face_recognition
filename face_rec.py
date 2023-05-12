import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

st.title("Face Detection App")
st.markdown('This is a face detection model created by the Pumpkin Redeemers Class!')
user_name = st.text_input('Please enter your name')
if user_name == '':
    user_name
else:
    st.success(f'Welcome, {user_name}!')

    st.write('Please click on the Stop button only once, when you no longer want to proceed with the face detection process. \n Where the stop button is erroneously clicked, please refresh the page to continue with the facial detection.')

    button = st.button('Recognise my face')
    frame_window = st.image([])

    camera = cv2.VideoCapture(0) # this presumes your webcam can be reached at port 0
    while button:
        _, frame = camera.read()
        
        # turn the color to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # detect the faces 
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        
        # draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # convert color style from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # show the image
        frame_window.image(frame)
    stopper = st.button('Stop!')
    if stopper:
        camera.release()