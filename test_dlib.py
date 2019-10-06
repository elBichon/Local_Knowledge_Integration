import numpy as np
import cv2
import requests
import numpy as np
import os
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import imutils
import numpy as np
import argparse
import sys
import itertools
import dlib




emotion_model_path = 'emotion_recognition.h5'
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry","disgust","scared", "happy", "sad", "surprised","neutral"]

def white_balance(img):
    result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    return result

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()

parser = argparse.ArgumentParser(description='script running')
parser.add_argument('ip_address', type=str, help='ip of the camera to use')
args = parser.parse_args()
ip = args.ip_address
url = "http://"+ip+":8080/shot.jpg"

if __name__ == "__main__":
    while True:
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr,-1)
        img = white_balance(img)
        detector = dlib.get_frontal_face_detector()
        color_green = (0,255,0)
        line_width = 3
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(rgb_image)
        for det in dets:
            cv2.rectangle(img,(det.left(), det.top()), (det.right(), det.bottom()), color_green, line_width)
            roi_gray = gray[det.top():det.bottom(),det.left():det.right()]
            try:
                roi = cv2.resize(roi_gray, (48, 48))
                roi = roi.astype("float") / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                preds = emotion_classifier.predict(roi)[0]
                print(preds)
                emotion_probability = np.max(preds)
                print(emotion_probability)
                label = EMOTIONS[preds.argmax()]
                current_emotion = str('emotion: '+str(label))
                cv2.putText(img,current_emotion,(0,200), font, 1, (0,0,0), 2, cv2.LINE_AA)
                print(label)
                print('--------------------')
                print('--------------------')
            except Exception as e:
                print(str(e))
            font = cv2.FONT_HERSHEY_SIMPLEX
            number_of_persons = str('number of persons: '+ str(len(dets)))
            cv2.putText(img,number_of_persons,(0,130), font, 1, (0,0,0), 2, cv2.LINE_AA)
            cv2.imshow('my webcam', img)

        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()
