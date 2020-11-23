from flask import Blueprint, Response
from ai_backend.video_stream.video_camera import VideoCamera
from ai_backend.neural_network.predict_image import PredictImage

video_stream = Blueprint('video_stream', __name__)
predict = PredictImage()

def gen(camera):
    while True:
        frame = camera.get_frame()
        frame_person = camera.detect_person()
        print(predict.predict_image(frame_person))
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@video_stream.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')
