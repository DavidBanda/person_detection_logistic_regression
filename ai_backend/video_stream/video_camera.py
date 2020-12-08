import cv2
import numpy as np


class VideoCamera:
    def __init__(self, path):
        self.video = cv2.VideoCapture(path)
        # self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # Obtenemos el frame
        ret, image = self.video.read()

        # Redimenzionamos el frame a un frame de 128 * 128
        frame = cv2.resize(image, (128, 128), interpolation=cv2.INTER_AREA)
        # transformamos la imagen a RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Creamos un arreglo del tipo numpy-array
        frame = np.array(frame[None])
        # Transformamos el frame de tipo (128, 128, 3) a numpy-array de (128*128*3, 1)
        frame = frame.reshape(frame.shape[0], -1).T

        return image, frame
