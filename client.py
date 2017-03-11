import numpy as np # numpy: used by cv2 the OpenCV
import cv2 # cv2: the python binding for OpenCV for fetching video from camera
import threading
'''
    This module will be used to send the data recorded by the camera,
    the video, the audio and then finally the multiplexed output.

'''

class Camera:
    '''
        This class will work in 1 thread, i.e. thread using showStream
        will keeps on working till 'q' button is pressed, and the
        getFrame method will return the frame information, the image
        at the time of calling of the function.

        Though this technique will have some lagging but it will be a
        better solution for the modern fast computers
    '''
    def __init__(self):
        self.frame = 0
        streamer = threading.Thread(target = self.showStream)
        streamer.start()

    def showStream(self):
        camera = cv2.VideoCapture(0)
        while True:
            ret, self.frame = camera.read()
            cv2.imshow("Stream", self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        camera.release()

    def getFrame(self):
        return self.frame
